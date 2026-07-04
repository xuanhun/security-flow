from __future__ import annotations

import asyncio
import hashlib
import json
from pathlib import Path
from typing import Any

from .. import knowledge
from ..engagement import log_command, log_event
from ..scope import assert_in_scope, load_scope
from ..utils import write_json


def solve_pow(prefix: str, target: str, *, max_nonce: int = 10_000_000) -> str:
    nonce = 0
    while nonce < max_nonce:
        nonce_text = str(nonce)
        if hashlib.sha256((prefix + nonce_text).encode("utf-8")).hexdigest().startswith(target):
            return nonce_text
        nonce += 1
    raise RuntimeError("PoW limit reached")


async def _run(url: str, message: str | None, timeout: float) -> dict[str, Any]:
    try:
        import websockets
    except ImportError as exc:
        raise RuntimeError("missing dependency: websockets. Install python-core requirements first.") from exc

    events: list[dict[str, Any]] = []
    async with websockets.connect(url, ping_interval=30, ping_timeout=10) as ws:
        challenge = json.loads(await asyncio.wait_for(ws.recv(), timeout=timeout))
        events.append({"direction": "recv", "data": challenge})
        if challenge.get("type") == "pow_challenge":
            nonce = solve_pow(challenge["prefix"], challenge["target"])
            submit = {"type": "pow_submit", "nonce": nonce}
            await ws.send(json.dumps(submit))
            events.append({"direction": "send", "data": submit | {"nonce": "<redacted>"}})
            accept = json.loads(await asyncio.wait_for(ws.recv(), timeout=timeout))
            events.append({"direction": "recv", "data": accept})
        if message:
            payload = {"type": "chat", "query": message}
            await ws.send(json.dumps(payload))
            events.append({"direction": "send", "data": payload})
            while True:
                data = json.loads(await asyncio.wait_for(ws.recv(), timeout=timeout))
                events.append({"direction": "recv", "data": data})
                if data.get("type") in {"end_event", "error", "disconnect"}:
                    break
    return {"url": url, "events": events}


def probe(root: Path, url: str, *, message: str | None = None, timeout: float = 30.0) -> dict:
    scope = load_scope(root)
    assert_in_scope(url, scope)
    try:
        result = asyncio.run(_run(url, message, timeout))
        outcome = "completed"
        error = None
    except Exception as exc:  # noqa: BLE001
        result = {"url": url, "events": []}
        outcome = "error"
        error = str(exc)
    if error:
        result["error"] = error
    evidence_path = root / "evidence" / "agent-ws.json"
    write_json(evidence_path, result)
    query = f"agent websocket pow {' '.join(str(item.get('data', {}).get('type', '')) for item in result.get('events', []))}"
    hits = knowledge.search(query, limit=5)
    refs = [item["id"] for item in hits.get("results") or []]
    log_command(root, f"agent-ws {url}", tool="agent-ws", target=url, outcome=outcome, evidence_refs=[str(evidence_path)])
    log_event(root, "probe-agent-ws", tool="agent-ws", target=url, outcome=outcome, evidence_refs=[str(evidence_path)], knowledge_refs=refs)
    return {"evidence": str(evidence_path), "knowledge_refs": refs, "result": result}
