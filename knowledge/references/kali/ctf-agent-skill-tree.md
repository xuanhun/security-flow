# CTF Agent Skill Tree

Use this reference as the Nemo-style base layer for authorized CTF work in
`src/security_framework`. The local system has no containers and no Web UI. A case
directory is the execution boundary, and `ctf_agent.py` is the scheduler and
state machine.

## Core Loop

1. Initialize or reuse a case with `ctf_agent.py init`.
2. Start the case with `ctf_agent.py start`.
3. Read all notes with `ctf_agent.py note --read-all` before probing.
4. Follow phases in order: `note_replay`, `phase1_recon`, `phase2_active`,
   `phase3_knowledge`, `phase4_verify`, `result`, `distill`.
5. Complete each phase with a checkpoint before advancing.
6. Run `ctf_agent.py knowledge` after first-pass evidence and whenever the
   route changes materially.
7. Use `ctf_agent.py candidate`, `attempt`, and `memory --next` for candidate
   routes, negative evidence, and next constraints before repeating probes.
8. Mark `solve`, `block`, or `fail` with proof and evidence instead of leaving
   a case implicit.

## State And Notes

- `state.json` is the source of truth for state, phase, retry count, timeout,
  blocked reason, failure reason, and next action.
- `notes/info.md` stores verified facts and failed methods.
- `notes/infer.md` stores hypotheses, knowledge hits, and route candidates.
- `notes/result.md` stores successful routes, flags, proof, and replay
  commands.
- `notes/timeline.md` stores human-readable progress and handoff notes.
- `memory/state.json` stores structured goals, surface paths, input formats,
  candidate routes, negative evidence, verification state, and next
  constraints.
- `memory/lanes/<lane-id>.json` stores the lane-local view for shared-memory
  parallel exploration.
- `events.jsonl`, `phase-checkpoints.jsonl`, and `knowledge/hits.json` keep
  machine-readable evidence for recovery.

## Phase Protocol

| Phase | Required action | Evidence |
| --- | --- | --- |
| `note_replay` | Read notes, replay any successful route, reuse verified facts, skip failed routes. | Notes read event and checkpoint. |
| `phase1_recon` | Collect safe first-pass target or artifact evidence. | Snapshots, inventory, headers, files, screenshots, summaries. |
| `phase2_active` | Run bounded probes chosen by category and evidence. | Tool JSON, raw responses, parser output, command record. |
| `phase3_knowledge` | Query local casebook, category knowledge, solved cases, and optional local vuln indexes; convert useful hits into candidate routes. | `knowledge/hits.json`, `infer.md`, and `memory/state.json`. |
| `phase4_verify` | Verify the route with the smallest sufficient probe; record success, negative, inconclusive, blocked, or gated attempts. | Proof request, decoded artifact, recovered value, reproduced behavior, and `verification_state`. |
| `result` | Write flag, proof route, and replay commands. | `result.md` and `solve` event. |
| `distill` | Update reusable knowledge, case cards, or skill tools. | Knowledge/case/tool change and validation command. |

## Capability Domains

### core

- Signal: every CTF case.
- First tool: `ctf_agent.py`.
- Knowledge: this file, `ctf-knowledge-index.md`, `ctf-casebook.md`.
- Avoid: probing before notes and first-pass evidence.
- Evidence: state, notes, events, checkpoints, structured memory.
- Gate: no, unless the selected downstream action is gated.

### web

- Signal: URL, HTTP service, cookies, JWT, route, form, API, source map.
- First tools: `ctf_web.py init-case`, `snapshot`, `request`,
  `login-probe`, `summary`.
- Knowledge: `ctf-knowledge-web.md`, local casebook category `Pentesting`.
- Avoid: blind fuzzing before reading scripts, routes, cookies, and source.
- Evidence: raw HTTP, response summaries, cookies, redirects, scripts.
- Gate: heavy scans and exploit attempts follow `safety-gates.md`.

### artifact

- Signal: provided file, archive, document, media, packet capture, image.
- First tools: `ctf_artifact.py inventory`, `zip-inspect`, `tar-inspect`,
  `pcapng-http`, `mp4-inspect`.
- Knowledge: `ctf-knowledge-misc-forensics.md`, casebook artifact hierarchy.
- Avoid: extracting or rewriting before inventory and hashes.
- Evidence: inventory JSON, extracted file paths, hashes, metadata.
- Gate: no for read-only inspection.

