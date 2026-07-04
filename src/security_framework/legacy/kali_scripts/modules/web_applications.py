from __future__ import annotations

from pathlib import Path

from core.evidence import add_finding, record_event, write_json
from core.runner import run_command, which
from core.scope import assert_in_scope
from core.web import fetch_baseline


def web_baseline(project_dir: Path, scope: dict, target: str, use_whatweb: bool = False) -> dict:
    assert_in_scope(target, scope)
    result = fetch_baseline(target)
    output_path = project_dir / "evidence" / f"{target.replace('/', '_').replace(':', '_')}_web.json"
    result["evidence"] = str(output_path)
    write_json(output_path, result)
    if result.get("missing_security_headers"):
        add_finding(
            project_dir,
            {
                "title": "Missing common HTTP security headers",
                "severity": "low",
                "target": target,
                "evidence": str(output_path),
                "description": "The baseline response did not include one or more common browser security headers: "
                + ", ".join(result["missing_security_headers"]),
                "recommendation": "Review whether CSP, HSTS, X-Content-Type-Options, frame, referrer, and permissions policies are appropriate for this application.",
            },
        )
    if use_whatweb and which("whatweb"):
        run_command(["whatweb", "--log-json", str(project_dir / "evidence" / "whatweb.json"), target], project_dir)
    record_event(project_dir, "web-baseline", {"target": target, "output": str(output_path)})
    return result
