# AI Agent Entry

This repository is meant to be operated by an AI agent with human-approved
scope. Read this file first, then read `README.md` and
`framework/workflows/engagement-lifecycle.md`.

## Operating Model

- You are not running an autonomous penetration-testing script.
- Use the framework to manage scope, context, knowledge recall, evidence,
  hypotheses, validation, reporting, and distillation.
- Treat `scripts/sec.py` as the control plane for state and checks.
- Treat shell, browser, network, and analysis tools as scoped probes that need
  evidence and justification.

## First Steps

1. Confirm the task type: CTF, lab, authorized assessment, framework work, or
   knowledge distillation.
2. Confirm the authorized target and explicit boundaries before target activity.
3. Inspect or create the relevant engagement workspace.
4. Recall local knowledge before leaving intake, recon, hypothesis, validation,
   proof, report, or distill phases.
5. Prefer small safe probes and record both positive and negative evidence.

## Useful Commands

```bash
python scripts/sec.py knowledge search --query "<topic>" --limit 10
python scripts/sec.py knowledge recall --engagement <id> --phase <phase>
python scripts/sec.py scope validate --engagement <id>
python scripts/sec.py report --engagement <id>
python scripts/sec.py summary validate --engagement <id>
python scripts/sec.py validate --tier smoke
```

## Evidence And Knowledge

- Put raw engagement work in `engagements/`; this directory is local by default.
- Promote reusable, sanitized lessons into `knowledge/`.
- Keep secrets, tokens, private endpoints, raw sessions, and unreviewed captures
  out of public Git history.
- When a result is reusable, add a concise case card or reference and reindex
  local knowledge.

## Completion Criteria

A task is not complete just because a command ran. It is complete when the
authorized scope was respected, useful evidence was recorded, validation passed
where applicable, and the human operator has a clear summary of what changed,
what was learned, and what remains uncertain.