### forensics

- Signal: pcap, disk image, logs, event records, memory, browser artifacts.
- First tools: `ctf_artifact.py`, category-specific external tools when
  already installed.
- Knowledge: `ctf-knowledge-misc-forensics.md`, casebook forensics cards.
- Avoid: trusting one artifact without correlation.
- Evidence: timelines, streams, carved files, packet or log references.
- Gate: no for read-only analysis.

### crypto

- Signal: cipher text, oracle, PRNG, OTP, signature, key derivation.
- First tools: `ctf_crypto.py`, `ctf_prng.py`, `ctf_tcp.py`, small local
  scripts promoted into skill commands when repeated.
- Knowledge: `ctf-knowledge-crypto.md`.
- Avoid: brute force without identifying the primitive or leak.
- Evidence: inputs, outputs, recovered seed/key, verification transcript.
- Gate: no for local challenge computation.

### reverse-pwn

- Signal: binary, wasm, ELF, PE, interactive service, crash, encoded routine.
- First tools: `ctf_artifact.py inventory`, system `strings/file` when present,
  then category-specific tools.
- Knowledge: `ctf-knowledge-reverse-pwn.md`.
- Avoid: patching or exploitation before static triage.
- Evidence: file type, strings, symbols, constraints, reproduced IO.
- Gate: exploit-like actions against live targets require safety review.

### mobile

- Signal: APK, Android routes, exported activity, mobile API, app storage.
- First tools: `ctf_mobile.py apk-summary`, `jadx-decompile`, `source-grep`.
- Knowledge: `ctf-knowledge-mobile.md`.
- Avoid: assuming UI restrictions are server-side restrictions.
- Evidence: manifest, exported components, source snippets, API replay.
- Gate: no for local APK analysis.

### ai-watermark

- Signal: model output, image watermark, prompt boundary, multimodal artifact.
- First tools: `ctf_image.py inspect`, `channel-diff`, `channel-mod`,
  `bitplanes`, `crop`, `barcode-scan`, `ctf_crypto.py base64-chain` for
  encoded model-output secrets.
- Knowledge: `ctf-knowledge-ai-watermark.md`.
- Avoid: semantic guessing before pixel/channel evidence.
- Evidence: masks, crops, residue statistics, recovered literal text.
- Gate: no for local artifact analysis.

### database/pg

- Signal: PostgreSQL endpoint, PGDATA, verifier, large object, catalog clue.
- First tools: `ctf_pg.py query`, artifact inventory, local notes.
- Knowledge: `ctf-knowledge-web.md` plus solved PG case notes when present.
- Avoid: treating authentication bypass ideas as proven without packet or SQL
  evidence.
- Evidence: SQL output, catalog metadata, LO ids, decoded fragments.
- Gate: live database mutation or privileged execution must be explicitly
  scoped.

### osint

- Signal: domain, email, public profile, repository, image location clue.
- First tools: local evidence extraction, `ctf_image.py exif-gps` for JPG/TIFF
  GPS metadata, `ctf_crypto.py triage` for obvious encoded profile hints,
  browser snapshots, documented web search only after the workflow allows it.
- Knowledge: `ctf-knowledge-osint.md`.
- Avoid: submitting external answers without local validation.
- Evidence: URLs, timestamps, screenshots, source attribution.
- Gate: respect public-source and privacy limits.

### knowledge

- Signal: after first-pass evidence, route change, stall, or new technology.
- First tools: `ctf_agent.py knowledge`, `ctf_casebook.py browse/show`.
- Knowledge: case notes, casebook, category references, solved cases, optional
  local `vulhub` and `vulnerability-wiki` indexes.
- Avoid: using WebSearch before the stall gate.
- Evidence: `knowledge/hits.json`, selected card paths, rejected false leads.
- Gate: WebSearch only after local evidence and local hypotheses stall.

### reporting

- Signal: solve, block, fail, handoff, or user asks for status.
- First tools: `ctf_agent.py summary`, existing skill summaries.
- Knowledge: `report-template.md`, `evidence-schema.md`.
- Avoid: summaries that omit failed routes or missing evidence.
- Evidence: status, phase, next step, proof path, replay commands.
- Gate: no.
