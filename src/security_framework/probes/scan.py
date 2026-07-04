from __future__ import annotations

import socket
from pathlib import Path

from .. import knowledge
from ..engagement import log_command, log_event
from ..scope import assert_in_scope, load_scope, normalize_target
from ..utils import write_json


def parse_ports(value: str | None) -> list[int]:
    if not value:
        return [22, 80, 443, 8000, 8080, 8443]
    ports: list[int] = []
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start, end = part.split("-", 1)
            ports.extend(range(int(start), int(end) + 1))
        else:
            ports.append(int(part))
    return sorted({port for port in ports if 1 <= port <= 65535})


def tcp_scan(root: Path, target: str, *, ports: str | None = None, timeout: float = 1.0) -> dict:
    scope = load_scope(root)
    assert_in_scope(target, scope)
    host = normalize_target(target)
    results: list[dict] = []
    for port in parse_ports(ports):
        open_state = False
        error = None
        try:
            with socket.create_connection((host, port), timeout=timeout):
                open_state = True
        except OSError as exc:
            error = exc.__class__.__name__
        results.append({"host": host, "port": port, "open": open_state, "error": error})
    evidence_path = root / "evidence" / "tcp-scan.json"
    write_json(evidence_path, {"target": host, "ports": results})
    open_ports = [str(item["port"]) for item in results if item["open"]]
    hits = knowledge.search(f"{host} {' '.join(open_ports)} tcp service port scan", limit=5)
    refs = [item["id"] for item in hits.get("results") or []]
    log_command(root, f"scan {host} --ports {ports or 'default'}", tool="scan", target=host, outcome="completed", evidence_refs=[str(evidence_path)])
    log_event(root, "probe-scan", tool="scan", target=host, outcome="completed", evidence_refs=[str(evidence_path)], knowledge_refs=refs)
    return {"evidence": str(evidence_path), "knowledge_refs": refs, "open_ports": open_ports, "results": results}
