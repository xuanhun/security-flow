#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fcntl
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from core import memory as memory_store


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPT_DIR.parent
REPO_ROOT = SKILL_ROOT.parents[1]
REPORT_ROOT = REPO_ROOT / "test-reports" / "kali"
GLOBAL_INDEX = REPORT_ROOT / "ctf-agent-index.json"

VALID_STATES = ("open", "started", "blocked", "solved", "failed", "closed")
VALID_NOTES = ("info", "infer", "result", "timeline")
PHASES = (
    "intake",
    "note_replay",
    "phase1_recon",
    "phase2_active",
    "phase3_knowledge",
    "phase4_verify",
    "result",
    "distill",
)
NOTE_REVIEW_SECONDS = 8 * 60

PHASE_GUIDANCE = {
    "intake": {
        "goal": "Normalize target, artifacts, hints, scope, and expected flag count.",
        "next": "Run start after intake is complete.",
    },
    "note_replay": {
        "goal": "Read notes first. Reuse result chains, verified facts, and failed-route records.",
        "next": "If result.md has a route, replay it. Otherwise advance to phase1_recon.",
    },
    "phase1_recon": {
        "goal": "Collect first-pass evidence with safe skill tools before using cases.",
        "next": "Capture landing pages, artifacts, visible routes, headers, cookies, and summaries.",
    },
    "phase2_active": {
        "goal": "Run bounded active probes selected by category and evidence.",
        "next": "Record probe evidence and avoid repeated failed methods from info.md.",
    },
    "phase3_knowledge": {
        "goal": "Query local notes, casebook, category knowledge, solved cases, and optional local vuln indexes.",
        "next": "Use knowledge hits only as hypotheses, then verify with skill tools.",
    },
    "phase4_verify": {
        "goal": "Verify the chosen route, preserve proof evidence, and avoid ungated high-risk actions.",
        "next": "If the route proves a flag, run solve. If stalled, block or fail with evidence.",
    },
    "result": {
        "goal": "Record the final route, proof, replay commands, and flag.",
        "next": "Advance to distill after the result note is complete.",
    },
    "distill": {
        "goal": "Promote reusable lessons into knowledge, cases, or skill tools.",
        "next": "Close only after distillation is recorded.",
    },
}

KNOWLEDGE_FILES = {
    "web": "ctf-knowledge-web.md",
    "crypto": "ctf-knowledge-crypto.md",
    "misc": "ctf-knowledge-misc-forensics.md",
    "forensics": "ctf-knowledge-misc-forensics.md",
    "reverse": "ctf-knowledge-reverse-pwn.md",
    "pwn": "ctf-knowledge-reverse-pwn.md",
    "mobile": "ctf-knowledge-mobile.md",
    "android": "ctf-knowledge-mobile.md",
    "ios": "ctf-knowledge-mobile.md",
    "ipa": "ctf-knowledge-mobile.md",
    "assets.car": "ctf-knowledge-mobile.md",
    "coreui": "ctf-knowledge-mobile.md",
    "assetutil": "ctf-knowledge-mobile.md",
    "acextract": "ctf-knowledge-mobile.md",
    "cartool": "ctf-knowledge-mobile.md",
    "bvx2": "ctf-knowledge-mobile.md",
    "dmp2": "ctf-knowledge-mobile.md",
    "osint": "ctf-knowledge-osint.md",
    "malware": "ctf-knowledge-malware.md",
    "ai": "ctf-knowledge-ai-watermark.md",
    "watermark": "ctf-knowledge-ai-watermark.md",
    "cdn": "ctf-knowledge-cdn-privacy-client.md",
    "privacy": "ctf-knowledge-cdn-privacy-client.md",
    "coding": "ctf-knowledge-coding-spec.md",
    "spec": "ctf-knowledge-coding-spec.md",
    "database": "ctf-knowledge-web.md",
    "postgres": "ctf-knowledge-web.md",
    "pg": "ctf-knowledge-web.md",
}

CASEBOOK_CATEGORY_HINTS = {
    "web": "Pentesting",
    "pentest": "Pentesting",
    "network": "Network Forensics",
    "pcap": "Network Forensics",
    "forensics": "Endpoint Forensics",
    "memory": "Endpoint Forensics",
    "malware": "Malware Analysis",
    "email": "Email Analysis",
    "mobile": "Mobile Forensics",
    "ios": "Mobile Forensics",
    "ipa": "Mobile Forensics",
    "assets.car": "Mobile Forensics",
    "coreui": "Mobile Forensics",
    "assetutil": "Mobile Forensics",
    "acextract": "Mobile Forensics",
    "cartool": "Mobile Forensics",
    "bvx2": "Mobile Forensics",
    "dmp2": "Mobile Forensics",
    "reverse": "Reverse Engineering",
    "pwn": "Reverse Engineering",
    "osint": "Cyber Threat Intelligence (CTI)",
    "cti": "Cyber Threat Intelligence (CTI)",
    "siem": "SIEM (ELK, Splunk, etc.)",
    "ids": "IDS/IPS",
}

