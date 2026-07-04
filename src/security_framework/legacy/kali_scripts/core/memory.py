from __future__ import annotations

import fcntl
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable


VERSION = "1.0"

VALID_OBJECT_KINDS = (
    "goal",
    "surface_path",
    "input_format",
    "candidate_route",
    "negative_evidence",
    "verification_state",
    "next_constraint",
)
VALID_OUTCOMES = ("success", "negative", "inconclusive", "blocked", "gated")
VALID_CANDIDATE_STATUSES = (
    "proposed",
    "active",
    "inconclusive",
    "negative",
    "blocked",
    "gated",
    "verified",
    "superseded",
)

OBJECT_KEYS = {
    "goal": "goals",
    "surface_path": "surface_paths",
    "input_format": "input_formats",
    "candidate_route": "candidate_routes",
    "negative_evidence": "negative_evidence",
    "verification_state": "verification_states",
    "next_constraint": "next_constraints",
}

ID_PREFIXES = {
    "goal": "goal",
    "surface_path": "surf",
    "input_format": "input",
    "candidate_route": "cand",
    "negative_evidence": "neg",
    "verification_state": "ver",
    "next_constraint": "next",
}

ACTIVE_CANDIDATE_STATUSES = {"proposed", "active", "inconclusive"}
SECRET_REPLACEMENTS = (
    (
        re.compile(
            r"(?i)\b(password|passwd|pwd|api[_-]?key|access[_-]?token|refresh[_-]?token|secret)\s*[:=]\s*([^\s,;]+)"
        ),
        r"\1=<redacted>",
    ),
    (re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._~+/=-]+"), "Bearer <redacted>"),
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def memory_dir(root: Path) -> Path:
    return root / "memory"


def _safe_lane_id(value: str | None) -> str:
    value = (value or "main").lower().strip()
    value = re.sub(r"[^a-z0-9._-]+", "-", value)
    return value.strip("-") or "main"


def _redact_text(value: str) -> str:
    redacted = value
    for pattern, replacement in SECRET_REPLACEMENTS:
        redacted = pattern.sub(replacement, redacted)
    return redacted


def _sanitize(value: Any) -> Any:
    if isinstance(value, str):
        return _redact_text(value)
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    if isinstance(value, dict):
        return {str(key): _sanitize(item) for key, item in value.items()}
    return value


def _list(value: list[str] | None) -> list[str]:
    return [_redact_text(str(item)) for item in value or [] if str(item).strip()]


def _unique(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def _default_state() -> dict[str, Any]:
    now = utc_now()
    return {
        "version": VERSION,
        "created_at": now,
        "updated_at": now,
        "objects": {key: [] for key in OBJECT_KEYS.values()},
        "counters": {kind: 0 for kind in VALID_OBJECT_KINDS},
    }


def _normalize_state(state: dict[str, Any] | None) -> dict[str, Any]:
    if not isinstance(state, dict):
        state = _default_state()
    state["version"] = state.get("version") or VERSION
    state["created_at"] = state.get("created_at") or utc_now()
    state["updated_at"] = state.get("updated_at") or utc_now()
    objects = state.setdefault("objects", {})
    for key in OBJECT_KEYS.values():
        if not isinstance(objects.get(key), list):
            objects[key] = []
    counters = state.setdefault("counters", {})
    for kind in VALID_OBJECT_KINDS:
        counters[kind] = int(counters.get(kind) or 0)
    return state


def ensure_memory(root: Path) -> Path:
    path = memory_dir(root)
    path.mkdir(parents=True, exist_ok=True)
    (path / "lanes").mkdir(exist_ok=True)
    state_path = path / "state.json"
    if not state_path.exists():
        _atomic_write_json(state_path, _default_state())
    return path


def _read_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def _atomic_write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    with temp.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temp, path)


def _append_jsonl(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(data, ensure_ascii=False, sort_keys=True) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def _load_state_unlocked(root: Path) -> dict[str, Any]:
    path = ensure_memory(root) / "state.json"
    return _normalize_state(_read_json(path, default=None))


def load_memory(root: Path) -> dict[str, Any]:
    return _load_state_unlocked(root)


def _save_state_unlocked(root: Path, state: dict[str, Any]) -> None:
    state["updated_at"] = utc_now()
    _atomic_write_json(ensure_memory(root) / "state.json", state)


def _with_lock(root: Path, mutator: Callable[[dict[str, Any]], Any]) -> Any:
    path = ensure_memory(root)
    lock_path = path / ".lock"
    with lock_path.open("w", encoding="utf-8") as lock_file:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
        try:
            state = _load_state_unlocked(root)
            result = mutator(state)
            _save_state_unlocked(root, state)
            _write_next_constraints_unlocked(root, state)
            return result
        finally:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)


def _object_key(kind: str) -> str:
    if kind not in OBJECT_KEYS:
        raise ValueError(f"memory object kind must be one of: {', '.join(VALID_OBJECT_KINDS)}")
    return OBJECT_KEYS[kind]


def _next_id(state: dict[str, Any], kind: str) -> str:
    counters = state.setdefault("counters", {})
    counters[kind] = int(counters.get(kind) or 0) + 1
    return f"{ID_PREFIXES[kind]}-{counters[kind]:04d}"


def _find_by_dedupe(state: dict[str, Any], kind: str, dedupe_key: str | None) -> dict[str, Any] | None:
    if not dedupe_key:
        return None
    for item in state["objects"][_object_key(kind)]:
        if item.get("dedupe_key") == dedupe_key:
            return item
    return None


def _append_event(root: Path, event: str, data: dict[str, Any]) -> None:
    _append_jsonl(ensure_memory(root) / "events.jsonl", {"time": utc_now(), "event": event, "data": _sanitize(data)})


def _candidate_by_id(state: dict[str, Any], candidate_id: str | None) -> dict[str, Any] | None:
    if not candidate_id:
        return None
    for item in state["objects"]["candidate_routes"]:
        if item.get("id") == candidate_id:
            return item
    return None


def add_structured_object(
    root: Path,
    kind: str,
    data: dict[str, Any],
    *,
    lane_id: str | None = None,
    dedupe_key: str | None = None,
) -> dict[str, Any]:
    lane = _safe_lane_id(lane_id or data.get("lane_id"))

    def mutate(state: dict[str, Any]) -> dict[str, Any]:
        existing = _find_by_dedupe(state, kind, dedupe_key)
        now = utc_now()
        if existing:
            existing.update(_sanitize(data))
            existing["updated_at"] = now
            if lane:
                existing["lane_id"] = lane
            _append_event(root, f"{kind}-update", {"id": existing.get("id"), "dedupe_key": dedupe_key})
            _write_lane_unlocked(root, state, existing.get("lane_id"))
            return existing
        item = {
            "id": _next_id(state, kind),
            "kind": kind,
            "lane_id": lane,
            "created_at": now,
            "updated_at": now,
            **_sanitize(data),
        }
        if dedupe_key:
            item["dedupe_key"] = dedupe_key
        state["objects"][_object_key(kind)].append(item)
        _append_event(root, f"{kind}-add", {"id": item["id"], "lane_id": lane, "dedupe_key": dedupe_key})
        _write_lane_unlocked(root, state, lane)
        return item

    return _with_lock(root, mutate)


def add_goal(root: Path, title: str, summary: str, *, evidence_refs: list[str] | None = None) -> dict[str, Any]:
    return add_structured_object(
        root,
        "goal",
        {"title": title, "summary": summary, "evidence_refs": _list(evidence_refs)},
        lane_id="main",
        dedupe_key=f"goal:{title}",
    )


def add_surface_path(
    root: Path,
    *,
    source: str,
    title: str,
    summary: str,
    evidence_refs: list[str] | None = None,
    lane_id: str = "recon",
    dedupe_key: str | None = None,
) -> dict[str, Any]:
    return add_structured_object(
        root,
        "surface_path",
        {
            "source": source,
            "title": title,
            "summary": summary,
            "evidence_refs": _list(evidence_refs),
        },
        lane_id=lane_id,
        dedupe_key=dedupe_key or f"surface:{source}:{title}",
    )


def add_candidate(
    root: Path,
    *,
    title: str,
    hypothesis: str,
    lane_id: str = "main",
    constraints: list[str] | None = None,
    evidence_refs: list[str] | None = None,
    status: str = "proposed",
    dedupe_key: str | None = None,
) -> dict[str, Any]:
    if status not in VALID_CANDIDATE_STATUSES:
        raise ValueError(f"candidate status must be one of: {', '.join(VALID_CANDIDATE_STATUSES)}")
    lane = _safe_lane_id(lane_id)

    def mutate(state: dict[str, Any]) -> dict[str, Any]:
        existing = _find_by_dedupe(state, "candidate_route", dedupe_key)
        now = utc_now()
        if existing:
            existing["constraints"] = _unique([*_list(existing.get("constraints")), *_list(constraints)])
            existing["evidence_refs"] = _unique([*_list(existing.get("evidence_refs")), *_list(evidence_refs)])
            existing["updated_at"] = now
            existing["title"] = _redact_text(title)
            existing["hypothesis"] = _redact_text(hypothesis)
            if existing.get("status") not in {"negative", "verified", "blocked", "gated"}:
                existing["status"] = status
            _append_event(root, "candidate-route-update", {"id": existing["id"], "lane_id": existing.get("lane_id")})
            _write_lane_unlocked(root, state, existing.get("lane_id"))
            return existing
        item = {
            "id": _next_id(state, "candidate_route"),
            "kind": "candidate_route",
            "lane_id": lane,
            "title": _redact_text(title),
            "hypothesis": _redact_text(hypothesis),
            "constraints": _list(constraints),
            "evidence_refs": _list(evidence_refs),
            "status": status,
            "created_at": now,
            "updated_at": now,
        }
        if dedupe_key:
            item["dedupe_key"] = dedupe_key
        state["objects"]["candidate_routes"].append(item)
        _append_event(root, "candidate-route-add", {"id": item["id"], "lane_id": lane, "dedupe_key": dedupe_key})
        _write_lane_unlocked(root, state, lane)
        return item

    return _with_lock(root, mutate)


def record_attempt(
    root: Path,
    *,
    candidate_id: str,
    outcome: str,
    summary: str,
    evidence_refs: list[str] | None = None,
    failure_reason: str | None = None,
    next_constraints: list[str] | None = None,
) -> dict[str, Any]:
    return record_verification(
        root,
        candidate_id=candidate_id,
        outcome=outcome,
        summary=summary,
        evidence_refs=evidence_refs,
        failure_reason=failure_reason,
        next_constraints=next_constraints,
        require_candidate=True,
    )


def record_verification(
    root: Path,
    *,
    outcome: str,
    summary: str,
    candidate_id: str | None = None,
    evidence_refs: list[str] | None = None,
    failure_reason: str | None = None,
    next_constraints: list[str] | None = None,
    require_candidate: bool = False,
) -> dict[str, Any]:
    if outcome not in VALID_OUTCOMES:
        raise ValueError(f"attempt outcome must be one of: {', '.join(VALID_OUTCOMES)}")

    def mutate(state: dict[str, Any]) -> dict[str, Any]:
        now = utc_now()
        candidate = _candidate_by_id(state, candidate_id)
        if require_candidate and candidate is None:
            raise ValueError(f"unknown candidate id: {candidate_id}")
        lane = _safe_lane_id(candidate.get("lane_id") if candidate else "main")
        item = {
            "id": _next_id(state, "verification_state"),
            "kind": "verification_state",
            "lane_id": lane,
            "candidate_id": candidate_id,
            "outcome": outcome,
            "summary": _redact_text(summary),
            "evidence_refs": _list(evidence_refs),
            "failure_reason": _redact_text(failure_reason or ""),
            "next_constraints": _list(next_constraints),
            "created_at": now,
            "updated_at": now,
        }
        state["objects"]["verification_states"].append(item)
        if candidate is not None:
            candidate["status"] = {
                "success": "verified",
                "negative": "negative",
                "inconclusive": "inconclusive",
                "blocked": "blocked",
                "gated": "gated",
            }[outcome]
            candidate["updated_at"] = now
        if outcome == "negative":
            _add_negative_evidence_unlocked(
                root,
                state,
                lane_id=lane,
                candidate_id=candidate_id,
                summary=summary,
                evidence_refs=evidence_refs,
                failure_reason=failure_reason,
                next_constraints=next_constraints,
            )
        elif outcome in {"blocked", "gated"} and not next_constraints:
            default_constraint = (
                "Resolve the blocking condition before continuing this route."
                if outcome == "blocked"
                else "Obtain the required safety gate approval before continuing this route."
            )
            _add_next_constraint_unlocked(root, state, lane, candidate_id, default_constraint, source=outcome)
        for constraint in _list(next_constraints):
            _add_next_constraint_unlocked(root, state, lane, candidate_id, constraint, source=f"attempt:{outcome}")
        _append_event(root, "attempt-record", {"id": item["id"], "candidate_id": candidate_id, "outcome": outcome})
        _write_lane_unlocked(root, state, lane)
        return item

    return _with_lock(root, mutate)


def _add_negative_evidence_unlocked(
    root: Path,
    state: dict[str, Any],
    *,
    lane_id: str,
    candidate_id: str | None,
    summary: str,
    evidence_refs: list[str] | None,
    failure_reason: str | None,
    next_constraints: list[str] | None,
) -> dict[str, Any]:
    now = utc_now()
    item = {
        "id": _next_id(state, "negative_evidence"),
        "kind": "negative_evidence",
        "lane_id": _safe_lane_id(lane_id),
        "candidate_id": candidate_id,
        "summary": _redact_text(summary),
        "failure_reason": _redact_text(failure_reason or ""),
        "evidence_refs": _list(evidence_refs),
        "next_constraints": _list(next_constraints),
        "created_at": now,
        "updated_at": now,
    }
    state["objects"]["negative_evidence"].append(item)
    if not next_constraints:
        _add_next_constraint_unlocked(
            root,
            state,
            lane_id,
            candidate_id,
            f"Avoid repeating negative route: {failure_reason or summary}",
            source="negative_evidence",
        )
    _append_event(root, "negative-evidence-add", {"id": item["id"], "candidate_id": candidate_id})
    return item


def _add_next_constraint_unlocked(
    root: Path,
    state: dict[str, Any],
    lane_id: str,
    candidate_id: str | None,
    constraint: str,
    *,
    source: str,
) -> dict[str, Any]:
    now = utc_now()
    text = _redact_text(constraint)
    for item in state["objects"]["next_constraints"]:
        if item.get("constraint") == text and item.get("candidate_id") == candidate_id:
            item["updated_at"] = now
            return item
    item = {
        "id": _next_id(state, "next_constraint"),
        "kind": "next_constraint",
        "lane_id": _safe_lane_id(lane_id),
        "candidate_id": candidate_id,
        "constraint": text,
        "source": source,
        "status": "open",
        "created_at": now,
        "updated_at": now,
    }
    state["objects"]["next_constraints"].append(item)
    _append_event(root, "next-constraint-add", {"id": item["id"], "candidate_id": candidate_id})
    return item


def _generate_next_constraints(state: dict[str, Any], *, limit: int = 50) -> dict[str, Any]:
    candidates = [
        item
        for item in state["objects"]["candidate_routes"]
        if item.get("status") in ACTIVE_CANDIDATE_STATUSES
    ]
    candidates = sorted(candidates, key=lambda item: item.get("updated_at") or "", reverse=True)
    candidate_map = {item.get("id"): item for item in state["objects"]["candidate_routes"]}
    rows: list[dict[str, Any]] = []

    for item in state["objects"]["next_constraints"]:
        if item.get("status") == "resolved":
            continue
        rows.append(
            {
                "constraint": item.get("constraint", ""),
                "source": item.get("source", "next_constraint"),
                "candidate_id": item.get("candidate_id"),
                "lane_id": item.get("lane_id"),
                "updated_at": item.get("updated_at"),
            }
        )
    for item in state["objects"]["negative_evidence"]:
        if item.get("next_constraints"):
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
        else:
            rows.append(
                {
                    "constraint": f"Avoid repeating negative route: {item.get('failure_reason') or item.get('summary')}",
                    "source": "negative_evidence",
                    "candidate_id": item.get("candidate_id"),
                    "lane_id": item.get("lane_id"),
                    "updated_at": item.get("updated_at"),
                }
            )
    for candidate in candidates:
        for constraint in candidate.get("constraints") or []:
            rows.append(
                {
                    "constraint": f"Candidate {candidate.get('id')} must satisfy: {constraint}",
                    "source": "candidate_route",
                    "candidate_id": candidate.get("id"),
                    "lane_id": candidate.get("lane_id"),
                    "updated_at": candidate.get("updated_at"),
                }
            )

    deduped: list[dict[str, Any]] = []
    seen: set[tuple[str, str | None]] = set()
    for row in sorted(rows, key=lambda item: item.get("updated_at") or "", reverse=True):
        key = (row.get("constraint", ""), row.get("candidate_id"))
        if not key[0] or key in seen:
            continue
        seen.add(key)
        deduped.append(row)
        if len(deduped) >= limit:
            break

    return {
        "generated_at": utc_now(),
        "constraints": deduped,
        "recommended_candidates": [
            {
                "id": item.get("id"),
                "lane_id": item.get("lane_id"),
                "title": item.get("title"),
                "hypothesis": item.get("hypothesis"),
                "status": item.get("status"),
                "constraints": item.get("constraints", []),
                "evidence_refs": item.get("evidence_refs", []),
            }
            for item in candidates[:10]
        ],
        "candidate_status": {
            candidate_id: candidate.get("status") for candidate_id, candidate in candidate_map.items()
        },
    }


def _write_next_constraints_unlocked(root: Path, state: dict[str, Any]) -> None:
    _atomic_write_json(ensure_memory(root) / "next-constraints.json", _generate_next_constraints(state))


def generate_next_constraints(root: Path) -> dict[str, Any]:
    result: dict[str, Any] = {}

    def mutate(state: dict[str, Any]) -> dict[str, Any]:
        nonlocal result
        result = _generate_next_constraints(state)
        return result

    _with_lock(root, mutate)
    return result


def _write_lane_unlocked(root: Path, state: dict[str, Any], lane_id: str | None) -> None:
    lane = _safe_lane_id(lane_id)
    candidates = [item for item in state["objects"]["candidate_routes"] if item.get("lane_id") == lane]
    candidate_ids = {item.get("id") for item in candidates}
    data = {
        "version": VERSION,
        "lane_id": lane,
        "updated_at": utc_now(),
        "candidate_routes": candidates,
        "verification_states": [
            item
            for item in state["objects"]["verification_states"]
            if item.get("lane_id") == lane or item.get("candidate_id") in candidate_ids
        ],
        "negative_evidence": [
            item
            for item in state["objects"]["negative_evidence"]
            if item.get("lane_id") == lane or item.get("candidate_id") in candidate_ids
        ],
        "next_constraints": [
            item
            for item in state["objects"]["next_constraints"]
            if item.get("lane_id") == lane or item.get("candidate_id") in candidate_ids
        ],
    }
    _atomic_write_json(ensure_memory(root) / "lanes" / f"{lane}.json", data)


def summarize_memory(root: Path, *, limit: int = 5) -> dict[str, Any]:
    state = load_memory(root)
    objects = state["objects"]
    active_candidates = [
        item for item in objects["candidate_routes"] if item.get("status") in ACTIVE_CANDIDATE_STATUSES
    ]
    negative_routes = [item for item in objects["candidate_routes"] if item.get("status") == "negative"]
    next_data = _generate_next_constraints(state, limit=20)
    return {
        "version": state.get("version"),
        "memory_dir": str(memory_dir(root)),
        "counts": {kind: len(objects[key]) for kind, key in OBJECT_KEYS.items()},
        "top_candidates": sorted(active_candidates, key=lambda item: item.get("updated_at") or "", reverse=True)[:limit],
        "negative_routes": sorted(negative_routes, key=lambda item: item.get("updated_at") or "", reverse=True)[:limit],
        "negative_evidence": sorted(
            objects["negative_evidence"], key=lambda item: item.get("updated_at") or "", reverse=True
        )[:limit],
        "verification_recent": sorted(
            objects["verification_states"], key=lambda item: item.get("updated_at") or "", reverse=True
        )[:limit],
        "next_constraints": next_data["constraints"][:limit],
        "recommended_candidates": next_data["recommended_candidates"][:limit],
    }


def render_summary_lines(summary: dict[str, Any]) -> list[str]:
    counts = summary.get("counts", {})
    lines = [
        "## Structured Memory",
        "",
        f"- Candidate routes: {counts.get('candidate_route', 0)}",
        f"- Negative evidence: {counts.get('negative_evidence', 0)}",
        f"- Verification states: {counts.get('verification_state', 0)}",
        f"- Next constraints: {counts.get('next_constraint', 0)}",
    ]
    candidates = summary.get("top_candidates") or []
    lines.extend(["", "### Top Candidates"])
    if candidates:
        for item in candidates:
            lines.append(f"- {item.get('id')} [{item.get('status')}]: {item.get('title')}")
    else:
        lines.append("- none")
    negatives = summary.get("negative_routes") or summary.get("negative_evidence") or []
    lines.extend(["", "### Negative Evidence"])
    if negatives:
        for item in negatives[:5]:
            title = item.get("title") or item.get("failure_reason") or item.get("summary")
            lines.append(f"- {item.get('id')} [{item.get('candidate_id') or 'global'}]: {title}")
    else:
        lines.append("- none")
    lines.extend(["", "### Next Constraints"])
    constraints = summary.get("next_constraints") or []
    if constraints:
        for item in constraints:
            lines.append(f"- {item.get('constraint')}")
    else:
        lines.append("- none")
    return lines
