#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import random
import re
import socket
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


FLAG_RE = re.compile(r"flag\{[^}\s]+\}", re.IGNORECASE)


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


def recv_until(sock: socket.socket, marker: bytes, timeout: float, max_bytes: int) -> bytes:
    sock.settimeout(timeout)
    data = bytearray()
    while marker not in data:
        if len(data) >= max_bytes:
            break
        chunk = sock.recv(4096)
        if not chunk:
            break
        data.extend(chunk)
    return bytes(data)


def balanced_codes(length: int, weight: int, columns: int, seed: int, max_attempts: int = 2000) -> list[int]:
    rng = random.Random(seed)
    for _attempt in range(max_attempts):
        codes = [0] * length
        for bit in range(columns):
            ones = set(rng.sample(range(length), weight))
            mask = 1 << bit
            for index in ones:
                codes[index] |= mask
        if len(set(codes)) == length:
            return codes
    raise SystemExit(f"could not generate unique balanced codes for length={length}, weight={weight}, columns={columns}")


def bits_to_bytes(bit_string: str) -> bytes:
    if len(bit_string) % 8 != 0:
        raise ValueError(f"bit string length is not byte-aligned: {len(bit_string)}")
    return bytes(int(bit_string[i : i + 8], 2) for i in range(0, len(bit_string), 8))


def decode_binary_base64(bit_string: str) -> dict[str, Any]:
    raw = bits_to_bytes(bit_string)
    result: dict[str, Any] = {
        "binary_length": len(bit_string),
        "base64_bytes_hex": raw.hex(),
        "base64_text": raw.decode("ascii", errors="replace"),
        "decoded_text": None,
        "flags": [],
        "error": None,
    }
    try:
        decoded = base64.b64decode(raw, validate=True)
        text = decoded.decode("utf-8", errors="replace")
        result["decoded_text"] = text
        result["decoded_hex"] = decoded.hex()
        result["flags"] = sorted(set(FLAG_RE.findall(text)))
    except Exception as exc:  # noqa: BLE001 - preserve decode error in evidence
        result["error"] = f"{type(exc).__name__}: {exc}"
    return result


def parse_first(pattern: str, text: str, description: str) -> str:
    match = re.search(pattern, text, re.S)
    if not match:
        raise SystemExit(f"could not parse {description}")
    return match.group(1)


