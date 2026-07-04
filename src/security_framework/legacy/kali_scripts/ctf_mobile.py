#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import plistlib
import re
import shutil
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.request import urlopen
from xml.etree import ElementTree as ET


FLAG_RE = re.compile(r"flag\{[^}\s]+\}", re.IGNORECASE)
PRINTABLE_RE = re.compile(rb"[\x20-\x7e]{4,}")
MOBILE_HINT_RE = re.compile(
    r"(flag|ctf|key|iv|aes|des|rc4|base64|decrypt|encrypt|password|secret|cipher|xor)",
    re.IGNORECASE,
)
ANDROID_NS = "{http://schemas.android.com/apk/res/android}"
JADX_VERSION = "1.5.5"
JADX_URL = f"https://github.com/skylot/jadx/releases/download/v{JADX_VERSION}/jadx-{JADX_VERSION}.zip"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slug(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "mobile"


def ensure_case(case_dir: str | Path) -> Path:
    path = Path(case_dir)
    path.mkdir(parents=True, exist_ok=True)
    for child in ["artifacts", "files", "notes", "responses"]:
        (path / child).mkdir(exist_ok=True)
    return path


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_input(path_value: str) -> Path:
    path = Path(path_value).expanduser().resolve()
    if not path.exists():
        raise SystemExit(f"missing input: {path}")
    return path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def printable_strings(data: bytes, min_len: int = 4, limit: int = 200) -> list[str]:
    out: list[str] = []
    for match in PRINTABLE_RE.finditer(data):
        if len(match.group(0)) < min_len:
            continue
        out.append(match.group(0).decode("utf-8", errors="replace"))
        if len(out) >= limit:
            break
    return out


def flags_from_text(text: str) -> list[str]:
    return sorted(set(FLAG_RE.findall(text)))


def flags_from_bytes(data: bytes) -> list[str]:
    return flags_from_text(data.decode("utf-8", errors="replace"))


def jsonable(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, bytes):
        return {"bytes_hex": value.hex(), "length": len(value)}
    if isinstance(value, datetime):
        return value.replace(microsecond=0).isoformat()
    return value


def parse_plist_bytes(data: bytes) -> dict[str, Any] | None:
    try:
        parsed = plistlib.loads(data)
    except Exception:
        return None
    if not isinstance(parsed, dict):
        return {"value": jsonable(parsed)}
    return jsonable(parsed)


def safe_zip_member_path(root: Path, member_name: str) -> Path:
    name = member_name.replace("\\", "/")
    if name.startswith("/") or name.startswith("../") or "/../" in name or name == "..":
        raise SystemExit(f"unsafe zip path: {member_name}")
    target = (root / name).resolve()
    root_resolved = root.resolve()
    if root_resolved != target and root_resolved not in target.parents:
        raise SystemExit(f"zip path escapes output root: {member_name}")
    return target


def macho_kind(data: bytes) -> str | None:
    magics = {
        b"\xcf\xfa\xed\xfe": "mach-o-64-le",
        b"\xfe\xed\xfa\xcf": "mach-o-64-be",
        b"\xce\xfa\xed\xfe": "mach-o-32-le",
        b"\xfe\xed\xfa\xce": "mach-o-32-be",
        b"\xca\xfe\xba\xbe": "fat-mach-o",
        b"\xbe\xba\xfe\xca": "fat-mach-o-le",
    }
    return magics.get(data[:4])


def interesting_mobile_strings(strings: list[str], limit: int = 200) -> list[str]:
    hits: list[str] = []
    for item in strings:
        compact = item.strip()
        if not compact:
            continue
        if MOBILE_HINT_RE.search(compact) or re.fullmatch(r"[A-Za-z0-9+/=_-]{16,}", compact):
            hits.append(compact)
        if len(hits) >= limit:
            break
    return hits


def safe_zip_extract(zip_path: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path) as archive:
        for info in archive.infolist():
            name = info.filename.replace("\\", "/")
            if name.startswith("/") or ".." in Path(name).parts:
                raise SystemExit(f"unsafe zip path: {info.filename}")
            target = output_dir / name
            if info.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.read(info))
    for candidate in (output_dir / "bin").glob("*"):
        candidate.chmod(candidate.stat().st_mode | 0o111)


def default_jadx_bin() -> Path:
    return Path.home() / ".cache" / "kali-skill" / "jadx" / f"jadx-{JADX_VERSION}" / "bin" / "jadx"


