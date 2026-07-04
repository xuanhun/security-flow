from __future__ import annotations

import hashlib
import sqlite3
from pathlib import Path
from typing import Any

from .engagement import load_state, log_event, save_state
from .paths import KNOWLEDGE_DIR
from .scope import load_scope, target_values
from .utils import append_jsonl, read_json, read_jsonl, standard_log_record, utc_now, write_json


REGISTRY = KNOWLEDGE_DIR / "registry.jsonl"
INDEX = KNOWLEDGE_DIR / "index.sqlite"
LINKS = KNOWLEDGE_DIR / "links.jsonl"
TAXONOMY = KNOWLEDGE_DIR / "taxonomy.json"
TEXT_SUFFIXES = {".md", ".txt", ".json", ".yaml", ".yml", ".py", ".js", ".sh", ".toml", ".html", ".http"}
MAX_INDEX_BYTES = 1_000_000


def ensure_knowledge() -> None:
    KNOWLEDGE_DIR.mkdir(parents=True, exist_ok=True)
    REGISTRY.touch(exist_ok=True)
    LINKS.touch(exist_ok=True)
    if not TAXONOMY.exists():
        write_json(
            TAXONOMY,
            {
                "phases": [
                    "intake",
                    "recon",
                    "surface-map",
                    "knowledge-recall",
                    "hypothesis",
                    "validation",
                    "proof",
                    "report",
                    "distill",
                ],
                "domains": ["web", "network", "mobile", "forensics", "crypto", "agent", "osint", "general"],
                "risk_levels": ["safe", "medium", "high", "gated"],
                "resource_types": ["case", "playbook", "tool", "report", "asset", "reference"],
            },
        )


def resource_id(path: Path, resource_type: str) -> str:
    digest = hashlib.sha1(str(path.resolve()).encode("utf-8", errors="ignore")).hexdigest()[:12]
    stem = path.stem.lower().replace("_", "-")[:48] or "resource"
    return f"{resource_type}:{stem}:{digest}"


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def classify(path: Path, resource_type: str) -> dict[str, Any]:
    lower = path.as_posix().lower()
    tags: list[str] = []
    domain = "general"
    for name in ("web", "network", "mobile", "forensics", "crypto", "agent", "osint", "malware", "reverse", "pwn"):
        if name in lower:
            domain = name if name not in {"reverse", "pwn"} else "forensics"
            tags.append(name)
    phase = "knowledge-recall"
    if resource_type in {"tool", "playbook"}:
        phase = "recon"
    if resource_type == "report":
        phase = "report"
    if resource_type == "case":
        phase = "hypothesis"
    return {"domain": domain, "phase": phase, "tags": sorted(set(tags))}


def iter_resources(path: Path) -> list[Path]:
    path = path.expanduser().resolve()
    if not path.exists():
        raise SystemExit(f"resource path does not exist: {path}")
    if path.is_file():
        return [path]
    files: list[Path] = []
    for child in sorted(path.rglob("*")):
        if not child.is_file():
            continue
        if child.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            if child.stat().st_size > MAX_INDEX_BYTES:
                continue
        except OSError:
            continue
        files.append(child)
    return files


def registry_rows() -> list[dict[str, Any]]:
    return read_jsonl(REGISTRY)


def registry_by_id() -> dict[str, dict[str, Any]]:
    return {row.get("id"): row for row in registry_rows() if row.get("id")}


def ingest(path: Path, resource_type: str, *, domain: str | None = None, phase: str | None = None) -> dict[str, Any]:
    ensure_knowledge()
    existing = registry_by_id()
    rows: list[dict[str, Any]] = []
    for item in iter_resources(path):
        meta = classify(item, resource_type)
        rid = resource_id(item, resource_type)
        row = {
            "id": rid,
            "type": resource_type,
            "domain": domain or meta["domain"],
            "phase": phase or meta["phase"],
            "tags": meta["tags"],
            "techniques": [],
            "artifacts": [],
            "source_path": item.as_posix(),
            "sensitivity": "normal",
            "updated_at": utc_now(),
        }
        existing[rid] = row
        rows.append(row)
    REGISTRY.write_text("", encoding="utf-8")
    for row in sorted(existing.values(), key=lambda item: item["id"]):
        append_jsonl(REGISTRY, row)
    return {"ingested": len(rows), "registry": str(REGISTRY)}


