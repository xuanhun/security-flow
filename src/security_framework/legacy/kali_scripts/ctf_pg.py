#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import socket
import struct
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


def flags_from_text(value: str) -> list[str]:
    return sorted(set(FLAG_RE.findall(value)))


def recv_exact(sock: socket.socket, size: int) -> bytes:
    data = bytearray()
    while len(data) < size:
        chunk = sock.recv(size - len(data))
        if not chunk:
            raise EOFError(f"socket closed while reading {size} bytes")
        data.extend(chunk)
    return bytes(data)


def read_message(sock: socket.socket) -> tuple[str, bytes]:
    message_type = recv_exact(sock, 1).decode("ascii", errors="replace")
    length = struct.unpack("!I", recv_exact(sock, 4))[0]
    if length < 4:
        raise ValueError(f"invalid PostgreSQL message length: {length}")
    return message_type, recv_exact(sock, length - 4)


def cstring(data: bytes, offset: int = 0) -> tuple[str, int]:
    end = data.index(b"\x00", offset)
    return data[offset:end].decode("utf-8", errors="replace"), end + 1


def parse_error(payload: bytes) -> dict[str, str]:
    names = {
        "S": "severity",
        "V": "severity_nonlocalized",
        "C": "sqlstate",
        "M": "message",
        "D": "detail",
        "H": "hint",
        "P": "position",
        "W": "where",
        "F": "file",
        "L": "line",
        "R": "routine",
    }
    out: dict[str, str] = {}
    offset = 0
    while offset < len(payload) and payload[offset] != 0:
        key = chr(payload[offset])
        value, offset = cstring(payload, offset + 1)
        out[names.get(key, key)] = value
    return out


def parse_row_description(payload: bytes) -> list[dict[str, Any]]:
    count = struct.unpack("!H", payload[:2])[0]
    offset = 2
    columns = []
    for _ in range(count):
        name, offset = cstring(payload, offset)
        table_oid, attr_num, type_oid, type_size, type_mod, fmt = struct.unpack("!IhIhih", payload[offset : offset + 18])
        offset += 18
        columns.append(
            {
                "name": name,
                "table_oid": table_oid,
                "attribute_number": attr_num,
                "type_oid": type_oid,
                "type_size": type_size,
                "type_modifier": type_mod,
                "format": fmt,
            }
        )
    return columns


def parse_data_row(payload: bytes) -> list[str | None]:
    count = struct.unpack("!H", payload[:2])[0]
    offset = 2
    values: list[str | None] = []
    for _ in range(count):
        length = struct.unpack("!i", payload[offset : offset + 4])[0]
        offset += 4
        if length == -1:
            values.append(None)
            continue
        raw = payload[offset : offset + length]
        offset += length
        values.append(raw.decode("utf-8", errors="replace"))
    return values


def startup_packet(
    user: str,
    database: str,
    application_name: str,
    extra_params: dict[str, str] | None = None,
) -> bytes:
    fields = [
        ("user", user),
        ("database", database),
        ("application_name", application_name),
        ("client_encoding", "UTF8"),
    ]
    if extra_params:
        fields.extend(sorted(extra_params.items()))
    params = b"".join(key.encode() + b"\x00" + value.encode() + b"\x00" for key, value in fields) + b"\x00"
    return struct.pack("!II", 4 + 4 + len(params), 196608) + params


def password_packet(password_response: str) -> bytes:
    payload = password_response.encode("utf-8") + b"\x00"
    return b"p" + struct.pack("!I", 4 + len(payload)) + payload


def simple_query_packet(query: str) -> bytes:
    payload = query.encode("utf-8") + b"\x00"
    return b"Q" + struct.pack("!I", 4 + len(payload)) + payload


def md5_response(verifier: str, salt: bytes) -> str:
    inner = verifier[3:] if verifier.startswith("md5") else verifier
    if not re.fullmatch(r"[0-9a-fA-F]{32}", inner):
        raise ValueError("md5 verifier must be md5-prefixed or a 32 hex character inner hash")
    return "md5" + hashlib.md5(inner.lower().encode("ascii") + salt).hexdigest()