def ensure_jadx(download: bool) -> Path:
    env_bin = os.environ.get("JADX_BIN")
    candidates = [
        Path(env_bin).expanduser() if env_bin else None,
        default_jadx_bin(),
        Path(shutil.which("jadx") or ""),
    ]
    for candidate in candidates:
        if candidate and str(candidate) and candidate.exists() and os.access(candidate, os.X_OK):
            return candidate
    if not download:
        raise SystemExit("missing jadx; rerun with --download-jadx or set JADX_BIN")

    cache_root = Path.home() / ".cache" / "kali-skill" / "jadx"
    zip_path = cache_root / f"jadx-{JADX_VERSION}.zip"
    output_dir = cache_root / f"jadx-{JADX_VERSION}"
    cache_root.mkdir(parents=True, exist_ok=True)
    if not zip_path.exists():
        with urlopen(JADX_URL, timeout=60) as response:
            zip_path.write_bytes(response.read())
    safe_zip_extract(zip_path, output_dir)
    jadx_bin = output_dir / "bin" / "jadx"
    if not jadx_bin.exists():
        raise SystemExit(f"downloaded jadx but binary is missing: {jadx_bin}")
    return jadx_bin


def apk_entries(input_path: Path, string_limit: int = 20) -> tuple[list[dict[str, Any]], list[str]]:
    entries: list[dict[str, Any]] = []
    all_flags: list[str] = []
    with zipfile.ZipFile(input_path) as archive:
        for info in archive.infolist():
            entry: dict[str, Any] = {
                "name": info.filename,
                "is_dir": info.is_dir(),
                "file_size": info.file_size,
                "compress_size": info.compress_size,
                "crc": f"{info.CRC:08x}",
                "flags": flags_from_text(info.filename),
                "strings": [],
            }
            if not info.is_dir() and info.file_size <= 1024 * 1024:
                try:
                    data = archive.read(info)
                    entry["flags"] = sorted(set(entry["flags"] + flags_from_bytes(data)))
                    entry["strings"] = printable_strings(data, limit=string_limit)
                except RuntimeError as exc:
                    entry["error"] = str(exc)
            all_flags.extend(entry["flags"])
            entries.append(entry)
    return entries, sorted(set(all_flags))


def ipa_entries(
    input_path: Path,
    case_dir: Path,
    label: str,
    extract: bool,
    string_limit: int,
    max_entry_bytes: int,
    include_entries: bool,
) -> dict[str, Any]:
    extract_root = case_dir / "files" / f"{label}-ipa" if extract else None
    entries: list[dict[str, Any]] = []
    all_flags: list[str] = []
    plists: list[dict[str, Any]] = []
    executable_candidates: list[dict[str, Any]] = []
    app_dirs: set[str] = set()
    app_info: dict[str, Any] | None = None

    with zipfile.ZipFile(input_path) as archive:
        for info in archive.infolist():
            name = info.filename.replace("\\", "/")
            parts = Path(name).parts
            if len(parts) >= 2 and parts[0] == "Payload" and parts[1].endswith(".app"):
                app_dirs.add("/".join(parts[:2]))

            entry: dict[str, Any] = {
                "name": info.filename,
                "is_dir": info.is_dir(),
                "file_size": info.file_size,
                "compress_size": info.compress_size,
                "crc": f"{info.CRC:08x}",
                "flags": flags_from_text(info.filename),
                "strings": [],
                "interesting_strings": [],
                "sha256": None,
                "plist": None,
                "macho": None,
                "extracted_path": None,
            }
            if info.is_dir():
                entries.append(entry)
                continue
            if info.file_size <= max_entry_bytes:
                try:
                    data = archive.read(info)
                except RuntimeError as exc:
                    entry["error"] = str(exc)
                    entries.append(entry)
                    continue
                entry["sha256"] = hashlib.sha256(data).hexdigest()
                entry["flags"] = sorted(set(entry["flags"] + flags_from_bytes(data)))
                entry["strings"] = printable_strings(data, limit=string_limit)
                entry["interesting_strings"] = interesting_mobile_strings(entry["strings"])
                entry["macho"] = macho_kind(data)
                if name.endswith(".plist"):
                    parsed_plist = parse_plist_bytes(data)
                    if parsed_plist is not None:
                        entry["plist"] = parsed_plist
                        plist_item = {"path": name, "plist": parsed_plist}
                        plists.append(plist_item)
                        if name.count("/") == 2 and name.startswith("Payload/") and name.endswith(".app/Info.plist"):
                            app_info = plist_item
                if entry["macho"]:
                    executable_candidates.append(
                        {
                            "path": name,
                            "kind": entry["macho"],
                            "size": info.file_size,
                            "sha256": entry["sha256"],
                            "interesting_strings": entry["interesting_strings"],
                        }
                    )
                all_flags.extend(entry["flags"])
                if extract_root:
                    target = safe_zip_member_path(extract_root, info.filename)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(data)
                    entry["extracted_path"] = str(target)
            else:
                entry["skipped"] = f"entry too large for inspection: {info.file_size}"
            entries.append(entry)

    main_executable = None
    if app_info:
        plist_value = app_info.get("plist", {})
        app_root = str(app_info["path"]).rsplit("/", 1)[0]
        executable_name = plist_value.get("CFBundleExecutable") if isinstance(plist_value, dict) else None
        if executable_name:
            expected = f"{app_root}/{executable_name}"
            for candidate in executable_candidates:
                if candidate["path"] == expected:
                    main_executable = candidate
                    break

    return {
        "app_dirs": sorted(app_dirs),
        "app_info": app_info,
        "plist_count": len(plists),
        "plists": plists,
        "executable_candidates": executable_candidates,
        "main_executable": main_executable,
        "entries": entries if include_entries else [],
        "entry_count": len(entries),
        "extract_root": str(extract_root) if extract_root else None,
        "flags": sorted(set(all_flags)),
    }


