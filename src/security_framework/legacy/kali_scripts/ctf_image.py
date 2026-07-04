#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import struct
import sys
import zlib
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PNG_SIG = b"\x89PNG\r\n\x1a\n"
FLAG_RE = re.compile(rb"flag\{[^}\s]+\}", re.IGNORECASE)
PRINTABLE_RE = re.compile(rb"[\x20-\x7e]{4,}")
CHANNEL_INDEX = {"r": 0, "g": 1, "b": 2, "a": 3, "gray": 0}


@dataclass
class PngImage:
    width: int
    height: int
    color_type: int
    channels: int
    pixels: bytearray
    chunks: list[dict[str, Any]]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slug(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "image"


def ensure_case(case_dir: str | Path) -> Path:
    path = Path(case_dir)
    path.mkdir(parents=True, exist_ok=True)
    for child in ["artifacts", "responses", "notes", "files"]:
        (path / child).mkdir(exist_ok=True)
    return path


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


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


def jsonable_value(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, bytes):
        try:
            return value.decode("utf-8")
        except UnicodeDecodeError:
            return value.hex()
    if isinstance(value, dict):
        return {str(key): jsonable_value(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [jsonable_value(item) for item in value]
    try:
        return float(value)
    except Exception:
        return str(value)


def rational_to_float(value: Any) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, tuple) and len(value) == 2:
        numerator, denominator = value
        denominator_float = float(denominator)
        if denominator_float == 0:
            raise ValueError("EXIF rational denominator is zero")
        return float(numerator) / denominator_float
    numerator = getattr(value, "numerator", None)
    denominator = getattr(value, "denominator", None)
    if numerator is not None and denominator is not None:
        denominator_float = float(denominator)
        if denominator_float == 0:
            raise ValueError("EXIF rational denominator is zero")
        return float(numerator) / denominator_float
    return float(value)


def gps_dms_to_decimal(value: Any, ref: Any) -> float:
    if not isinstance(value, (list, tuple)) or len(value) != 3:
        raise ValueError(f"unexpected GPS DMS value: {value!r}")
    degrees = rational_to_float(value[0])
    minutes = rational_to_float(value[1])
    seconds = rational_to_float(value[2])
    decimal = degrees + minutes / 60.0 + seconds / 3600.0
    if str(ref).upper() in {"S", "W"}:
        decimal = -decimal
    return decimal


def out_of_china(lat: float, lon: float) -> bool:
    return lon < 72.004 or lon > 137.8347 or lat < 0.8293 or lat > 55.8271


def transform_lat(x: float, y: float) -> float:
    ret = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * math.sqrt(abs(x))
    ret += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(y * math.pi) + 40.0 * math.sin(y / 3.0 * math.pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(y / 12.0 * math.pi) + 320.0 * math.sin(y * math.pi / 30.0)) * 2.0 / 3.0
    return ret


def transform_lon(x: float, y: float) -> float:
    ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * math.sqrt(abs(x))
    ret += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(x * math.pi) + 40.0 * math.sin(x / 3.0 * math.pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(x / 12.0 * math.pi) + 300.0 * math.sin(x / 30.0 * math.pi)) * 2.0 / 3.0
    return ret


def wgs84_to_gcj02(lat: float, lon: float) -> tuple[float, float]:
    if out_of_china(lat, lon):
        return lat, lon
    a = 6378245.0
    ee = 0.00669342162296594323
    dlat = transform_lat(lon - 105.0, lat - 35.0)
    dlon = transform_lon(lon - 105.0, lat - 35.0)
    radlat = lat / 180.0 * math.pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrt_magic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrt_magic) * math.pi)
    dlon = (dlon * 180.0) / (a / sqrt_magic * math.cos(radlat) * math.pi)
    return lat + dlat, lon + dlon


def gcj02_to_bd09(lat: float, lon: float) -> tuple[float, float]:
    x_pi = math.pi * 3000.0 / 180.0
    z = math.sqrt(lon * lon + lat * lat) + 0.00002 * math.sin(lat * x_pi)
    theta = math.atan2(lat, lon) + 0.000003 * math.cos(lon * x_pi)
    bd_lon = z * math.cos(theta) + 0.0065
    bd_lat = z * math.sin(theta) + 0.006
    return bd_lat, bd_lon


def bd09_to_gcj02(lat: float, lon: float) -> tuple[float, float]:
    x_pi = math.pi * 3000.0 / 180.0
    x = lon - 0.0065
    y = lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gcj_lon = z * math.cos(theta)
    gcj_lat = z * math.sin(theta)
    return gcj_lat, gcj_lon


def map_urls(lat: float, lon: float) -> dict[str, str]:
    return {
        "google": f"https://maps.google.com/?q={lat:.8f},{lon:.8f}",
        "osm": f"https://www.openstreetmap.org/?mlat={lat:.8f}&mlon={lon:.8f}#map=18/{lat:.8f}/{lon:.8f}",
        "amap": f"https://uri.amap.com/marker?position={lon:.8f},{lat:.8f}",
        "baidu": f"https://api.map.baidu.com/marker?location={lat:.8f},{lon:.8f}&output=html",
    }


def coordinate_candidates(lat: float, lon: float) -> list[dict[str, Any]]:
    candidates = [
        {
            "label": "raw_exif",
            "lat": round(lat, 8),
            "lon": round(lon, 8),
            "note": "Use first on WGS84-style maps, or when the challenge/source says the stored coordinate is already map-provider ready.",
            "map_urls": map_urls(lat, lon),
        }
    ]
    if out_of_china(lat, lon):
        return candidates

    gcj_lat, gcj_lon = wgs84_to_gcj02(lat, lon)
    bd_lat_from_wgs, bd_lon_from_wgs = gcj02_to_bd09(gcj_lat, gcj_lon)
    bd_lat_from_gcj, bd_lon_from_gcj = gcj02_to_bd09(lat, lon)
    gcj_lat_from_bd, gcj_lon_from_bd = bd09_to_gcj02(lat, lon)
    candidates.extend(
        [
            {
                "label": "raw_wgs84_to_gcj02",
                "lat": round(gcj_lat, 8),
                "lon": round(gcj_lon, 8),
                "note": "Try on Amap/Tencent when raw EXIF is real GPS/WGS84 in mainland China.",
                "map_urls": map_urls(gcj_lat, gcj_lon),
            },
            {
                "label": "raw_wgs84_to_bd09",
                "lat": round(bd_lat_from_wgs, 8),
                "lon": round(bd_lon_from_wgs, 8),
                "note": "Try on Baidu when raw EXIF is real GPS/WGS84 in mainland China.",
                "map_urls": map_urls(bd_lat_from_wgs, bd_lon_from_wgs),
            },
            {
                "label": "raw_gcj02_to_bd09",
                "lat": round(bd_lat_from_gcj, 8),
                "lon": round(bd_lon_from_gcj, 8),
                "note": "Try on Baidu when raw EXIF already matches Amap/Tencent GCJ-02 coordinates.",
                "map_urls": map_urls(bd_lat_from_gcj, bd_lon_from_gcj),
            },
            {
                "label": "raw_bd09_to_gcj02",
                "lat": round(gcj_lat_from_bd, 8),
                "lon": round(gcj_lon_from_bd, 8),
                "note": "Try on Amap/Tencent when raw EXIF appears to be Baidu BD-09 coordinates.",
                "map_urls": map_urls(gcj_lat_from_bd, gcj_lon_from_bd),
            },
        ]
    )
    return candidates


