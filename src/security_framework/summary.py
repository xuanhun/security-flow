from __future__ import annotations

from pathlib import Path
from typing import Any

from .memory import summary as memory_summary
from .utils import append_jsonl, read_json, read_jsonl, utc_now, write_json


RESULT_STATUSES = ("completed", "solved", "blocked", "failed", "partial")
REQUIRED_JSON_FIELDS = (
    "generated_at",
    "engagement_id",
    "result_status",
    "outcome_summary",
    "scope_summary",
    "authorization_summary",
    "knowledge_summary",
    "evidence_summary",
    "candidate_summary",
    "verification_summary",
    "negative_evidence_summary",
    "findings_summary",
    "proof_summary",
    "replay_summary",
    "distillation_summary",
    "next_steps",
    "redaction_summary",
)


def _latest_evidence(root: Path) -> list[str]:
    evidence_dir = root / "evidence"
    if not evidence_dir.exists():
        return []
    return [str(path) for path in sorted(evidence_dir.rglob("*")) if path.is_file()]


def _command_rows(root: Path) -> list[dict[str, Any]]:
    return read_jsonl(root / "logs" / "commands.jsonl")


def _knowledge_rows(root: Path) -> list[dict[str, Any]]:
    return read_jsonl(root / "logs" / "knowledge-search.jsonl")


def _verification_rows(memory: dict[str, Any]) -> list[dict[str, Any]]:
    return memory.get("verification_recent") or []


def generate(
    root: Path,
    *,
    result_status: str,
    outcome_summary: str,
    proof: list[str] | None = None,
    next_steps: list[str] | None = None,
    distillation: list[str] | None = None,
    flag: str | None = None,
    notes: list[str] | None = None,
) -> dict[str, str]:
    if result_status not in RESULT_STATUSES:
        raise SystemExit(f"result status must be one of: {', '.join(RESULT_STATUSES)}")
    engagement = read_json(root / "engagement.json", {})
    scope = read_json(root / "scope.json", {})
    state = read_json(root / "state.json", {})
    findings = read_json(root / "findings.json", [])
    memory = memory_summary(root)
    commands = _command_rows(root)
    knowledge = _knowledge_rows(root)
    evidence_refs = _latest_evidence(root)
    proof_refs = proof or []
    flag_record = None
    if flag:
        flag_record = {
            "provided": True,
            "value": flag if engagement.get("type") in {"ctf", "lab"} else "<redacted>",
            "redaction": "stored for ctf/lab only; redacted for authorized engagements",
        }
    summary = {
        "generated_at": utc_now(),
        "engagement_id": root.name,
        "engagement_type": engagement.get("type"),
        "result_status": result_status,
        "outcome_summary": outcome_summary,
        "scope_summary": {
            "targets": [item.get("value") for item in scope.get("targets") or []],
            "excluded": [item.get("value") for item in scope.get("excluded") or []],
            "phase_at_summary": state.get("phase"),
            "status_at_summary": state.get("status"),
        },
        "authorization_summary": scope.get("authorization") or {},
        "knowledge_summary": {
            "search_count": len(knowledge),
            "recent": [
                {
                    "phase": row.get("phase"),
                    "outcome": row.get("outcome"),
                    "knowledge_refs": row.get("knowledge_refs") or [],
                }
                for row in knowledge[-10:]
            ],
        },
        "evidence_summary": {
            "evidence_count": len(evidence_refs),
            "evidence_refs": evidence_refs,
            "command_count": len(commands),
            "recent_commands": [
                {
                    "phase": row.get("phase"),
                    "tool": row.get("tool"),
                    "command": row.get("command"),
                    "outcome": row.get("outcome"),
                    "evidence_refs": row.get("evidence_refs") or [],
                }
                for row in commands[-10:]
            ],
        },
        "candidate_summary": memory.get("active_candidates") or [],
        "verification_summary": _verification_rows(memory),
        "negative_evidence_summary": memory.get("negative_evidence") or [],
        "findings_summary": findings,
        "proof_summary": {"proof_refs": proof_refs, "flag": flag_record, "notes": notes or []},
        "replay_summary": {
            "entrypoint": "python scripts/sec.py",
            "report": str(root / "report.md"),
            "context": str(root / "context" / "current.md"),
            "commands_log": str(root / "logs" / "commands.jsonl"),
        },
        "distillation_summary": distillation or [],
        "next_steps": next_steps or [],
        "redaction_summary": "Logs and summaries are passed through framework redaction; review proof artifacts before sharing externally.",
    }
    write_json(root / "summary.json", summary)
    (root / "summary.md").write_text(render_markdown(summary), encoding="utf-8")
    append_jsonl(
        root / "logs" / "decisions.jsonl",
        {
            "time": utc_now(),
            "engagement_id": root.name,
            "phase": state.get("phase"),
            "action": "summary-generate",
            "outcome": result_status,
            "evidence_refs": [str(root / "summary.json"), str(root / "summary.md")],
            "knowledge_refs": [],
            "next_constraints": next_steps or [],
            "redaction_status": "redacted",
        },
    )
    return {"summary_md": str(root / "summary.md"), "summary_json": str(root / "summary.json")}


