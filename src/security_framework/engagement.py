from __future__ import annotations

from pathlib import Path
from typing import Any

from .paths import engagement_dir, ensure_base_dirs
from .utils import append_jsonl, read_json, slug, standard_log_record, utc_now, write_json


PHASES = (
    "intake",
    "recon",
    "surface-map",
    "knowledge-recall",
    "hypothesis",
    "validation",
    "proof",
    "report",
    "distill",
    "closed",
    "blocked",
)

ACTIVE_PHASES = PHASES[:-2]

ENGAGEMENT_TYPES = ("lab", "authorized", "ctf", "mixed")


def root(engagement_id: str) -> Path:
    return engagement_dir(slug(engagement_id))


def ensure_layout(engagement_id: str) -> Path:
    ensure_base_dirs()
    path = root(engagement_id)
    for child in ("context", "memory", "logs", "evidence", "pending", "reports"):
        (path / child).mkdir(parents=True, exist_ok=True)
    for log_name in ("commands.jsonl", "events.jsonl", "knowledge-search.jsonl", "decisions.jsonl"):
        (path / "logs" / log_name).touch(exist_ok=True)
    (path / "memory" / "events.jsonl").touch(exist_ok=True)
    return path


def default_scope(engagement_id: str, name: str, targets: list[str], excluded: list[str] | None = None) -> dict[str, Any]:
    return {
        "engagement_id": engagement_id,
        "name": name,
        "authorization": {
            "status": "required",
            "note": "Record written authorization or lab/CTF context before real target activity.",
        },
        "limits": {
            "max_concurrency": 4,
            "timeout_seconds": 15,
            "rate_limit": "safe-default",
        },
        "targets": [{"value": target, "kind": "auto", "include_subdomains": False} for target in targets],
        "excluded": [{"value": item, "kind": "auto"} for item in excluded or []],
        "allowed_techniques": ["safe discovery", "bounded validation", "local artifact analysis"],
        "gated_techniques": [
            "exploitation",
            "online password attacks",
            "sniffing or spoofing",
            "wireless attacks",
            "post-exploitation",
            "destructive fuzzing",
            "heavy scans",
            "third-party token validation",
        ],
    }


def init_engagement(
    *,
    engagement_id: str,
    name: str,
    engagement_type: str,
    targets: list[str],
    excluded: list[str] | None = None,
) -> dict[str, Any]:
    engagement_id = slug(engagement_id)
    if engagement_type not in ENGAGEMENT_TYPES:
        raise SystemExit(f"type must be one of: {', '.join(ENGAGEMENT_TYPES)}")
    path = ensure_layout(engagement_id)
    now = utc_now()
    engagement_data = {
        "id": engagement_id,
        "name": name,
        "type": engagement_type,
        "created_at": now,
        "updated_at": now,
        "framework_version": "0.1.0",
    }
    state = {
        "version": "1.0",
        "engagement_id": engagement_id,
        "phase": "intake",
        "status": "open",
        "created_at": now,
        "updated_at": now,
        "phase_entered_at": now,
        "knowledge_recalls": {},
        "phase_history": [{"time": now, "event": "init", "phase": "intake"}],
    }
    write_json(path / "engagement.json", engagement_data)
    write_json(path / "scope.json", default_scope(engagement_id, name, targets, excluded))
    write_json(path / "state.json", state)
    write_json(path / "findings.json", [])
    init_memory(path)
    write_context(path, "Initialized engagement.", [])
    log_event(path, "init", outcome="success", target=", ".join(targets), command="init")
    return {"engagement": str(path), "state": str(path / "state.json"), "scope": str(path / "scope.json")}


def load_state(path: Path) -> dict[str, Any]:
    state = read_json(path / "state.json")
    if not isinstance(state, dict):
        raise SystemExit(f"missing state.json in {path}")
    return state


def save_state(path: Path, state: dict[str, Any]) -> None:
    state["updated_at"] = utc_now()
    write_json(path / "state.json", state)


def init_memory(path: Path) -> None:
    now = utc_now()
    memory_path = path / "memory" / "state.json"
    if memory_path.exists():
        return
    write_json(
        memory_path,
        {
            "version": "1.0",
            "created_at": now,
            "updated_at": now,
            "objects": {
                "goals": [],
                "surface_paths": [],
                "input_formats": [],
                "candidate_routes": [],
                "negative_evidence": [],
                "verification_states": [],
                "next_constraints": [],
            },
            "counters": {
                "goal": 0,
                "surface_path": 0,
                "input_format": 0,
                "candidate_route": 0,
                "negative_evidence": 0,
                "verification_state": 0,
                "next_constraint": 0,
            },
        },
    )
    write_json(path / "memory" / "next-constraints.json", {"generated_at": now, "constraints": []})


