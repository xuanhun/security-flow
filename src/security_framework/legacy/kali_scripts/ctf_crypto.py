#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import binascii
import json
import math
import re
import string
import unicodedata
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from typing import Any


FLAG_RE = re.compile(r"flag\{[^}\s]+\}", re.IGNORECASE)
WORD_RE = re.compile(r"[A-Za-z0-9]+")
UNICODE_WORD_RE = re.compile(r"[^\W_]+", re.UNICODE)
TAG_RE = re.compile(r"<[^>]+>")
ALPHABETS = {
    "upper": string.ascii_uppercase,
    "lower": string.ascii_lowercase,
    "alpha": string.ascii_letters,
    "base62": string.ascii_uppercase + string.ascii_lowercase + string.digits,
    "base64": string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/",
    "base64url": string.ascii_uppercase + string.ascii_lowercase + string.digits + "-_",
    "printable": "".join(chr(i) for i in range(32, 127)),
}
MORSE_CODE = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    ".-.-.-": ".",
    "--..--": ",",
    "..--..": "?",
    ".----.": "'",
    "-.-.--": "!",
    "-..-.": "/",
    "-.--.": "(",
    "-.--.-": ")",
    ".-...": "&",
    "---...": ":",
    "-.-.-.": ";",
    "-...-": "=",
    ".-.-.": "+",
    "-....-": "-",
    "..--.-": "_",
    ".-..-.": '"',
    "...-..-": "$",
    ".--.-.": "@",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slug(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "crypto"


def ensure_case(case_dir: str | Path) -> Path:
    path = Path(case_dir)
    path.mkdir(parents=True, exist_ok=True)
    for child in ["artifacts", "files", "notes", "requests", "responses"]:
        (path / child).mkdir(exist_ok=True)
    return path


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_text_arg(text: str | None, file_path: str | None) -> str:
    if text is not None:
        return text
    if file_path:
        return Path(file_path).expanduser().read_text(encoding="utf-8")
    raise SystemExit("provide --text or --file")


def printable_ratio(data: bytes) -> float:
    if not data:
        return 1.0
    printable = sum(1 for byte in data if byte in b"\r\n\t" or 32 <= byte <= 126)
    return printable / len(data)


def entropy(data: bytes) -> float:
    if not data:
        return 0.0
    counts = {byte: data.count(byte) for byte in set(data)}
    total = len(data)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())


def decode_base64(value: str, *, urlsafe: bool) -> dict[str, Any]:
    cleaned = re.sub(r"\s+", "", value)
    padded = cleaned + "=" * ((4 - len(cleaned) % 4) % 4)
    try:
        if urlsafe:
            decoded = base64.urlsafe_b64decode(padded)
        else:
            decoded = base64.b64decode(padded, validate=False)
    except (binascii.Error, ValueError) as exc:
        return {"ok": False, "error": str(exc)}
    text = decoded.decode("utf-8", errors="replace")
    return {
        "ok": True,
        "length": len(decoded),
        "hex": decoded.hex(),
        "printable_ratio": printable_ratio(decoded),
        "text": text if printable_ratio(decoded) > 0.75 else "",
        "flags": sorted(set(FLAG_RE.findall(text))),
    }


def strict_decode_base64(value: str, *, urlsafe: bool) -> dict[str, Any]:
    cleaned = re.sub(r"\s+", "", value)
    alphabet = ALPHABETS["base64url" if urlsafe else "base64"] + "="
    if not cleaned or any(ch not in alphabet for ch in cleaned):
        return {"ok": False, "error": "input contains characters outside the selected Base64 alphabet"}
    padded = cleaned + "=" * ((4 - len(cleaned) % 4) % 4)
    try:
        if urlsafe:
            decoded = base64.urlsafe_b64decode(padded)
        else:
            decoded = base64.b64decode(padded, validate=True)
    except (binascii.Error, ValueError) as exc:
        return {"ok": False, "error": str(exc)}
    text = decoded.decode("utf-8", errors="replace")
    return {
        "ok": True,
        "encoding": "base64url" if urlsafe else "base64",
        "input": cleaned,
        "length": len(decoded),
        "hex": decoded.hex(),
        "printable_ratio": printable_ratio(decoded),
        "text": text if printable_ratio(decoded) > 0.75 else "",
        "flags": sorted(set(FLAG_RE.findall(text))),
    }


