from __future__ import annotations

import ipaddress
from pathlib import Path
from urllib.parse import urlparse

from .utils import read_json


def normalize_target(value: str) -> str:
    parsed = urlparse(value if "://" in value else f"scheme://{value}")
    host = parsed.hostname or value
    return host.lower().strip("[]")


def _matches(value: str, rule: str, *, include_subdomains: bool = False) -> bool:
    value_norm = normalize_target(value)
    rule_norm = normalize_target(rule)
    try:
        if "/" in rule_norm:
            return ipaddress.ip_address(value_norm) in ipaddress.ip_network(rule_norm, strict=False)
        if ipaddress.ip_address(value_norm) == ipaddress.ip_address(rule_norm):
            return True
    except ValueError:
        pass
    if value_norm == rule_norm:
        return True
    return include_subdomains and value_norm.endswith(f".{rule_norm}")


def load_scope(engagement_path: Path) -> dict:
    scope = read_json(engagement_path / "scope.json")
    if not isinstance(scope, dict):
        raise SystemExit(f"missing scope.json in {engagement_path}")
    return scope


def target_values(scope: dict) -> list[str]:
    return [item.get("value", "") for item in scope.get("targets") or [] if item.get("value")]


def assert_in_scope(target: str, scope: dict) -> None:
    for excluded in scope.get("excluded") or []:
        if _matches(target, excluded.get("value", ""), include_subdomains=True):
            raise SystemExit(f"target is excluded from scope: {target}")
    for allowed in scope.get("targets") or []:
        if _matches(target, allowed.get("value", ""), include_subdomains=bool(allowed.get("include_subdomains"))):
            return
    raise SystemExit(f"target is out of scope: {target}")