def log_event(
    path: Path,
    action: str,
    *,
    tool: str | None = None,
    target: str | None = None,
    command: str | None = None,
    risk: str = "safe",
    outcome: str = "recorded",
    evidence_refs: list[str] | None = None,
    knowledge_refs: list[str] | None = None,
    next_constraints: list[str] | None = None,
) -> dict[str, Any]:
    state = read_json(path / "state.json", {})
    record = standard_log_record(
        engagement_id=state.get("engagement_id") or path.name,
        phase=state.get("phase") or "intake",
        action=action,
        tool=tool,
        target=target,
        command=command,
        risk=risk,
        outcome=outcome,
        evidence_refs=evidence_refs or [],
        knowledge_refs=knowledge_refs or [],
        next_constraints=next_constraints or [],
    )
    append_jsonl(path / "logs" / "events.jsonl", record)
    return record


def log_command(path: Path, command: list[str] | str, *, tool: str, target: str | None, outcome: str, evidence_refs: list[str] | None = None) -> None:
    state = read_json(path / "state.json", {})
    append_jsonl(
        path / "logs" / "commands.jsonl",
        standard_log_record(
            engagement_id=state.get("engagement_id") or path.name,
            phase=state.get("phase") or "intake",
            action="command",
            tool=tool,
            target=target,
            command=command if isinstance(command, str) else " ".join(command),
            outcome=outcome,
            evidence_refs=evidence_refs or [],
        ),
    )


def write_context(path: Path, summary: str, next_constraints: list[str]) -> None:
    state = read_json(path / "state.json", {})
    memory = read_json(path / "memory" / "state.json", {})
    current = [
        f"# Current Context: {path.name}",
        "",
        f"- Phase: {state.get('phase', 'intake')}",
        f"- Status: {state.get('status', 'open')}",
        f"- Summary: {summary}",
        "",
        "## Active Candidates",
    ]
    for candidate in (memory.get("objects", {}).get("candidate_routes") or [])[:10]:
        if candidate.get("status") in {"proposed", "active", "inconclusive"}:
            current.append(f"- {candidate.get('id')}: {candidate.get('title')}")
    current.extend(["", "## Do Not Repeat"])
    for item in (memory.get("objects", {}).get("negative_evidence") or [])[:10]:
        current.append(f"- {item.get('summary') or item.get('failure_reason')}")
    current.extend(["", "## Next Constraints"])
    for constraint in next_constraints[:10]:
        current.append(f"- {constraint}")
    (path / "context" / "current.md").write_text("\n".join(current) + "\n", encoding="utf-8")
    snapshot = {
        "time": utc_now(),
        "engagement_id": path.name,
        "phase": state.get("phase", "intake"),
        "status": state.get("status", "open"),
        "summary": summary,
        "next_constraints": next_constraints,
    }
    write_json(path / "context" / "snapshot.json", snapshot)
    append_jsonl(path / "context" / "history.jsonl", snapshot)


def phase_enter(path: Path, phase: str) -> dict[str, Any]:
    if phase not in PHASES:
        raise SystemExit(f"phase must be one of: {', '.join(PHASES)}")
    if phase in {"closed", "blocked"}:
        from .summary import require_valid

        require_valid(path)
    state = load_state(path)
    now = utc_now()
    state["phase"] = phase
    if phase in {"closed", "blocked"}:
        state["status"] = phase
    state["phase_entered_at"] = now
    state.setdefault("phase_history", []).append({"time": now, "event": "enter", "phase": phase})
    save_state(path, state)
    log_event(path, "phase-enter", target=phase, outcome="success")
    write_context(path, f"Entered phase {phase}.", [])
    return state


def phase_exit(path: Path, phase: str | None = None) -> dict[str, Any]:
    state = load_state(path)
    current_phase = phase or state.get("phase")
    if current_phase not in PHASES:
        raise SystemExit(f"unknown phase: {current_phase}")
    recalls = state.get("knowledge_recalls") or {}
    if current_phase in ACTIVE_PHASES and not recalls.get(current_phase):
        raise SystemExit(
            f"phase '{current_phase}' cannot exit before knowledge recall. "
            f"Run: python scripts/sec.py knowledge recall --engagement {path.name} --phase {current_phase}"
        )
    now = utc_now()
    state.setdefault("phase_history", []).append({"time": now, "event": "exit", "phase": current_phase})
    save_state(path, state)
    append_jsonl(
        path / "logs" / "decisions.jsonl",
        standard_log_record(
            engagement_id=path.name,
            phase=current_phase,
            action="phase-exit",
            target=current_phase,
            outcome="success",
            knowledge_refs=recalls.get(current_phase, []),
        ),
    )
    log_event(path, "phase-exit", target=current_phase, outcome="success", knowledge_refs=recalls.get(current_phase, []))
    return state


def phase_next(path: Path) -> dict[str, Any]:
    state = load_state(path)
    phase = state.get("phase") or "intake"
    if phase not in ACTIVE_PHASES:
        return state
    idx = ACTIVE_PHASES.index(phase)
    next_phase = ACTIVE_PHASES[min(idx + 1, len(ACTIVE_PHASES) - 1)]
    phase_exit(path, phase)
    return phase_enter(path, next_phase)
