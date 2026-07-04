# Evidence Schema

## Project Layout

```text
engagements/<project-id>/
  scope.json
  commands.jsonl
  tool-status.json
  install-plan.json
  evidence/
  scans/
  findings.json
  memory/
    state.json
    events.jsonl
    next-constraints.json
    lanes/
      <lane-id>.json
  pending/
    actions.jsonl
  report.md
  report.json
```

## CTF Agent Case Layout

`ctf_agent.py` manages local CTF cases without containers. A case directory may
live under `engagements/<case-id>/` and uses these files as durable state:

```text
engagements/<case-id>/
  case.json
  state.json
  events.jsonl
  phase-checkpoints.jsonl
  knowledge/
    hits.json
  memory/
    state.json
    events.jsonl
    next-constraints.json
    lanes/
      <lane-id>.json
  notes/
    info.md
    infer.md
    result.md
    timeline.md
  artifacts/
  files/
  requests/
  responses/
```

`state.json` is the source of truth. The global
`engagements/ctf-agent-index.json` is generated from case states and
should be treated as a summary only.

`memory/state.json` is the source of truth for structured route memory. See
[structured-memory.md](structured-memory.md) for the seven object kinds,
candidate route fields, attempt outcomes, lane files, and next-constraint
rules.

## Scope

```json
{
  "project_id": "local-lab",
  "name": "local-lab",
  "authorization": {
    "status": "required",
    "note": "Written authorization reference"
  },
  "limits": {
    "max_concurrency": 8,
    "timeout_seconds": 15
  },
  "targets": [
    {
      "value": "127.0.0.1",
      "kind": "ip",
      "include_subdomains": false
    }
  ],
  "excluded": []
}
```

## Finding

```json
{
  "time": "2026-06-20T00:00:00+00:00",
  "title": "Missing common HTTP security headers",
  "severity": "low",
  "target": "https://example.test",
  "evidence": "engagements/project/evidence/example_web.json",
  "description": "What was observed and why it matters.",
  "recommendation": "Concrete remediation guidance."
}
```

Severity values: `info`, `low`, `medium`, `high`, `critical`.
