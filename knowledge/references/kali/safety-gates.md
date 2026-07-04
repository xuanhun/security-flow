# Safety Gates

## Gated Actions

The CLI records a pending action unless the user explicitly confirms risk for:

- `exploit`;
- `online-password-attack`;
- `sniffing-spoofing`;
- `wireless-attack`;
- `post-exploitation`;
- `destructive-fuzzing`;
- `heavy-scan`.

## Gate Record

Pending actions are written to:

```text
engagements/<project-id>/pending/actions.jsonl
```

Each record names the action, target, reason, and timestamp.

## Adding New Gates

When adding a module:

1. Identify whether the action can affect availability, confidentiality,
   integrity, privacy, or legal exposure.
2. Add a gate in `core/safety.py` if any risk is material.
3. Default to pending action, not execution.
4. Require explicit CLI confirmation for execution.
5. Record command output and evidence.
