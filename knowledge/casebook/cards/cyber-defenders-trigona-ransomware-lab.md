# Trigona Ransomware Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_trigona_ransomware_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, registry, windows-events challenges.

## Input Signals

- Artifacts: disk-image, registry, windows-events
- Tools: evtxecmd, mftecmd, pecmd, registry-explorer, virustotal
- Techniques: cti-enrichment, http-analysis, memory-forensics, registry-forensics, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: determine the delivery method of the ransomware and to trace all activities of the attacker to understand the progression of the attack.

- Route type: `mftecmd-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use mftecmd, pecmd, registry-explorer to collect the smallest evidence slice that answers the goal.
- Tools: mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as mftecmd-driven evidence lookup.
  - Use mftecmd, pecmd, registry-explorer to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 2: origin. What is the IP address of the attacker's machine?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, mftecmd, pecmd, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: evtxecmd, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, mftecmd, pecmd, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.19.100`

### Step 3: What was the first PowerShell command the attacker used for defense evasion?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, mftecmd, pecmd, registry-explorer to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, mftecmd, pecmd, registry-explorer to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Set-MpPreference -DisableRealtimeMonitoring $true`

### Step 4: performed by the attacker?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use mftecmd, pecmd, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use mftecmd, pecmd, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ipall.txt`

### Step 5: identify the file share and perform network enumeration?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use mftecmd, pecmd, registry-explorer to enumerate processes, network sockets, injected regions, and command lines.
- Tools: mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use mftecmd, pecmd, registry-explorer to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `netscan`

### Step 6: use to attempt data exfiltration?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, mftecmd, pecmd, registry-explorer to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, mftecmd, pecmd, registry-explorer to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `rclone`

### Step 7: share on the file server that was targeted by the attacker?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use mftecmd, pecmd, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use mftecmd, pecmd, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `F:\Shares\BusinessMaterial`

### Step 8: ransomware run on the file server and IT-machine?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use mftecmd, pecmd, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use mftecmd, pecmd, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `AmcacheParser.exe`

### Step 9: When the SHA1 hash of this binary was submitted to VirusTotal, it shows 63/72 detections and was flagged as ransomware:

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `cfaa59dd3288387f62efbf54477d531f4d3964f3`

### Step 10: ransomware variant. What is the file extension of the encrypted files?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use mftecmd, pecmd, registry-explorer to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use mftecmd, pecmd, registry-explorer to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `_vNrFy5`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