def validate(root: Path) -> dict[str, Any]:
    summary = read_json(root / "summary.json")
    errors: list[str] = []
    if not isinstance(summary, dict):
        errors.append("missing summary.json")
    else:
        for field in REQUIRED_JSON_FIELDS:
            if field not in summary:
                errors.append(f"missing field: {field}")
        if summary.get("result_status") not in RESULT_STATUSES:
            errors.append("invalid result_status")
        knowledge = summary.get("knowledge_summary") or {}
        if int(knowledge.get("search_count") or 0) < 1:
            errors.append("summary must include at least one knowledge-search record")
        evidence = summary.get("evidence_summary") or {}
        if int(evidence.get("command_count") or 0) < 1 and int(evidence.get("evidence_count") or 0) < 1:
            errors.append("summary must include commands or evidence")
    if not (root / "summary.md").exists():
        errors.append("missing summary.md")
    return {"status": "ok" if not errors else "failed", "errors": errors}


def require_valid(root: Path) -> None:
    result = validate(root)
    if result["status"] != "ok":
        raise SystemExit(
            "completion summary is not valid. Run: "
            f"python scripts/sec.py summary generate --engagement {root.name} --result-status completed "
            "--outcome-summary '<what happened>'"
        )


def render_markdown(summary: dict[str, Any]) -> str:
    lines = [
        f"# Test Summary: {summary['engagement_id']}",
        "",
        f"- Generated: {summary['generated_at']}",
        f"- Result: {summary['result_status']}",
        f"- Outcome: {summary['outcome_summary']}",
        f"- Type: {summary.get('engagement_type')}",
        "",
        "## Scope And Authorization",
    ]
    for target in summary["scope_summary"].get("targets") or []:
        lines.append(f"- Target: {target}")
    auth = summary.get("authorization_summary") or {}
    lines.append(f"- Authorization: {auth.get('status', 'unknown')} - {auth.get('note', '')}")
    lines.extend(["", "## Knowledge Retrieval"])
    lines.append(f"- Search records: {summary['knowledge_summary'].get('search_count', 0)}")
    for row in summary["knowledge_summary"].get("recent") or []:
        refs = row.get("knowledge_refs") or []
        lines.append(f"- {row.get('phase')}: {row.get('outcome')} ({len(refs)} refs)")
    lines.extend(["", "## Evidence And Replay"])
    lines.append(f"- Evidence files: {summary['evidence_summary'].get('evidence_count', 0)}")
    lines.append(f"- Commands logged: {summary['evidence_summary'].get('command_count', 0)}")
    lines.append(f"- Commands log: `{summary['replay_summary'].get('commands_log')}`")
    lines.extend(["", "## Findings And Proof"])
    findings = summary.get("findings_summary") or []
    if findings:
        for item in findings:
            lines.append(f"- [{item.get('severity', 'info')}] {item.get('title')}")
    else:
        lines.append("- No confirmed findings recorded.")
    proof = summary.get("proof_summary") or {}
    for ref in proof.get("proof_refs") or []:
        lines.append(f"- Proof: `{ref}`")
    flag = proof.get("flag") or {}
    if flag.get("provided"):
        lines.append(f"- Flag/result token: `{flag.get('value')}`")
    lines.extend(["", "## Candidates And Negative Evidence"])
    for item in summary.get("candidate_summary") or []:
        lines.append(f"- Candidate {item.get('id')}: {item.get('title')} [{item.get('status')}]")
    for item in summary.get("negative_evidence_summary") or []:
        lines.append(f"- Negative: {item.get('summary') or item.get('failure_reason')}")
    lines.extend(["", "## Distillation And Next Steps"])
    for item in summary.get("distillation_summary") or []:
        lines.append(f"- Distill: {item}")
    next_steps = summary.get("next_steps") or []
    if next_steps:
        for item in next_steps:
            lines.append(f"- Next: {item}")
    else:
        lines.append("- Next: none recorded.")
    lines.extend(["", "## Redaction", f"- {summary.get('redaction_summary')}"])
    return "\n".join(lines) + "\n"
