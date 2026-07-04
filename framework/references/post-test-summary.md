# Post-Test Summary Standard

Every completed, solved, blocked, failed, or partially completed engagement
must produce a post-test summary. This applies equally to CTF solving, lab
testing, and authorized penetration testing.

## Required Files

```text
engagements/<id>/
  summary.md
  summary.json
```

`summary.json` is the machine-readable source of truth. `summary.md` is the
human handoff.

## Required Content

- Result status: `completed`, `solved`, `blocked`, `failed`, or `partial`.
- Outcome summary: one concise sentence explaining what happened.
- Scope and authorization: target list, exclusions, authorization note, phase
  and status at summary time.
- Knowledge retrieval: count, recent query outcomes, and referenced resources.
- Evidence: evidence file list, command count, recent replay commands, and
  command log path.
- Candidate routes: active or relevant hypotheses and their status.
- Verification: recent validation outcomes and proof references.
- Negative evidence: failed routes that must not be repeated without new facts.
- Findings or solved result: confirmed issues, flags, proof artifacts, or
  explicit "no confirmed findings".
- Replay path: CLI entrypoint, report, context, and command log.
- Distillation: knowledge, case, probe, or playbook updates needed.
- Next steps: follow-up work, blockers, or "none recorded".
- Redaction: whether sensitive data was redacted and what must be reviewed
  before external sharing.

## Completion Gate

The framework refuses to enter `closed` or `blocked` unless
`summary validate` passes:

```bash
python scripts/sec.py summary generate \
  --engagement <id> \
  --result-status completed \
  --outcome-summary "<what happened>"

python scripts/sec.py summary validate --engagement <id>
python scripts/sec.py phase enter --engagement <id> --phase closed
```

The summary must include at least one knowledge-search record and at least one
command or evidence record. A no-hit knowledge recall is acceptable only when
it is logged.

## CTF And Solving Notes

For CTF or lab solves, `--flag` may be stored in the summary. For authorized
engagements, supplied result tokens are redacted in `summary.json` and
`summary.md`; keep sensitive proof in scoped evidence files.
