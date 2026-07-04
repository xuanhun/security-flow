#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


FLAG_RE = re.compile(r"flag\{[^}\s]+\}", re.IGNORECASE)
SKILL_ROOT = Path(__file__).resolve().parents[1]
RUNTIME_ROOT = Path(os.environ.get("KALI_SKILL_RUNTIME", Path.home() / ".cache" / "kali-skill"))
PDF_RUNTIME = RUNTIME_ROOT / "pdf"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def ensure_pypdf():
    try:
        from pypdf import PdfReader  # type: ignore
        return PdfReader
    except Exception:
        pass

    PDF_RUNTIME.mkdir(parents=True, exist_ok=True)
    if str(PDF_RUNTIME) not in sys.path:
        sys.path.insert(0, str(PDF_RUNTIME))
    try:
        from pypdf import PdfReader  # type: ignore
        return PdfReader
    except Exception:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--quiet", "--target", str(PDF_RUNTIME), "pypdf"],
            check=True,
        )
        from pypdf import PdfReader  # type: ignore
        return PdfReader


def command_check_env(_args: argparse.Namespace) -> None:
    available = False
    error = None
    try:
        ensure_pypdf()
        available = True
    except Exception as exc:
        error = str(exc)
    print(
        json.dumps(
            {
                "python": sys.version.split()[0],
                "skill_root": str(SKILL_ROOT),
                "runtime_root": str(RUNTIME_ROOT),
                "pdf_runtime": str(PDF_RUNTIME),
                "pypdf_available": available,
                "error": error,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def command_extract_text(args: argparse.Namespace) -> None:
    PdfReader = ensure_pypdf()
    input_path = Path(args.input).expanduser().resolve()
    if not input_path.exists():
        raise SystemExit(f"missing PDF: {input_path}")

    output_path = Path(args.output).expanduser().resolve() if args.output else input_path.with_suffix(".extracted.txt")
    json_path = Path(args.json_out).expanduser().resolve() if args.json_out else input_path.with_suffix(".pdf-summary.json")
    reader = PdfReader(str(input_path))
    pages: list[dict[str, Any]] = []
    text_parts: list[str] = []
    for index, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        pages.append(
            {
                "page": index,
                "chars": len(text),
                "flags": sorted(set(FLAG_RE.findall(text))),
                "sample": text[:1000],
            }
        )
        text_parts.append(f"\n\n===== PAGE {index} =====\n{text}")

    full_text = "\n".join(text_parts)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(full_text, encoding="utf-8")
    flags = sorted(set(FLAG_RE.findall(full_text)))
    summary = {
        "time": utc_now(),
        "input": str(input_path),
        "output": str(output_path),
        "pages": len(reader.pages),
        "encrypted": bool(reader.is_encrypted),
        "metadata": {str(k): str(v) for k, v in (reader.metadata or {}).items()},
        "flags": flags,
        "page_summaries": pages,
    }
    write_json(json_path, summary)
    print(json.dumps({"status": "ok", "text": str(output_path), "summary": str(json_path), "flags": flags}, ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Reusable CTF PDF parsing tools")
    sub = parser.add_subparsers(dest="command", required=True)

    check = sub.add_parser("check-env", help="check and prepare PDF parsing runtime")
    check.set_defaults(func=command_check_env)

    extract = sub.add_parser("extract-text", help="extract PDF text and write a JSON summary")
    extract.add_argument("--input", required=True)
    extract.add_argument("--output")
    extract.add_argument("--json-out")
    extract.set_defaults(func=command_extract_text)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
