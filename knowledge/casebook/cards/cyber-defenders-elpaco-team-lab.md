# ELPACO-team Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_elpaco_team_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, ids, pe-malware challenges.

## Input Signals

- Artifacts: disk-image, ids, pe-malware, windows-events
- Tools: capa, evtxecmd, mftecmd, virustotal
- Techniques: browser-forensics, cti-enrichment, dns-analysis, http-analysis, malware-dynamic, malware-static, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: the MSSQL server?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, mftecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, mftecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `21`

### Step 2: When did the attacker first successfully log in to the MSSQL server during the brute-force attack?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use mftecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use mftecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2024-12-13 22:52`

### Step 3: that serves as a dropper for ransomware?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use capa, evtxecmd, mftecmd, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: capa, evtxecmd, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use capa, evtxecmd, mftecmd, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `oh_my_gotto.exe, 4224`

### Step 4: where the initial malicious components were dropped?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use mftecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use mftecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `7ZipSfx.000`

### Step 5: installed by the attacker on the victim's machine?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use mftecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use mftecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `FFF4B96876`

### Step 6: What is the MITRE sub-technique ID associated with the method the attacker used to establish persistence?

- Route type: `mftecmd-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use mftecmd, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as mftecmd-driven evidence lookup.
  - Use mftecmd, virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `T1136.001`

### Step 7: Which path did the attacker exclude to evade defenses?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use mftecmd, virustotal to enumerate processes, network sockets, injected regions, and command lines.
- Tools: mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use mftecmd, virustotal to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\`

### Step 8: What is the password for the protected archive that contains the additional malicious payloads?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use mftecmd, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use mftecmd, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7183204373585782`

### Step 9: copy the dropped files?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use mftecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use mftecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `BD3FDDDF`

### Step 10: legitimate system process. What new name was assigned to the ransomware?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use mftecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use mftecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `svhostss.exe`

### Step 11: stomped UTC creation timestamp of the ransomware file?

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use mftecmd, virustotal to recover or open the referenced file and inspect its metadata fields.
- Tools: mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use mftecmd, virustotal to recover or open the referenced file and inspect its metadata fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2021-08-19 01:32`

### Step 12: Defender. What is the name of the malicious file?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use mftecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use mftecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `DC.exe`

### Step 13: What are the IP address and port of the C2 server the attacker used to transfer their malicious tools?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use mftecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use mftecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `192.168.1.52:4561`

### Step 14: the process and PID?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use mftecmd, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use mftecmd, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `gui40.exe, 5484`

### Step 15: What is the name of the exfiltrated file?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use mftecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use mftecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Mimikatz_dump.txt`

### Step 16: for encryption. What is the name of the DLL?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use mftecmd, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use mftecmd, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Everything32.dll`

### Step 17: generated specified decryption ID. What are the first 10 characters of the decryption ID?

- Route type: `mftecmd-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use mftecmd, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as mftecmd-driven evidence lookup.
  - Use mftecmd, virustotal to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `BbvdsgAoTi`

### Step 18: data to prevent recovery. What is the official name of the tool the attacker used ?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use capa, mftecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: capa, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use capa, mftecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `SDelete`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
