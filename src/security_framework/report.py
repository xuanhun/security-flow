from __future__ import annotations

from pathlib import Path

from .memory import summary as memory_summary
from .utils import read_json, read_jsonl, utc_now, write_json


def generate(root: Path) -> dict:
    engagement = read_json(root / "engagement.json", {})
    scope = read_json(root / "scope.json", {})
    state = read_json(root / "state.json", {})
    findings = read_json(root / "findings.json", [])
    completion_summary = read_json(root / "summary.json", {})
    events = read_jsonl(root / "logs" / "events.jsonl")
    knowledge = read_jsonl(root / "logs" / "knowledge-search.jsonl")
    memory = memory_summary(root)
    report_json = {
        "generated_at": utc_now(),
        "engagement": engagement,
        "scope": scope,
        "state": state,
        "findings": findings,
        "memory": memory,
        "event_count": len(events),
        "knowledge_search_count": len(knowledge),
        "completion_summary": completion_summary if isinstance(completion_summary, dict) else {},
    }
    write_json(root / "report.json", report_json)
    lines = [
        f"# Security Assessment Report: {engagement.get('name', root.name)}",
        "",
        f"- Generated: {report_json['generated_at']}",
        f"- Engagement ID: {root.name}",
        f"- Type: {engagement.get('type', 'unknown')}",
        f"- Phase: {state.get('phase', 'unknown')}",
        f"- Status: {state.get('status', 'unknown')}",
        "",
        "## Scope",
    ]
    for target in scope.get("targets") or []:
        lines.append(f"- {target.get('value')}")
    lines.extend(["", "## Knowledge Retrieval", f"- Search records: {len(knowledge)}"])
    for row in knowledge[-10:]:
        refs = row.get("knowledge_refs") or []
        lines.append(f"- {row.get('phase')}: {row.get('outcome')} ({len(refs)} refs)")
    lines.extend(["", "## Memory", f"- Candidates: {memory['counts'].get('candidate_routes', 0)}"])
    for item in memory.get("next_constraints") or []:
        lines.append(f"- Next: {item.get('constraint')}")
    lines.extend(["", "## Findings"])
    if findings:
        for item in findings:
            lines.append(f"- [{item.get('severity', 'info')}] {item.get('title')}")
    else:
        lines.append("- No confirmed findings recorded.")
    if isinstance(completion_summary, dict) and completion_summary:
        lines.extend(
            [
                "",
                "## Completion Summary",
                f"- Result: {completion_summary.get('result_status')}",
                f"- Outcome: {completion_summary.get('outcome_summary')}",
                f"- Summary: `{root / 'summary.md'}`",
            ]
        )
    lines.extend(["", "## Evidence", f"- Events: `{root / 'logs' / 'events.jsonl'}`", f"- Commands: `{root / 'logs' / 'commands.jsonl'}`"])
    (root / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"report_md": str(root / "report.md"), "report_json": str(root / "report.json")}
