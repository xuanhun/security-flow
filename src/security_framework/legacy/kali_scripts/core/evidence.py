from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
REPORT_ROOT = REPO_ROOT / "test-reports" / "kali"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def ensure_project(project: str | Path) -> Path:
    path = Path(project)
    if not path.is_absolute():
        path = REPORT_ROOT / path
    path.mkdir(parents=True, exist_ok=True)
    for child in ["evidence", "scans", "findings", "pending"]:
        (path / child).mkdir(exist_ok=True)
    return path


def read_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def append_jsonl(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(data, sort_keys=True) + "\n")


def record_event(project_dir: Path, event: str, data: dict[str, Any] | None = None) -> None:
    append_jsonl(
        project_dir / "commands.jsonl",
        {
            "time": utc_now(),
            "event": event,
            "data": data or {},
        },
    )


def add_finding(project_dir: Path, finding: dict[str, Any]) -> None:
    findings_path = project_dir / "findings.json"
    findings = read_json(findings_path, default=[])
    finding = {"time": utc_now(), **finding}
    findings.append(finding)
    write_json(findings_path, findings)
