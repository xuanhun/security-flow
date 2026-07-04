---
name: kali
description: Kali-style authorized penetration testing and CTF workflow for environments where Kali Linux is unavailable or optional. Use when Codex needs to plan, initialize, run, review, or report a scoped security assessment or solve authorized CTF challenges using installable free tools, Python orchestration, CTF knowledge by category, information gathering, vulnerability analysis, web application assessment, crypto/misc/reverse/mobile triage, exploitation gates, evidence handling, and report generation.
---

# Kali

## Mission

Run authorized security assessments as a Kali-style workflow without requiring a
Kali installation. Use Python for scope enforcement, tool orchestration,
evidence capture, high-risk gates, and reporting; use free installable tools
when they reduce custom code.

## Operating Rules

1. Require a project `scope.json` before touching a target.
2. Refuse out-of-scope targets.
3. Prefer safe discovery and baseline checks first.
4. Put generated evidence under `engagements/<project-id>/`.
5. Treat exploitation, online password attacks, sniffing/spoofing, wireless
   attacks, post-exploitation, destructive fuzzing, and heavy scans as gated
   actions.
6. Record commands and generated artifacts so another operator can replay or
   review the work.
7. Use structured memory for hypotheses, candidate routes, negative evidence,
   verification state, and next-step constraints before repeating probes.

## Quick Start

```bash
python scripts/sec.py init-project \
  --name local-lab \
  --target 127.0.0.1

python scripts/sec.py check-env --project local-lab
python scripts/sec.py install-tools --profile safe-core --project local-lab
python scripts/sec.py validate-scope --project local-lab
python scripts/sec.py scan --project local-lab --ports 22,80,443,8000-8100
python scripts/sec.py web --project local-lab --target http://127.0.0.1:8000
python scripts/sec.py report --project local-lab
```

`install-tools` prints an install plan by default. Add `--execute` only when the
user approves package installation.

Use `memory --summary` and `memory --next` to review route memory and current
constraints. Use `candidate` to record a hypothesis and `attempt` to record its
evidence outcome.

## Kali-Style Modules

- Information gathering: host, DNS, port, and service discovery.
- Vulnerability analysis: safe baseline first; heavier scanners behind gates.
- Web applications: HTTP headers, status, redirects, fingerprinting, and
  bounded web probes.
- Database assessment: identify exposed database services and route manual
  checks.
- Password audit: offline hash review only by default; online attacks are
  gated.
- Wireless: tool detection and lab workflow only by default.
- Reverse engineering: file triage, strings, hashes, and binary analysis tools.
- Exploitation: evidence preparation and explicit gate; no automatic exploit.
- Sniffing/spoofing: explicit gate; no automatic traffic interception.
- Post-exploitation: explicit gate; no automatic persistence or lateral action.
- Forensics: hash, timeline, artifact inventory, and read-only analysis.
- Reporting: Markdown and JSON assessment reports from captured evidence.

## CTF Knowledge

For CTF work, first read
[references/ctf-agent-skill-tree.md](references/ctf-agent-skill-tree.md), then
[references/ctf-knowledge-index.md](references/ctf-knowledge-index.md). The
CTF agent flow is based on a Nemo-style local state machine: notes first,
phases in order, local knowledge routing, explicit checkpoints, and proof
before solve. Open the target with skill tools for first-pass information
gathering, then browse the local casebook by category, artifact, technique, and
route. Load only the category file that matches the observed challenge surface.

Use CTF references for authorized challenge environments only. Keep notes
evidence-driven: symptom, hypothesis, probe, result, and next route.

When this skill is used from the security wisdom workspace, follow
`framework/workflows/engagement-lifecycle.md` before solving a challenge. The
workflow controls intake, first-pass information gathering, tool-first
execution, capability gaps, replay evidence, and post-solve distillation.

## CTF Tool Rule

Use `scripts/ctf_agent.py` as the local CTF scheduler and handoff surface when
the task needs durable state, recovery, or multi-step solving. It does not use
containers and does not execute high-risk actions. Its core commands are:

- `init`
- `queue`
- `next`
- `start`
- `note`
- `phase`
- `knowledge`
- `block`
- `fail`
- `solve`
- `summary`
- `memory`
- `candidate`
- `attempt`

Typical local case loop:

```bash
python scripts/sec.py memory init --case-dir local-demo --name local-demo --category web --url http://127.0.0.1
python scripts/sec.py memory start --case-dir local-demo
python scripts/sec.py memory note --case-dir local-demo --read-all
python scripts/sec.py memory phase --case-dir local-demo
python scripts/sec.py memory knowledge --case-dir local-demo
python scripts/sec.py memory summary --case-dir local-demo
```

Use the skill tools before manual probing. For Web CTF tasks, start with:

```bash
python scripts/sec.py probe web --help
python scripts/sec.py probe web init-case ...
python scripts/sec.py probe web snapshot ...
```

After this first-pass evidence is captured, browse the local casebook by
content hierarchy. Start broad and go one level deeper only when evidence
supports it:

```bash
python scripts/sec.py knowledge browse
python scripts/sec.py knowledge browse --category 'Network Forensics'
python scripts/sec.py knowledge browse --category 'Network Forensics' --artifact pcap
python scripts/sec.py knowledge browse --category 'Network Forensics' --artifact pcap --technique http-analysis --cards
```

When the first-pass evidence, local casebook, and two or three skill-backed
hypotheses do not produce a viable route, open the wisdom workflow's stall web
search gate. Use web results only as hypotheses, record the search queries and
useful URLs in the challenge notes, and verify every borrowed idea against the
current target with skill tools before relying on it.

