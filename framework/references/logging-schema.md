# Logging Schema

Standard process logs live under `engagements/<id>/logs/`.

Required JSONL fields:

- `time`
- `engagement_id`
- `phase`
- `lane_id`
- `action`
- `tool`
- `target`
- `command`
- `risk`
- `outcome`
- `evidence_refs`
- `knowledge_refs`
- `decision_id`
- `next_constraints`
- `redaction_status`

Use `logs/events.jsonl` for actions, `logs/commands.jsonl` for executed
commands, `logs/knowledge-search.jsonl` for local knowledge retrieval, and
`logs/decisions.jsonl` for phase exits and human decisions.
