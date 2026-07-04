# Structured Memory

Use structured memory when a CTF case or authorized assessment needs durable
hypotheses, negative evidence, verification state, or a clean next-step handoff.
The design borrows MopMonkAgent's evidence-converging loop without adding any
new attack capability.

## Layout

Each case or assessment project owns a local memory directory:

```text
memory/
  state.json
  events.jsonl
  next-constraints.json
  lanes/
    <lane-id>.json
```

`state.json` is the machine-readable source of truth. `events.jsonl` is the
append-only audit trail. `next-constraints.json` is regenerated from the current
memory and must be treated as planning guidance, not an executable action.

## Object Kinds

Structured memory has exactly seven object kinds:

| Kind | Purpose |
| --- | --- |
| `goal` | Assessment or challenge objective and scope pointer. |
| `surface_path` | Observed route, artifact, technology, scanner result, casebook hit, or code path. |
| `input_format` | Known input shape, request format, file format, protocol, or parser boundary. |
| `candidate_route` | A hypothesis to verify with skill tools. |
| `negative_evidence` | A failed or disproven route that should constrain future attempts. |
| `verification_state` | Outcome of a candidate attempt or project-level verification. |
| `next_constraint` | A concrete constraint that the next attempt must satisfy or avoid. |

## Candidate Route

Every candidate route has:

```json
{
  "id": "cand-0001",
  "lane_id": "main",
  "title": "short route name",
  "hypothesis": "why this route might work",
  "constraints": ["facts the route must satisfy"],
  "evidence_refs": ["paths to local evidence"],
  "status": "proposed",
  "created_at": "ISO-8601",
  "updated_at": "ISO-8601"
}
```

Valid statuses are `proposed`, `active`, `inconclusive`, `negative`,
`blocked`, `gated`, `verified`, and `superseded`.

## Attempt Outcomes

Record every meaningful attempt with:

```json
{
  "candidate_id": "cand-0001",
  "outcome": "negative",
  "summary": "what happened",
  "evidence_refs": ["paths to local evidence"],
  "failure_reason": "why it failed, if known",
  "next_constraints": ["what must change next time"]
}
```

Valid outcomes are `success`, `negative`, `inconclusive`, `blocked`, and
`gated`. Negative attempts create `negative_evidence` and open
`next_constraint` records so repeated failures become useful constraints.

## Commands

CTF cases:

```bash
python scripts/sec.py memory memory --case-dir <case> --summary
python scripts/sec.py memory memory --case-dir <case> --next
python scripts/sec.py memory candidate --case-dir <case> --title ... --hypothesis ...
python scripts/sec.py memory attempt --case-dir <case> --candidate-id cand-0001 --outcome negative --summary ...
```

Authorized assessments:

```bash
python scripts/sec.py memory --project <project> --summary
python scripts/sec.py memory --project <project> --next
python scripts/sec.py candidate --project <project> --title ... --hypothesis ...
python scripts/sec.py attempt --project <project> --candidate-id cand-0001 --outcome negative --summary ...
```

## Operating Rule

Use `memory --next` to clarify the next constraints before choosing a probe.
It must not execute probes. Use the existing safe skill tools, scope checks, and
safety gates for execution.
