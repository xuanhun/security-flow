# VaultBreak Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_vaultbreak_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, email, ids challenges.

## Input Signals

- Artifacts: disk-image, email, ids, office-document, registry, windows-events
- Tools: cyberchef, db-browser-sqlite, evtxecmd, mftecmd
- Techniques: browser-forensics, dns-analysis, http-analysis, maldoc-analysis, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: in the phishing email?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd to extract macros, streams, embedded URLs, and decoded script content.
- Tools: db-browser-sqlite, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use db-browser-sqlite, evtxecmd, mftecmd to extract macros, streams, embedded URLs, and decoded script content.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Finanical_Support.docm`

### Step 2: malware payload. What is the name of the first executable that was launched?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use cyberchef, db-browser-sqlite, evtxecmd, mftecmd to extract macros, streams, embedded URLs, and decoded script content.
- Tools: cyberchef, db-browser-sqlite, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use cyberchef, db-browser-sqlite, evtxecmd, mftecmd to extract macros, streams, embedded URLs, and decoded script content.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `msupdate-2381.exe`

### Step 3: during the attack?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, evtxecmd, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `10660`

### Step 4: Windows process was impersonated during the attack?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, evtxecmd, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `notepad.exe`

### Step 5: path that was created?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd with the extracted filter/query `2025-05-19 16:09:33 that contains the base64 encoded PowerShell payload we have observed` and inspect the matching evidence.
- Tools: db-browser-sqlite, evtxecmd, mftecmd
- Filters or commands:
  - `2025-05-19 16:09:33 that contains the base64 encoded PowerShell payload we have observed`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use db-browser-sqlite, evtxecmd, mftecmd with the extracted filter/query `2025-05-19 16:09:33 that contains the base64 encoded PowerShell payload we have observed` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Microsoft\Windows\UpdateOrchestrator\UpdateAssistant`

### Step 6: What MITRE ATT&CK technique ID is associated with the WMI persistence mechanism?

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite, evtxecmd, mftecmd to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `T1546.003`

### Step 7: and port used for C2 communications?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd to extract macros, streams, embedded URLs, and decoded script content.
- Tools: db-browser-sqlite, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use db-browser-sqlite, evtxecmd, mftecmd to extract macros, streams, embedded URLs, and decoded script content.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3.127.36.5`

### Step 8: which has a parent process of powershell.exe:

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd to enumerate processes, network sockets, injected regions, and command lines.
- Tools: db-browser-sqlite, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use db-browser-sqlite, evtxecmd, mftecmd to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `3.127.36.5:8443`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
