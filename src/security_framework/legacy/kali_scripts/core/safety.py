from __future__ import annotations

from pathlib import Path

from .evidence import append_jsonl, utc_now


HIGH_RISK_ACTIONS = {
    "exploit",
    "online-password-attack",
    "sniffing-spoofing",
    "wireless-attack",
    "post-exploitation",
    "destructive-fuzzing",
    "heavy-scan",
}


def require_gate(
    project_dir: Path,
    action: str,
    *,
    target: str | None = None,
    reason: str,
    confirmed: bool = False,
) -> bool:
    if action not in HIGH_RISK_ACTIONS:
        return True
    if confirmed:
        append_jsonl(
            project_dir / "commands.jsonl",
            {
                "time": utc_now(),
                "event": "high-risk-confirmed",
                "action": action,
                "target": target,
                "reason": reason,
            },
        )
        return True

    append_jsonl(
        project_dir / "pending" / "actions.jsonl",
        {
            "time": utc_now(),
            "action": action,
            "target": target,
            "reason": reason,
            "status": "needs-human-confirmation",
        },
    )
    return False
