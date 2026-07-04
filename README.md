# Unified Security Assessment Framework

This workspace manages CTF, lab, and authorized penetration testing work with
one engagement model. The framework is built around scope validation, local
knowledge recall, structured context, evidence logs, candidate routes, and
reports.

## Entry Points

- CLI: `scripts/sec.py`
- Process: `framework/workflows/engagement-lifecycle.md`
- Logging schema: `framework/references/logging-schema.md`
- Context rules: `framework/references/context-management.md`
- Knowledge retrieval: `framework/references/knowledge-retrieval.md`
- Post-test summary: `framework/references/post-test-summary.md`
- Engagements: `engagements/`
- Knowledge base: `knowledge/`

## Quick Start

```bash
scripts/bootstrap.sh --profile python-core

python scripts/sec.py init \
  --id local-lab \
  --name local-lab \
  --type lab \
  --target 127.0.0.1

python scripts/sec.py knowledge reindex
python scripts/sec.py knowledge recall --engagement local-lab --phase intake
python scripts/sec.py phase exit --engagement local-lab --phase intake
python scripts/sec.py phase enter --engagement local-lab --phase recon
python scripts/sec.py scope validate --engagement local-lab
python scripts/sec.py probe scan --engagement local-lab --target 127.0.0.1
python scripts/sec.py report --engagement local-lab
python scripts/sec.py summary generate \
  --engagement local-lab \
  --result-status completed \
  --outcome-summary "Local smoke assessment completed."
python scripts/sec.py summary validate --engagement local-lab
```

## Runtime Profiles

Python is the control runtime. Node is optional and loaded only when browser or
frontend probes need it.

```bash
scripts/bootstrap.sh --profile python-core
scripts/bootstrap.sh --profile node-browser
scripts/bootstrap.sh --profile full-lab
```

## Knowledge Loop

Every active phase must have a knowledge recall record before phase exit:

```bash
python scripts/sec.py knowledge recall --engagement <id> --phase <phase>
```

The recall can return no hits, but the no-hit record is still required. This
keeps testing decisions tied to local cases, playbooks, tools, and prior
reports.

## Validate

```bash
python scripts/sec.py validate --tier smoke
```