If the current task needs a repeatable probe that `ctf_web.py` cannot perform,
add the missing command to the skill first, then run it. Do not rely on ad hoc
one-off curl or Python snippets when the action is likely to recur.

After a challenge is solved, update the relevant CTF knowledge reference and
case card with the exact skill commands needed to replay the route.

## Script Entry

Use `scripts/kali.py` as the only public CLI. Read or patch modules under
`scripts/core/` and `scripts/modules/` only when extending behavior.

Core commands:

- `init-project`
- `check-env`
- `install-tools`
- `validate-scope`
- `scan`
- `web`
- `vuln-nikto`
- `exploit-gate`
- `report`
- `memory`
- `candidate`
- `attempt`

Use `scripts/ctf_web.py` for CTF Web challenge probing:

- `init-case`
- `snapshot`
- `request`
- `aes-envelope-request`
- `login-probe`
- `cookie-audit`
- `cookie-decode`
- `jwt-decode`
- `jwt-sign`
- `jwt-batch-sign`
- `jwt-crack`
- `jwt-variant-probe`
- `auth-confirm`
- `repeat-request`
- `param-probe`
- `lfi-probe`
- `signed-download-probe`
- `dp-sample`
- `sql-rewrite-sim`
- `agent-ws-chat`
- `agent-ws-protocol-probe`
- `js-analyze`
- `source-map-extract`
- `summary`

Use `scripts/ctf_browser.sh` for browser-rendered CTF evidence. The wrapper
uses the skill-local `.nvmrc` through nvm, then runs `ctf_browser.js`. Use
`--cookie` to inject scoped challenge cookies and `--capture-bodies` when small
non-video API responses should be preserved with the browser trace.

- `snapshot`
- `video-captures`
- `contact-sheet`

Use `scripts/ctf_pdf.py` for PDF reports and PDF-based challenge artifacts:

- `check-env`
- `extract-text`

Use `scripts/ctf_artifact.py` for local CTF artifacts when external tools such
as tshark or ffmpeg are unavailable:

- `inventory`
- `download-url`
- `zip-inspect`
- `tar-inspect`
- `pcapng-http`
- `mp4-inspect`

Use `scripts/ctf_mobile.py` for APK and mobile challenge triage:

- `apk-summary`
- `jadx-decompile`
- `source-grep`

Use `scripts/ctf_image.py` for image metadata, PNG forensics, and
watermark-style CTF artifacts:

- `exif-gps`
- `inspect`
- `extract-appended`
- `render-partial`
- `channel-diff`
- `channel-band`
- `channel-mod`
- `bitplanes`
- `resize`
- `crop`
- `lsb-scan`
- `barcode-scan`

Use `scripts/ctf_oob.py` for blind XSS, blind SSRF, webhook, or callback-style
CTF probes where the target or an admin bot may make an out-of-band HTTP
request:

- `serve`

Use `scripts/ctf_prng.py` for predictable random-token or OTP challenges:

- `go-rand-predict`
- `go-rand-otp`

Use `scripts/ctf_crypto.py` for local ciphertext triage, recursive Base64
decoding, Morse/two-symbol decoding, book-coordinate key extraction, and simple
Vigenere-style alphabet shifts:

- `triage`
- `base64-chain`
- `morse`
- `book-extract`
- `line-extract`
- `vigenere`

Use `scripts/ctf_tcp.py` for raw TCP CTF services and interactive oracles:

- `shuffle-oracle-solve`

Use `scripts/ctf_pg.py` for PostgreSQL CTF services where a challenge exposes
PGDATA, md5 verifiers, catalog clues, or simple database query surfaces:

- `query`

Use `scripts/ctf_agent.py` for Nemo-style local CTF state management:

- `init`
- `queue`
- `next`
- `start`
- `note`
- `phase`
- `knowledge`
- `block`
- `fail`
- `solve`
- `summary`

Use `scripts/ctf_casebook.py` for local CTF casebook ingestion and lookup:

- `ingest-writeups`
- `ingest-markdown-repo`
- `reindex`
- `search`
- `browse`
- `show`

## References

- Read [references/rules-of-engagement.md](references/rules-of-engagement.md)
  before real assessments.
- Read [references/kali-framework-map.md](references/kali-framework-map.md)
  when choosing the right Kali-style module.
- Read [references/tool-profiles.md](references/tool-profiles.md) before
  installing or invoking external tools.
- Read [references/evidence-schema.md](references/evidence-schema.md) when
  extending evidence or finding formats.
- Read [references/structured-memory.md](references/structured-memory.md) when
  extending or relying on candidate routes, failed attempts, verification
  state, lanes, or next-step constraints.
- Read [references/safety-gates.md](references/safety-gates.md) before adding
  high-risk automation.
- Read [references/report-template.md](references/report-template.md) when
  modifying reports.
- Read [references/ctf-knowledge-index.md](references/ctf-knowledge-index.md)
  when solving CTF challenges or adding new category knowledge.
- Read [references/ctf-agent-skill-tree.md](references/ctf-agent-skill-tree.md)
  when a challenge needs durable local state, phase checkpoints, or handoff.
- Read [references/ctf-external-pattern-map.md](references/ctf-external-pattern-map.md)
  when the category is unclear or a challenge stalls and needs a broad CTF
  pattern cross-check.
- Read [references/ctf-case-index.md](references/ctf-case-index.md) when a
  solved challenge should guide future CTF work.
- Read [references/ctf-casebook.md](references/ctf-casebook.md)
  when using or refreshing the parsed external writeup casebook.
