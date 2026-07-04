# Chollima Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_chollima_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, ids, registry challenges.

## Input Signals

- Artifacts: disk-image, ids, registry, windows-events
- Tools: db-browser-sqlite, ftk-imager, ida, mftecmd, registry-explorer, virustotal
- Techniques: browser-forensics, cti-enrichment, http-analysis, privilege-escalation, registry-forensics, reverse-engineering, service-enumeration, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: vector. What is the full URL from which the malicious software was downloaded?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager, mftecmd, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager, mftecmd, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `http://3.101.53.248:8080/vcam-installer.exe`

### Step 2: What is the timestamp when the malicious ZIP file was created on the machine?

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use ftk-imager, mftecmd, registry-explorer, virustotal to recover or open the referenced file and inspect its metadata fields.
- Tools: ftk-imager, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use ftk-imager, mftecmd, registry-explorer, virustotal to recover or open the referenced file and inspect its metadata fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2025-07-27 21:33`

### Step 3: hash of this malicious script?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: ftk-imager, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0EC9D355F482A292990055A9074FDABDB75D72630B920A61BDF387F2826F5385`

### Step 4: the function responsible for creating the persistence mechanism?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager, mftecmd, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager, mftecmd, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `csshost.exe`

### Step 5: What we are concerned with is the register_startup function. A basic persistence mechanism

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager, mftecmd, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager, mftecmd, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `register_startup`

### Step 6: the sub-technique used by the malware to achieve persistence?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager, mftecmd, registry-explorer, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager, mftecmd, registry-explorer, virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `T1547.001`

### Step 7: of the function that attempts to re-launch the malware with administrator rights?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use ftk-imager, mftecmd, registry-explorer, virustotal to align timestamps and identify the event that satisfies the question.
- Tools: ftk-imager, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use ftk-imager, mftecmd, registry-explorer, virustotal to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `auto_mode_chrome_cookie`

### Step 8: traffic. What is the name of this technique?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use ftk-imager, mftecmd, registry-explorer, virustotal to align timestamps and identify the event that satisfies the question.
- Tools: ftk-imager, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use ftk-imager, mftecmd, registry-explorer, virustotal to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `jitter`

### Step 9: and stored to identify this specific infected machine?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager, mftecmd, registry-explorer, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager, mftecmd, registry-explorer, virustotal to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 10: how to identify the file extension of the file containing the UID. Use the parsed MFT file to locate

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager, mftecmd, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager, mftecmd, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `fa2a216e`

### Step 11: Process ID (PID) of the malware recorded in this file?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ftk-imager, ida, mftecmd, registry-explorer to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ftk-imager, ida, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use ftk-imager, ida, mftecmd, registry-explorer to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7900`

### Step 12: decompression. What is the name of the vulnerability this check protects against?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ftk-imager, ida, mftecmd, registry-explorer with the extracted filter/query `The util.py script contains all the compression, decompression, and validation logic. We can` and inspect the matching evidence.
- Tools: ftk-imager, ida, mftecmd, registry-explorer, virustotal
- Filters or commands:
  - `The util.py script contains all the compression, decompression, and validation logic. We can`
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use ftk-imager, ida, mftecmd, registry-explorer with the extracted filter/query `The util.py script contains all the compression, decompression, and validation logic. We can` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Path Traversal`

### Step 13: functions used to get the master key and decrypt the password blob, respectively?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use ftk-imager, mftecmd, registry-explorer, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: ftk-imager, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use ftk-imager, mftecmd, registry-explorer, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `get_secret_key,decrypt_password`

### Step 14: created to store stolen browser credentials?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use ftk-imager, mftecmd, registry-explorer, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: ftk-imager, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use ftk-imager, mftecmd, registry-explorer, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\z4hra\AppData\Local\Temp\nvidiaRelease\chrome_logins_dump.txt`

### Step 15: package stolen directories for exfiltration?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager, mftecmd, registry-explorer, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager, mftecmd, registry-explorer, virustotal to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `compress_0509`

### Step 16: address and port of the C2 server?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager, mftecmd, registry-explorer, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager, mftecmd, registry-explorer, virustotal to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `154.58.204.15:8080`

### Step 17: is used to encrypt the data sent to and from the C2 server?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager, mftecmd, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager, mftecmd, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `RC4`

### Step 18: download a second-stage payload onto the victim's machine?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use ftk-imager, mftecmd, registry-explorer, virustotal with the extracted filter/query `The command.py script contains all the command logic. Here we can find a function called` and inspect the matching evidence.
- Tools: ftk-imager, mftecmd, registry-explorer, virustotal
- Filters or commands:
  - `The command.py script contains all the command logic. Here we can find a function called`
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use ftk-imager, mftecmd, registry-explorer, virustotal with the extracted filter/query `The command.py script contains all the command logic. Here we can find a function called` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `process_upload`

### Step 19: the malware to steal browser cookies and passwords?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use ftk-imager, mftecmd, registry-explorer, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: ftk-imager, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use ftk-imager, mftecmd, registry-explorer, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `R4ys`

### Step 20: outbound data into the custom encrypted packet format?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager, mftecmd, registry-explorer, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager, mftecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager, mftecmd, registry-explorer, virustotal to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `packet_make0509`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
