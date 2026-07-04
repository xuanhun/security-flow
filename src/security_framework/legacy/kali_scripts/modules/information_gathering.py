from __future__ import annotations

from pathlib import Path

from core.evidence import add_finding, record_event, write_json
from core.net import parse_ports, tcp_scan
from core.runner import run_command, which
from core.scope import assert_in_scope


def scan_target(project_dir: Path, scope: dict, target: str, ports: str | None, use_nmap: bool) -> dict:
    assert_in_scope(target, scope)
    output_path = project_dir / "scans" / f"{target.replace('/', '_')}_ports.json"
    if use_nmap and which("nmap"):
        command = ["nmap", "-sV", "-oX", str(project_dir / "scans" / f"{target}_nmap.xml"), target]
        result = run_command(command, project_dir, timeout=600)
        summary = {
            "target": target,
            "tool": "nmap",
            "returncode": result["returncode"],
            "xml": command[3],
            "output": str(output_path),
        }
    else:
        port_list = parse_ports(ports)
        results = tcp_scan(
            target,
            port_list,
            concurrency=int(scope.get("limits", {}).get("max_concurrency", 8)),
        )
        summary = {"target": target, "tool": "python-socket", "results": results, "output": str(output_path)}
        for item in results:
            if item.get("open"):
                add_finding(
                    project_dir,
                    {
                        "title": f"Open TCP port {item['port']}",
                        "severity": "info",
                        "target": target,
                        "evidence": str(output_path),
                        "description": f"TCP port {item['port']} accepted a connection.",
                        "recommendation": "Confirm the service is expected and access-controlled.",
                    },
                )
    write_json(output_path, summary)
    record_event(project_dir, "scan-target", {"target": target, "output": str(output_path)})
    return summary