def auto_ingest_defaults() -> None:
    ensure_knowledge()
    if registry_rows():
        return
    defaults = [
        (KNOWLEDGE_DIR / "references", "reference"),
        (KNOWLEDGE_DIR / "casebook" / "cards", "case"),
        (KNOWLEDGE_DIR / "casebook" / "indexes", "reference"),
        (KNOWLEDGE_DIR / "playbooks", "playbook"),
    ]
    for path, resource_type in defaults:
        if path.exists():
            ingest(path, resource_type)


def connect() -> sqlite3.Connection:
    ensure_knowledge()
    conn = sqlite3.connect(INDEX)
    conn.row_factory = sqlite3.Row
    return conn


def reset_index(conn: sqlite3.Connection) -> bool:
    conn.executescript(
        """
        DROP TABLE IF EXISTS resources;
        DROP TABLE IF EXISTS resources_fts;
        CREATE TABLE resources (
          id TEXT PRIMARY KEY,
          type TEXT,
          domain TEXT,
          phase TEXT,
          tags TEXT,
          source_path TEXT,
          sensitivity TEXT,
          updated_at TEXT,
          content TEXT
        );
        """
    )
    try:
        conn.execute(
            """
            CREATE VIRTUAL TABLE resources_fts USING fts5(
              id UNINDEXED,
              type,
              domain,
              phase,
              tags,
              source_path,
              content
            )
            """
        )
        return True
    except sqlite3.OperationalError:
        conn.execute(
            """
            CREATE TABLE resources_fts (
              id TEXT,
              type TEXT,
              domain TEXT,
              phase TEXT,
              tags TEXT,
              source_path TEXT,
              content TEXT
            )
            """
        )
        return False


def reindex() -> dict[str, Any]:
    auto_ingest_defaults()
    rows = registry_rows()
    conn = connect()
    fts = reset_index(conn)
    indexed = 0
    for row in rows:
        path = Path(row.get("source_path", ""))
        content = read_text(path)
        if not content:
            continue
        tags = " ".join(row.get("tags") or [])
        values = (
            row.get("id"),
            row.get("type"),
            row.get("domain"),
            row.get("phase"),
            tags,
            row.get("source_path"),
            row.get("sensitivity"),
            row.get("updated_at"),
            content,
        )
        conn.execute("INSERT OR REPLACE INTO resources VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", values)
        conn.execute(
            "INSERT INTO resources_fts(id, type, domain, phase, tags, source_path, content) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (row.get("id"), row.get("type"), row.get("domain"), row.get("phase"), tags, row.get("source_path"), content),
        )
        indexed += 1
    conn.commit()
    conn.close()
    return {"indexed": indexed, "registry_count": len(rows), "index": str(INDEX), "fts5": fts}


def _query_to_fts(query: str) -> str:
    tokens = [token for token in "".join(ch if ch.isalnum() or ch in "-_." else " " for ch in query).split() if token]
    return " OR ".join(tokens[:12]) or "general"


def search(query: str, *, phase: str | None = None, domain: str | None = None, limit: int = 10) -> dict[str, Any]:
    if not INDEX.exists():
        reindex()
    conn = connect()
    params: list[Any] = []
    filters: list[str] = []
    if phase:
        filters.append("r.phase = ?")
        params.append(phase)
    if domain:
        filters.append("r.domain = ?")
        params.append(domain)
    where = ("WHERE " + " AND ".join(filters)) if filters else ""
    try:
        fts_query = _query_to_fts(query)
        sql = f"""
        SELECT r.id, r.type, r.domain, r.phase, r.tags, r.source_path, snippet(resources_fts, 6, '[', ']', ' ... ', 12) AS snippet
        FROM resources_fts
        JOIN resources r ON r.id = resources_fts.id
        {where + (' AND' if where else 'WHERE')} resources_fts MATCH ?
        LIMIT ?
        """
        rows = conn.execute(sql, [*params, fts_query, limit]).fetchall()
    except sqlite3.OperationalError:
        like = f"%{query}%"
        sql = f"""
        SELECT id, type, domain, phase, tags, source_path, substr(content, 1, 240) AS snippet
        FROM resources r
        {where + (' AND' if where else 'WHERE')} (content LIKE ? OR source_path LIKE ? OR tags LIKE ?)
        LIMIT ?
        """
        rows = conn.execute(sql, [*params, like, like, like, limit]).fetchall()
    finally:
        conn.close()
    results = [dict(row) for row in rows]
    return {"query": query, "phase": phase, "domain": domain, "count": len(results), "results": results}


