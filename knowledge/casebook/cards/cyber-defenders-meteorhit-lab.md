# MeteorHit Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_meteorhit_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, email, registry challenges.

## Input Signals

- Artifacts: disk-image, email, registry, windows-events
- Tools: evtxecmd, mftecmd, registry-explorer, virustotal
- Techniques: cti-enrichment, dns-analysis, http-analysis, malware-dynamic, registry-forensics, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the name of the malicious GPO responsible for initiating the attack by running a script?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use mftecmd, registry-explorer, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use mftecmd, registry-explorer, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `DeploySetup`

### Step 2: where the image was taken from had Sysmon enabled. We can use this to search for Event ID 1

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use evtxecmd, mftecmd, registry-explorer, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: evtxecmd, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use evtxecmd, mftecmd, registry-explorer, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\ProgramData\Microsoft\env\env.cab`

### Step 3: extract the malicious files?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use mftecmd, registry-explorer, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use mftecmd, registry-explorer, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `hackemall`

### Step 4: What is the name of the first file added to the Windows Defender exclusion list?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use mftecmd, registry-explorer, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use mftecmd, registry-explorer, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `update.bat`

### Step 5: many seconds after the task creation time is it scheduled to run?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use mftecmd, registry-explorer, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use mftecmd, registry-explorer, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `210`

### Step 6: responsible for performing this action?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use mftecmd, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use mftecmd, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7492`

### Step 7: scheduled task created by the malware to maintain persistence?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use mftecmd, registry-explorer, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use mftecmd, registry-explorer, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Aa153!EGzN`

### Step 8: tampering. What is the USN associated with the deletion of the file msuser.reg?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use mftecmd, registry-explorer, virustotal with the extracted filter/query `FileDelete|Close Update Reason, meaning that this file was deleted. Its USN (Update Sequence` and inspect the matching evidence.
- Tools: mftecmd, registry-explorer, virustotal
- Filters or commands:
  - `FileDelete|Close Update Reason, meaning that this file was deleted. Its USN (Update Sequence`
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use mftecmd, registry-explorer, virustotal with the extracted filter/query `FileDelete|Close Update Reason, meaning that this file was deleted. Its USN (Update Sequence` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `11721008`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
