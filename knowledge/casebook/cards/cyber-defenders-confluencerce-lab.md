# ConfluenceRCE Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_confluencerce_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for artifact-driven challenges.

## Input Signals

- Artifacts: not detected
- Tools: virustotal
- Techniques: cti-enrichment, http-analysis, malware-dynamic, timeline-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: determine that these crafted HTTP requests are used to execute arbitrary commands on

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal with the extracted filter/query `grep "/template/aui/text-inline.vm" conf_access_log.* | cut -d " " -` and inspect the matching evidence.
- Tools: virustotal
- Filters or commands:
  - `grep "/template/aui/text-inline.vm" conf_access_log.* | cut -d " " -`
  - `f5 | uniq -c`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal with the extracted filter/query `grep "/template/aui/text-inline.vm" conf_access_log.* | cut -d " " -` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `18.184.255.235`

### Step 2: dropped by the threat actor. What is the name of the first file dropped by the attacker?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `system.sh`

### Step 3: were attempted to be downloaded?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal with the extracted filter/query `This folder contains network logs at the time of collection. We are concerned with the “lsof_-` and inspect the matching evidence.
- Tools: virustotal
- Filters or commands:
  - `This folder contains network logs at the time of collection. We are concerned with the “lsof_-`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal with the extracted filter/query `This folder contains network logs at the time of collection. We are concerned with the “lsof_-` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `107.21.147.117`

### Step 4: framework utilized by the attacker?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `sliver`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