def command_base64_chain(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    current = read_text_arg(args.text, args.file).strip()
    steps: list[dict[str, Any]] = []
    stop_reason = "max_depth_reached"
    for depth in range(1, args.max_depth + 1):
        variants = [
            strict_decode_base64(current, urlsafe=False),
            strict_decode_base64(current, urlsafe=True),
        ]
        viable = [
            item
            for item in variants
            if item.get("ok")
            and item.get("text")
            and item.get("printable_ratio", 0.0) >= args.min_printable
            and item.get("text") != current
        ]
        if not viable:
            stop_reason = "no_printable_next_base64_layer"
            break
        chosen = next((item for item in viable if item.get("flags")), viable[0])
        step = dict(chosen)
        step["depth"] = depth
        steps.append(step)
        current = str(chosen["text"]).strip()
        if step["flags"] and args.stop_on_flag:
            stop_reason = "flag_found"
            break

    flags = sorted({flag for step in steps for flag in step.get("flags", [])})
    result = {
        "time": utc_now(),
        "label": args.label,
        "input": read_text_arg(args.text, args.file).strip(),
        "max_depth": args.max_depth,
        "min_printable": args.min_printable,
        "steps": steps,
        "final_text": current,
        "flags": flags,
        "stop_reason": stop_reason,
    }
    output = case_dir / "artifacts" / f"{slug(args.label)}-base64-chain.json"
    write_json(output, result)
    print(json.dumps({"status": "ok", "summary": str(output), "flags": flags, "final_text": current}, ensure_ascii=False, indent=2))


def normalize_morse_token(token: str, dot: str, dash: str, *, swap: bool) -> str:
    normalized = []
    for ch in token:
        if ch == dot:
            normalized.append("-" if swap else ".")
        elif ch == dash:
            normalized.append("." if swap else "-")
        else:
            normalized.append(ch)
    return "".join(normalized)


def split_morse_words(text: str, separator: str | None) -> list[list[str]]:
    if separator:
        words: list[list[str]] = []
        current: list[str] = []
        for raw in text.split(separator):
            token = raw.strip()
            if not token:
                if raw and current:
                    words.append(current)
                    current = []
                continue
            current.append(token)
        if current:
            words.append(current)
        return words

    words = []
    for word in re.split(r"\s*/\s*|\s{2,}", text.strip()):
        tokens = [token for token in word.split() if token]
        if tokens:
            words.append(tokens)
    return words


def decode_morse_words(words: list[list[str]], dot: str, dash: str, *, swap: bool) -> dict[str, Any]:
    decoded_words: list[str] = []
    unknown: list[dict[str, str]] = []
    normalized_words: list[list[str]] = []
    for word in words:
        decoded_chars: list[str] = []
        normalized_word: list[str] = []
        for token in word:
            normalized = normalize_morse_token(token, dot, dash, swap=swap)
            normalized_word.append(normalized)
            char = MORSE_CODE.get(normalized)
            if char is None:
                char = "?"
                unknown.append({"token": token, "normalized": normalized})
            decoded_chars.append(char)
        normalized_words.append(normalized_word)
        decoded_words.append("".join(decoded_chars))
    decoded = " ".join(decoded_words)
    return {
        "swap_dot_dash": swap,
        "tokens": words,
        "normalized_tokens": normalized_words,
        "decoded": decoded,
        "unknown": unknown,
        "all_known": not unknown,
    }


def command_morse(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    text = read_text_arg(args.text, args.file).strip()
    separator = None if args.no_separator else args.separator
    words = split_morse_words(text, separator)
    variants = [
        decode_morse_words(words, args.dot, args.dash, swap=False),
        decode_morse_words(words, args.dot, args.dash, swap=True),
    ]
    result = {
        "time": utc_now(),
        "label": args.label,
        "input": text,
        "separator": separator,
        "dot": args.dot,
        "dash": args.dash,
        "variants": variants,
    }
    output = case_dir / "artifacts" / f"{slug(args.label)}-morse.json"
    write_json(output, result)
    print(json.dumps({"status": "ok", "summary": str(output), "result": result}, ensure_ascii=False, indent=2))


def command_triage(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    value = read_text_arg(args.text, args.file).strip()
    data = value.encode("utf-8", errors="replace")
    charsets = [name for name, alphabet in ALPHABETS.items() if all(ch in alphabet for ch in value)]
    result = {
        "time": utc_now(),
        "label": args.label,
        "input": value,
        "length": len(value),
        "unique_chars": "".join(sorted(set(value))),
        "candidate_charsets": charsets,
        "entropy_bits_per_byte": entropy(data),
        "flags": sorted(set(FLAG_RE.findall(value))),
        "base64": decode_base64(value, urlsafe=False),
        "base64url": decode_base64(value, urlsafe=True),
    }
    output = case_dir / "artifacts" / f"{slug(args.label)}-crypto-triage.json"
    write_json(output, result)
    print(json.dumps({"status": "ok", "summary": str(output), "result": result}, ensure_ascii=False, indent=2))


def split_units(text: str) -> list[list[str]]:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text.strip()) if part.strip()]
    if not paragraphs:
        paragraphs = [text]
    return [WORD_RE.findall(paragraph) for paragraph in paragraphs]


def parse_coords(value: str) -> list[tuple[int, int, int]]:
    coords: list[tuple[int, int, int]] = []
    for raw in re.split(r"[\s,;]+", value.strip()):
        if not raw:
            continue
        parts = raw.split(".")
        if len(parts) != 3 or not all(part.isdigit() for part in parts):
            raise SystemExit(f"invalid coordinate, expected paragraph.word.char: {raw}")
        coords.append(tuple(int(part) for part in parts))
    return coords


def ascii_fold(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch))