def parse_decoded_manifest(manifest_path: Path) -> dict[str, Any]:
    if not manifest_path.exists():
        return {"path": str(manifest_path), "exists": False}
    root = ET.parse(manifest_path).getroot()
    package = root.attrib.get("package", "")
    app = root.find("application")
    components: list[dict[str, Any]] = []
    if app is not None:
        for tag in ["activity", "activity-alias", "service", "receiver", "provider"]:
            for element in app.findall(tag):
                name = element.attrib.get(ANDROID_NS + "name") or element.attrib.get("name") or ""
                exported = element.attrib.get(ANDROID_NS + "exported")
                permission = element.attrib.get(ANDROID_NS + "permission")
                filters = []
                for intent_filter in element.findall("intent-filter"):
                    filters.append(
                        {
                            "actions": [
                                item.attrib.get(ANDROID_NS + "name", "")
                                for item in intent_filter.findall("action")
                            ],
                            "categories": [
                                item.attrib.get(ANDROID_NS + "name", "")
                                for item in intent_filter.findall("category")
                            ],
                            "data": [dict(item.attrib) for item in intent_filter.findall("data")],
                        }
                    )
                components.append(
                    {
                        "type": tag,
                        "name": name,
                        "exported": exported,
                        "permission": permission,
                        "intent_filters": filters,
                    }
                )
    return {
        "path": str(manifest_path),
        "exists": True,
        "package": package,
        "components": components,
    }


def collect_source_flags(source_dir: Path, max_files: int = 20000) -> tuple[list[str], list[dict[str, Any]]]:
    flags: list[str] = []
    hits: list[dict[str, Any]] = []
    count = 0
    for path in source_dir.rglob("*"):
        if not path.is_file():
            continue
        count += 1
        if count > max_files:
            break
        if path.suffix.lower() not in {".java", ".kt", ".xml", ".txt", ".json", ".smali"}:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        found = flags_from_text(text)
        if found:
            flags.extend(found)
            hits.append({"path": str(path), "flags": found})
    return sorted(set(flags)), hits


