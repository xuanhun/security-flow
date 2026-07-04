# CTF Casebook

Use this compact local casebook as an offline reasoning library after
first-pass target information gathering. It stores hierarchical indexes and
human-readable cards plus optional mirrored source repositories and searchable
asset inventory; raw extracted text and per-case full structured dumps are
still intentionally not kept in the skill.

## Local Contents

- Root: `knowledge/casebook`
- `index.json`: compact browse index, aggregate stats, route metadata, and
  card paths.
- `taxonomy.json`: machine-readable hierarchy for category, artifact,
  technique, route, and card navigation.
- `indexes/root.md`: human-readable root index. Follow links downward instead
  of using fuzzy search.
- `overview.md`: category, tool, technique, and route-type summary.
- `cards/*.md`: human-readable solve-thinking cards. Read these first.
- `indexes/sources/root.md`: mirrored source repository summary and raw asset
  index entry point.
- `sources/*/repo/**`: optional local mirrors of imported external repositories.

## Required Lookup Step

After opening the target and capturing first-pass evidence, run at least one
local casebook browse using observed category, artifact type, technology, and
route shape. Pick one level at a time:

1. Category: broad problem space, such as `Network Forensics` or `Pentesting`.
2. Artifact: evidence shape, such as `pcap`, `web-service`, `memory`, or
   `office-document`.
3. Technique: analysis technique, such as `http-analysis`, `dns-analysis`, or
   `malware-static`.
4. Route/card: choose the matching route type or read the returned cards.

Examples:

```bash
python scripts/sec.py knowledge browse
python scripts/sec.py knowledge browse --category 'Network Forensics'
python scripts/sec.py knowledge browse --category 'Network Forensics' --artifact pcap
python scripts/sec.py knowledge browse --category 'Network Forensics' --artifact pcap --technique http-analysis --cards
```

Then inspect the best local card before selecting hypothesis-driven probes:

```bash
python scripts/sec.py knowledge show --slug cyber-defenders-packetmaze-lab
python scripts/sec.py knowledge search --query ssti
python scripts/sec.py knowledge search --query yakit --type asset
```

## How To Apply Results

- Treat casebook hits as hypotheses, not answers.
- Extract transferable route shape: artifact type, first probes, route type,
  evidence rule, result, and reusable pattern.
- Prefer cases reached by matching artifact and technique signals over
  title-only similarity.
- Record the browse path in challenge notes, even when no card is useful.
- Do not let casebook hits replace first-pass evidence collection.

## Refresh

Refresh only when an upstream writeup repository needs to be re-learned:

```bash
python scripts/sec.py knowledge ingest-writeups \
  --repo /path/to/ctf_writeups \
  --progress 20

python scripts/sec.py knowledge ingest-markdown-repo \
  --repo /path/to/ctf-wps \
  --repo-url https://github.com/CUCCS/ctf-wps \
  --repo-name CUCCS/ctf-wps \
  --copy-source
```