ARTIFACT_HINTS = {
    "pcap": ("pcap", "network-forensics"),
    "pcapng": ("pcap", "network-forensics"),
    "apk": ("apk-mobile", "mobile-forensics"),
    "android": ("apk-mobile", "mobile-forensics"),
    "ios": ("apk-mobile", "mobile-forensics"),
    "ipa": ("apk-mobile", "mobile-forensics"),
    "assets.car": ("apk-mobile", "mobile-forensics"),
    "coreui": ("apk-mobile", "mobile-forensics"),
    "assetutil": ("apk-mobile", "mobile-forensics"),
    "acextract": ("apk-mobile", "mobile-forensics"),
    "cartool": ("apk-mobile", "mobile-forensics"),
    "bvx2": ("apk-mobile", "mobile-forensics"),
    "dmp2": ("apk-mobile", "mobile-forensics"),
    "http": ("web-service", "http-analysis"),
    "web": ("web-service", "web-enumeration"),
    "jwt": ("web-service", "web-enumeration"),
    "cookie": ("web-service", "web-enumeration"),
    "png": ("office-document", "stego-extraction"),
    "jpg": ("office-document", "stego-extraction"),
    "image": ("office-document", "stego-extraction"),
    "zip": ("disk-image", "stego-extraction"),
    "tar": ("disk-image", "stego-extraction"),
    "pdf": ("office-document", "maldoc-analysis"),
    "doc": ("office-document", "maldoc-analysis"),
    "xls": ("office-document", "maldoc-analysis"),
    "evtx": ("windows-events", "windows-event-analysis"),
    "memory": ("memory", "memory-forensics"),
    "vmem": ("memory", "memory-forensics"),
}

CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b", re.IGNORECASE)
URL_RE = re.compile(r"https?://[^\s)>\]]+")
ROUTE_RE = re.compile(r"(?<![A-Za-z0-9_])/[A-Za-z0-9._~!$&'()*+,;=:@%/-]{1,120}")
EXT_RE = re.compile(r"\b[\w.-]+\.(?:7z|apk|bin|db|docx?|elf|evtx|gz|jar|jpg|json|pcapng?|pdf|png|rar|sqlite|tar|txt|wasm|xlsx?|zip)\b", re.IGNORECASE)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        normalized = value.replace("Z", "+00:00")
        dt = datetime.fromisoformat(normalized)
        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except ValueError:
        return None


def slug(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "case"


def case_path(value: str | Path) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = REPORT_ROOT / path
    return path


def read_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def atomic_write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    with temp.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temp, path)


def append_jsonl(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(data, ensure_ascii=False, sort_keys=True) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def ensure_case(case_dir: Path) -> Path:
    case_dir.mkdir(parents=True, exist_ok=True)
    for child in ("requests", "responses", "artifacts", "files", "notes", "knowledge"):
        (case_dir / child).mkdir(exist_ok=True)
    for note_type in VALID_NOTES:
        note_path = case_dir / "notes" / f"{note_type}.md"
        if not note_path.exists():
            note_path.write_text(f"# {note_type.upper()}\n", encoding="utf-8")
    memory_store.ensure_memory(case_dir)
    return case_dir


def default_state(case_dir: Path, meta: dict[str, Any]) -> dict[str, Any]:
    now = utc_now()
    return {
        "version": "1.0",
        "case_dir": str(case_dir),
        "name": meta.get("name") or case_dir.name,
        "category": meta.get("category") or "ctf",
        "target": meta.get("url") or meta.get("target") or "",
        "artifacts": meta.get("artifacts") or [],
        "hint": meta.get("hint") or "",
        "flag_count": int(meta.get("flag_count") or 1),
        "priority": int(meta.get("priority") or 50),
        "state": "open",
        "phase": "intake",
        "created_at": now,
        "updated_at": now,
        "phase_entered_at": now,
        "started_at": None,
        "solved_at": None,
        "timeout_seconds": int(meta.get("timeout_seconds") or 3600),
        "max_retries": int(meta.get("max_retries") or 3),
        "retry_num": int(meta.get("retry_num") or 0),
        "notes_last_read_at": None,
        "notes_read_phase": None,
        "last_checkpoint_phase": None,
        "blocked_reason": None,
        "failure_reason": None,
        "result": None,
        "next_step": "Read notes, then start the Nemo-style phase loop.",
    }


def load_state(case_dir: Path) -> dict[str, Any]:
    state_path = case_dir / "state.json"
    state = read_json(state_path, default=None)
    if state is None:
        meta = read_json(case_dir / "case.json", default={"name": case_dir.name})
        state = default_state(case_dir, meta)
        atomic_write_json(state_path, state)
    return state


def save_state(case_dir: Path, state: dict[str, Any]) -> None:
    state["updated_at"] = utc_now()
    atomic_write_json(case_dir / "state.json", state)
    sync_index()


def record_event(case_dir: Path, event: str, data: dict[str, Any] | None = None) -> None:
    append_jsonl(case_dir / "events.jsonl", {"time": utc_now(), "event": event, "data": data or {}})


def append_note(case_dir: Path, note_type: str, content: str, *, source: str = "operator") -> None:
    if note_type not in VALID_NOTES:
        raise SystemExit(f"note type must be one of: {', '.join(VALID_NOTES)}")
    note_path = case_dir / "notes" / f"{note_type}.md"
    lock_path = case_dir / "notes" / f"{note_type}.lock"
    with lock_path.open("w", encoding="utf-8") as lock_file:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
        try:
            with note_path.open("a", encoding="utf-8") as handle:
                handle.write(f"\n\n---\n**[{utc_now()}] [{source}]**\n\n{content.rstrip()}\n")
                handle.flush()
                os.fsync(handle.fileno())
        finally:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)


def read_notes(case_dir: Path) -> dict[str, str]:
    notes = {}
    for note_type in VALID_NOTES:
        path = case_dir / "notes" / f"{note_type}.md"
        notes[note_type] = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
    return notes


def note_has_body(text: str) -> bool:
    stripped = re.sub(r"^# .*$", "", text, flags=re.MULTILINE).strip()
    return bool(stripped)


def checkpoint_records(case_dir: Path) -> list[dict[str, Any]]:
    path = case_dir / "phase-checkpoints.jsonl"
    if not path.exists():
        return []
    records = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.strip():
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return records


def latest_events(case_dir: Path, limit: int = 8) -> list[dict[str, Any]]:
    path = case_dir / "events.jsonl"
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows[-limit:]