def command_shuffle_oracle_solve(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    label = slug(args.label)
    prompt = args.prompt.encode()
    transcript_chunks: list[dict[str, Any]] = []

    with socket.create_connection((args.host, args.port), timeout=args.connect_timeout) as sock:
        banner_bytes = recv_until(sock, prompt, args.timeout, args.max_recv_bytes)
        banner = banner_bytes.decode("utf-8", errors="replace")
        transcript_chunks.append({"direction": "recv", "text": banner})
        shuffled = parse_first(args.target_regex, banner, "target shuffled binary")
        length = len(shuffled)
        ones = shuffled.count("1")
        zeros = shuffled.count("0")
        if ones == 0 or zeros == 0:
            raise SystemExit("target must contain both 0 and 1")
        columns = args.columns
        if columns is None:
            columns = 1
            while (1 << columns) < length:
                columns += 1
            columns += args.extra_columns

        codes = balanced_codes(length, ones, columns, args.code_seed)
        code_to_index = {code: index for index, code in enumerate(codes)}
        output_codes = [0] * length
        queries: list[dict[str, Any]] = []

        for bit in range(columns):
            mask = 1 << bit
            query = "".join("1" if code & mask else "0" for code in codes)
            if len(query) != length or query.count("1") != ones:
                raise SystemExit(f"internal query generation error at bit {bit}")
            sock.sendall(query.encode() + b"\n")
            response_bytes = recv_until(sock, prompt, args.timeout, args.max_recv_bytes)
            response = response_bytes.decode("utf-8", errors="replace")
            transcript_chunks.append({"direction": "send", "text": query})
            transcript_chunks.append({"direction": "recv", "text": response})
            output = parse_first(args.response_regex, response, f"oracle output for bit {bit}")
            if len(output) != length:
                raise SystemExit(f"oracle output length mismatch at bit {bit}: {len(output)} != {length}")
            if output.count("1") != ones:
                raise SystemExit(f"oracle output weight mismatch at bit {bit}: {output.count('1')} != {ones}")
            for index, char in enumerate(output):
                if char == "1":
                    output_codes[index] |= mask
            queries.append(
                {
                    "bit": bit,
                    "query": query if args.store_queries else None,
                    "output": output if args.store_queries else None,
                    "query_ones": query.count("1"),
                    "output_ones": output.count("1"),
                }
            )

    missing_codes = sorted(set(output_codes) - set(code_to_index))
    duplicate_output_codes = len(set(output_codes)) != length
    if missing_codes or duplicate_output_codes:
        raise SystemExit(
            f"could not reconstruct permutation: unknown_codes={len(missing_codes)}, duplicate_output_codes={duplicate_output_codes}"
        )

    original = ["?"] * length
    inverse_map: list[int] = []
    for output_index, code in enumerate(output_codes):
        original_index = code_to_index[code]
        inverse_map.append(original_index)
        original[original_index] = shuffled[output_index]
    original_bits = "".join(original)
    decoded = decode_binary_base64(original_bits)

    transcript_path = case_dir / "artifacts" / f"{label}-transcript.json"
    summary_path = case_dir / "artifacts" / f"{label}-shuffle-oracle.json"
    write_json(transcript_path, {"time": utc_now(), "chunks": transcript_chunks})
    summary = {
        "time": utc_now(),
        "host": args.host,
        "port": args.port,
        "target_shuffled": shuffled,
        "length": length,
        "ones": ones,
        "zeros": zeros,
        "columns": columns,
        "code_seed": args.code_seed,
        "queries": queries,
        "inverse_map": inverse_map if args.store_map else None,
        "original_bits": original_bits,
        "decoded": decoded,
        "transcript": str(transcript_path),
    }
    write_json(summary_path, summary)
    print(
        json.dumps(
            {
                "status": "ok",
                "summary": str(summary_path),
                "transcript": str(transcript_path),
                "length": length,
                "ones": ones,
                "columns": columns,
                "base64_text": decoded.get("base64_text"),
                "decoded_text": decoded.get("decoded_text"),
                "flags": decoded.get("flags", []),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Reusable raw TCP CTF interaction helpers")
    sub = parser.add_subparsers(dest="command", required=True)

    oracle = sub.add_parser(
        "shuffle-oracle-solve",
        help="recover a binary string hidden by a fixed shuffle oracle with equal-weight anagram queries",
    )
    oracle.add_argument("--case-dir", required=True)
    oracle.add_argument("--host", required=True)
    oracle.add_argument("--port", type=int, required=True)
    oracle.add_argument("--prompt", default="input encrypted flag's anagram: ")
    oracle.add_argument("--target-regex", default=r"shuffled encrypted flag:\s*([01]+)")
    oracle.add_argument("--response-regex", default=r"shuffled encrypted flag's anagram:\s*([01]+)")
    oracle.add_argument("--columns", type=int)
    oracle.add_argument("--extra-columns", type=int, default=8)
    oracle.add_argument("--code-seed", type=int, default=20260621)
    oracle.add_argument("--connect-timeout", type=float, default=10)
    oracle.add_argument("--timeout", type=float, default=10)
    oracle.add_argument("--max-recv-bytes", type=int, default=1024 * 1024)
    oracle.add_argument("--store-queries", action="store_true")
    oracle.add_argument("--store-map", action="store_true")
    oracle.add_argument("--label", default="shuffle-oracle")
    oracle.set_defaults(func=command_shuffle_oracle_solve)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