def command_book_extract(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    text = read_text_arg(args.text, args.file)
    units = split_units(text)
    coords = parse_coords(args.coords)
    extracted: list[dict[str, Any]] = []
    key_chars: list[str] = []
    for paragraph_idx, word_idx, char_idx in coords:
        item: dict[str, Any] = {
            "coord": [paragraph_idx, word_idx, char_idx],
            "ok": False,
            "paragraph_word_count": None,
            "word": None,
            "char": None,
            "error": None,
        }
        if paragraph_idx < 1 or paragraph_idx > len(units):
            item["error"] = f"paragraph {paragraph_idx} out of range"
            extracted.append(item)
            continue
        words = units[paragraph_idx - 1]
        item["paragraph_word_count"] = len(words)
        if word_idx < 1 or word_idx > len(words):
            item["error"] = f"word {word_idx} out of range"
            extracted.append(item)
            continue
        word = words[word_idx - 1]
        item["word"] = word
        if char_idx < 1 or char_idx > len(word):
            item["error"] = f"char {char_idx} out of range for word {word!r}"
            extracted.append(item)
            continue
        item["ok"] = True
        item["char"] = word[char_idx - 1]
        key_chars.append(item["char"])
        extracted.append(item)
    result = {
        "time": utc_now(),
        "label": args.label,
        "source": str(Path(args.file).expanduser()) if args.file else "inline-text",
        "paragraphs": len(units),
        "paragraph_word_counts": [len(words) for words in units],
        "coords": [list(coord) for coord in coords],
        "extracted": extracted,
        "key": "".join(key_chars),
        "all_ok": all(item["ok"] for item in extracted),
    }
    output = case_dir / "artifacts" / f"{slug(args.label)}-book-extract.json"
    write_json(output, result)
    print(json.dumps({"status": "ok" if result["all_ok"] else "partial", "summary": str(output), "result": result}, ensure_ascii=False, indent=2))


def parse_mapping(items: list[str] | None, label: str) -> dict[int, str]:
    mapping: dict[int, str] = {}
    for item in items or []:
        if "=" not in item:
            raise SystemExit(f"invalid {label}, expected BOOK=VALUE: {item}")
        key, value = item.split("=", 1)
        if not key.isdigit():
            raise SystemExit(f"invalid {label} book id: {item}")
        mapping[int(key)] = value
    return mapping


def html_or_text_lines(path: Path) -> list[str]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    raw = re.sub(r"(?i)<br\s*/?>", "\n", raw)
    raw = TAG_RE.sub(" ", raw)
    raw = unescape(raw).replace("\xa0", " ")
    lines: list[str] = []
    for line in raw.splitlines():
        cleaned = " ".join(line.strip().split())
        cleaned = re.sub(r"\s+\d+\s*$", "", cleaned)
        if cleaned:
            lines.append(cleaned)
    return lines


def trim_lines(lines: list[str], first_line: str | None) -> list[str]:
    if not first_line:
        return lines
    needle = first_line.casefold()
    for index, line in enumerate(lines):
        if needle in ascii_fold(line).casefold() or needle in line.casefold():
            return lines[index:]
    raise SystemExit(f"first line marker not found: {first_line}")


def command_line_extract(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    book_paths = {book: Path(path).expanduser() for book, path in parse_mapping(args.book, "--book").items()}
    first_lines = parse_mapping(args.first_line, "--first-line")
    if not book_paths:
        raise SystemExit("provide at least one --book BOOK=PATH")
    coords = parse_coords(args.coords)
    books: dict[int, list[str]] = {}
    for book, path in book_paths.items():
        if not path.exists():
            raise SystemExit(f"missing book file: {path}")
        books[book] = trim_lines(html_or_text_lines(path), first_lines.get(book))

    extracted: list[dict[str, Any]] = []
    selected_words: list[str] = []
    selected_ascii_words: list[str] = []
    selected_initials: list[str] = []
    for book_idx, line_idx, item_idx in coords:
        item: dict[str, Any] = {
            "coord": [book_idx, line_idx, item_idx],
            "ok": False,
            "line": None,
            "line_count": None,
            "word_count": None,
            "word": None,
            "word_ascii": None,
            "char": None,
            "char_ascii": None,
            "error": None,
        }
        if book_idx not in books:
            item["error"] = f"book {book_idx} not provided"
            extracted.append(item)
            continue
        lines = books[book_idx]
        item["line_count"] = len(lines)
        if line_idx < 1 or line_idx > len(lines):
            item["error"] = f"line {line_idx} out of range"
            extracted.append(item)
            continue
        line = lines[line_idx - 1]
        item["line"] = line
        words = UNICODE_WORD_RE.findall(line)
        item["word_count"] = len(words)
        if args.unit == "word":
            if item_idx < 1 or item_idx > len(words):
                item["error"] = f"word {item_idx} out of range"
                extracted.append(item)
                continue
            word = words[item_idx - 1]
            folded = ascii_fold(word)
            item["ok"] = True
            item["word"] = word
            item["word_ascii"] = folded
            selected_words.append(word)
            selected_ascii_words.append(folded)
            selected_initials.append(folded[:1])
        else:
            letters = [ch for ch in line if ch.isalpha()]
            folded_letters = [ascii_fold(ch) for ch in letters]
            if item_idx < 1 or item_idx > len(letters):
                item["error"] = f"char {item_idx} out of range"
                extracted.append(item)
                continue
            item["ok"] = True
            item["char"] = letters[item_idx - 1]
            item["char_ascii"] = folded_letters[item_idx - 1]
            selected_words.append(letters[item_idx - 1])
            selected_ascii_words.append(folded_letters[item_idx - 1])
            selected_initials.append(folded_letters[item_idx - 1])
        extracted.append(item)

    result = {
        "time": utc_now(),
        "label": args.label,
        "unit": args.unit,
        "books": {str(book): str(path) for book, path in book_paths.items()},
        "line_counts": {str(book): len(lines) for book, lines in books.items()},
        "coords": [list(coord) for coord in coords],
        "extracted": extracted,
        "joined": "".join(selected_words),
        "joined_ascii": "".join(selected_ascii_words),
        "space_joined": " ".join(selected_words),
        "space_joined_ascii": " ".join(selected_ascii_words),
        "initials": "".join(selected_initials),
        "all_ok": all(item["ok"] for item in extracted),
    }
    output = case_dir / "artifacts" / f"{slug(args.label)}-line-extract.json"
    write_json(output, result)
    print(json.dumps({"status": "ok" if result["all_ok"] else "partial", "summary": str(output), "result": result}, ensure_ascii=False, indent=2))


def vigenere_transform(cipher: str, key: str, alphabet: str, decrypt: bool) -> str:
    if not key:
        raise SystemExit("key must not be empty")
    key_indexes = [alphabet.index(ch) for ch in key if ch in alphabet]
    if not key_indexes:
        raise SystemExit("key has no characters in the selected alphabet")
    out: list[str] = []
    key_pos = 0
    for ch in cipher:
        if ch not in alphabet:
            out.append(ch)
            continue
        shift = key_indexes[key_pos % len(key_indexes)]
        idx = alphabet.index(ch)
        out.append(alphabet[(idx - shift if decrypt else idx + shift) % len(alphabet)])
        key_pos += 1
    return "".join(out)


def command_vigenere(args: argparse.Namespace) -> None:
    case_dir = ensure_case(args.case_dir)
    alphabet = ALPHABETS[args.alphabet]
    text = read_text_arg(args.text, args.file).strip()
    transformed = vigenere_transform(text, args.key, alphabet, args.decrypt)
    result = {
        "time": utc_now(),
        "label": args.label,
        "mode": "decrypt" if args.decrypt else "encrypt",
        "alphabet": args.alphabet,
        "key": args.key,
        "input": text,
        "output": transformed,
        "flags": sorted(set(FLAG_RE.findall(transformed))),
        "base64": decode_base64(transformed, urlsafe=False),
        "base64url": decode_base64(transformed, urlsafe=True),
    }
    output = case_dir / "artifacts" / f"{slug(args.label)}-vigenere.json"
    write_json(output, result)
    print(json.dumps({"status": "ok", "summary": str(output), "result": result}, ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Local CTF crypto helpers for encodings, Morse, book coordinates, and classical ciphers")
    sub = parser.add_subparsers(dest="command", required=True)

    triage = sub.add_parser("triage", help="summarize a local ciphertext or encoded value")
    triage.add_argument("--case-dir", required=True)
    triage.add_argument("--label", default="ciphertext")
    triage.add_argument("--text")
    triage.add_argument("--file")
    triage.set_defaults(func=command_triage)

    b64_chain = sub.add_parser("base64-chain", help="recursively decode printable Base64/Base64URL layers")
    b64_chain.add_argument("--case-dir", required=True)
    b64_chain.add_argument("--label", default="base64-chain")
    b64_chain.add_argument("--text")
    b64_chain.add_argument("--file")
    b64_chain.add_argument("--max-depth", type=int, default=5)
    b64_chain.add_argument("--min-printable", type=float, default=0.75)
    b64_chain.add_argument("--stop-on-flag", action="store_true")
    b64_chain.set_defaults(func=command_base64_chain)

    morse = sub.add_parser("morse", help="decode Morse-like two-symbol text and record swapped dot/dash variants")
    morse.add_argument("--case-dir", required=True)
    morse.add_argument("--label", default="morse")
    morse.add_argument("--text")
    morse.add_argument("--file")
    morse.add_argument("--separator", default="\\", help="letter separator; default is backslash")
    morse.add_argument("--no-separator", action="store_true", help="parse conventional space-separated Morse with slash or blank word gaps")
    morse.add_argument("--dot", default=".")
    morse.add_argument("--dash", default="-")
    morse.set_defaults(func=command_morse)

    book = sub.add_parser("book-extract", help="extract a key from paragraph.word.char coordinates")
    book.add_argument("--case-dir", required=True)
    book.add_argument("--label", default="book")
    book.add_argument("--coords", required=True, help="comma or space separated coordinates like 1.1.3,1.2.1")
    book.add_argument("--text")
    book.add_argument("--file")
    book.set_defaults(func=command_book_extract)

    line = sub.add_parser("line-extract", help="extract words or letters from book.line.item coordinates")
    line.add_argument("--case-dir", required=True)
    line.add_argument("--label", default="line-book")
    line.add_argument("--coords", required=True, help="comma or space separated coordinates like 1.156.3")
    line.add_argument("--book", action="append", help="mapping like 1=/path/to/book1.txt; repeat for each book")
    line.add_argument("--first-line", action="append", help="optional trim marker like 1='Arma virumque'")
    line.add_argument("--unit", choices=["word", "char"], default="word")
    line.set_defaults(func=command_line_extract)

    vig = sub.add_parser("vigenere", help="apply a Vigenere-style shift over a selected alphabet")
    vig.add_argument("--case-dir", required=True)
    vig.add_argument("--label", default="vigenere")
    vig.add_argument("--key", required=True)
    vig.add_argument("--alphabet", choices=sorted(ALPHABETS), default="base62")
    vig.add_argument("--text")
    vig.add_argument("--file")
    vig.add_argument("--decrypt", action="store_true")
    vig.set_defaults(func=command_vigenere)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