def has_checkpoint(case_dir: Path, phase: str) -> bool:
    return any(item.get("phase") == phase for item in checkpoint_records(case_dir))


def set_phase(state: dict[str, Any], phase: str) -> None:
    state["phase"] = phase
    state["phase_entered_at"] = utc_now()
    state["notes_read_phase"] = None
    state["next_step"] = PHASE_GUIDANCE[phase]["next"]


def next_phase(phase: str) -> str | None:
    try:
        index = PHASES.index(phase)
    except ValueError:
        return None
    if index + 1 >= len(PHASES):
        return None
    return PHASES[index + 1]


def phase_ready_to_advance(case_dir: Path, state: dict[str, Any]) -> tuple[bool, str]:
    phase = state.get("phase", "intake")
    if phase not in PHASES:
        return False, f"unknown phase: {phase}"
    if phase != "intake":
        if state.get("notes_read_phase") != phase:
            return False, f"notes must be read in current phase: {phase}"
        last_read = parse_time(state.get("notes_last_read_at"))
        if not last_read:
            return False, "notes_last_read_at is missing"
        age = (datetime.now(timezone.utc) - last_read).total_seconds()
        if age > NOTE_REVIEW_SECONDS:
            return False, "notes review is older than 8 minutes"
    if phase.startswith("phase") or phase in ("note_replay", "result"):
        if not has_checkpoint(case_dir, phase):
            return False, f"missing checkpoint for {phase}"
    return True, "ok"


def refresh_timeout(case_dir: Path) -> dict[str, Any]:
    state = load_state(case_dir)
    if state.get("state") != "started":
        return state
    started = parse_time(state.get("started_at"))
    timeout_seconds = int(state.get("timeout_seconds") or 0)
    if started and timeout_seconds > 0:
        elapsed = (datetime.now(timezone.utc) - started).total_seconds()
        if elapsed > timeout_seconds:
            state["state"] = "failed"
            state["failure_reason"] = f"timeout after {int(elapsed)}s > {timeout_seconds}s"
            state["next_step"] = "Review notes and decide whether retry is useful."
            save_state(case_dir, state)
            record_event(case_dir, "timeout", {"elapsed_seconds": int(elapsed), "timeout_seconds": timeout_seconds})
    return state


def discover_cases(root: Path = REPORT_ROOT) -> list[Path]:
    if not root.exists():
        return []
    return sorted(path.parent for path in root.rglob("state.json") if path.is_file())


def state_summary(case_dir: Path) -> dict[str, Any]:
    state = load_state(case_dir)
    return {
        "case_dir": str(case_dir),
        "name": state.get("name"),
        "category": state.get("category"),
        "target": state.get("target"),
        "state": state.get("state"),
        "phase": state.get("phase"),
        "priority": state.get("priority"),
        "retry_num": state.get("retry_num"),
        "max_retries": state.get("max_retries"),
        "updated_at": state.get("updated_at"),
        "next_step": state.get("next_step"),
        "blocked_reason": state.get("blocked_reason"),
        "failure_reason": state.get("failure_reason"),
        "result": state.get("result"),
    }


def sync_index() -> None:
    REPORT_ROOT.mkdir(parents=True, exist_ok=True)
    cases = []
    for case_dir in discover_cases(REPORT_ROOT):
        try:
            cases.append(state_summary(case_dir))
        except Exception:
            continue
    data = {
        "version": "1.0",
        "generated_at": utc_now(),
        "source": "case-local-state",
        "cases": cases,
        "counts": {state: sum(1 for item in cases if item.get("state") == state) for state in VALID_STATES},
    }
    atomic_write_json(GLOBAL_INDEX, data)


def command_init(args: argparse.Namespace) -> None:
    case_dir = ensure_case(case_path(args.case_dir))
    meta = read_json(case_dir / "case.json", default={}) or {}
    meta.update(
        {
            "time": meta.get("time") or utc_now(),
            "name": args.name or meta.get("name") or case_dir.name,
            "category": args.category or meta.get("category") or "ctf",
            "url": args.url or args.target or meta.get("url") or meta.get("target") or "",
            "target": args.target or args.url or meta.get("target") or meta.get("url") or "",
            "artifacts": args.artifact or meta.get("artifacts") or [],
            "hint": args.hint or meta.get("hint") or "",
            "flag_count": args.flag_count,
            "timeout_seconds": args.timeout,
            "priority": args.priority,
            "max_retries": args.max_retries,
        }
    )
    atomic_write_json(case_dir / "case.json", meta)
    state_path = case_dir / "state.json"
    if state_path.exists() and not args.force:
        state = load_state(case_dir)
    else:
        state = default_state(case_dir, meta)
        atomic_write_json(state_path, state)
    record_event(case_dir, "init", {"name": meta["name"], "category": meta["category"], "target": meta["target"]})
    memory_store.add_goal(
        case_dir,
        title=f"CTF case: {meta['name']}",
        summary=f"Category={meta['category']}; target={meta['target']}; flag_count={meta['flag_count']}",
        evidence_refs=[str(case_dir / "case.json"), str(case_dir / "state.json")],
    )
    sync_index()
    print(json.dumps({"status": "ok", "case_dir": str(case_dir), "state": state}, ensure_ascii=False, indent=2))


def command_queue(args: argparse.Namespace) -> None:
    root = case_path(args.root) if args.root else REPORT_ROOT
    rows = []
    for case_dir in discover_cases(root):
        state = refresh_timeout(case_dir) if args.refresh_timeouts else load_state(case_dir)
        rows.append(state_summary(case_dir))
    sync_index()
    print(json.dumps({"root": str(root), "count": len(rows), "cases": rows}, ensure_ascii=False, indent=2))


