# Engagement Lifecycle

All CTF, lab, and authorized penetration testing work uses one engagement
state machine. The engagement type changes expectations and authorization
language, but not evidence, logging, knowledge recall, or context handling.

## Phases

1. `intake`: normalize target, authorization, artifacts, constraints, and stop
   conditions.
2. `recon`: run safe discovery and collect first-pass evidence.
3. `surface-map`: map observed routes, services, files, protocols, identities,
   parameters, and parsers.
4. `knowledge-recall`: search local cases, playbooks, tools, and prior reports.
5. `hypothesis`: create candidate routes with evidence and constraints.
6. `validation`: run bounded checks selected by the candidate route.
7. `proof`: preserve proof evidence without exceeding scope.
8. `report`: generate factual report output.
9. `distill`: promote reusable lessons into knowledge or cases and generate
   the post-test summary.
10. `closed` or `blocked`: finish or pause with explicit state after
   `summary validate` passes.

## Required Gate

Every active phase must have a `knowledge recall` record before it can exit.
Run:

```bash
python scripts/sec.py knowledge recall --engagement <id> --phase <phase>
```

The recall may return no hits, but the no-hit record must be logged so the next
operator knows the local knowledge base was consulted.

## Post-Test Summary Gate

Every test or solve must end with `summary.md` and `summary.json`. Read
[../references/post-test-summary.md](../references/post-test-summary.md) for
required content and closure rules.
