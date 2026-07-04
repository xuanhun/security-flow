# LummaStealer Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_lummastealer_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for email, ids, registry challenges.

## Input Signals

- Artifacts: email, ids, registry, windows-events
- Tools: cyberchef, db-browser-sqlite, evtxecmd, virustotal
- Techniques: browser-forensics, cti-enrichment, dns-analysis, http-analysis, malware-dynamic, service-enumeration, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: device. What is this command in its decoded form?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use db-browser-sqlite, evtxecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: db-browser-sqlite, evtxecmd
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use db-browser-sqlite, evtxecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `EvtxECmd.exe`

### Step 2: This indicates that a new process has started. The critical fields within these logs

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, db-browser-sqlite, evtxecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, db-browser-sqlite, evtxecmd
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, db-browser-sqlite, evtxecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `mshta "https://clicktogo.click/uploads/tra15"`

### Step 3: What is the MITRE ATT&CK sub-technique ID for the technique used by the malware

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite, evtxecmd to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite, evtxecmd
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite, evtxecmd to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 4: previous PowerShell command?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, evtxecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, evtxecmd
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, evtxecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `T1218.005`

### Step 5: the URL of the malicious website to which the Powershell command belongs?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, evtxecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, evtxecmd
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, evtxecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `https://check-robot.b-cdn.net/Done-Captcha.html`

### Step 6: name of this file?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use db-browser-sqlite, evtxecmd to align timestamps and identify the event that satisfies the question.
- Tools: db-browser-sqlite, evtxecmd
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use db-browser-sqlite, evtxecmd to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `tera15.zip`

### Step 7: What is the URL from which the above file was downloaded?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, evtxecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, evtxecmd
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, evtxecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://clicktogo.click/uploads/tera15.zip`

### Step 8: detection. What is the name of this process?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use db-browser-sqlite, evtxecmd, virustotal with the extracted filter/query `Let’s start by navigating to the tera15.zip file which contains the chkbkx.exe binary that was` and inspect the matching evidence.
- Tools: db-browser-sqlite, evtxecmd, virustotal
- Filters or commands:
  - `Let’s start by navigating to the tera15.zip file which contains the chkbkx.exe binary that was`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use db-browser-sqlite, evtxecmd, virustotal with the extracted filter/query `Let’s start by navigating to the tera15.zip file which contains the chkbkx.exe binary that was` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `BitLockerToGo.exe`

### Step 9: What is the first domain it attempts to connect to?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use db-browser-sqlite, evtxecmd, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: db-browser-sqlite, evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use db-browser-sqlite, evtxecmd, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `votteryloeq.shop`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