def sort_key(item: dict[str, Any]) -> tuple[int, str]:
    return (-int(item.get("priority") or 0), item.get("updated_at") or "")


def command_next(args: argparse.Namespace) -> None:
    candidates = []
    blocked = []
    for case_dir in discover_cases(REPORT_ROOT):
        state = refresh_timeout(case_dir)
        item = state_summary(case_dir)
        item["_case_dir"] = case_dir
        if state.get("state") == "open":
            candidates.append(("open", item))
        elif state.get("state") == "failed" and int(state.get("retry_num") or 0) < int(state.get("max_retries") or 0):
            candidates.append(("retryable_failed", item))
        elif state.get("state") == "blocked":
            blocked.append(item)
    if candidates:
        reason, item = sorted(candidates, key=lambda pair: sort_key(pair[1]))[0]
        item.pop("_case_dir", None)
        print(json.dumps({"status": "ok", "reason": reason, "case": item}, ensure_ascii=False, indent=2))
        return
    print(json.dumps({"status": "none", "blocked": blocked}, ensure_ascii=False, indent=2))


def command_start(args: argparse.Namespace) -> None:
    case_dir = ensure_case(case_path(args.case_dir))
    state = refresh_timeout(case_dir)
    old_state = state.get("state")
    if old_state == "failed":
        if int(state.get("retry_num") or 0) >= int(state.get("max_retries") or 0):
            raise SystemExit("failed case reached max_retries; use init --force or update state manually")
        state["retry_num"] = int(state.get("retry_num") or 0) + 1
    elif old_state not in ("open", "started"):
        raise SystemExit(f"cannot start case in state: {old_state}")
    state["state"] = "started"
    state["started_at"] = state.get("started_at") or utc_now()
    state["blocked_reason"] = None
    state["failure_reason"] = None
    set_phase(state, "note_replay")
    save_state(case_dir, state)
    record_event(case_dir, "start", {"previous_state": old_state, "phase": state["phase"], "retry_num": state["retry_num"]})
    print(json.dumps({"status": "ok", "state": state, "required_next": "run note --read-all before probing"}, ensure_ascii=False, indent=2))


def command_note(args: argparse.Namespace) -> None:
    case_dir = ensure_case(case_path(args.case_dir))
    state = load_state(case_dir)
    if args.read_all:
        notes = read_notes(case_dir)
        state["notes_last_read_at"] = utc_now()
        state["notes_read_phase"] = state.get("phase")
        save_state(case_dir, state)
        record_event(case_dir, "notes-read", {"phase": state.get("phase")})
        print(json.dumps({"status": "ok", "phase": state.get("phase"), "notes": notes}, ensure_ascii=False, indent=2))
        return
    content = args.content
    if args.file:
        content = Path(args.file).read_text(encoding="utf-8")
    if not content:
        raise SystemExit("provide --content, --file, or --read-all")
    append_note(case_dir, args.type, content, source=args.source)
    record_event(case_dir, "note-append", {"type": args.type, "source": args.source})
    print(json.dumps({"status": "ok", "note": str(case_dir / "notes" / f"{args.type}.md")}, ensure_ascii=False, indent=2))


