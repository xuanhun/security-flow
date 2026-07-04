from __future__ import annotations

import base64
import binascii
import hashlib
from pathlib import Path

from .. import knowledge
from ..engagement import log_command, log_event
from ..utils import write_json


def crypto_triage(root: Path, value: str) -> dict:
    attempts: list[dict] = []
    raw = value.strip()
    for label, candidate in (("raw", raw), ("padded", raw + "=" * (-len(raw) % 4))):
        try:
            decoded = base64.b64decode(candidate, validate=False)
            attempts.append({"label": label, "encoding": "base64", "decoded_sample": decoded[:200].decode("utf-8", errors="replace")})
        except (binascii.Error, ValueError):
            pass
    result = {"input_sha256": hashlib.sha256(raw.encode()).hexdigest(), "attempts": attempts}
    evidence_path = root / "evidence" / "crypto-triage.json"
    write_json(evidence_path, result)
    hits = knowledge.search(f"crypto base64 encoding {raw[:80]}", limit=5)
    refs = [item["id"] for item in hits.get("results") or []]
    log_command(root, "crypto triage", tool="crypto", target="<local>", outcome="completed", evidence_refs=[str(evidence_path)])
    log_event(root, "probe-crypto", tool="crypto", outcome="completed", evidence_refs=[str(evidence_path)], knowledge_refs=refs)
    return {"evidence": str(evidence_path), "knowledge_refs": refs, "result": result}


def file_stub(root: Path, tool: str, path: Path) -> dict:
    path = path.expanduser().resolve()
    if not path.exists():
        raise SystemExit(f"file does not exist: {path}")
    result = {
        "path": str(path),
        "size": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "note": f"{tool} detailed parser is not installed in core; evidence inventory recorded.",
    }
    evidence_path = root / "evidence" / f"{tool}-{path.name}.json"
    write_json(evidence_path, result)
    hits = knowledge.search(f"{tool} {path.name} {path.suffix}", limit=5)
    refs = [item["id"] for item in hits.get("results") or []]
    log_command(root, f"{tool} inspect {path}", tool=tool, target=str(path), outcome="completed", evidence_refs=[str(evidence_path)])
    log_event(root, f"probe-{tool}", tool=tool, outcome="completed", evidence_refs=[str(evidence_path)], knowledge_refs=refs)
    return {"evidence": str(evidence_path), "knowledge_refs": refs, "result": result}
