from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


LOG_FIELDS = (
    "time",
    "engagement_id",
    "phase",
    "lane_id",
    "action",
    "tool",
    "target",
    "command",
    "risk",
    "outcome",
    "evidence_refs",
    "knowledge_refs",
    "decision_id",
    "next_constraints",
    "redaction_status",
)

SECRET_PATTERNS = (
    (
        re.compile(
            r"(?i)\b(password|passwd|pwd|api[_-]?key|access[_-]?token|refresh[_-]?token|secret)\s*[:=]\s*([^\s,;]+)"
        ),
        r"\1=<redacted>",
    ),
    (re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._~+/=-]+"), "Bearer <redacted>"),
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slug(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9._-]+", "-", value)
    return value.strip("-") or "engagement"


def read_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    with tmp.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(tmp, path)


def append_jsonl(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(redact(data), ensure_ascii=False, sort_keys=True) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            rows.append({"parse_error": True, "raw": line[:500]})
    return rows


def redact(value: Any) -> Any:
    if isinstance(value, str):
        redacted = value
        for pattern, replacement in SECRET_PATTERNS:
            redacted = pattern.sub(replacement, redacted)
        return redacted
    if isinstance(value, list):
        return [redact(item) for item in value]
    if isinstance(value, tuple):
        return [redact(item) for item in value]
    if isinstance(value, dict):
        return {str(key): redact(item) for key, item in value.items()}
    return value


def relative(path: str | Path) -> str:
    return str(path).replace(os.sep, "/")


def standard_log_record(**kwargs: Any) -> dict[str, Any]:
    record = {field: kwargs.get(field) for field in LOG_FIELDS}
    record["time"] = record.get("time") or utc_now()
    record["lane_id"] = record.get("lane_id") or "main"
    record["risk"] = record.get("risk") or "safe"
    record["outcome"] = record.get("outcome") or "recorded"
    record["evidence_refs"] = record.get("evidence_refs") or []
    record["knowledge_refs"] = record.get("knowledge_refs") or []
    record["next_constraints"] = record.get("next_constraints") or []
    record["redaction_status"] = record.get("redaction_status") or "redacted"
    return record
