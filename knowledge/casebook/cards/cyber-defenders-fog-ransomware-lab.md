# Fog Ransomware Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_fog_ransomware_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, email, registry challenges.

## Input Signals

- Artifacts: disk-image, email, registry, windows-events
- Tools: db-browser-sqlite, evtxecmd, mftecmd, registry-explorer, virustotal
- Techniques: browser-forensics, cti-enrichment, http-analysis, privilege-escalation, registry-forensics, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: Initial Access

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, evtxecmd, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `file?`

### Step 2: find the Administrator users’ browser history at: C\Users\Administrator\AppData\Local\Microsoft\Edge\User Data\Default\History

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, evtxecmd, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://limewire.com/d/lihUt#NrUgowrb29`

### Step 3: the exact timestamp when the user downloaded the RAR file to the system?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to align timestamps and identify the event that satisfies the question.
- Tools: db-browser-sqlite, evtxecmd, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2025-04-30 20:28`

### Step 4: payloads. What is the name of the PowerShell script that executed the payloads?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, evtxecmd, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `troubleshooting.ps1`

### Step 5: When did the ransomware first execute on the victim machine?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: db-browser-sqlite, evtxecmd, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2025-04-30 20:32`

### Step 6: sources. What is the SHA256 hash of the ransomware executable used in this attack?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: db-browser-sqlite, evtxecmd, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Acrobat.exe`

### Step 7: which we believe to be the ransomware executable.

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: db-browser-sqlite, evtxecmd, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `113A06C8BA6069D345F3C3DB89051553D8AFF7D27408945B50AA94256277DCB3`

### Step 8: MITRE ATT&CK sub-technique ID did the attacker use to gain persistence post-reboot?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: db-browser-sqlite, evtxecmd, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use db-browser-sqlite, evtxecmd, mftecmd, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `T1547.001`

### Step 9: the name of the vulnerable driver the attacker used for privilege escalation?

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: db-browser-sqlite, evtxecmd, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `iqvw64e.sys`

### Step 10: What technique did the attacker use to gain kernel-level access?

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite, evtxecmd, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Bring Your Own Vulnerable Driver`

### Step 11: name of the log file created by the ransomware to record its operations?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to align timestamps and identify the event that satisfies the question.
- Tools: db-browser-sqlite, evtxecmd, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `DbgLog.sys`

### Step 12: retrieve the payload?

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite, evtxecmd, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `192.168.1.54:4561`

### Step 13: extension did the ransomware append to encrypted files?

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite, evtxecmd, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite, evtxecmd, mftecmd, virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `.flocked`

### Step 14: .onion link provided by the attacker for ransom payment or communication?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use db-browser-sqlite, evtxecmd, mftecmd, virustotal with the extracted filter/query `Unfortunately, we can’t see the contents of the file here, but it likely contains the .onion link. I` and inspect the matching evidence.
- Tools: db-browser-sqlite, evtxecmd, mftecmd, virustotal
- Filters or commands:
  - `Unfortunately, we can’t see the contents of the file here, but it likely contains the .onion link. I`
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use db-browser-sqlite, evtxecmd, mftecmd, virustotal with the extracted filter/query `Unfortunately, we can’t see the contents of the file here, but it likely contains the .onion link. I` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `xql562evsy7njcsngacphc2erzjfecwotdkobn3m4uxu2gtqh26newid.onion`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
