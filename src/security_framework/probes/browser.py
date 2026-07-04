from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from ..engagement import log_event
from ..utils import write_json


def check(root: Path) -> dict:
    node = shutil.which("node")
    npm = shutil.which("npm")
    result = {
        "node": node,
        "npm": npm,
        "status": "ready" if node and npm else "missing-node-runtime",
        "message": "Install with scripts/bootstrap.sh --profile node-browser before running browser probes."
        if not (node and npm)
        else "Node runtime is available.",
    }
    if node:
        try:
            result["node_version"] = subprocess.check_output([node, "--version"], text=True).strip()
        except Exception as exc:  # noqa: BLE001
            result["node_error"] = str(exc)
    evidence_path = root / "evidence" / "node-browser-check.json"
    write_json(evidence_path, result)
    log_event(root, "probe-browser-check", tool="browser", outcome=result["status"], evidence_refs=[str(evidence_path)])
    return {"evidence": str(evidence_path), "result": result}