def command_phase(args: argparse.Namespace) -> None:
    case_dir = ensure_case(case_path(args.case_dir))
    state = load_state(case_dir)
    phase = state.get("phase", "intake")
    if phase not in PHASES:
        raise SystemExit(f"unknown phase: {phase}")
    if args.checkpoint_summary:
        record = {
            "time": utc_now(),
            "phase": phase,
            "summary": args.checkpoint_summary,
            "evidence": args.evidence or [],
            "next_step": args.next_step or "",
        }
        append_jsonl(case_dir / "phase-checkpoints.jsonl", record)
        state["last_checkpoint_phase"] = phase
        state["next_step"] = args.next_step or PHASE_GUIDANCE[phase]["next"]
        save_state(case_dir, state)
        record_event(case_dir, "phase-checkpoint", record)
    if args.advance:
        ready, reason = phase_ready_to_advance(case_dir, state)
        if not ready:
            state["blocked_reason"] = reason
            save_state(case_dir, state)
            record_event(case_dir, "phase-advance-denied", {"phase": phase, "reason": reason})
            raise SystemExit(f"cannot advance: {reason}")
        upcoming = next_phase(phase)
        if not upcoming:
            raise SystemExit("already at final phase")
        set_phase(state, upcoming)
        save_state(case_dir, state)
        record_event(case_dir, "phase-advance", {"from": phase, "to": upcoming})
        phase = upcoming
    guidance = PHASE_GUIDANCE[phase]
    print(
        json.dumps(
            {
                "status": "ok",
                "state": state.get("state"),
                "phase": phase,
                "goal": guidance["goal"],
                "next": guidance["next"],
                "must_read_notes": phase != "intake",
                "requires_checkpoint_to_advance": phase.startswith("phase") or phase in ("note_replay", "result"),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def gather_corpus(case_dir: Path) -> str:
    parts: list[str] = []
    for path in [
        case_dir / "case.json",
        case_dir / "state.json",
        case_dir / "notes" / "info.md",
        case_dir / "notes" / "infer.md",
        case_dir / "notes" / "result.md",
        case_dir / "notes" / "tool-summary.md",
    ]:
        if path.exists():
            parts.append(path.read_text(encoding="utf-8", errors="replace"))
    for path in sorted((case_dir / "artifacts").glob("*.json"))[:50]:
        parts.append(path.read_text(encoding="utf-8", errors="replace")[:8000])
    return "\n".join(parts)[:500000]


def extract_terms(text: str, meta: dict[str, Any], state: dict[str, Any]) -> dict[str, list[str]]:
    lowered = text.lower()
    seeds = " ".join(str(value) for value in [meta.get("category"), state.get("category"), meta.get("url"), state.get("target")] if value)
    combined = f"{lowered}\n{seeds.lower()}"
    keywords = sorted({key for key in list(KNOWLEDGE_FILES) + list(CASEBOOK_CATEGORY_HINTS) + list(ARTIFACT_HINTS) if key in combined})
    return {
        "cves": sorted({item.upper() for item in CVE_RE.findall(text)})[:30],
        "urls": sorted(set(URL_RE.findall(text)))[:30],
        "routes": sorted(set(ROUTE_RE.findall(text)))[:50],
        "files": sorted(set(EXT_RE.findall(text)))[:50],
        "keywords": keywords[:60],
    }


def select_casebook_hits(terms: dict[str, list[str]], state: dict[str, Any]) -> list[dict[str, Any]]:
    taxonomy_path = SKILL_ROOT / "assets" / "casebook" / "taxonomy.json"
    if not taxonomy_path.exists():
        return []
    taxonomy = read_json(taxonomy_path, default={})
    categories = taxonomy.get("categories", {})
    keyword_pool = [str(state.get("category") or "").lower(), *terms.get("keywords", [])]
    selected_category = None
    for keyword in keyword_pool:
        if keyword in CASEBOOK_CATEGORY_HINTS:
            selected_category = CASEBOOK_CATEGORY_HINTS[keyword]
            break
    if not selected_category:
        selected_category = next(iter(categories), None)
    if not selected_category or selected_category not in categories:
        return []
    hit = {
        "source": "casebook",
        "kind": "category",
        "category": selected_category,
        "path": str(SKILL_ROOT / "assets" / "casebook" / categories[selected_category].get("index", "")),
        "reason": "matched category or fallback first local casebook category",
    }
    artifact_hits = []
    cat = categories[selected_category]
    artifacts = cat.get("artifacts", {})
    for keyword in terms.get("keywords", []):
        if keyword not in ARTIFACT_HINTS:
            continue
        artifact, technique = ARTIFACT_HINTS[keyword]
        if artifact in artifacts:
            artifact_hits.append(
                {
                    "source": "casebook",
                    "kind": "artifact",
                    "category": selected_category,
                    "artifact": artifact,
                    "technique": technique,
                    "path": str(SKILL_ROOT / "assets" / "casebook" / artifacts[artifact].get("index", "")),
                    "reason": f"keyword {keyword}",
                }
            )
    return [hit, *artifact_hits[:5]]


def select_reference_hits(terms: dict[str, list[str]], state: dict[str, Any]) -> list[dict[str, Any]]:
    hits = []
    keywords = set(terms.get("keywords", []))
    category = str(state.get("category") or "").lower()
    keywords.add(category)
    for keyword in sorted(keywords):
        filename = KNOWLEDGE_FILES.get(keyword)
        if not filename:
            continue
        path = SKILL_ROOT / "references" / filename
        if path.exists():
            hits.append({"source": "category-knowledge", "keyword": keyword, "path": str(path), "reason": "local category reference"})
    skill_tree = SKILL_ROOT / "references" / "ctf-agent-skill-tree.md"
    if skill_tree.exists():
        hits.insert(0, {"source": "skill-tree", "path": str(skill_tree), "reason": "Nemo-style routing base"})
    return hits[:12]


def select_case_card_hits(terms: dict[str, list[str]]) -> list[dict[str, Any]]:
    cards = sorted((SKILL_ROOT / "references").glob("ctf-case-*.md"))
    if not cards:
        return []
    tokens = {token for token in terms.get("keywords", []) if len(token) >= 3}
    tokens.update({Path(item).suffix.lower().lstrip(".") for item in terms.get("files", [])})
    hits = []
    for card in cards:
        text = card.read_text(encoding="utf-8", errors="replace").lower()[:20000]
        score = sum(1 for token in tokens if token and token in text)
        if score:
            hits.append({"source": "solved-case-card", "path": str(card), "score": score})
    return sorted(hits, key=lambda item: item["score"], reverse=True)[:8]


def select_optional_vuln_hits(terms: dict[str, list[str]]) -> list[dict[str, Any]]:
    hits = []
    vulhub = SKILL_ROOT / "assets" / "vulhub" / "index" / "master-index.json"
    if vulhub.exists():
        index = read_json(vulhub, default=[])
        for entry in index:
            entry_text = json.dumps(entry, ensure_ascii=False).lower()
            if any(cve.lower() in entry_text for cve in terms.get("cves", [])) or any(keyword in entry_text for keyword in terms.get("keywords", [])):
                hits.append({"source": "vulhub-local", "entry": entry})
                if len(hits) >= 5:
                    break
    sidebar = SKILL_ROOT / "assets" / "vulnerability-wiki" / "_sidebar.md"
    if sidebar.exists():
        text = sidebar.read_text(encoding="utf-8", errors="replace")
        for cve in terms.get("cves", []):
            if cve in text:
                hits.append({"source": "vulnerability-wiki-local", "match": cve, "path": str(sidebar)})
    return hits


def record_knowledge_memory(case_dir: Path, hits: dict[str, Any]) -> None:
    layers = hits.get("layers", {})
    terms = hits.get("terms", {})
    term_summary = ", ".join(terms.get("keywords", [])[:12]) or "no local keyword terms"
    for item in layers.get("casebook", [])[:6]:
        title = item.get("category") or item.get("artifact") or item.get("kind") or "casebook hit"
        path = item.get("path")
        memory_store.add_surface_path(
            case_dir,
            source="casebook",
            title=f"Casebook: {title}",
            summary=item.get("reason") or "Local casebook route candidate.",
            evidence_refs=[path] if path else [],
            lane_id="knowledge",
            dedupe_key=f"ctf-knowledge-casebook:{path or title}",
        )
        memory_store.add_candidate(
            case_dir,
            title=f"Verify casebook route: {title}",
            hypothesis=f"A local casebook hit may match observed terms: {term_summary}.",
            lane_id="knowledge",
            constraints=[
                "Treat the casebook hit as a hypothesis, not an answer.",
                "Verify the route with a skill-backed probe against the current target.",
            ],
            evidence_refs=[path] if path else [],
            dedupe_key=f"ctf-candidate-casebook:{path or title}",
        )
    for item in layers.get("category_knowledge", [])[:6]:
        path = item.get("path")
        keyword = item.get("keyword") or Path(path or "category").stem
        memory_store.add_surface_path(
            case_dir,
            source="category_knowledge",
            title=f"Category knowledge: {keyword}",
            summary=item.get("reason") or "Local category reference matched current evidence.",
            evidence_refs=[path] if path else [],
            lane_id="knowledge",
            dedupe_key=f"ctf-knowledge-category:{path or keyword}",
        )
        memory_store.add_candidate(
            case_dir,
            title=f"Probe category pattern: {keyword}",
            hypothesis=f"The {keyword} reference may contain a reusable route for the observed surface.",
            lane_id="knowledge",
            constraints=[
                "Extract only the transferable pattern.",
                "Keep first-pass evidence and current target behavior as the deciding signal.",
            ],
            evidence_refs=[path] if path else [],
            dedupe_key=f"ctf-candidate-category:{path or keyword}",
        )


def command_knowledge(args: argparse.Namespace) -> None:
    case_dir = ensure_case(case_path(args.case_dir))
    state = load_state(case_dir)
    meta = read_json(case_dir / "case.json", default={}) or {}
    corpus = gather_corpus(case_dir)
    terms = extract_terms(corpus, meta, state)
    hits = {
        "generated_at": utc_now(),
        "terms": terms,
        "layers": {
            "notes": {
                "info_has_body": note_has_body(read_notes(case_dir).get("info", "")),
                "infer_has_body": note_has_body(read_notes(case_dir).get("infer", "")),
                "result_has_body": note_has_body(read_notes(case_dir).get("result", "")),
            },
            "casebook": select_casebook_hits(terms, state),
            "category_knowledge": select_reference_hits(terms, state),
            "solved_cases": select_case_card_hits(terms),
            "optional_vuln_indexes": select_optional_vuln_hits(terms),
            "web_search": {"allowed": bool(args.stall_gate), "reason": "stall gate required before WebSearch"},
        },
    }
    atomic_write_json(case_dir / "knowledge" / "hits.json", hits)
    record_knowledge_memory(case_dir, hits)
    summary_lines = [
        "## Knowledge Routing",
        "",
        f"- Terms: {', '.join(terms.get('keywords', [])[:20]) or 'none'}",
        f"- CVEs: {', '.join(terms.get('cves', [])[:10]) or 'none'}",
        f"- Casebook hits: {len(hits['layers']['casebook'])}",
        f"- Category knowledge hits: {len(hits['layers']['category_knowledge'])}",
        f"- Solved case hits: {len(hits['layers']['solved_cases'])}",
        f"- Optional vuln index hits: {len(hits['layers']['optional_vuln_indexes'])}",
        f"- WebSearch allowed: {hits['layers']['web_search']['allowed']}",
    ]
    append_note(case_dir, "infer", "\n".join(summary_lines), source="ctf_agent.knowledge")
    record_event(case_dir, "knowledge", {"hits": str(case_dir / "knowledge" / "hits.json"), "stall_gate": args.stall_gate})
    print(json.dumps({"status": "ok", "hits": hits}, ensure_ascii=False, indent=2))


def command_memory(args: argparse.Namespace) -> None:
    case_dir = ensure_case(case_path(args.case_dir))
    if args.next:
        result = memory_store.generate_next_constraints(case_dir)
    else:
        result = memory_store.summarize_memory(case_dir)
    print(json.dumps({"status": "ok", "memory": result}, ensure_ascii=False, indent=2))


def command_candidate(args: argparse.Namespace) -> None:
    case_dir = ensure_case(case_path(args.case_dir))
    try:
        candidate = memory_store.add_candidate(
            case_dir,
            title=args.title,
            hypothesis=args.hypothesis,
            lane_id=args.lane,
            constraints=args.constraint,
            evidence_refs=args.evidence,
            status=args.status,
            dedupe_key=args.dedupe_key,
        )
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    append_note(
        case_dir,
        "infer",
        "\n".join(
            [
                "## Candidate Route",
                "",
                f"- ID: `{candidate['id']}`",
                f"- Lane: `{candidate.get('lane_id')}`",
                f"- Title: {candidate.get('title')}",
                f"- Hypothesis: {candidate.get('hypothesis')}",
                f"- Constraints: {', '.join(candidate.get('constraints') or []) or 'none'}",
                f"- Evidence: {', '.join(candidate.get('evidence_refs') or []) or 'none'}",
            ]
        ),
        source="ctf_agent.candidate",
    )
    record_event(case_dir, "candidate", {"id": candidate["id"], "lane_id": candidate.get("lane_id")})
    print(json.dumps({"status": "ok", "candidate": candidate}, ensure_ascii=False, indent=2))


def command_attempt(args: argparse.Namespace) -> None:
    case_dir = ensure_case(case_path(args.case_dir))
    try:
        attempt = memory_store.record_attempt(
            case_dir,
            candidate_id=args.candidate_id,
            outcome=args.outcome,
            summary=args.summary,
            evidence_refs=args.evidence,
            failure_reason=args.failure_reason,
            next_constraints=args.next_constraint,
        )
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    note_type = "info" if args.outcome == "negative" else "infer"
    append_note(
        case_dir,
        note_type,
        "\n".join(
            [
                "## Candidate Attempt",
                "",
                f"- Candidate: `{args.candidate_id}`",
                f"- Outcome: `{args.outcome}`",
                f"- Summary: {args.summary}",
                f"- Failure reason: {args.failure_reason or 'n/a'}",
                f"- Next constraints: {', '.join(args.next_constraint or []) or 'none'}",
                f"- Evidence: {', '.join(args.evidence or []) or 'none'}",
            ]
        ),
        source="ctf_agent.attempt",
    )
    record_event(case_dir, "attempt", {"id": attempt["id"], "candidate_id": args.candidate_id, "outcome": args.outcome})
    print(json.dumps({"status": "ok", "attempt": attempt}, ensure_ascii=False, indent=2))


def command_block(args: argparse.Namespace) -> None:
    case_dir = ensure_case(case_path(args.case_dir))
    state = load_state(case_dir)
    state["state"] = "blocked"
    state["blocked_reason"] = args.reason
    state["next_step"] = args.needs_input or "Human input or new evidence is required."
    save_state(case_dir, state)
    memory_store.record_verification(
        case_dir,
        outcome="blocked",
        summary=args.reason,
        failure_reason=args.tried or args.reason,
        next_constraints=[args.needs_input] if args.needs_input else None,
    )
    content = "\n".join(
        [
            "## Blocked",
            "",
            f"- Reason: {args.reason}",
            f"- Tried: {args.tried or 'not specified'}",
            f"- Needs input: {args.needs_input or 'not specified'}",
        ]
    )
    append_note(case_dir, "timeline", content, source="ctf_agent.block")
    record_event(case_dir, "block", {"reason": args.reason, "tried": args.tried, "needs_input": args.needs_input})
    print(json.dumps({"status": "ok", "state": state}, ensure_ascii=False, indent=2))


def command_fail(args: argparse.Namespace) -> None:
    case_dir = ensure_case(case_path(args.case_dir))
    state = load_state(case_dir)
    state["state"] = "failed"
    state["failure_reason"] = args.reason
    state["next_step"] = "Review failed route, read notes, and retry only if a new hypothesis exists."
    save_state(case_dir, state)
    memory_store.record_verification(
        case_dir,
        outcome="negative",
        summary=args.reason,
        evidence_refs=args.evidence,
        failure_reason=args.reason,
        next_constraints=[f"Retry only with a new hypothesis; avoid failed route: {args.reason}"],
    )
    append_note(case_dir, "info", f"## Failure Record\n\n- Reason: {args.reason}\n- Evidence: {', '.join(args.evidence or []) or 'not specified'}", source="ctf_agent.fail")
    record_event(case_dir, "fail", {"reason": args.reason, "evidence": args.evidence or []})
    print(json.dumps({"status": "ok", "state": state}, ensure_ascii=False, indent=2))


def command_solve(args: argparse.Namespace) -> None:
    if not args.evidence:
        raise SystemExit("solve requires at least one --evidence path")
    case_dir = ensure_case(case_path(args.case_dir))
    state = load_state(case_dir)
    result_note = [
        "## Successful Route",
        "",
        f"- Flag: `{args.flag}`",
        f"- Proof: {args.proof}",
        "",
        "### Evidence",
        *[f"- `{item}`" for item in args.evidence],
    ]
    if args.replay_command:
        result_note.extend(["", "### Replay Commands", *[f"- `{item}`" for item in args.replay_command]])
    append_note(case_dir, "result", "\n".join(result_note), source="ctf_agent.solve")
    state["state"] = "solved"
    state["phase"] = "distill"
    state["phase_entered_at"] = utc_now()
    state["solved_at"] = utc_now()
    state["result"] = {"flag": args.flag, "proof": args.proof, "evidence": args.evidence, "replay_command": args.replay_command or []}
    state["next_step"] = "Distill reusable knowledge into case cards, category notes, or skill tools."
    save_state(case_dir, state)
    memory_store.record_verification(
        case_dir,
        outcome="success",
        summary=f"Solved route proved: {args.proof}",
        evidence_refs=args.evidence,
    )
    record_event(case_dir, "solve", state["result"])
    print(json.dumps({"status": "ok", "state": state}, ensure_ascii=False, indent=2))


def command_summary(args: argparse.Namespace) -> None:
    case_dir = ensure_case(case_path(args.case_dir))
    state = refresh_timeout(case_dir)
    notes = read_notes(case_dir)
    hits = read_json(case_dir / "knowledge" / "hits.json", default={}) or {}
    summary = {
        "case": state_summary(case_dir),
        "notes": {key: {"has_body": note_has_body(value), "preview": value[:500]} for key, value in notes.items()},
        "recent_events": latest_events(case_dir, args.events),
        "checkpoints": checkpoint_records(case_dir)[-args.checkpoints :],
        "knowledge": {
            "terms": hits.get("terms", {}),
            "casebook": hits.get("layers", {}).get("casebook", [])[:5],
            "category_knowledge": hits.get("layers", {}).get("category_knowledge", [])[:5],
                "solved_cases": hits.get("layers", {}).get("solved_cases", [])[:5],
        },
        "memory": memory_store.summarize_memory(case_dir),
    }
    if args.format == "json":
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return
    lines = [
        f"# CTF Agent Summary: {state.get('name')}",
        "",
        f"- State: {state.get('state')}",
        f"- Phase: {state.get('phase')}",
        f"- Target: {state.get('target')}",
        f"- Next: {state.get('next_step')}",
        f"- Blocked: {state.get('blocked_reason') or 'no'}",
        f"- Failure: {state.get('failure_reason') or 'no'}",
        "",
        "## Notes",
        *[f"- {key}: {'yes' if note_has_body(value) else 'empty'}" for key, value in notes.items()],
        "",
        "## Recent Events",
        *[f"- {item.get('time')} {item.get('event')}: {item.get('data')}" for item in summary["recent_events"]],
        "",
        "## Knowledge",
        f"- Keywords: {', '.join(summary['knowledge']['terms'].get('keywords', [])[:20]) if summary['knowledge']['terms'] else 'none'}",
        f"- Casebook hits: {len(summary['knowledge']['casebook'])}",
        f"- Category knowledge hits: {len(summary['knowledge']['category_knowledge'])}",
        f"- Solved case hits: {len(summary['knowledge']['solved_cases'])}",
        "",
        *memory_store.render_summary_lines(summary["memory"]),
    ]
    print("\n".join(lines))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Nemo-style local CTF agent state machine without containers")
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="initialize a local CTF case")
    init.add_argument("--case-dir", required=True)
    init.add_argument("--name")
    init.add_argument("--category", default="ctf")
    init.add_argument("--target")
    init.add_argument("--url")
    init.add_argument("--artifact", action="append")
    init.add_argument("--hint")
    init.add_argument("--flag-count", type=int, default=1)
    init.add_argument("--timeout", type=int, default=3600)
    init.add_argument("--priority", type=int, default=50)
    init.add_argument("--max-retries", type=int, default=3)
    init.add_argument("--force", action="store_true")
    init.set_defaults(func=command_init)

    queue = sub.add_parser("queue", help="list local CTF cases")
    queue.add_argument("--root")
    queue.add_argument("--refresh-timeouts", action=argparse.BooleanOptionalAction, default=True)
    queue.set_defaults(func=command_queue)

    nxt = sub.add_parser("next", help="select the next open or retryable case")
    nxt.set_defaults(func=command_next)

    start = sub.add_parser("start", help="mark a case started and enter note replay")
    start.add_argument("--case-dir", required=True)
    start.set_defaults(func=command_start)

    note = sub.add_parser("note", help="read or append case notes")
    note.add_argument("--case-dir", required=True)
    note.add_argument("--type", choices=VALID_NOTES, default="info")
    note.add_argument("--content")
    note.add_argument("--file")
    note.add_argument("--source", default="operator")
    note.add_argument("--read-all", action="store_true")
    note.set_defaults(func=command_note)

    phase = sub.add_parser("phase", help="show, checkpoint, or advance the current phase")
    phase.add_argument("--case-dir", required=True)
    phase.add_argument("--checkpoint-summary")
    phase.add_argument("--evidence", action="append")
    phase.add_argument("--next-step")
    phase.add_argument("--advance", action="store_true")
    phase.set_defaults(func=command_phase)

    knowledge = sub.add_parser("knowledge", help="route local notes and evidence through local knowledge layers")
    knowledge.add_argument("--case-dir", required=True)
    knowledge.add_argument("--stall-gate", action="store_true", help="mark WebSearch as allowed after local routes stall")
    knowledge.set_defaults(func=command_knowledge)

    mem = sub.add_parser("memory", help="show structured route memory or generate next constraints")
    mem.add_argument("--case-dir", required=True)
    mem_group = mem.add_mutually_exclusive_group(required=True)
    mem_group.add_argument("--summary", action="store_true")
    mem_group.add_argument("--next", action="store_true")
    mem.set_defaults(func=command_memory)

    candidate = sub.add_parser("candidate", help="record a structured candidate route")
    candidate.add_argument("--case-dir", required=True)
    candidate.add_argument("--title", required=True)
    candidate.add_argument("--hypothesis", required=True)
    candidate.add_argument("--lane", default="main")
    candidate.add_argument("--constraint", action="append")
    candidate.add_argument("--evidence", action="append")
    candidate.add_argument("--status", choices=memory_store.VALID_CANDIDATE_STATUSES, default="proposed")
    candidate.add_argument("--dedupe-key")
    candidate.set_defaults(func=command_candidate)

    attempt = sub.add_parser("attempt", help="record a candidate attempt and its evidence outcome")
    attempt.add_argument("--case-dir", required=True)
    attempt.add_argument("--candidate-id", required=True)
    attempt.add_argument("--outcome", choices=memory_store.VALID_OUTCOMES, required=True)
    attempt.add_argument("--summary", required=True)
    attempt.add_argument("--evidence", action="append")
    attempt.add_argument("--failure-reason")
    attempt.add_argument("--next-constraint", action="append")
    attempt.set_defaults(func=command_attempt)

    block = sub.add_parser("block", help="mark a case blocked with a concrete handoff")
    block.add_argument("--case-dir", required=True)
    block.add_argument("--reason", required=True)
    block.add_argument("--tried")
    block.add_argument("--needs-input")
    block.set_defaults(func=command_block)

    fail = sub.add_parser("fail", help="mark a case failed and preserve the failed route")
    fail.add_argument("--case-dir", required=True)
    fail.add_argument("--reason", required=True)
    fail.add_argument("--evidence", action="append")
    fail.set_defaults(func=command_fail)

    solve = sub.add_parser("solve", help="mark a case solved and write result proof")
    solve.add_argument("--case-dir", required=True)
    solve.add_argument("--flag", required=True)
    solve.add_argument("--proof", required=True)
    solve.add_argument("--evidence", action="append", required=True)
    solve.add_argument("--replay-command", action="append")
    solve.set_defaults(func=command_solve)

    summary = sub.add_parser("summary", help="summarize a case for handoff")
    summary.add_argument("--case-dir", required=True)
    summary.add_argument("--format", choices=("markdown", "json"), default="markdown")
    summary.add_argument("--events", type=int, default=8)
    summary.add_argument("--checkpoints", type=int, default=6)
    summary.set_defaults(func=command_summary)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
