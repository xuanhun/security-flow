# MinerHunt Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_minerhunt_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for pe-malware, registry, windows-events challenges.

## Input Signals

- Artifacts: pe-malware, registry, windows-events
- Tools: capa, evtxecmd, virustotal
- Techniques: cti-enrichment, http-analysis, malware-static, privilege-escalation, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: Initial access was achieved through a brute force attack, ultimately leading to the threat actor

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 2: specific account was targeted?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use evtxecmd, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use evtxecmd, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `T1110,sa`

### Step 3: Server using the compromised account?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use evtxecmd, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use evtxecmd, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3.79.210.175`

### Step 4: when the threat actor last logged in:

- Route type: `evtxecmd-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use evtxecmd, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as evtxecmd-driven evidence lookup.
  - Use evtxecmd, virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2025-03-09 11:32`

### Step 5: What was the source IP address used by the attacker when attempting to access the SQL Server?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3.79.210.175`

### Step 6: from the attacker's machine?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use capa, evtxecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: capa, evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use capa, evtxecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\Public\xx.exe x C:\Users\Public\XeX.7z -oC:\Users\Public -y`

### Step 7: MITRE ATT&CK technique identifier is associated with its misuse?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `xp_cmdshell,T1059.003`

### Step 8: utilized during the attack?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2025-03-09 11:40`

### Step 9: targeted by the attacker?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Kaspersky`

### Step 10: What is the full path of the batch file created by the attacker, which contains multiple

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use evtxecmd, virustotal to align timestamps and identify the event that satisfies the question.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use evtxecmd, virustotal to align timestamps and identify the event that satisfies the question.
  - The proof is the timestamped artifact that matches the question constraint.
- Evidence rule: The proof is the timestamped artifact that matches the question constraint.

### Step 11: and system configuration modifications?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use evtxecmd, virustotal with the extracted filter/query `the threat actor used cmd.exe to create a batch file called N1F10.bat. This batch file contains` and inspect the matching evidence.
- Tools: evtxecmd, virustotal
- Filters or commands:
  - `the threat actor used cmd.exe to create a batch file called N1F10.bat. This batch file contains`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use evtxecmd, virustotal with the extracted filter/query `the threat actor used cmd.exe to create a batch file called N1F10.bat. This batch file contains` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\Public\N1F10.bat`

### Step 12: attempt to hide this account from the Windows login screen?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use evtxecmd, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use evtxecmd, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Admin_env$,HKLM\SOFTWARE\Microsoft\Windows`

### Step 13: the attacker, and what is the full path of the file executed as a result of this WMI setup?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `consumer occurs.`

### Step 14: find the name of the WMI Consumer event, we can filter for Event ID 20 (WmiEventConsumer

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `NF .bmof,BatConsumer, C:\Users\Public\XeX\mi.bat`

### Step 15: persistence, and what is the exact data assigned to that value?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use evtxecmd, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use evtxecmd, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution`

### Step 16: settings and enable plaintext credential storage, aiding in credential theft?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use evtxecmd, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use evtxecmd, virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `reg add "HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest" /v`

### Step 17: What is the complete file path of the encoded file that was later used to escalate privileges?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `C:\Temp\FM.txt`

### Step 18: that's available on GitHub. What is the full link to the GitHub repository for this tool?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `https://github.com/decoder-it/NetworkServiceExploit`

### Step 19: What is the attacker's machine IP used for downloading files during the attack activities?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `18.184.228.195`

### Step 20: MD5 hash of the miner?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `F6D520AE125F03056C4646C508218D16`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
