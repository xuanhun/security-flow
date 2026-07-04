from __future__ import annotations

import ipaddress
import re
from pathlib import Path
from urllib.parse import urlparse

from .evidence import read_json, utc_now, write_json


HOST_RE = re.compile(r"^[A-Za-z0-9.-]+$")


def normalize_target(value: str) -> str:
    value = value.strip()
    parsed = urlparse(value)
    if parsed.scheme and parsed.netloc:
        return parsed.netloc.split("@")[-1].split(":")[0].lower()
    return value.split("/")[0].split(":")[0].lower()


def target_kind(value: str) -> str:
    value = value.strip()
    try:
        ipaddress.ip_network(value, strict=False)
        return "cidr" if "/" in value else "ip"
    except ValueError:
        pass
    parsed = urlparse(value)
    if parsed.scheme in {"http", "https"} and parsed.netloc:
        return "url"
    if HOST_RE.match(value):
        return "domain"
    return "unknown"


def make_scope(
    project_id: str,
    name: str,
    targets: list[str],
    excluded: list[str] | None = None,
    include_subdomains: bool = False,
) -> dict:
    return {
        "project_id": project_id,
        "name": name,
        "created_at": utc_now(),
        "authorization": {
            "status": "required",
            "note": "Replace this note with the written authorization reference before testing real assets.",
        },
        "limits": {
            "max_concurrency": 8,
            "timeout_seconds": 15,
            "rate_limit_note": "Keep scans bounded and appropriate for the authorization.",
        },
        "targets": [
            {
                "value": target,
                "kind": target_kind(target),
                "include_subdomains": include_subdomains,
            }
            for target in targets
        ],
        "excluded": [
            {"value": item, "kind": target_kind(item)}
            for item in (excluded or [])
        ],
    }


def load_scope(project_dir: Path) -> dict:
    scope = read_json(project_dir / "scope.json")
    if not scope:
        raise SystemExit(f"missing scope file: {project_dir / 'scope.json'}")
    return scope


def save_scope(project_dir: Path, scope: dict) -> None:
    write_json(project_dir / "scope.json", scope)


def _matches_entry(target: str, entry: dict) -> bool:
    value = str(entry.get("value", "")).strip().lower()
    kind = entry.get("kind") or target_kind(value)
    host = normalize_target(target)
    value_host = normalize_target(value)

    if kind == "url":
        return target.rstrip("/") == value.rstrip("/") or host == value_host
    if kind == "ip":
        return host == value_host
    if kind == "cidr":
        try:
            return ipaddress.ip_address(host) in ipaddress.ip_network(value, strict=False)
        except ValueError:
            return False
    if kind == "domain":
        if host == value_host:
            return True
        return bool(entry.get("include_subdomains")) and host.endswith(f".{value_host}")
    return False


def is_in_scope(target: str, scope: dict) -> bool:
    excluded = scope.get("excluded", [])
    if any(_matches_entry(target, entry) for entry in excluded):
        return False
    return any(_matches_entry(target, entry) for entry in scope.get("targets", []))


def assert_in_scope(target: str, scope: dict) -> None:
    if not is_in_scope(target, scope):
        raise SystemExit(f"target is out of scope: {target}")


def scope_targets(scope: dict) -> list[str]:
    return [entry["value"] for entry in scope.get("targets", []) if entry.get("value")]
