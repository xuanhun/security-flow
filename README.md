# AI-Orchestrated Security Assessment Framework

This repository is a working framework for AI-assisted CTF, lab, and authorized
security assessment workflows. It is designed for agents such as Codex, Claude
Code, and similar coding/security assistants that can read instructions, inspect
local evidence, operate tools, update knowledge, and keep a scoped audit trail.

It is not a one-command penetration-testing product. Running `scripts/sec.py`
does not automatically perform a complete assessment. The Python CLI is a
control plane for state, knowledge recall, scope checks, evidence logging,
validation, and reports; the actual workflow is driven by an AI agent under
human authorization.

## Primary Entry

- AI agent guide: `agent.md`
- Lifecycle workflow: `framework/workflows/engagement-lifecycle.md`
- Knowledge retrieval: `framework/references/knowledge-retrieval.md`
- Logging schema: `framework/references/logging-schema.md`
- Context rules: `framework/references/context-management.md`
- Post-test summary: `framework/references/post-test-summary.md`
- Support CLI: `scripts/sec.py`
- Local knowledge base: `knowledge/`
- Local engagement workspaces: `engagements/`

If a local `AGENTS.md` exists, treat it as private operator-specific guidance.
It is intentionally not part of the public repository.

## How To Use With An AI Agent

Start a session with your AI agent in this repository and give it a scoped task.
A useful opening instruction is:

```text
Read agent.md, README.md, and framework/workflows/engagement-lifecycle.md.
Work only within the authorized scope I provide. Use scripts/sec.py for
engagement state, knowledge recall, validation, evidence logging, and reports.
Do not treat the CLI as an autonomous pentest runner.
```

The agent should then:

1. Confirm the authorized target, task type, and boundaries.
2. Initialize or resume an engagement workspace.
3. Run local knowledge recall before changing phase or testing a hypothesis.
4. Form candidate routes and validate them with the smallest safe probe.
5. Record commands, decisions, evidence paths, and negative findings.
6. Distill reusable results into `knowledge/` and validate the framework state.
7. Produce a final summary or report for the human operator.

## Support CLI

The CLI helps the agent keep work structured. Typical support commands include:

```bash
python scripts/sec.py init \
  --id local-lab \
  --name local-lab \
  --type lab \
  --target 127.0.0.1

python scripts/sec.py knowledge recall --engagement local-lab --phase intake
python scripts/sec.py scope validate --engagement local-lab
python scripts/sec.py report --engagement local-lab
python scripts/sec.py summary validate --engagement local-lab
python scripts/sec.py validate --tier smoke
```

These commands support the workflow; they do not replace agent judgment,
authorization checks, or evidence review.

## Runtime Setup

Python is the control runtime. Node is optional and used only when a specific
browser or frontend probe needs it.

```bash
scripts/bootstrap.sh --profile python-core
scripts/bootstrap.sh --profile node-browser
scripts/bootstrap.sh --profile full-lab
```

## Knowledge Loop

Every active phase should have a local knowledge recall record before phase
exit:

```bash
python scripts/sec.py knowledge recall --engagement <id> --phase <phase>
```

The recall can return no hits, but the no-hit record is still useful. It keeps
agent decisions tied to local cases, playbooks, tools, references, and prior
reports.

## Validate

After framework or knowledge changes, run:

```bash
python scripts/sec.py validate --tier smoke
```