def command_apk_summary(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    entries, flags = apk_entries(input_path, args.max_strings_per_file)
    dex_files = [entry for entry in entries if entry["name"].endswith(".dex")]
    summary_path = case_dir / "artifacts" / f"{slug(args.label)}-apk-summary.json"
    summary = {
        "time": utc_now(),
        "input": str(input_path),
        "size": input_path.stat().st_size,
        "sha256": sha256_file(input_path),
        "entry_count": len(entries),
        "dex_files": dex_files,
        "entries": entries if args.include_entries else [],
        "flags": flags,
    }
    write_json(summary_path, summary)
    print(json.dumps({"status": "ok", "summary": str(summary_path), "dex_files": len(dex_files), "flags": flags}, ensure_ascii=False, indent=2))


def command_ipa_summary(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    label = slug(args.label)
    ipa_summary = ipa_entries(
        input_path,
        case_dir,
        label,
        args.extract,
        args.max_strings_per_file,
        args.max_entry_bytes,
        args.include_entries,
    )
    summary_path = case_dir / "artifacts" / f"{label}-ipa-summary.json"
    summary = {
        "time": utc_now(),
        "input": str(input_path),
        "size": input_path.stat().st_size,
        "sha256": sha256_file(input_path),
        **ipa_summary,
    }
    write_json(summary_path, summary)
    print(
        json.dumps(
            {
                "status": "ok",
                "summary": str(summary_path),
                "entry_count": summary["entry_count"],
                "app_dirs": summary["app_dirs"],
                "main_executable": summary["main_executable"],
                "extract_root": summary["extract_root"],
                "flags": summary["flags"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def command_jadx_decompile(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    input_path = read_input(args.input)
    label = slug(args.label)
    jadx_bin = Path(args.jadx_bin).expanduser() if args.jadx_bin else ensure_jadx(args.download_jadx)
    output_dir = Path(args.output_dir).expanduser() if args.output_dir else case_dir / "files" / label
    if output_dir.exists() and args.clean:
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    command = [str(jadx_bin), "-d", str(output_dir), str(input_path)]
    proc = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    manifest = parse_decoded_manifest(output_dir / "resources" / "AndroidManifest.xml")
    flags, flag_hits = collect_source_flags(output_dir)
    summary_path = case_dir / "artifacts" / f"{label}-jadx.json"
    log_path = case_dir / "artifacts" / f"{label}-jadx.log"
    log_path.write_text(proc.stdout, encoding="utf-8", errors="replace")
    summary = {
        "time": utc_now(),
        "input": str(input_path),
        "output_dir": str(output_dir),
        "jadx_bin": str(jadx_bin),
        "command": command,
        "returncode": proc.returncode,
        "log": str(log_path),
        "manifest": manifest,
        "flags": flags,
        "flag_hits": flag_hits,
    }
    write_json(summary_path, summary)
    print(
        json.dumps(
            {
                "status": "ok" if proc.returncode in (0, 3) else "error",
                "summary": str(summary_path),
                "output_dir": str(output_dir),
                "returncode": proc.returncode,
                "components": len(manifest.get("components", [])),
                "flags": flags,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def command_source_grep(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    source_dir = Path(args.source_dir).expanduser()
    if not source_dir.exists():
        raise SystemExit(f"missing source dir: {source_dir}")
    patterns = [re.compile(pattern, re.IGNORECASE if args.ignore_case else 0) for pattern in args.pattern]
    hits: list[dict[str, Any]] = []
    for path in source_dir.rglob("*"):
        if not path.is_file():
            continue
        if args.ext and path.suffix.lower().lstrip(".") not in {item.lower().lstrip(".") for item in args.ext}:
            continue
        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for line_no, line in enumerate(lines, 1):
            matched = [pattern.pattern for pattern in patterns if pattern.search(line)]
            if matched:
                hits.append({"path": str(path), "line": line_no, "matched": matched, "text": line[:500]})
                if len(hits) >= args.max_hits:
                    break
        if len(hits) >= args.max_hits:
            break
    summary_path = case_dir / "artifacts" / f"{slug(args.label)}-source-grep.json"
    summary = {"time": utc_now(), "source_dir": str(source_dir), "patterns": args.pattern, "hits": hits}
    write_json(summary_path, summary)
    print(json.dumps({"status": "ok", "summary": str(summary_path), "hits": len(hits)}, ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Reusable CTF mobile/APK/IPA analysis tools")
    sub = parser.add_subparsers(dest="command", required=True)

    apk_summary = sub.add_parser("apk-summary", help="summarize APK entries, hashes, DEX files, and obvious flags")
    apk_summary.add_argument("--case-dir", required=True)
    apk_summary.add_argument("--input", required=True)
    apk_summary.add_argument("--label", default="apk")
    apk_summary.add_argument("--max-strings-per-file", type=int, default=20)
    apk_summary.add_argument("--include-entries", action="store_true")
    apk_summary.set_defaults(func=command_apk_summary)

    ipa_summary = sub.add_parser("ipa-summary", help="summarize IPA app bundle, plists, Mach-O files, and obvious flags")
    ipa_summary.add_argument("--case-dir", required=True)
    ipa_summary.add_argument("--input", required=True)
    ipa_summary.add_argument("--label", default="ipa")
    ipa_summary.add_argument("--extract", action="store_true")
    ipa_summary.add_argument("--max-entry-bytes", type=int, default=8 * 1024 * 1024)
    ipa_summary.add_argument("--max-strings-per-file", type=int, default=200)
    ipa_summary.add_argument("--include-entries", action="store_true")
    ipa_summary.set_defaults(func=command_ipa_summary)

    jadx = sub.add_parser("jadx-decompile", help="decompile an APK with skill-local jadx and summarize manifest components")
    jadx.add_argument("--case-dir", required=True)
    jadx.add_argument("--input", required=True)
    jadx.add_argument("--label", default="jadx")
    jadx.add_argument("--output-dir")
    jadx.add_argument("--jadx-bin")
    jadx.add_argument("--download-jadx", action="store_true")
    jadx.add_argument("--clean", action="store_true")
    jadx.set_defaults(func=command_jadx_decompile)

    grep = sub.add_parser("source-grep", help="grep decoded mobile sources and save matching evidence")
    grep.add_argument("--case-dir", required=True)
    grep.add_argument("--source-dir", required=True)
    grep.add_argument("--label", default="source-grep")
    grep.add_argument("--pattern", action="append", required=True)
    grep.add_argument("--ext", action="append", help="file extension filter, repeatable")
    grep.add_argument("--max-hits", type=int, default=200)
    grep.add_argument("--ignore-case", action="store_true")
    grep.set_defaults(func=command_source_grep)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
