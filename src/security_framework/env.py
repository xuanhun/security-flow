from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from .utils import write_json


PROFILES = {
    "python-core": ["python", "sqlite3"],
    "node-browser": ["node", "npm"],
    "safe-core": ["python", "sqlite3", "curl"],
    "web": ["python", "curl"],
    "network": ["python"],
    "mobile": ["python"],
    "forensics": ["python"],
    "crypto": ["python"],
    "ai-agent": ["python"],
    "full-lab": ["python", "sqlite3", "node", "npm", "curl"],
}


def check(root: Path | None = None, *, profile: str = "python-core") -> dict:
    if profile not in PROFILES:
        raise SystemExit(f"unknown profile: {profile}")
    tools = []
    for item in PROFILES[profile]:
        if item == "sqlite3":
            try:
                import sqlite3

                tools.append({"name": item, "path": "python-stdlib", "installed": True, "version": sqlite3.sqlite_version})
                continue
            except ImportError:
                tools.append({"name": item, "path": None, "installed": False, "version": None})
                continue
        binary = sys.executable if item == "python" else item
        path = sys.executable if item == "python" else shutil.which(item)
        version = None
        if path:
            try:
                version = subprocess.check_output([binary, "--version"], stderr=subprocess.STDOUT, text=True, timeout=5).strip()
            except Exception:  # noqa: BLE001
                version = None
        tools.append({"name": item, "path": path, "installed": bool(path), "version": version})
    result = {"profile": profile, "tools": tools, "status": "ready" if all(item["installed"] for item in tools) else "missing-tools"}
    if root:
        write_json(root / "evidence" / f"env-{profile}.json", result)
    return result


def plan(profile: str) -> dict:
    if profile not in PROFILES:
        raise SystemExit(f"unknown profile: {profile}")
    if profile == "node-browser":
        commands = ["npm install", "npx playwright install --with-deps"]
    elif profile == "full-lab":
        commands = ["python -m pip install -r requirements.txt", "npm install", "npx playwright install --with-deps"]
    else:
        commands = ["python -m pip install -r requirements.txt"]
    return {"profile": profile, "execute": False, "commands": commands, "note": "Plans only; bootstrap profiles perform installation explicitly."}