def connect_pg(args: argparse.Namespace) -> tuple[socket.socket, dict[str, Any]]:
    transcript: dict[str, Any] = {
        "time": utc_now(),
        "host": args.host,
        "port": args.port,
        "user": args.user,
        "database": args.database,
        "auth": [],
        "parameters": {},
        "backend_key": None,
        "errors": [],
        "notices": [],
    }
    sock = socket.create_connection((args.host, args.port), timeout=args.connect_timeout)
    sock.settimeout(args.timeout)
    sock.sendall(startup_packet(args.user, args.database, args.application_name, dict(args.startup_param or [])))

    authenticated = False
    while True:
        message_type, payload = read_message(sock)
        if message_type == "R":
            code = struct.unpack("!I", payload[:4])[0]
            item: dict[str, Any] = {"type": "Authentication", "code": code}
            if code == 0:
                authenticated = True
            elif code == 5:
                salt = payload[4:8]
                item["method"] = "md5"
                item["salt_hex"] = salt.hex()
                if not args.md5_verifier:
                    raise SystemExit("server requested md5 authentication; pass --md5-verifier")
                sock.sendall(password_packet(md5_response(args.md5_verifier, salt)))
            elif code == 3:
                raise SystemExit("server requested cleartext password; this helper intentionally does not send one")
            else:
                item["unsupported"] = True
                raise SystemExit(f"unsupported authentication code: {code}")
            transcript["auth"].append(item)
        elif message_type == "S":
            key, offset = cstring(payload, 0)
            value, _ = cstring(payload, offset)
            transcript["parameters"][key] = value
        elif message_type == "K":
            pid, secret = struct.unpack("!II", payload)
            transcript["backend_key"] = {"pid": pid, "secret": secret}
        elif message_type == "E":
            error = parse_error(payload)
            transcript["errors"].append(error)
            raise RuntimeError(error.get("message", "PostgreSQL error"))
        elif message_type == "N":
            transcript["notices"].append(parse_error(payload))
        elif message_type == "Z":
            transcript["ready_status"] = payload.decode("ascii", errors="replace")
            if not authenticated:
                raise RuntimeError("server reached ReadyForQuery before AuthenticationOk")
            return sock, transcript
        else:
            transcript.setdefault("messages", []).append({"type": message_type, "payload_hex": payload[:128].hex()})


def run_query(sock: socket.socket, query: str) -> dict[str, Any]:
    sock.sendall(simple_query_packet(query))
    result: dict[str, Any] = {
        "columns": [],
        "rows": [],
        "command_complete": [],
        "errors": [],
        "notices": [],
        "ready_status": None,
    }
    while True:
        message_type, payload = read_message(sock)
        if message_type == "T":
            result["columns"] = parse_row_description(payload)
        elif message_type == "D":
            result["rows"].append(parse_data_row(payload))
        elif message_type == "C":
            tag, _ = cstring(payload, 0)
            result["command_complete"].append(tag)
        elif message_type == "E":
            result["errors"].append(parse_error(payload))
        elif message_type == "N":
            result["notices"].append(parse_error(payload))
        elif message_type == "Z":
            result["ready_status"] = payload.decode("ascii", errors="replace")
            return result
        else:
            result.setdefault("messages", []).append({"type": message_type, "payload_hex": payload[:128].hex()})


def command_query(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    label = slug(args.label)
    try:
        sock, connect_summary = connect_pg(args)
        with sock:
            query_result = run_query(sock, args.query)
    except Exception as exc:  # noqa: BLE001 - evidence should preserve protocol errors
        output = {
            "time": utc_now(),
            "host": args.host,
            "port": args.port,
            "user": args.user,
            "database": args.database,
            "query": args.query,
            "error": f"{type(exc).__name__}: {exc}",
        }
        summary_path = case_dir / "artifacts" / f"{label}-pg-query.json"
        write_json(summary_path, output)
        print(json.dumps({"status": "error", "summary": str(summary_path), "error": output["error"]}, indent=2))
        raise SystemExit(1) from exc

    text_blob = json.dumps(query_result, ensure_ascii=False)
    flags = flags_from_text(text_blob)
    summary = {
        "time": utc_now(),
        "connection": connect_summary,
        "query": args.query,
        "result": query_result,
        "flags": flags,
    }
    summary_path = case_dir / "artifacts" / f"{label}-pg-query.json"
    write_json(summary_path, summary)
    print(
        json.dumps(
            {
                "status": "ok",
                "summary": str(summary_path),
                "row_count": len(query_result["rows"]),
                "columns": [column["name"] for column in query_result["columns"]],
                "command_complete": query_result["command_complete"],
                "flags": flags,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Reusable PostgreSQL CTF protocol helpers")
    sub = parser.add_subparsers(dest="command", required=True)

    query = sub.add_parser("query", help="run one PostgreSQL simple-query request and save JSON evidence")
    query.add_argument("--case-dir", required=True)
    query.add_argument("--host", required=True)
    query.add_argument("--port", type=int, required=True)
    query.add_argument("--user", required=True)
    query.add_argument("--database", default="postgres")
    query.add_argument("--md5-verifier", help="stored md5 verifier, e.g. md5<32 hex>, for pass-the-hash auth")
    query.add_argument("--query", required=True)
    query.add_argument("--label", default="pg-query")
    query.add_argument("--application-name", default="ctf_pg")
    query.add_argument(
        "--startup-param",
        action="append",
        default=[],
        type=parse_key_value,
        metavar="KEY=VALUE",
        help="extra PostgreSQL startup parameter for HBA or protocol probes; repeatable",
    )
    query.add_argument("--connect-timeout", type=float, default=5)
    query.add_argument("--timeout", type=float, default=5)
    query.set_defaults(func=command_query)
    return parser


def parse_key_value(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("expected KEY=VALUE")
    key, item = value.split("=", 1)
    key = key.strip()
    if not key:
        raise argparse.ArgumentTypeError("startup parameter key cannot be empty")
    return key, item


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
