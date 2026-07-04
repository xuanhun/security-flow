# Zerologon Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Hard`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_zerologon_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, email, registry challenges.

## Input Signals

- Artifacts: disk-image, email, registry, windows-events
- Tools: cyberchef, evtxecmd, mftecmd
- Techniques: browser-forensics, dns-analysis, http-analysis, malware-dynamic, privilege-escalation, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: from the ZIP archive?

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use cyberchef, evtxecmd, mftecmd to recover or open the referenced file and inspect its metadata fields.
- Tools: cyberchef, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use cyberchef, evtxecmd, mftecmd to recover or open the referenced file and inspect its metadata fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `documents.lnk`

### Step 2: the malicious script inside the ZIP Archive?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, evtxecmd, mftecmd to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, evtxecmd, mftecmd to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `easygoing.exe`

### Step 3: determine that the zip archive contained these documents due to the parent path along with the creation timestamp (all three files within the max directory were created at the same time). A .bat file, or batch file, is a

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use cyberchef, evtxecmd, mftecmd to align timestamps and identify the event that satisfies the question.
- Tools: cyberchef, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use cyberchef, evtxecmd, mftecmd to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `eyewear.bat`

### Step 4: the C2 IP address?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, evtxecmd, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, evtxecmd, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `42.63.200.142`

### Step 5: and export data about the domain's computers?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, evtxecmd, mftecmd with the extracted filter/query `Answer: Get-ADComputer -Filter * -Properties * | Export-CSV` and inspect the matching evidence.
- Tools: cyberchef, evtxecmd, mftecmd
- Filters or commands:
  - `Answer: Get-ADComputer -Filter * -Properties * | Export-CSV`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, evtxecmd, mftecmd with the extracted filter/query `Answer: Get-ADComputer -Filter * -Properties * | Export-CSV` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Get-ADComputer -Filter * -Properties * | Export-CSV`

### Step 6: the attacker use to attempt privilege escalation?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use cyberchef, evtxecmd, mftecmd to align timestamps and identify the event that satisfies the question.
- Tools: cyberchef, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use cyberchef, evtxecmd, mftecmd to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `echo ddb867670d7 > \\.\pipe\308808`

### Step 7: user account? Can you provide the password of the user account the attacker

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, evtxecmd, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, evtxecmd, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `MYpassword123#`

### Step 8: the command used by the attacker to achieve persistence?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use cyberchef, evtxecmd, mftecmd to enumerate processes, network sockets, injected regions, and command lines.
- Tools: cyberchef, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use cyberchef, evtxecmd, mftecmd to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `schtasks /create /tn "ChromeUpdater" /tr "powershell -File`

### Step 9: the folder whose data was targeted by the PowerShell script?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use cyberchef, evtxecmd, mftecmd to enumerate processes, network sockets, injected regions, and command lines.
- Tools: cyberchef, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use cyberchef, evtxecmd, mftecmd to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users`

### Step 10: attempts. What is the name of the malicious service installed remotely on FileServer?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use cyberchef, evtxecmd, mftecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: cyberchef, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use cyberchef, evtxecmd, mftecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `075b12b`

### Step 11: which is behaviour consistent with credential dumping. Both granted access values are

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use cyberchef, evtxecmd, mftecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: cyberchef, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use cyberchef, evtxecmd, mftecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `rundll32.exe`

### Step 12: the attacker install on one of the machines?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use cyberchef, evtxecmd, mftecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: cyberchef, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use cyberchef, evtxecmd, mftecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `AnyDesk`

### Step 13: What password did the attacker set for the installed software?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, evtxecmd, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, evtxecmd, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Qwerty123!@#_!`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
