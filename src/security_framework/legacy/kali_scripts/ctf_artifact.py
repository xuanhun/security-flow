#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
import socket
import struct
import sys
import tarfile
import zipfile
import zlib
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from urllib.request import Request, urlopen


FLAG_RE = re.compile(rb"flag\{[^}\s]+\}", re.IGNORECASE)
PRINTABLE_RE = re.compile(rb"[\x20-\x7e]{4,}")
HTTP_METHOD_RE = re.compile(rb"^(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS|TRACE) ")


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


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def flags_from_bytes(data: bytes) -> list[str]:
    return sorted({item.decode("utf-8", errors="replace") for item in FLAG_RE.findall(data)})


def printable_strings(data: bytes, min_len: int = 4, limit: int = 200) -> list[str]:
    out: list[str] = []
    for match in PRINTABLE_RE.finditer(data):
        if len(match.group(0)) < min_len:
            continue
        out.append(match.group(0).decode("utf-8", errors="replace"))
        if len(out) >= limit:
            break
    return out


def read_input(path_value: str) -> Path:
    path = Path(path_value).expanduser().resolve()
    if not path.exists():
        raise SystemExit(f"missing input: {path}")
    return path


def command_inventory(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    data = input_path.read_bytes()
    output = case_dir / "artifacts" / f"{slug(args.label)}-inventory.json"
    summary = {
        "time": utc_now(),
        "input": str(input_path),
        "size": input_path.stat().st_size,
        "sha256": sha256_file(input_path),
        "magic_hex": data[:32].hex(),
        "flags": flags_from_bytes(data),
        "strings": printable_strings(data, args.min_len, args.max_strings),
    }
    write_json(output, summary)
    print(json.dumps({"status": "ok", "summary": str(output), "flags": summary["flags"]}, ensure_ascii=False, indent=2))


def safe_archive_path(root: Path, member_name: str) -> Path:
    name = member_name.replace("\\", "/")
    if name.startswith("/") or name.startswith("../") or "/../" in name or name == "..":
        raise ValueError(f"unsafe archive path: {member_name}")
    target = (root / name).resolve()
    root_resolved = root.resolve()
    if root_resolved != target and root_resolved not in target.parents:
        raise ValueError(f"archive path escapes output root: {member_name}")
    return target


def looks_text(data: bytes) -> bool:
    if not data:
        return True
    if b"\x00" in data[:4096]:
        return False
    sample = data[:4096]
    printable = sum(1 for byte in sample if byte in b"\n\r\t" or 32 <= byte <= 126)
    return printable / max(len(sample), 1) > 0.85


def command_zip_inspect(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    label = slug(args.label)
    extract_root = case_dir / "files" / f"{label}-zip" if args.extract else None
    entries: list[dict[str, Any]] = []
    all_flags: list[str] = []
    total_uncompressed = 0
    with zipfile.ZipFile(input_path) as archive:
        archive_comment = archive.comment.decode("utf-8", errors="replace")
        for info in archive.infolist():
            total_uncompressed += info.file_size
            is_dir = info.is_dir()
            entry: dict[str, Any] = {
                "name": info.filename,
                "is_dir": is_dir,
                "file_size": info.file_size,
                "compress_size": info.compress_size,
                "crc": f"{info.CRC:08x}",
                "date_time": list(info.date_time),
                "comment": info.comment.decode("utf-8", errors="replace"),
                "encrypted": bool(info.flag_bits & 0x1),
                "flags": flags_from_bytes(info.filename.encode()) + flags_from_bytes(info.comment),
                "strings": [],
                "sha256": None,
                "text_sample": "",
                "extracted_path": None,
            }
            if is_dir:
                entries.append(entry)
                continue
            if info.file_size > args.max_entry_bytes:
                entry["skipped"] = f"entry too large for inspection: {info.file_size}"
                entries.append(entry)
                continue
            if total_uncompressed > args.max_total_bytes:
                entry["skipped"] = f"archive exceeds max total bytes: {total_uncompressed}"
                entries.append(entry)
                continue
            try:
                data = archive.read(info)
            except RuntimeError as exc:
                entry["skipped"] = str(exc)
                entries.append(entry)
                continue
            entry["sha256"] = hashlib.sha256(data).hexdigest()
            entry_flags = flags_from_bytes(data)
            entry["flags"] = sorted(set(entry["flags"] + entry_flags))
            entry["strings"] = printable_strings(data, args.min_len, args.max_strings_per_file)
            if looks_text(data):
                entry["text_sample"] = data[: args.text_sample_bytes].decode("utf-8", errors="replace")
            all_flags.extend(entry["flags"])
            if extract_root:
                target = safe_archive_path(extract_root, info.filename)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                entry["extracted_path"] = str(target)
            entries.append(entry)
    summary_path = case_dir / "artifacts" / f"{label}-zip.json"
    summary = {
        "time": utc_now(),
        "input": str(input_path),
        "sha256": sha256_file(input_path),
        "size": input_path.stat().st_size,
        "archive_comment": archive_comment,
        "entries": entries,
        "entry_count": len(entries),
        "total_uncompressed": total_uncompressed,
        "extract_root": str(extract_root) if extract_root else None,
        "flags": sorted(set(all_flags)),
    }
    write_json(summary_path, summary)
    print(
        json.dumps(
            {
                "status": "ok",
                "summary": str(summary_path),
                "entries": len(entries),
                "extract_root": str(extract_root) if extract_root else None,
                "flags": summary["flags"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def command_tar_inspect(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    label = slug(args.label)
    extract_root = case_dir / "files" / f"{label}-tar" if args.extract else None
    entries: list[dict[str, Any]] = []
    all_flags: list[str] = []
    total_size = 0
    with tarfile.open(input_path) as archive:
        for member in archive.getmembers():
            total_size += member.size if member.isfile() else 0
            entry: dict[str, Any] = {
                "name": member.name,
                "type": member.type.decode("ascii", errors="replace")
                if isinstance(member.type, bytes)
                else str(member.type),
                "is_file": member.isfile(),
                "is_dir": member.isdir(),
                "is_link": member.islnk() or member.issym(),
                "size": member.size,
                "mtime": member.mtime,
                "mode": oct(member.mode),
                "uid": member.uid,
                "gid": member.gid,
                "uname": member.uname,
                "gname": member.gname,
                "linkname": member.linkname,
                "flags": flags_from_bytes(member.name.encode())
                + flags_from_bytes(member.linkname.encode()),
                "strings": [],
                "sha256": None,
                "text_sample": "",
                "extracted_path": None,
            }
            if not member.isfile():
                if extract_root and member.isdir():
                    safe_archive_path(extract_root, member.name).mkdir(parents=True, exist_ok=True)
                entries.append(entry)
                continue
            if member.size > args.max_entry_bytes:
                entry["skipped"] = f"entry too large for inspection: {member.size}"
                entries.append(entry)
                continue
            if total_size > args.max_total_bytes:
                entry["skipped"] = f"archive exceeds max total bytes: {total_size}"
                entries.append(entry)
                continue
            handle = archive.extractfile(member)
            if handle is None:
                entry["skipped"] = "could not read member"
                entries.append(entry)
                continue
            data = handle.read()
            entry["sha256"] = hashlib.sha256(data).hexdigest()
            entry_flags = flags_from_bytes(data)
            entry["flags"] = sorted(set(entry["flags"] + entry_flags))
            entry["strings"] = printable_strings(data, args.min_len, args.max_strings_per_file)
            if looks_text(data):
                entry["text_sample"] = data[: args.text_sample_bytes].decode("utf-8", errors="replace")
            all_flags.extend(entry["flags"])
            if extract_root:
                target = safe_archive_path(extract_root, member.name)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                entry["extracted_path"] = str(target)
            entries.append(entry)
    summary_path = case_dir / "artifacts" / f"{label}-tar.json"
    summary = {
        "time": utc_now(),
        "input": str(input_path),
        "sha256": sha256_file(input_path),
        "size": input_path.stat().st_size,
        "entries": entries,
        "entry_count": len(entries),
        "total_file_size": total_size,
        "extract_root": str(extract_root) if extract_root else None,
        "flags": sorted(set(all_flags)),
    }
    write_json(summary_path, summary)
    print(
        json.dumps(
            {
                "status": "ok",
                "summary": str(summary_path),
                "entries": len(entries),
                "extract_root": str(extract_root) if extract_root else None,
                "flags": summary["flags"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def headers_from_args(items: list[str] | None) -> dict[str, str]:
    headers = {"User-Agent": "kali-ctf-artifact/1.0"}
    for item in items or []:
        if ":" not in item:
            raise SystemExit(f"invalid header, expected name:value: {item}")
        name, value = item.split(":", 1)
        headers[name.strip()] = value.strip()
    return headers


def command_download_url(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    label = slug(args.label)
    parsed = urlparse(args.url)
    guessed = Path(parsed.path).name or f"{label}.bin"
    suffix = Path(guessed).suffix or ".bin"
    output = case_dir / "files" / f"{label}{suffix}"
    request = Request(args.url, headers=headers_from_args(args.header), method="GET")
    with urlopen(request, timeout=args.timeout) as response:
        output.write_bytes(response.read())
        response_headers = dict(response.headers.items())
        status = response.status
        final_url = response.geturl()
    data = output.read_bytes()
    summary_path = case_dir / "artifacts" / f"{label}-download.json"
    summary = {
        "time": utc_now(),
        "url": args.url,
        "final_url": final_url,
        "status": status,
        "headers": response_headers,
        "output": str(output),
        "size": output.stat().st_size,
        "sha256": sha256_file(output),
        "flags": flags_from_bytes(data),
        "strings": printable_strings(data, limit=100),
    }
    write_json(summary_path, summary)
    print(
        json.dumps(
            {"status": "ok", "file": str(output), "summary": str(summary_path), "flags": summary["flags"]},
            ensure_ascii=False,
            indent=2,
        )
    )


@dataclass
class Segment:
    seq: int
    data: bytes


def parse_ipv4_tcp(packet: bytes) -> dict[str, Any] | None:
    if len(packet) < 14:
        return None
    eth_type = struct.unpack("!H", packet[12:14])[0]
    offset = 14
    if eth_type == 0x8100 and len(packet) >= 18:
        eth_type = struct.unpack("!H", packet[16:18])[0]
        offset = 18
    if eth_type != 0x0800 or len(packet) < offset + 20:
        return None
    ip = packet[offset:]
    version_ihl = ip[0]
    if version_ihl >> 4 != 4:
        return None
    ihl = (version_ihl & 0x0F) * 4
    if len(ip) < ihl + 20 or ip[9] != 6:
        return None
    total_len = struct.unpack("!H", ip[2:4])[0]
    src_ip = socket.inet_ntoa(ip[12:16])
    dst_ip = socket.inet_ntoa(ip[16:20])
    tcp = ip[ihl:total_len]
    if len(tcp) < 20:
        return None
    src_port, dst_port, seq, _ack = struct.unpack("!HHII", tcp[:12])
    data_offset = (tcp[12] >> 4) * 4
    flags = tcp[13]
    if len(tcp) < data_offset:
        return None
    payload = tcp[data_offset:]
    if not payload:
        return None
    return {
        "src": src_ip,
        "dst": dst_ip,
        "src_port": src_port,
        "dst_port": dst_port,
        "seq": seq,
        "flags": flags,
        "payload": payload,
    }


def iter_pcapng_packets(path: Path) -> tuple[list[bytes], dict[str, Any]]:
    data = path.read_bytes()
    offset = 0
    endian = "<"
    linktypes: dict[int, int] = {}
    packets: list[bytes] = []
    block_counts: dict[str, int] = {}
    while offset + 12 <= len(data):
        block_type = struct.unpack(endian + "I", data[offset : offset + 4])[0]
        block_len = struct.unpack(endian + "I", data[offset + 4 : offset + 8])[0]
        if block_len < 12 or offset + block_len > len(data):
            break
        body = data[offset + 8 : offset + block_len - 4]
        block_counts[hex(block_type)] = block_counts.get(hex(block_type), 0) + 1
        if block_type == 0x0A0D0D0A and len(body) >= 4:
            bom_raw = body[:4]
            if bom_raw == b"\x4d\x3c\x2b\x1a":
                endian = "<"
            elif bom_raw == b"\x1a\x2b\x3c\x4d":
                endian = ">"
        elif block_type == 0x00000001 and len(body) >= 8:
            iface_id = len(linktypes)
            linktypes[iface_id] = struct.unpack(endian + "H", body[:2])[0]
        elif block_type == 0x00000006 and len(body) >= 20:
            iface_id, _ts_hi, _ts_lo, cap_len, _orig_len = struct.unpack(endian + "IIIII", body[:20])
            packet = body[20 : 20 + cap_len]
            if linktypes.get(iface_id, 1) == 1:
                packets.append(packet)
        elif block_type == 0x00000003 and len(body) >= 4:
            orig_len = struct.unpack(endian + "I", body[:4])[0]
            packets.append(body[4 : 4 + orig_len])
        offset += block_len
    return packets, {"block_counts": block_counts, "linktypes": linktypes, "packets": len(packets)}


def assemble_segments(segments: list[Segment]) -> bytes:
    if not segments:
        return b""
    ordered = sorted(segments, key=lambda item: item.seq)
    start = ordered[0].seq
    out = bytearray()
    for segment in ordered:
        rel = segment.seq - start
        if rel < 0:
            continue
        if rel > len(out):
            out.extend(b"\x00" * (rel - len(out)))
        overlap = len(out) - rel
        if overlap < len(segment.data):
            out.extend(segment.data[max(overlap, 0) :])
    return bytes(out)


def parse_headers(raw: bytes) -> tuple[str, dict[str, str]]:
    text = raw.decode("iso-8859-1", errors="replace")
    lines = text.split("\r\n")
    start = lines[0] if lines else ""
    headers: dict[str, str] = {}
    for line in lines[1:]:
        if ":" in line:
            name, value = line.split(":", 1)
            headers[name.lower()] = value.strip()
    return start, headers


def decode_body(body: bytes, headers: dict[str, str]) -> bytes:
    encoding = headers.get("content-encoding", "").lower()
    try:
        if "gzip" in encoding:
            return gzip.decompress(body)
        if "deflate" in encoding:
            return zlib.decompress(body)
    except Exception:
        return body
    return body


def read_chunked(data: bytes, start: int) -> tuple[bytes, int] | None:
    pos = start
    chunks: list[bytes] = []
    while True:
        line_end = data.find(b"\r\n", pos)
        if line_end == -1:
            return None
        size_text = data[pos:line_end].split(b";", 1)[0].strip()
        try:
            size = int(size_text, 16)
        except ValueError:
            return None
        pos = line_end + 2
        if len(data) < pos + size + 2:
            return None
        if size == 0:
            trailer_end = data.find(b"\r\n\r\n", pos)
            return b"".join(chunks), (trailer_end + 4 if trailer_end != -1 else pos + 2)
        chunks.append(data[pos : pos + size])
        pos += size + 2


def extract_http_messages(stream: bytes) -> list[dict[str, Any]]:
    messages: list[dict[str, Any]] = []
    pos = 0
    while pos < len(stream):
        candidates = [idx for idx in (stream.find(b"HTTP/1.", pos),) if idx != -1]
        for method in [b"GET ", b"POST ", b"PUT ", b"PATCH ", b"DELETE ", b"HEAD ", b"OPTIONS "]:
            idx = stream.find(method, pos)
            if idx != -1:
                candidates.append(idx)
        if not candidates:
            break
        start = min(candidates)
        header_end = stream.find(b"\r\n\r\n", start)
        if header_end == -1:
            break
        start_line, headers = parse_headers(stream[start:header_end])
        body_start = header_end + 4
        body = b""
        next_pos = body_start
        if start_line.startswith("HTTP/"):
            if "chunked" in headers.get("transfer-encoding", "").lower():
                chunked = read_chunked(stream, body_start)
                if chunked:
                    body, next_pos = chunked
            elif "content-length" in headers:
                try:
                    length = int(headers["content-length"])
                except ValueError:
                    length = 0
                body = stream[body_start : body_start + length]
                next_pos = body_start + length
            else:
                next_http = stream.find(b"HTTP/1.", body_start)
                body = stream[body_start : next_http if next_http != -1 else len(stream)]
                next_pos = next_http if next_http != -1 else len(stream)
        decoded = decode_body(body, headers)
        messages.append(
            {
                "start_line": start_line,
                "headers": headers,
                "body": body,
                "decoded_body": decoded,
                "is_response": start_line.startswith("HTTP/"),
                "is_request": bool(HTTP_METHOD_RE.match(start_line.encode("ascii", errors="ignore"))),
            }
        )
        pos = max(next_pos, start + 1)
    return messages


def extension_for(headers: dict[str, str], body: bytes) -> str:
    content_type = headers.get("content-type", "").lower()
    if "html" in content_type:
        return ".html"
    if "json" in content_type:
        return ".json"
    if "jpeg" in content_type:
        return ".jpg"
    if "png" in content_type:
        return ".png"
    if "mp4" in content_type or body[:8].endswith(b"ftyp"):
        return ".mp4"
    if "text" in content_type:
        return ".txt"
    return ".bin"


def command_pcapng_http(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    label = slug(args.label)
    packets, capture_meta = iter_pcapng_packets(input_path)
    flows: dict[tuple[str, int, str, int], list[Segment]] = {}
    tcp_payload_packets = 0
    for packet in packets:
        parsed = parse_ipv4_tcp(packet)
        if not parsed:
            continue
        tcp_payload_packets += 1
        key = (parsed["src"], parsed["src_port"], parsed["dst"], parsed["dst_port"])
        flows.setdefault(key, []).append(Segment(parsed["seq"], parsed["payload"]))

    http_items: list[dict[str, Any]] = []
    flags: list[str] = []
    for stream_index, (key, segments) in enumerate(sorted(flows.items()), 1):
        stream = assemble_segments(segments)
        if not stream:
            continue
        stream_flags = flags_from_bytes(stream)
        flags.extend(stream_flags)
        if args.save_streams:
            stream_path = case_dir / "artifacts" / f"{label}-stream-{stream_index:03d}.bin"
            stream_path.write_bytes(stream)
        messages = extract_http_messages(stream)
        for message_index, message in enumerate(messages, 1):
            body = message["decoded_body"]
            item_flags = flags_from_bytes(body)
            flags.extend(item_flags)
            body_path = None
            if message["is_response"] and body:
                suffix = extension_for(message["headers"], body)
                body_path = case_dir / "files" / f"{label}-http-{stream_index:03d}-{message_index:03d}{suffix}"
                body_path.write_bytes(body)
            http_items.append(
                {
                    "stream": stream_index,
                    "flow": {
                        "src": key[0],
                        "src_port": key[1],
                        "dst": key[2],
                        "dst_port": key[3],
                    },
                    "message": message_index,
                    "start_line": message["start_line"],
                    "is_response": message["is_response"],
                    "headers": message["headers"],
                    "body_size": len(body),
                    "body_sha256": hashlib.sha256(body).hexdigest() if body else None,
                    "body_path": str(body_path) if body_path else None,
                    "flags": item_flags,
                    "strings": printable_strings(body, limit=20) if args.strings else [],
                }
            )
    summary_path = case_dir / "artifacts" / f"{label}-pcapng-http.json"
    summary = {
        "time": utc_now(),
        "input": str(input_path),
        "sha256": sha256_file(input_path),
        "capture": capture_meta,
        "tcp_payload_packets": tcp_payload_packets,
        "flows": len(flows),
        "http_messages": http_items,
        "flags": sorted(set(flags)),
    }
    write_json(summary_path, summary)
    print(
        json.dumps(
            {
                "status": "ok",
                "summary": str(summary_path),
                "flows": len(flows),
                "http_messages": len(http_items),
                "flags": summary["flags"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def parse_mp4_boxes(data: bytes, start: int = 0, end: int | None = None, depth: int = 0, max_depth: int = 2) -> list[dict[str, Any]]:
    end = len(data) if end is None else min(end, len(data))
    boxes: list[dict[str, Any]] = []
    pos = start
    container_types = {b"moov", b"trak", b"mdia", b"minf", b"stbl", b"edts", b"udta", b"meta"}
    while pos + 8 <= end:
        size = struct.unpack(">I", data[pos : pos + 4])[0]
        box_type = data[pos + 4 : pos + 8]
        header = 8
        if size == 1 and pos + 16 <= end:
            size = struct.unpack(">Q", data[pos + 8 : pos + 16])[0]
            header = 16
        elif size == 0:
            size = end - pos
        if size < header or pos + size > end:
            break
        item: dict[str, Any] = {
            "type": box_type.decode("ascii", errors="replace"),
            "offset": pos,
            "size": size,
            "depth": depth,
        }
        if depth < max_depth and box_type in container_types:
            child_start = pos + header + (4 if box_type == b"meta" else 0)
            item["children"] = parse_mp4_boxes(data, child_start, pos + size, depth + 1, max_depth)
        boxes.append(item)
        pos += size
    return boxes


def command_mp4_inspect(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    data = input_path.read_bytes()
    output = case_dir / "artifacts" / f"{slug(args.label)}-mp4.json"
    summary = {
        "time": utc_now(),
        "input": str(input_path),
        "size": input_path.stat().st_size,
        "sha256": sha256_file(input_path),
        "flags": flags_from_bytes(data),
        "boxes": parse_mp4_boxes(data, max_depth=args.max_depth),
        "strings": printable_strings(data, args.min_len, args.max_strings),
    }
    write_json(output, summary)
    print(json.dumps({"status": "ok", "summary": str(output), "flags": summary["flags"]}, ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Reusable CTF artifact parsing tools")
    sub = parser.add_subparsers(dest="command", required=True)

    inventory = sub.add_parser("inventory", help="hash and string-scan a local artifact")
    inventory.add_argument("--case-dir", required=True)
    inventory.add_argument("--input", required=True)
    inventory.add_argument("--label", default="artifact")
    inventory.add_argument("--min-len", type=int, default=4)
    inventory.add_argument("--max-strings", type=int, default=200)
    inventory.set_defaults(func=command_inventory)

    download = sub.add_parser("download-url", help="download a binary URL into the case files directory")
    download.add_argument("--case-dir", required=True)
    download.add_argument("--url", required=True)
    download.add_argument("--label", default="download")
    download.add_argument("--header", action="append")
    download.add_argument("--timeout", type=int, default=60)
    download.set_defaults(func=command_download_url)

    zip_parser = sub.add_parser("zip-inspect", help="safely list, scan, and optionally extract a ZIP archive")
    zip_parser.add_argument("--case-dir", required=True)
    zip_parser.add_argument("--input", required=True)
    zip_parser.add_argument("--label", default="zip")
    zip_parser.add_argument("--extract", action="store_true")
    zip_parser.add_argument("--max-entry-bytes", type=int, default=5 * 1024 * 1024)
    zip_parser.add_argument("--max-total-bytes", type=int, default=50 * 1024 * 1024)
    zip_parser.add_argument("--min-len", type=int, default=4)
    zip_parser.add_argument("--max-strings-per-file", type=int, default=100)
    zip_parser.add_argument("--text-sample-bytes", type=int, default=2000)
    zip_parser.set_defaults(func=command_zip_inspect)

    tar_parser = sub.add_parser("tar-inspect", help="safely list, scan, and optionally extract a TAR archive")
    tar_parser.add_argument("--case-dir", required=True)
    tar_parser.add_argument("--input", required=True)
    tar_parser.add_argument("--label", default="tar")
    tar_parser.add_argument("--extract", action="store_true")
    tar_parser.add_argument("--max-entry-bytes", type=int, default=5 * 1024 * 1024)
    tar_parser.add_argument("--max-total-bytes", type=int, default=50 * 1024 * 1024)
    tar_parser.add_argument("--min-len", type=int, default=4)
    tar_parser.add_argument("--max-strings-per-file", type=int, default=100)
    tar_parser.add_argument("--text-sample-bytes", type=int, default=2000)
    tar_parser.set_defaults(func=command_tar_inspect)

    pcap = sub.add_parser("pcapng-http", help="extract HTTP streams and response bodies from Ethernet/IPv4/TCP pcapng")
    pcap.add_argument("--case-dir", required=True)
    pcap.add_argument("--input", required=True)
    pcap.add_argument("--label", default="pcap")
    pcap.add_argument("--save-streams", action="store_true")
    pcap.add_argument("--strings", action="store_true")
    pcap.set_defaults(func=command_pcapng_http)

    mp4 = sub.add_parser("mp4-inspect", help="inspect MP4 boxes, strings, hashes, and flags")
    mp4.add_argument("--case-dir", required=True)
    mp4.add_argument("--input", required=True)
    mp4.add_argument("--label", default="mp4")
    mp4.add_argument("--min-len", type=int, default=4)
    mp4.add_argument("--max-strings", type=int, default=300)
    mp4.add_argument("--max-depth", type=int, default=2)
    mp4.set_defaults(func=command_mp4_inspect)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
