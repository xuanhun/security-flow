from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from .evidence import append_jsonl, utc_now


def which(binary: str) -> str | None:
    return shutil.which(binary)


def run_command(
    command: list[str],
    project_dir: Path,
    *,
    timeout: int = 120,
    dry_run: bool = False,
    cwd: Path | None = None,
) -> dict:
    record = {
        "time": utc_now(),
        "command": command,
        "cwd": str(cwd) if cwd else None,
        "dry_run": dry_run,
    }
    if dry_run:
        record.update({"returncode": 0, "stdout": "", "stderr": ""})
        append_jsonl(project_dir / "commands.jsonl", record)
        return record

    try:
        completed = subprocess.run(
            command,
            cwd=str(cwd) if cwd else None,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
        record.update(
            {
                "returncode": completed.returncode,
                "stdout": completed.stdout,
                "stderr": completed.stderr,
            }
        )
    except subprocess.TimeoutExpired as exc:
        record.update(
            {
                "returncode": 124,
                "stdout": exc.stdout or "",
                "stderr": f"timeout after {timeout}s",
            }
        )
    append_jsonl(project_dir / "commands.jsonl", record)
    return record
