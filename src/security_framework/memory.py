from __future__ import annotations

from pathlib import Path
from typing import Any

from .engagement import log_event, write_context
from .utils import append_jsonl, read_json, utc_now, write_json


VALID_OUTCOMES = ("success", "negative", "inconclusive", "blocked", "gated")
VALID_STATUSES = ("proposed", "active", "inconclusive", "negative", "blocked", "gated", "verified", "superseded")


def memory_path(root: Path) -> Path:
    return root / "memory" / "state.json"


def load(root: Path) -> dict[str, Any]:
    state = read_json(memory_path(root))
    if not isinstance(state, dict):
        raise SystemExit(f"missing memory state: {memory_path(root)}")
    return state


def save(root: Path, state: dict[str, Any]) -> None:
    state["updated_at"] = utc_now()
    write_json(memory_path(root), state)
    write_json(root / "memory" / "next-constraints.json", next_constraints(root))


def _next_id(state: dict[str, Any], kind: str, prefix: str) -> str:
    counters = state.setdefault("counters", {})
    counters[kind] = int(counters.get(kind) or 0) + 1
    return f"{prefix}-{counters[kind]:04d}"


def add_candidate(
    root: Path,
    *,
    title: str,
    hypothesis: str,
    constraints: list[str] | None = None,
    evidence_refs: list[str] | None = None,
    knowledge_refs: list[str] | None = None,
    lane_id: str = "main",
    status: str = "proposed",
) -> dict[str, Any]:
    if status not in VALID_STATUSES:
        raise SystemExit(f"candidate status must be one of: {', '.join(VALID_STATUSES)}")
    state = load(root)
    item = {
        "id": _next_id(state, "candidate_route", "cand"),
        "lane_id": lane_id,
        "title": title,
        "hypothesis": hypothesis,
        "constraints": constraints or [],
        "evidence_refs": evidence_refs or [],
        "knowledge_refs": knowledge_refs or [],
        "status": status,
        "created_at": utc_now(),
        "updated_at": utc_now(),
    }
    state["objects"]["candidate_routes"].append(item)
    save(root, state)
    append_jsonl(root / "memory" / "events.jsonl", {"time": utc_now(), "event": "candidate-add", "data": item})
    log_event(root, "candidate", tool="memory", outcome="success", evidence_refs=evidence_refs or [], knowledge_refs=knowledge_refs or [])
    write_context(root, f"Candidate added: {title}", [*item["constraints"]])
    return item


def record_attempt(
    root: Path,
    *,
    candidate_id: str,
    outcome: str,
    summary: str,
    evidence_refs: list[str] | None = None,
    failure_reason: str | None = None,
    next_constraints_list: list[str] | None = None,
) -> dict[str, Any]:
    if outcome not in VALID_OUTCOMES:
        raise SystemExit(f"attempt outcome must be one of: {', '.join(VALID_OUTCOMES)}")
    state = load(root)
    candidate = None
    for item in state["objects"]["candidate_routes"]:
        if item.get("id") == candidate_id:
            candidate = item
            break
    if not candidate:
        raise SystemExit(f"unknown candidate: {candidate_id}")
    status_map = {
        "success": "verified",
        "negative": "negative",
        "inconclusive": "inconclusive",
        "blocked": "blocked",
        "gated": "gated",
    }
    candidate["status"] = status_map[outcome]
    candidate["updated_at"] = utc_now()
    attempt = {
        "id": _next_id(state, "verification_state", "ver"),
        "candidate_id": candidate_id,
        "lane_id": candidate.get("lane_id") or "main",
        "outcome": outcome,
        "summary": summary,
        "evidence_refs": evidence_refs or [],
        "failure_reason": failure_reason,
        "next_constraints": next_constraints_list or [],
        "created_at": utc_now(),
        "updated_at": utc_now(),
    }
    state["objects"]["verification_states"].append(attempt)
    if outcome == "negative":
        state["objects"]["negative_evidence"].append(
            {
                "id": _next_id(state, "negative_evidence", "neg"),
                "candidate_id": candidate_id,
                "lane_id": attempt["lane_id"],
                "summary": summary,
                "failure_reason": failure_reason,
                "evidence_refs": evidence_refs or [],
                "next_constraints": next_constraints_list or [f"Avoid repeating candidate {candidate_id} without new evidence."],
                "created_at": utc_now(),
                "updated_at": utc_now(),
            }
        )
    for constraint in next_constraints_list or []:
        state["objects"]["next_constraints"].append(
            {
                "id": _next_id(state, "next_constraint", "next"),
                "candidate_id": candidate_id,
                "lane_id": attempt["lane_id"],
                "constraint": constraint,
                "source": f"attempt:{outcome}",
                "status": "open",
                "created_at": utc_now(),
                "updated_at": utc_now(),
            }
        )
    save(root, state)
    append_jsonl(root / "memory" / "events.jsonl", {"time": utc_now(), "event": "attempt", "data": attempt})
    log_event(root, "attempt", tool="memory", outcome=outcome, evidence_refs=evidence_refs or [], next_constraints=next_constraints_list or [])
    write_context(root, f"Attempt recorded for {candidate_id}: {summary}", [item["constraint"] for item in state["objects"]["next_constraints"] if item.get("status") == "open"])
    return attempt


def next_constraints(root: Path) -> dict[str, Any]:
    state = load(root) if memory_path(root).exists() else {"objects": {}}
    rows: list[dict[str, Any]] = []
    for item in state.get("objects", {}).get("next_constraints", []):
        if item.get("status") != "resolved":
            rows.append(
                {
                    "constraint": item.get("constraint"),
                    "source": item.get("source"),
                    "candidate_id": item.get("candidate_id"),
                    "lane_id": item.get("lane_id"),
                    "updated_at": item.get("updated_at"),
                }
            )
    for item in state.get("objects", {}).get("negative_evidence", []):
        for constraint in item.get("next_constraints") or []:
            rows.append(
                {
                    "constraint": constraint,
                    "source": "negative_evidence",
                    "candidate_id": item.get("candidate_id"),
                    "lane_id": item.get("lane_id"),
                    "updated_at": item.get("updated_at"),
                }
            )
    return {"generated_at": utc_now(), "constraints": rows[:50]}


def summary(root: Path) -> dict[str, Any]:
    state = load(root)
    objects = state.get("objects", {})
    return {
        "memory_dir": str(root / "memory"),
        "counts": {key: len(value) for key, value in objects.items()},
        "active_candidates": [
            item for item in objects.get("candidate_routes", []) if item.get("status") in {"proposed", "active", "inconclusive"}
        ][:10],
        "negative_evidence": objects.get("negative_evidence", [])[-10:],
        "verification_recent": objects.get("verification_states", [])[-10:],
        "next_constraints": next_constraints(root)["constraints"][:10],
    }
