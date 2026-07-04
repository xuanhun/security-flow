# Lockbit Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_lockbit_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for windows-events challenges.

## Input Signals

- Artifacts: windows-events
- Tools: cyberchef, evtxecmd, virustotal
- Techniques: cti-enrichment, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: when a user reported a ransom note on their screen alongside a Windows Defender alert

- Route type: `virustotal-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `executable?`

### Step 2: When Windows Defender detects malware, it logs Event ID 1116 (malware detected), which

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `8fe9c39.exe`

### Step 3: What's the path that was added to the exclusions of Windows Defender?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\`

### Step 4: What’s the IP of the machine that initiated the remote installation of the malicious service?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.170.142`

### Step 5: What’s the name of the process that had suspicious behavior as detected by Windows Defender?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `cmd.exe`

### Step 6: What’s the parent process name of the detected suspicious process?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `sqlservr.exe`

### Step 7: username that was compromised?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `sa`

### Step 8: enabled by the attacker?

- Route type: `virustotal-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `xp_cmdshell`

### Step 9: What’s the command executed by the attacker to disable Windows Defender on the server?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Set-MpPreference -DisableRealtimeMonitoring 1`

### Step 10: What's the name of the malicious script that the attacker executed upon disabling AV?

- Route type: `virustotal-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `fJSYAso.ps1`

### Step 11: What's the PID of the injected process by the attacker?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `596`

### Step 12: the scheduled task created by the attacker?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use virustotal to align timestamps and identify the event that satisfies the question.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use virustotal to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `UpdateCheck`

### Step 13: What’s the PID of the malicious process that dumped credentials?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5456`

### Step 14: What's the command used by the attacker to disable Windows Defender remotely on FileServer?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Invoke-Command -ComputerName FileServer -ScriptBlock { reg add`

### Step 15: What's the name of the malicious service executable blocked by Windows Defender?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ceabe99.exe`

### Step 16: What’s the name of the ransomware executable dropped on the machine?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `vmware.exe`

### Step 17: What’s the full path of the first file dropped by the ransomware?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\dmiller\Downloads\HHuYRxB06.README.txt`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
