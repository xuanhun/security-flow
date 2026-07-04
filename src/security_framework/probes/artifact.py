from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path

from .. import knowledge
from ..engagement import log_command, log_event
from ..utils import write_json


def inventory(root: Path, artifact: Path) -> dict:
    artifact = artifact.expanduser().resolve()
    if not artifact.exists():
        raise SystemExit(f"artifact does not exist: {artifact}")
    data = artifact.read_bytes()
    result = {
        "path": str(artifact),
        "size": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "kind": artifact.suffix.lower().lstrip(".") or "unknown",
        "zip_entries": [],
    }
    if zipfile.is_zipfile(artifact):
        with zipfile.ZipFile(artifact) as zf:
            result["zip_entries"] = [
                {"name": info.filename, "size": info.file_size, "compressed_size": info.compress_size}
                for info in zf.infolist()[:500]
            ]
    evidence_path = root / "evidence" / f"artifact-{artifact.name}.json"
    write_json(evidence_path, result)
    query = f"{artifact.name} {result['kind']} {result['sha256']} {' '.join(item['name'] for item in result['zip_entries'][:20])}"
    hits = knowledge.search(query, limit=5)
    refs = [item["id"] for item in hits.get("results") or []]
    log_command(root, f"artifact inventory {artifact}", tool="artifact", target=str(artifact), outcome="completed", evidence_refs=[str(evidence_path)])
    log_event(root, "probe-artifact", tool="artifact", target=str(artifact), outcome="completed", evidence_refs=[str(evidence_path)], knowledge_refs=refs)
    return {"evidence": str(evidence_path), "knowledge_refs": refs, "result": result}
