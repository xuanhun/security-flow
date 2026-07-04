from __future__ import annotations

import ssl
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

from .. import knowledge
from ..engagement import log_command, log_event
from ..scope import assert_in_scope, load_scope
from ..utils import write_json


SECURITY_HEADERS = (
    "content-security-policy",
    "strict-transport-security",
    "x-content-type-options",
    "x-frame-options",
    "referrer-policy",
)


def baseline(root: Path, target: str, *, timeout: int = 15) -> dict:
    scope = load_scope(root)
    assert_in_scope(target, scope)
    parsed = urlparse(target)
    url = target if parsed.scheme else f"http://{target}"
    headers: dict[str, str] = {}
    body_sample = ""
    status = None
    error = None
    try:
        context = ssl.create_default_context()
        req = urllib.request.Request(url, headers={"User-Agent": "security-framework/0.1"})
        with urllib.request.urlopen(req, timeout=timeout, context=context) as resp:
            status = resp.status
            headers = {key: value for key, value in resp.headers.items()}
            body_sample = resp.read(4096).decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        status = exc.code
        headers = {key: value for key, value in exc.headers.items()}
        body_sample = exc.read(4096).decode("utf-8", errors="replace")
    except Exception as exc:  # noqa: BLE001
        error = str(exc)
    missing = [name for name in SECURITY_HEADERS if name not in {key.lower() for key in headers}]
    evidence = {
        "target": url,
        "status": status,
        "headers": headers,
        "missing_security_headers": missing,
        "body_sample": body_sample,
        "error": error,
    }
    evidence_path = root / "evidence" / "web-baseline.json"
    write_json(evidence_path, evidence)
    query = " ".join([url, str(status or ""), headers.get("Server", ""), headers.get("X-Powered-By", ""), body_sample[:300]])
    hits = knowledge.search(query, limit=5)
    refs = [item["id"] for item in hits.get("results") or []]
    log_command(root, f"web baseline {url}", tool="web", target=url, outcome="completed" if not error else "error", evidence_refs=[str(evidence_path)])
    log_event(root, "probe-web", tool="web", target=url, outcome="completed" if not error else "error", evidence_refs=[str(evidence_path)], knowledge_refs=refs)
    return {"evidence": str(evidence_path), "knowledge_refs": refs, "result": evidence}