def read_input(path_value: str) -> Path:
    path = Path(path_value).expanduser().resolve()
    if not path.exists():
        raise SystemExit(f"missing input: {path}")
    return path


def paeth(a: int, b: int, c: int) -> int:
    p = a + b - c
    pa = abs(p - a)
    pb = abs(p - b)
    pc = abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    if pb <= pc:
        return b
    return c


def channel_count(color_type: int) -> int:
    if color_type == 0:
        return 1
    if color_type == 2:
        return 3
    if color_type == 4:
        return 2
    if color_type == 6:
        return 4
    raise ValueError(f"unsupported PNG color type: {color_type}")


def parse_png(path: Path) -> PngImage:
    data = path.read_bytes()
    if not data.startswith(PNG_SIG):
        raise ValueError("input is not a PNG file")
    pos = len(PNG_SIG)
    chunks: list[dict[str, Any]] = []
    idat_parts: list[bytes] = []
    width = height = bit_depth = color_type = interlace = None
    while pos + 8 <= len(data):
        length = struct.unpack(">I", data[pos : pos + 4])[0]
        kind = data[pos + 4 : pos + 8]
        chunk_data = data[pos + 8 : pos + 8 + length]
        crc = data[pos + 8 + length : pos + 12 + length]
        if len(kind) != 4 or len(crc) != 4:
            raise ValueError("truncated PNG chunk")
        kind_text = kind.decode("ascii", errors="replace")
        chunks.append({"type": kind_text, "length": length, "crc": crc.hex()})
        if kind == b"IHDR":
            width, height, bit_depth, color_type, _compression, _filter, interlace = struct.unpack(
                ">IIBBBBB", chunk_data
            )
        elif kind == b"IDAT":
            idat_parts.append(chunk_data)
        elif kind == b"IEND":
            break
        pos += 12 + length

    if width is None or height is None or bit_depth is None or color_type is None or interlace is None:
        raise ValueError("missing IHDR")
    if bit_depth != 8:
        raise ValueError(f"only 8-bit PNGs are supported, got bit depth {bit_depth}")
    if interlace != 0:
        raise ValueError("interlaced PNGs are not supported")

    channels = channel_count(color_type)
    raw = zlib.decompress(b"".join(idat_parts))
    stride = width * channels
    expected = height * (stride + 1)
    if len(raw) < expected:
        raise ValueError(f"decompressed PNG data is shorter than expected: {len(raw)} < {expected}")

    out = bytearray(width * height * channels)
    src_pos = 0
    for y in range(height):
        filter_type = raw[src_pos]
        src_pos += 1
        row = bytearray(raw[src_pos : src_pos + stride])
        src_pos += stride
        prior = out[(y - 1) * stride : y * stride] if y else bytearray(stride)
        for x in range(stride):
            left = row[x - channels] if x >= channels else 0
            up = prior[x] if y else 0
            up_left = prior[x - channels] if y and x >= channels else 0
            if filter_type == 0:
                value = row[x]
            elif filter_type == 1:
                value = (row[x] + left) & 0xFF
            elif filter_type == 2:
                value = (row[x] + up) & 0xFF
            elif filter_type == 3:
                value = (row[x] + ((left + up) // 2)) & 0xFF
            elif filter_type == 4:
                value = (row[x] + paeth(left, up, up_left)) & 0xFF
            else:
                raise ValueError(f"unsupported PNG filter type: {filter_type}")
            row[x] = value
        out[y * stride : (y + 1) * stride] = row
    return PngImage(width, height, color_type, channels, out, chunks)


def read_png_idat(path: Path) -> tuple[int, int, int, int, int, list[dict[str, Any]], bytes]:
    data = path.read_bytes()
    if not data.startswith(PNG_SIG):
        raise ValueError("input is not a PNG file")
    pos = len(PNG_SIG)
    chunks: list[dict[str, Any]] = []
    idat_parts: list[bytes] = []
    width = height = bit_depth = color_type = interlace = None
    while pos + 8 <= len(data):
        length = struct.unpack(">I", data[pos : pos + 4])[0]
        kind = data[pos + 4 : pos + 8]
        chunk_data = data[pos + 8 : pos + 8 + length]
        crc = data[pos + 8 + length : pos + 12 + length]
        if len(kind) != 4 or len(crc) != 4:
            raise ValueError("truncated PNG chunk")
        chunks.append({"type": kind.decode("ascii", errors="replace"), "length": length, "crc": crc.hex()})
        if kind == b"IHDR":
            width, height, bit_depth, color_type, _compression, _filter, interlace = struct.unpack(
                ">IIBBBBB", chunk_data
            )
        elif kind == b"IDAT":
            idat_parts.append(chunk_data)
        elif kind == b"IEND":
            break
        pos += 12 + length

    if width is None or height is None or bit_depth is None or color_type is None or interlace is None:
        raise ValueError("missing IHDR")
    return width, height, bit_depth, color_type, interlace, chunks, b"".join(idat_parts)


def unfilter_rows(raw: bytes, width: int, height: int, channels: int) -> bytearray:
    stride = width * channels
    out = bytearray(width * height * channels)
    src_pos = 0
    for y in range(height):
        filter_type = raw[src_pos]
        src_pos += 1
        row = bytearray(raw[src_pos : src_pos + stride])
        src_pos += stride
        prior = out[(y - 1) * stride : y * stride] if y else bytearray(stride)
        for x in range(stride):
            left = row[x - channels] if x >= channels else 0
            up = prior[x] if y else 0
            up_left = prior[x - channels] if y and x >= channels else 0
            if filter_type == 0:
                value = row[x]
            elif filter_type == 1:
                value = (row[x] + left) & 0xFF
            elif filter_type == 2:
                value = (row[x] + up) & 0xFF
            elif filter_type == 3:
                value = (row[x] + ((left + up) // 2)) & 0xFF
            elif filter_type == 4:
                value = (row[x] + paeth(left, up, up_left)) & 0xFF
            else:
                raise ValueError(f"unsupported PNG filter type: {filter_type}")
            row[x] = value
        out[y * stride : (y + 1) * stride] = row
    return out


def png_iend_end_offset(data: bytes) -> int:
    if not data.startswith(PNG_SIG):
        raise ValueError("input is not a PNG file")
    pos = len(PNG_SIG)
    while pos + 12 <= len(data):
        length = struct.unpack(">I", data[pos : pos + 4])[0]
        kind = data[pos + 4 : pos + 8]
        end = pos + 12 + length
        if end > len(data):
            raise ValueError("truncated PNG chunk")
        if kind == b"IEND":
            return end
        pos = end
    raise ValueError("missing IEND")


def detect_magic(data: bytes) -> str:
    if data.startswith(PNG_SIG):
        return "png"
    if data.startswith(b"\x47"):
        return "mpeg-ts-or-data-with-ts-sync"
    if data.startswith(b"\xff\xd8\xff"):
        return "jpeg"
    if data.startswith(b"GIF8"):
        return "gif"
    if data.startswith(b"PK\x03\x04"):
        return "zip"
    if data.startswith(b"%PDF"):
        return "pdf"
    if len(data) >= 12 and data[4:8] == b"ftyp":
        return "mp4"
    return "unknown"


def write_gray_png(path: Path, width: int, height: int, pixels: bytes | bytearray) -> None:
    if len(pixels) != width * height:
        raise ValueError("gray PNG pixel buffer size mismatch")
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = bytearray()
    for y in range(height):
        rows.append(0)
        start = y * width
        rows.extend(pixels[start : start + width])
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 0, 0, 0, 0)
    body = png_chunk(b"IHDR", ihdr) + png_chunk(b"IDAT", zlib.compress(bytes(rows), 9)) + png_chunk(b"IEND", b"")
    path.write_bytes(PNG_SIG + body)


def write_png(path: Path, width: int, height: int, channels: int, pixels: bytes | bytearray) -> None:
    if channels == 1:
        write_gray_png(path, width, height, pixels)
        return
    if channels != 3:
        raise ValueError("only grayscale and RGB PNG output are supported")
    if len(pixels) != width * height * channels:
        raise ValueError("RGB PNG pixel buffer size mismatch")
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = bytearray()
    stride = width * channels
    for y in range(height):
        rows.append(0)
        start = y * stride
        rows.extend(pixels[start : start + stride])
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    body = png_chunk(b"IHDR", ihdr) + png_chunk(b"IDAT", zlib.compress(bytes(rows), 9)) + png_chunk(b"IEND", b"")
    path.write_bytes(PNG_SIG + body)


def png_chunk(kind: bytes, data: bytes) -> bytes:
    crc = zlib.crc32(kind + data) & 0xFFFFFFFF
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", crc)


def resolve_channel(image: PngImage, name: str) -> int:
    key = name.lower()
    if image.channels == 1:
        if key not in {"gray", "r", "g", "b"}:
            raise ValueError(f"unsupported channel for grayscale PNG: {name}")
        return 0
    if key not in CHANNEL_INDEX:
        raise ValueError(f"unknown channel: {name}")
    index = CHANNEL_INDEX[key]
    if index >= image.channels:
        raise ValueError(f"channel {name} not present in PNG")
    return index


def map_diff(diff: int, mode: str, gain: float) -> int:
    if mode == "centered":
        value = 128 + diff * gain
    elif mode == "positive":
        value = max(diff, 0) * gain
    elif mode == "negative":
        value = max(-diff, 0) * gain
    elif mode == "abs":
        value = abs(diff) * gain
    else:
        raise ValueError(f"unknown diff map mode: {mode}")
    return max(0, min(255, int(round(value))))


def percentile(sorted_values: list[int], percent: float) -> int:
    if not sorted_values:
        return 0
    percent = max(0.0, min(100.0, percent))
    index = round((len(sorted_values) - 1) * percent / 100.0)
    return sorted_values[int(index)]


def command_inspect(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    raw = input_path.read_bytes()
    image = parse_png(input_path)
    iend_offset = png_iend_end_offset(raw)
    appended = raw[iend_offset:]
    summary = {
        "time": utc_now(),
        "input": str(input_path),
        "size": input_path.stat().st_size,
        "sha256": sha256_file(input_path),
        "width": image.width,
        "height": image.height,
        "color_type": image.color_type,
        "channels": image.channels,
        "chunks": image.chunks,
        "iend_end_offset": iend_offset,
        "appended_bytes": len(appended),
        "appended_magic": detect_magic(appended) if appended else None,
        "flags": flags_from_bytes(raw),
        "strings": printable_strings(raw, args.min_len, args.max_strings),
    }
    output = case_dir / "artifacts" / f"{slug(args.label)}-image-inspect.json"
    write_json(output, summary)
    print(json.dumps({"status": "ok", "summary": str(output), "flags": summary["flags"]}, ensure_ascii=False, indent=2))


def command_extract_appended(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    raw = input_path.read_bytes()
    iend_offset = png_iend_end_offset(raw)
    appended = raw[iend_offset:]
    if len(appended) < args.min_bytes:
        raise ValueError(f"appended data too small: {len(appended)} < {args.min_bytes}")
    label = slug(args.label)
    suffix = args.ext if args.ext.startswith(".") else f".{args.ext}"
    output_path = case_dir / "files" / f"{label}-appended{suffix}"
    output_path.write_bytes(appended)
    flags = flags_from_bytes(appended)
    summary_path = case_dir / "artifacts" / f"{label}-extract-appended.json"
    write_json(
        summary_path,
        {
            "time": utc_now(),
            "input": str(input_path),
            "source_size": len(raw),
            "iend_end_offset": iend_offset,
            "appended_bytes": len(appended),
            "appended_magic": detect_magic(appended),
            "output": str(output_path),
            "output_sha256": hashlib.sha256(appended).hexdigest(),
            "flags": flags,
            "strings": printable_strings(appended, args.min_len, args.max_strings),
        },
    )
    print(
        json.dumps(
            {"status": "ok", "summary": str(summary_path), "output": str(output_path), "flags": flags},
            ensure_ascii=False,
            indent=2,
        )
    )


def command_render_partial(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    label = slug(args.label)
    width, declared_height, bit_depth, color_type, interlace, chunks, idat = read_png_idat(input_path)
    if bit_depth != 8:
        raise ValueError(f"only 8-bit PNGs are supported, got bit depth {bit_depth}")
    if interlace != 0:
        raise ValueError("interlaced PNGs are not supported")
    channels = channel_count(color_type)
    render_width = args.width or width
    render_channels = args.channels or channels
    target_height = args.height or declared_height
    if render_width <= 0 or target_height <= 0:
        raise ValueError("render dimensions must be positive")
    if render_channels not in {1, 3, 4}:
        raise ValueError("--channels must be 1, 3, or 4")
    raw = zlib.decompress(idat)
    stride = render_width * render_channels
    row_bytes = stride + 1
    available_rows = len(raw) // row_bytes
    partial_row_bytes = len(raw) % row_bytes
    render_height = min(target_height, available_rows)
    if render_height <= 0:
        raise ValueError("no complete PNG scanlines were available")
    pixels = unfilter_rows(raw[: render_height * row_bytes], render_width, render_height, render_channels)
    if render_channels == 4:
        rgb = bytearray(render_width * render_height * 3)
        for pos in range(render_width * render_height):
            src = pos * 4
            dst = pos * 3
            rgb[dst : dst + 3] = pixels[src : src + 3]
        output_channels = 3
        output_pixels: bytes | bytearray = rgb
    elif render_channels in {1, 3}:
        output_channels = render_channels
        output_pixels = pixels
    else:
        raise ValueError("partial render supports grayscale, RGB, and RGBA PNGs")
    output_path = case_dir / "files" / f"{label}-partial-{render_width}x{render_height}.png"
    write_png(output_path, render_width, render_height, output_channels, output_pixels)
    summary_path = case_dir / "artifacts" / f"{label}-render-partial.json"
    summary = {
        "time": utc_now(),
        "input": str(input_path),
        "sha256": sha256_file(input_path),
        "declared_width": width,
        "declared_height": declared_height,
        "rendered_width": render_width,
        "rendered_height": render_height,
        "bit_depth": bit_depth,
        "color_type": color_type,
        "channels": channels,
        "render_channels": render_channels,
        "idat_decompressed_bytes": len(raw),
        "expected_decompressed_bytes": target_height * row_bytes,
        "available_complete_rows": available_rows,
        "partial_row_bytes": partial_row_bytes,
        "chunks": chunks,
        "output": str(output_path),
        "output_sha256": sha256_file(output_path),
    }
    write_json(summary_path, summary)
    print(
        json.dumps(
            {"status": "ok", "summary": str(summary_path), "output": str(output_path)},
            ensure_ascii=False,
            indent=2,
        )
    )


def command_channel_diff(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    label = slug(args.label)
    image = parse_png(input_path)
    left = resolve_channel(image, args.left)
    right = resolve_channel(image, args.right)
    diffs = [
        image.pixels[pos * image.channels + left] - image.pixels[pos * image.channels + right]
        for pos in range(image.width * image.height)
    ]
    sorted_diffs = sorted(diffs)
    low = percentile(sorted_diffs, args.low_percentile)
    high = percentile(sorted_diffs, args.high_percentile)
    if high == low:
        high = low + 1
    modes = ["centered", "positive", "negative", "abs", "stretch"] if args.all_maps else [args.mode]
    outputs: list[dict[str, str]] = []
    for mode in modes:
        gray = bytearray(image.width * image.height)
        for pos, diff in enumerate(diffs):
            if mode == "stretch":
                value = (diff - low) * 255.0 / (high - low)
                gray[pos] = max(0, min(255, int(round(value))))
            else:
                gray[pos] = map_diff(diff, mode, args.gain)
        out_path = case_dir / "files" / f"{label}-{args.left.lower()}-minus-{args.right.lower()}-{mode}-g{args.gain:g}.png"
        write_gray_png(out_path, image.width, image.height, gray)
        outputs.append({"mode": mode, "path": str(out_path)})
    summary = {
        "time": utc_now(),
        "input": str(input_path),
        "left": args.left,
        "right": args.right,
        "gain": args.gain,
        "diff_min": sorted_diffs[0] if sorted_diffs else 0,
        "diff_max": sorted_diffs[-1] if sorted_diffs else 0,
        "low_percentile": args.low_percentile,
        "low_value": low,
        "high_percentile": args.high_percentile,
        "high_value": high,
        "outputs": outputs,
    }
    summary_path = case_dir / "artifacts" / f"{label}-channel-diff.json"
    write_json(summary_path, summary)
    print(json.dumps({"status": "ok", "summary": str(summary_path), "outputs": outputs}, ensure_ascii=False, indent=2))


def command_channel_band(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    label = slug(args.label)
    image = parse_png(input_path)
    left = resolve_channel(image, args.left)
    right = resolve_channel(image, args.right)
    if args.center is not None:
        if args.radius is None:
            raise ValueError("--radius is required when --center is used")
        min_diff = args.center - args.radius
        max_diff = args.center + args.radius
    else:
        if args.min_diff is None or args.max_diff is None:
            raise ValueError("provide either --center/--radius or --min-diff/--max-diff")
        min_diff = args.min_diff
        max_diff = args.max_diff
    if min_diff > max_diff:
        min_diff, max_diff = max_diff, min_diff

    gray = bytearray(image.width * image.height)
    matches = 0
    for pos in range(image.width * image.height):
        diff = image.pixels[pos * image.channels + left] - image.pixels[pos * image.channels + right]
        in_band = min_diff <= diff <= max_diff
        if args.invert:
            in_band = not in_band
        gray[pos] = 255 if in_band else 0
        if in_band:
            matches += 1

    out_path = case_dir / "files" / f"{label}-{args.left.lower()}-minus-{args.right.lower()}-band-{min_diff}-to-{max_diff}.png"
    write_gray_png(out_path, image.width, image.height, gray)
    summary_path = case_dir / "artifacts" / f"{label}-channel-band.json"
    write_json(
        summary_path,
        {
            "time": utc_now(),
            "input": str(input_path),
            "left": args.left,
            "right": args.right,
            "min_diff": min_diff,
            "max_diff": max_diff,
            "invert": args.invert,
            "matched_pixels": matches,
            "matched_ratio": round(matches / float(image.width * image.height), 6),
            "output": str(out_path),
        },
    )
    print(json.dumps({"status": "ok", "summary": str(summary_path), "output": str(out_path)}, ensure_ascii=False, indent=2))


def command_channel_mod(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    label = slug(args.label)
    image = parse_png(input_path)
    left = resolve_channel(image, args.left)
    right = resolve_channel(image, args.right)
    if args.modulus <= 0:
        raise ValueError("--modulus must be positive")
    if args.remainder < 0 or args.remainder >= args.modulus:
        raise ValueError("--remainder must be between 0 and modulus - 1")

    gray = bytearray(image.width * image.height)
    matches = 0
    for pos in range(image.width * image.height):
        diff = image.pixels[pos * image.channels + left] - image.pixels[pos * image.channels + right]
        in_class = diff % args.modulus == args.remainder
        if args.invert:
            in_class = not in_class
        gray[pos] = 255 if in_class else 0
        if in_class:
            matches += 1

    out_path = (
        case_dir
        / "files"
        / f"{label}-{args.left.lower()}-minus-{args.right.lower()}-mod{args.modulus}-eq{args.remainder}.png"
    )
    write_gray_png(out_path, image.width, image.height, gray)
    summary_path = case_dir / "artifacts" / f"{label}-channel-mod.json"
    write_json(
        summary_path,
        {
            "time": utc_now(),
            "input": str(input_path),
            "left": args.left,
            "right": args.right,
            "modulus": args.modulus,
            "remainder": args.remainder,
            "invert": args.invert,
            "matched_pixels": matches,
            "matched_ratio": round(matches / float(image.width * image.height), 6),
            "output": str(out_path),
        },
    )
    print(json.dumps({"status": "ok", "summary": str(summary_path), "output": str(out_path)}, ensure_ascii=False, indent=2))


def command_bitplanes(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    label = slug(args.label)
    image = parse_png(input_path)
    channels = args.channels.lower()
    if channels == "all":
        channel_names = ["gray"] if image.channels == 1 else ["r", "g", "b"] + (["a"] if image.channels == 4 else [])
    else:
        channel_names = [item.strip().lower() for item in channels.split(",") if item.strip()]
    outputs: list[dict[str, Any]] = []
    for channel_name in channel_names:
        channel = resolve_channel(image, channel_name)
        for bit in args.bits:
            gray = bytearray(image.width * image.height)
            for pos in range(image.width * image.height):
                base = pos * image.channels
                gray[pos] = 255 if image.pixels[base + channel] & (1 << bit) else 0
            out_path = case_dir / "files" / f"{label}-{channel_name}-bit{bit}.png"
            write_gray_png(out_path, image.width, image.height, gray)
            outputs.append({"channel": channel_name, "bit": bit, "path": str(out_path)})
    summary_path = case_dir / "artifacts" / f"{label}-bitplanes.json"
    write_json(
        summary_path,
        {
            "time": utc_now(),
            "input": str(input_path),
            "channels": channel_names,
            "bits": args.bits,
            "outputs": outputs,
        },
    )
    print(json.dumps({"status": "ok", "summary": str(summary_path), "outputs": outputs}, ensure_ascii=False, indent=2))


def command_raw_bgra_render(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    label = slug(args.label)
    raw = input_path.read_bytes()
    if args.width <= 0 or args.height <= 0:
        raise ValueError("render dimensions must be positive")
    offset = args.offset
    pixel_stride = args.width * 4
    row_stride = args.row_stride or pixel_stride
    if offset < 0:
        raise ValueError("--offset must be non-negative")
    if row_stride < pixel_stride:
        raise ValueError("--row-stride must be at least width * 4")
    needed = offset + row_stride * args.height
    if needed > len(raw):
        raise ValueError(f"input too small for requested layout: need {needed}, have {len(raw)}")

    order = args.order.lower()
    index = {name: pos for pos, name in enumerate(order)}
    if not {"r", "g", "b"}.issubset(index):
        raise ValueError("--order must include r, g, and b")

    rgb = bytearray(args.width * args.height * 3)
    padding = bytearray()
    padding_bytes_per_row = row_stride - pixel_stride
    for y in range(args.height):
        row_start = offset + y * row_stride
        visible = raw[row_start : row_start + pixel_stride]
        if padding_bytes_per_row:
            padding.extend(raw[row_start + pixel_stride : row_start + row_stride])
        for x in range(args.width):
            src = x * 4
            dst = (y * args.width + x) * 3
            rgb[dst] = visible[src + index["r"]]
            rgb[dst + 1] = visible[src + index["g"]]
            rgb[dst + 2] = visible[src + index["b"]]

    output_path = case_dir / "files" / f"{label}-raw-{args.width}x{args.height}.png"
    write_png(output_path, args.width, args.height, 3, rgb)
    padding_output = None
    if args.emit_padding and padding_bytes_per_row:
        padding_output_path = case_dir / "files" / f"{label}-padding-bytes-{padding_bytes_per_row}x{args.height}.png"
        write_gray_png(padding_output_path, padding_bytes_per_row, args.height, padding)
        padding_output = str(padding_output_path)

    summary_path = case_dir / "artifacts" / f"{label}-raw-bgra-render.json"
    write_json(
        summary_path,
        {
            "time": utc_now(),
            "input": str(input_path),
            "sha256": sha256_file(input_path),
            "width": args.width,
            "height": args.height,
            "offset": offset,
            "row_stride": row_stride,
            "pixel_stride": pixel_stride,
            "padding_bytes_per_row": padding_bytes_per_row,
            "order": args.order,
            "output": str(output_path),
            "output_sha256": sha256_file(output_path),
            "padding_output": padding_output,
            "flags": flags_from_bytes(rgb) + flags_from_bytes(padding),
        },
    )
    print(
        json.dumps(
            {"status": "ok", "summary": str(summary_path), "output": str(output_path), "padding_output": padding_output},
            ensure_ascii=False,
            indent=2,
        )
    )


def command_resize(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    label = slug(args.label)
    image = parse_png(input_path)
    if image.channels == 4:
        source_channels = 3
    elif image.channels in {1, 3}:
        source_channels = image.channels
    else:
        raise ValueError("resize supports grayscale, RGB, and RGBA PNGs")
    out = bytearray(args.width * args.height * source_channels)
    for y in range(args.height):
        src_y = min(image.height - 1, int(y * image.height / args.height))
        for x in range(args.width):
            src_x = min(image.width - 1, int(x * image.width / args.width))
            src_base = (src_y * image.width + src_x) * image.channels
            dst_base = (y * args.width + x) * source_channels
            out[dst_base : dst_base + source_channels] = image.pixels[src_base : src_base + source_channels]
    out_path = case_dir / "files" / f"{label}-{args.width}x{args.height}.png"
    write_png(out_path, args.width, args.height, source_channels, out)
    summary_path = case_dir / "artifacts" / f"{label}-resize.json"
    write_json(
        summary_path,
        {
            "time": utc_now(),
            "input": str(input_path),
            "source_width": image.width,
            "source_height": image.height,
            "output_width": args.width,
            "output_height": args.height,
            "output": str(out_path),
        },
    )
    print(json.dumps({"status": "ok", "summary": str(summary_path), "output": str(out_path)}, ensure_ascii=False, indent=2))


def command_crop(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    label = slug(args.label)
    image = parse_png(input_path)
    if args.x < 0 or args.y < 0 or args.width <= 0 or args.height <= 0:
        raise ValueError("crop coordinates must be non-negative and dimensions positive")
    if args.x + args.width > image.width or args.y + args.height > image.height:
        raise ValueError("crop rectangle exceeds image bounds")
    if image.channels == 4:
        out_channels = 3
    elif image.channels in {1, 3}:
        out_channels = image.channels
    else:
        raise ValueError("crop supports grayscale, RGB, and RGBA PNGs")
    out = bytearray(args.width * args.height * out_channels)
    for y in range(args.height):
        for x in range(args.width):
            src_base = ((args.y + y) * image.width + args.x + x) * image.channels
            dst_base = (y * args.width + x) * out_channels
            out[dst_base : dst_base + out_channels] = image.pixels[src_base : src_base + out_channels]
    out_path = case_dir / "files" / f"{label}-crop-x{args.x}-y{args.y}-w{args.width}-h{args.height}.png"
    write_png(out_path, args.width, args.height, out_channels, out)
    summary_path = case_dir / "artifacts" / f"{label}-crop.json"
    write_json(
        summary_path,
        {
            "time": utc_now(),
            "input": str(input_path),
            "x": args.x,
            "y": args.y,
            "width": args.width,
            "height": args.height,
            "output": str(out_path),
        },
    )
    print(json.dumps({"status": "ok", "summary": str(summary_path), "output": str(out_path)}, ensure_ascii=False, indent=2))


def bytes_from_bits(bits: list[int], msb_first: bool) -> bytes:
    out = bytearray()
    for i in range(0, len(bits) - 7, 8):
        value = 0
        chunk = bits[i : i + 8]
        if msb_first:
            for bit in chunk:
                value = (value << 1) | bit
        else:
            for offset, bit in enumerate(chunk):
                value |= bit << offset
        out.append(value)
    return bytes(out)


def command_lsb_scan(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    label = slug(args.label)
    image = parse_png(input_path)
    channel_names = [item.strip().lower() for item in args.channels.split(",") if item.strip()]
    channel_indexes = [resolve_channel(image, item) for item in channel_names]
    results: list[dict[str, Any]] = []
    for bit in args.bits:
        bits: list[int] = []
        for pos in range(image.width * image.height):
            base = pos * image.channels
            for channel in channel_indexes:
                bits.append((image.pixels[base + channel] >> bit) & 1)
        for msb_first in (True, False):
            payload = bytes_from_bits(bits, msb_first)
            strings = printable_strings(payload, args.min_len, args.max_strings)
            flags = flags_from_bytes(payload)
            results.append(
                {
                    "bit": bit,
                    "channels": channel_names,
                    "bit_order": "msb" if msb_first else "lsb",
                    "byte_count": len(payload),
                    "flags": flags,
                    "strings": strings,
                }
            )
    summary_path = case_dir / "artifacts" / f"{label}-lsb-scan.json"
    write_json(
        summary_path,
        {
            "time": utc_now(),
            "input": str(input_path),
            "channels": channel_names,
            "bits": args.bits,
            "results": results,
        },
    )
    flags = sorted({flag for result in results for flag in result["flags"]})
    print(json.dumps({"status": "ok", "summary": str(summary_path), "flags": flags}, ensure_ascii=False, indent=2))


def command_barcode_scan(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    label = slug(args.label)
    try:
        from PIL import Image, ImageOps
    except Exception as exc:  # pragma: no cover - depends on optional runtime package.
        raise RuntimeError("Pillow is required for barcode-scan") from exc

    try:
        import zxingcpp  # type: ignore[import-not-found]
    except Exception:
        zxingcpp = None

    try:
        import cv2  # type: ignore[import-not-found]
        import numpy as np  # type: ignore[import-not-found]
    except Exception:
        cv2 = None
        np = None

    if zxingcpp is None and cv2 is None:
        raise RuntimeError("barcode-scan requires zxingcpp or OpenCV")

    source = Image.open(input_path).convert("RGB")
    crop_box = None
    if args.x is not None or args.y is not None or args.width is not None or args.height is not None:
        if None in {args.x, args.y, args.width, args.height}:
            raise ValueError("--x, --y, --width, and --height must be provided together")
        if args.x < 0 or args.y < 0 or args.width <= 0 or args.height <= 0:
            raise ValueError("crop coordinates must be non-negative and dimensions positive")
        if args.x + args.width > source.width or args.y + args.height > source.height:
            raise ValueError("crop rectangle exceeds image bounds")
        crop_box = [args.x, args.y, args.x + args.width, args.y + args.height]
        source = source.crop(tuple(crop_box))

    scales = sorted({max(1, item) for item in args.scales})
    pads = sorted({max(0, item) for item in args.pads})
    rotations = sorted({item % 360 for item in args.rotations})
    thresholds = sorted({item for item in args.thresholds if 0 <= item <= 255})
    hits: list[dict[str, Any]] = []
    variants_scanned = 0
    variant_files: list[str] = []

    def record_hit(engine: str, variant: str, text: str, fmt: str = "", extra: dict[str, Any] | None = None) -> None:
        hit = {"engine": engine, "variant": variant, "format": fmt, "text": text}
        if extra:
            hit.update(extra)
        hits.append(hit)

    def scan_variant(variant_name: str, image: Any) -> None:
        nonlocal variants_scanned
        variants_scanned += 1
        if args.emit_variants:
            out_path = case_dir / "files" / f"{label}-barcode-{slug(variant_name)}.png"
            image.convert("RGB").save(out_path)
            variant_files.append(str(out_path))
        if zxingcpp is not None:
            try:
                for barcode in zxingcpp.read_barcodes(
                    image,
                    try_rotate=True,
                    try_downscale=True,
                    try_invert=True,
                    return_errors=args.return_errors,
                ):
                    text = getattr(barcode, "text", "") or ""
                    error = getattr(barcode, "error", "") or ""
                    fmt = str(getattr(barcode, "format", ""))
                    if text or error:
                        record_hit("zxingcpp", variant_name, text, fmt, {"error": str(error)})
            except Exception as exc:
                record_hit("zxingcpp-error", variant_name, "", "", {"error": str(exc)})
        if cv2 is not None and np is not None:
            detector = cv2.QRCodeDetector()
            gray = np.array(image.convert("L"))
            try:
                ok, decoded, _points, _straight = detector.detectAndDecodeMulti(gray)
                if ok:
                    for text in decoded:
                        if text:
                            record_hit("opencv-qrcode", variant_name, text, "QR_CODE")
            except Exception:
                text, _points, _straight = detector.detectAndDecode(gray)
                if text:
                    record_hit("opencv-qrcode", variant_name, text, "QR_CODE")

    for scale in scales:
        scaled = source.resize((source.width * scale, source.height * scale), Image.Resampling.NEAREST)
        for pad in pads:
            for pad_color in ("white", "black"):
                padded = ImageOps.expand(scaled, border=pad, fill=pad_color)
                gray = padded.convert("L")
                variants: list[tuple[str, Any]] = [
                    (f"s{scale}-p{pad}-{pad_color}-rgb", padded),
                    (f"s{scale}-p{pad}-{pad_color}-gray", gray),
                    (f"s{scale}-p{pad}-{pad_color}-invert", ImageOps.invert(gray)),
                ]
                for threshold in thresholds:
                    binary = gray.point(lambda value, t=threshold: 255 if value >= t else 0)
                    variants.append((f"s{scale}-p{pad}-{pad_color}-thr{threshold}", binary))
                    variants.append((f"s{scale}-p{pad}-{pad_color}-thr{threshold}-invert", ImageOps.invert(binary)))
                for name, variant in variants:
                    for rotation in rotations:
                        rotated = variant.rotate(rotation, expand=True) if rotation else variant
                        scan_variant(f"{name}-rot{rotation}", rotated)

    unique_hits: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str, str]] = set()
    for hit in hits:
        key = (hit.get("engine", ""), hit.get("format", ""), hit.get("text", ""), hit.get("error", ""))
        if key in seen:
            continue
        seen.add(key)
        unique_hits.append(hit)

    summary_path = case_dir / "artifacts" / f"{label}-barcode-scan.json"
    write_json(
        summary_path,
        {
            "time": utc_now(),
            "input": str(input_path),
            "sha256": sha256_file(input_path),
            "crop_box": crop_box,
            "source_width": source.width,
            "source_height": source.height,
            "engines": {
                "zxingcpp": zxingcpp is not None,
                "opencv_qrcode": cv2 is not None,
            },
            "scales": scales,
            "pads": pads,
            "rotations": rotations,
            "thresholds": thresholds,
            "variants_scanned": variants_scanned,
            "hits": unique_hits,
            "variant_files": variant_files,
        },
    )
    print(
        json.dumps(
            {"status": "ok", "summary": str(summary_path), "hits": unique_hits, "variants_scanned": variants_scanned},
            ensure_ascii=False,
            indent=2,
        )
    )


def command_exif_gps(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    label = slug(args.label)
    try:
        from PIL import ExifTags, Image
    except Exception as exc:  # pragma: no cover - depends on optional runtime package.
        raise RuntimeError("Pillow is required for exif-gps") from exc

    with Image.open(input_path) as image:
        exif = image.getexif()
        tag_names = getattr(ExifTags, "TAGS", {})
        gps_tag_names = getattr(ExifTags, "GPSTAGS", {})
        exif_fields: dict[str, Any] = {}
        for tag_id, value in exif.items():
            name = tag_names.get(tag_id, str(tag_id))
            if name == "GPSInfo":
                continue
            exif_fields[name] = jsonable_value(value)

        gps_info_raw: dict[Any, Any] = {}
        gps_ifd = getattr(ExifTags, "IFD", None)
        gps_ifd_id = getattr(gps_ifd, "GPSInfo", 34853)
        try:
            gps_info_raw = dict(exif.get_ifd(gps_ifd_id))
        except Exception:
            gps_value = exif.get(34853, {})
            if isinstance(gps_value, dict):
                gps_info_raw = gps_value

        gps_info = {gps_tag_names.get(key, str(key)): jsonable_value(value) for key, value in gps_info_raw.items()}
        decimal: dict[str, float] | None = None
        candidates: list[dict[str, Any]] = []
        if {"GPSLatitude", "GPSLatitudeRef", "GPSLongitude", "GPSLongitudeRef"}.issubset(gps_info):
            lat = gps_dms_to_decimal(gps_info_raw.get(2), gps_info_raw.get(1))
            lon = gps_dms_to_decimal(gps_info_raw.get(4), gps_info_raw.get(3))
            decimal = {"lat": round(lat, 8), "lon": round(lon, 8)}
            candidates = coordinate_candidates(lat, lon)

        summary = {
            "time": utc_now(),
            "input": str(input_path),
            "size": input_path.stat().st_size,
            "sha256": sha256_file(input_path),
            "format": image.format,
            "mode": image.mode,
            "width": image.width,
            "height": image.height,
            "has_exif": bool(exif),
            "exif": exif_fields,
            "gps": gps_info,
            "decimal": decimal,
            "coordinate_candidates": candidates,
            "flags": flags_from_bytes(input_path.read_bytes()),
        }
    summary_path = case_dir / "artifacts" / f"{label}-exif-gps.json"
    write_json(summary_path, summary)
    print(
        json.dumps(
            {"status": "ok", "summary": str(summary_path), "coordinates": decimal, "candidate_count": len(candidates)},
            ensure_ascii=False,
            indent=2,
        )
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Reusable CTF image forensics and PNG watermark tools")
    sub = parser.add_subparsers(dest="command", required=True)

    exif_gps = sub.add_parser("exif-gps", help="extract EXIF GPS coordinates from JPG/TIFF images")
    exif_gps.add_argument("--case-dir", required=True)
    exif_gps.add_argument("--input", required=True)
    exif_gps.add_argument("--label", default="exif-gps")
    exif_gps.set_defaults(func=command_exif_gps)

    inspect = sub.add_parser("inspect", help="inspect PNG metadata, chunks, strings, and flags")
    inspect.add_argument("--case-dir", required=True)
    inspect.add_argument("--input", required=True)
    inspect.add_argument("--label", default="image")
    inspect.add_argument("--min-len", type=int, default=4)
    inspect.add_argument("--max-strings", type=int, default=200)
    inspect.set_defaults(func=command_inspect)

    appended = sub.add_parser("extract-appended", help="extract bytes appended after a PNG IEND chunk")
    appended.add_argument("--case-dir", required=True)
    appended.add_argument("--input", required=True)
    appended.add_argument("--label", default="appended")
    appended.add_argument("--ext", default="bin")
    appended.add_argument("--min-bytes", type=int, default=1)
    appended.add_argument("--min-len", type=int, default=4)
    appended.add_argument("--max-strings", type=int, default=200)
    appended.set_defaults(func=command_extract_appended)

    partial = sub.add_parser("render-partial", help="render complete scanlines from a truncated or height-mismatched PNG")
    partial.add_argument("--case-dir", required=True)
    partial.add_argument("--input", required=True)
    partial.add_argument("--label", default="partial")
    partial.add_argument("--width", type=int, help="override PNG IHDR width when row boundaries are corrupted")
    partial.add_argument("--height", type=int, help="override PNG IHDR height when row boundaries are corrupted")
    partial.add_argument("--channels", type=int, help="override channel count used for row decoding")
    partial.set_defaults(func=command_render_partial)

    diff = sub.add_parser("channel-diff", help="render one image channel minus another")
    diff.add_argument("--case-dir", required=True)
    diff.add_argument("--input", required=True)
    diff.add_argument("--label", default="channel-diff")
    diff.add_argument("--left", default="B")
    diff.add_argument("--right", default="R")
    diff.add_argument("--mode", choices=["centered", "positive", "negative", "abs", "stretch"], default="centered")
    diff.add_argument("--gain", type=float, default=1.0)
    diff.add_argument("--low-percentile", type=float, default=1.0)
    diff.add_argument("--high-percentile", type=float, default=99.0)
    diff.add_argument("--all-maps", action="store_true")
    diff.set_defaults(func=command_channel_diff)

    band = sub.add_parser("channel-band", help="render a binary mask for pixels whose channel difference falls in a target band")
    band.add_argument("--case-dir", required=True)
    band.add_argument("--input", required=True)
    band.add_argument("--label", default="channel-band")
    band.add_argument("--left", default="B")
    band.add_argument("--right", default="R")
    band.add_argument("--min-diff", type=int)
    band.add_argument("--max-diff", type=int)
    band.add_argument("--center", type=int)
    band.add_argument("--radius", type=int)
    band.add_argument("--invert", action="store_true")
    band.set_defaults(func=command_channel_band)

    mod = sub.add_parser("channel-mod", help="render a binary mask for a channel difference modulo class")
    mod.add_argument("--case-dir", required=True)
    mod.add_argument("--input", required=True)
    mod.add_argument("--label", default="channel-mod")
    mod.add_argument("--left", default="B")
    mod.add_argument("--right", default="R")
    mod.add_argument("--modulus", type=int, default=2)
    mod.add_argument("--remainder", type=int, default=1)
    mod.add_argument("--invert", action="store_true")
    mod.set_defaults(func=command_channel_mod)

    bitplanes = sub.add_parser("bitplanes", help="extract PNG channel bit planes as grayscale images")
    bitplanes.add_argument("--case-dir", required=True)
    bitplanes.add_argument("--input", required=True)
    bitplanes.add_argument("--label", default="bitplanes")
    bitplanes.add_argument("--channels", default="all", help="all or comma-separated r,g,b,a,gray")
    bitplanes.add_argument("--bits", type=int, nargs="+", default=list(range(8)), help="bit indexes, 0 is LSB")
    bitplanes.set_defaults(func=command_bitplanes)

    raw_bgra = sub.add_parser("raw-bgra-render", help="render raw 4-byte pixel rows with optional row padding")
    raw_bgra.add_argument("--case-dir", required=True)
    raw_bgra.add_argument("--input", required=True)
    raw_bgra.add_argument("--label", default="raw-bgra")
    raw_bgra.add_argument("--width", type=int, required=True)
    raw_bgra.add_argument("--height", type=int, required=True)
    raw_bgra.add_argument("--offset", type=int, default=0)
    raw_bgra.add_argument("--row-stride", type=int, help="bytes per source row, including padding")
    raw_bgra.add_argument("--order", default="bgra", help="four-byte channel order such as bgra or rgba")
    raw_bgra.add_argument("--emit-padding", action="store_true")
    raw_bgra.set_defaults(func=command_raw_bgra_render)

    resize = sub.add_parser("resize", help="resize a PNG with nearest-neighbor sampling")
    resize.add_argument("--case-dir", required=True)
    resize.add_argument("--input", required=True)
    resize.add_argument("--label", default="resize")
    resize.add_argument("--width", type=int, default=256)
    resize.add_argument("--height", type=int, default=256)
    resize.set_defaults(func=command_resize)

    crop = sub.add_parser("crop", help="crop a PNG region for close visual inspection")
    crop.add_argument("--case-dir", required=True)
    crop.add_argument("--input", required=True)
    crop.add_argument("--label", default="crop")
    crop.add_argument("--x", type=int, required=True)
    crop.add_argument("--y", type=int, required=True)
    crop.add_argument("--width", type=int, required=True)
    crop.add_argument("--height", type=int, required=True)
    crop.set_defaults(func=command_crop)

    lsb = sub.add_parser("lsb-scan", help="scan low bit planes for printable strings and flags")
    lsb.add_argument("--case-dir", required=True)
    lsb.add_argument("--input", required=True)
    lsb.add_argument("--label", default="lsb")
    lsb.add_argument("--channels", default="r,g,b")
    lsb.add_argument("--bits", type=int, nargs="+", default=[0, 1])
    lsb.add_argument("--min-len", type=int, default=4)
    lsb.add_argument("--max-strings", type=int, default=200)
    lsb.set_defaults(func=command_lsb_scan)

    barcode = sub.add_parser("barcode-scan", help="scan image or crop with zxingcpp/OpenCV after common transforms")
    barcode.add_argument("--case-dir", required=True)
    barcode.add_argument("--input", required=True)
    barcode.add_argument("--label", default="barcode")
    barcode.add_argument("--x", type=int)
    barcode.add_argument("--y", type=int)
    barcode.add_argument("--width", type=int)
    barcode.add_argument("--height", type=int)
    barcode.add_argument("--scales", type=int, nargs="+", default=[1, 2, 4, 8, 16])
    barcode.add_argument("--pads", type=int, nargs="+", default=[0, 8, 24, 64])
    barcode.add_argument("--rotations", type=int, nargs="+", default=[0, 90, 180, 270])
    barcode.add_argument("--thresholds", type=int, nargs="+", default=[64, 96, 128, 160, 192, 224])
    barcode.add_argument("--return-errors", action="store_true", help="include decoder error objects when available")
    barcode.add_argument("--emit-variants", action="store_true", help="save every transformed image under files/")
    barcode.set_defaults(func=command_barcode_scan)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        args.func(args)
    except Exception as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
