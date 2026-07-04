from __future__ import annotations

from pathlib import Path

from . import memory as memory_store
from .evidence import read_json, utc_now, write_json


SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}


def load_findings(project_dir: Path) -> list[dict]:
    findings = read_json(project_dir / "findings.json", default=[])
    return sorted(findings, key=lambda item: SEVERITY_ORDER.get(item.get("severity", "info"), 9))


def render_markdown(project_dir: Path) -> str:
    scope = read_json(project_dir / "scope.json", default={})
    findings = load_findings(project_dir)
    memory_summary = memory_store.summarize_memory(project_dir)
    lines = [
        f"# Security Assessment Report: {scope.get('name', project_dir.name)}",
        "",
        f"Generated: {utc_now()}",
        "",
        "## Scope",
        "",
    ]
    for target in scope.get("targets", []):
        lines.append(f"- {target.get('value')} ({target.get('kind')})")
    if scope.get("excluded"):
        lines.extend(["", "Excluded:"])
        for target in scope["excluded"]:
            lines.append(f"- {target.get('value')} ({target.get('kind')})")
    lines.extend(["", "## Findings", ""])
    if not findings:
        lines.append("No findings recorded.")
    for index, finding in enumerate(findings, start=1):
        lines.extend(
            [
                f"### {index}. {finding.get('title', 'Untitled finding')}",
                "",
                f"- Severity: {finding.get('severity', 'info')}",
                f"- Target: {finding.get('target', 'n/a')}",
                f"- Evidence: {finding.get('evidence', 'n/a')}",
                "",
                finding.get("description", "No description provided."),
                "",
                "Recommendation:",
                "",
                finding.get("recommendation", "Review and remediate according to asset owner guidance."),
                "",
            ]
        )
    lines.extend(["", *memory_store.render_summary_lines(memory_summary), ""])
    lines.extend(["## Evidence", "", f"- Project directory: `{project_dir}`", ""])
    return "\n".join(lines)


def write_report(project_dir: Path) -> dict:
    markdown = render_markdown(project_dir)
    report_md = project_dir / "report.md"
    report_md.write_text(markdown, encoding="utf-8")
    report_json = {
        "generated_at": utc_now(),
        "project_dir": str(project_dir),
        "findings": load_findings(project_dir),
        "memory": memory_store.summarize_memory(project_dir),
    }
    write_json(project_dir / "report.json", report_json)
    return {"markdown": str(report_md), "json": str(project_dir / "report.json")}
