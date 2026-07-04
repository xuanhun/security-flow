#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse


FLAG_RE = re.compile(r"flag\{[^}\s]+\}", re.IGNORECASE)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slug(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "oob"


def ensure_case(case_dir: str | Path) -> Path:
    path = Path(case_dir)
    path.mkdir(parents=True, exist_ok=True)
    for child in ["artifacts", "notes", "responses", "files"]:
        (path / child).mkdir(exist_ok=True)
    return path


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def append_jsonl(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(data, ensure_ascii=False, sort_keys=True) + "\n")
        handle.flush()


def flags_from_text(value: str) -> list[str]:
    return sorted(set(FLAG_RE.findall(value)))


class CallbackHandler(BaseHTTPRequestHandler):
    server_version = "kali-ctf-oob/1.0"

    def do_GET(self) -> None:  # noqa: N802
        self.server.record_request(self)  # type: ignore[attr-defined]
        self.server.write_response(self)  # type: ignore[attr-defined]

    def do_POST(self) -> None:  # noqa: N802
        self.server.record_request(self)  # type: ignore[attr-defined]
        self.server.write_response(self)  # type: ignore[attr-defined]

    def do_HEAD(self) -> None:  # noqa: N802
        self.server.record_request(self)  # type: ignore[attr-defined]
        self.server.write_response(self, include_body=False)  # type: ignore[attr-defined]

    def do_OPTIONS(self) -> None:  # noqa: N802
        self.server.record_request(self)  # type: ignore[attr-defined]
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, HEAD, OPTIONS")
        self.end_headers()

    def log_message(self, fmt: str, *args: Any) -> None:
        sys.stderr.write("%s - %s\n" % (self.log_date_time_string(), fmt % args))


class CallbackServer(ThreadingHTTPServer):
    def __init__(
        self,
        server_address: tuple[str, int],
        request_handler_class: type[BaseHTTPRequestHandler],
        *,
        log_path: Path,
        response_body: str,
        response_type: str,
    ) -> None:
        super().__init__(server_address, request_handler_class)
        self.log_path = log_path
        self.response_body = response_body.encode("utf-8")
        self.response_type = response_type

    def record_request(self, handler: BaseHTTPRequestHandler) -> None:
        length_header = handler.headers.get("Content-Length", "0")
        try:
            length = int(length_header)
        except ValueError:
            length = 0
        body_bytes = handler.rfile.read(length) if length > 0 else b""
        body = body_bytes.decode("utf-8", errors="replace")
        parsed = urlparse(handler.path)
        combined = "\n".join([handler.path, body, "\n".join(f"{k}: {v}" for k, v in handler.headers.items())])
        event = {
            "time": utc_now(),
            "client": handler.client_address[0],
            "client_port": handler.client_address[1],
            "method": handler.command,
            "path": handler.path,
            "url_path": parsed.path,
            "query": parse_qs(parsed.query, keep_blank_values=True),
            "headers": dict(handler.headers.items()),
            "body": body,
            "body_size": len(body_bytes),
            "flags": flags_from_text(combined),
        }
        append_jsonl(self.log_path, event)
        print(json.dumps(event, ensure_ascii=False, sort_keys=True), flush=True)

    def write_response(self, handler: BaseHTTPRequestHandler, *, include_body: bool = True) -> None:
        handler.send_response(200)
        handler.send_header("Content-Type", self.response_type)
        handler.send_header("Access-Control-Allow-Origin", "*")
        handler.send_header("Cache-Control", "no-store")
        handler.send_header("Content-Length", str(len(self.response_body) if include_body else 0))
        handler.end_headers()
        if include_body:
            handler.wfile.write(self.response_body)


def command_serve(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    label = slug(args.label)
    log_path = case_dir / "artifacts" / f"{label}-oob.jsonl"
    summary_path = case_dir / "artifacts" / f"{label}-oob-server.json"
    response_body = args.response_body
    response_file = None
    if args.response_file:
        response_file = Path(args.response_file).expanduser().resolve()
        if not response_file.exists():
            raise SystemExit(f"missing response file: {response_file}")
        response_body = response_file.read_text(encoding="utf-8")
    server = CallbackServer(
        (args.host, args.port),
        CallbackHandler,
        log_path=log_path,
        response_body=response_body,
        response_type=args.response_type,
    )
    summary = {
        "time": utc_now(),
        "host": args.host,
        "port": args.port,
        "label": label,
        "log_path": str(log_path),
        "response_file": str(response_file) if response_file else None,
        "response_type": args.response_type,
    }
    write_json(summary_path, summary)
    print(json.dumps({"status": "listening", "summary": str(summary_path), "log": str(log_path)}, indent=2), flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print(json.dumps({"status": "stopped", "log": str(log_path)}, indent=2), flush=True)
    finally:
        server.server_close()


def main() -> int:
    parser = argparse.ArgumentParser(description="Reusable CTF out-of-band callback tools")
    sub = parser.add_subparsers(dest="command", required=True)

    serve = sub.add_parser("serve", help="run a local HTTP callback logger")
    serve.add_argument("--case-dir", required=True)
    serve.add_argument("--label", default="callback")
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=9000)
    serve.add_argument("--response-body", default="ok")
    serve.add_argument("--response-file", help="serve response body from a UTF-8 file")
    serve.add_argument("--response-type", default="text/plain; charset=utf-8")
    serve.set_defaults(func=command_serve)

    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