def browse(*, domain: str | None = None, phase: str | None = None, resource_type: str | None = None, limit: int = 50) -> dict[str, Any]:
    auto_ingest_defaults()
    rows = registry_rows()
    filtered: list[dict[str, Any]] = []
    for row in rows:
        if domain and row.get("domain") != domain:
            continue
        if phase and row.get("phase") != phase:
            continue
        if resource_type and row.get("type") != resource_type:
            continue
        filtered.append(row)
    domains: dict[str, int] = {}
    phases: dict[str, int] = {}
    types: dict[str, int] = {}
    for row in filtered:
        domains[row.get("domain") or "general"] = domains.get(row.get("domain") or "general", 0) + 1
        phases[row.get("phase") or "knowledge-recall"] = phases.get(row.get("phase") or "knowledge-recall", 0) + 1
        types[row.get("type") or "reference"] = types.get(row.get("type") or "reference", 0) + 1
    return {
        "count": len(filtered),
        "filters": {"domain": domain, "phase": phase, "type": resource_type},
        "domains": dict(sorted(domains.items())),
        "phases": dict(sorted(phases.items())),
        "types": dict(sorted(types.items())),
        "resources": filtered[:limit],
    }


def engagement_query(engagement_path: Path, phase: str) -> str:
    scope = load_scope(engagement_path)
    engagement = read_json(engagement_path / "engagement.json", {})
    parts = [phase, engagement.get("type", ""), engagement.get("name", "")]
    parts.extend(target_values(scope))
    state = read_json(engagement_path / "state.json", {})
    parts.append(state.get("phase", ""))
    return " ".join(part for part in parts if part)


def recall(engagement_path: Path, phase: str, *, limit: int = 10) -> dict[str, Any]:
    query = engagement_query(engagement_path, phase)
    result = search(query, phase=phase, limit=limit)
    if result["count"] == 0:
        result = search(query, limit=limit)
    refs = [item["id"] for item in result.get("results") or []]
    record = standard_log_record(
        engagement_id=engagement_path.name,
        phase=phase,
        action="knowledge-recall",
        tool="knowledge",
        target=query,
        command=f"knowledge recall --phase {phase}",
        outcome="hit" if refs else "no-hit",
        knowledge_refs=refs,
    )
    append_jsonl(engagement_path / "logs" / "knowledge-search.jsonl", record | {"query": query, "results": result["results"]})
    state = load_state(engagement_path)
    state.setdefault("knowledge_recalls", {})[phase] = refs if refs else [f"no-hit:{utc_now()}"]
    save_state(engagement_path, state)
    for rid in refs:
        append_jsonl(
            LINKS,
            {
                "time": utc_now(),
                "engagement_id": engagement_path.name,
                "phase": phase,
                "resource_id": rid,
                "reason": "phase recall",
            },
        )
    log_event(engagement_path, "knowledge-recall", tool="knowledge", target=phase, outcome=record["outcome"], knowledge_refs=refs)
    return result


def show(resource_id_value: str) -> dict[str, Any]:
    rows = registry_by_id()
    row = rows.get(resource_id_value)
    if not row:
        raise SystemExit(f"unknown resource id: {resource_id_value}")
    path = Path(row.get("source_path", ""))
    return {"metadata": row, "content": read_text(path)[:6000]}
