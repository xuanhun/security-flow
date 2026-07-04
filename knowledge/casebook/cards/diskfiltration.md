# DiskFiltration

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `TryHackMe`
- Difficulty: `Hard`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/diskfiltration.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, registry challenges.

## Input Signals

- Artifacts: disk-image, registry
- Tools: autopsy, exiftool, mftecmd
- Techniques: browser-forensics, dns-analysis, http-analysis, registry-forensics, stego-extraction, timeline-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the serial number of the USB device Liam used for exfiltration?

- Route type: `autopsy-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use autopsy, exiftool, mftecmd to collect the smallest evidence slice that answers the goal.
- Tools: autopsy, exiftool, mftecmd
- Reasoning chain:
  - Recognize the goal as autopsy-driven evidence lookup.
  - Use autopsy, exiftool, mftecmd to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2651931097993496666`

### Step 2: What is the profile name of the personal hotspot Liam used to evade network-level detection?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use autopsy, exiftool, mftecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: autopsy, exiftool, mftecmd
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use autopsy, exiftool, mftecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Liam's Iphone`

### Step 3: What is the name of the zip file Liam copied from the USB to the machine for exfiltration instructions?

- Route type: `autopsy-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use autopsy, exiftool, mftecmd with the extracted filter/query `Shellbags are a forensic artifact that contains details about what folders a user has accessed. If` and inspect the matching evidence.
- Tools: autopsy, exiftool, mftecmd
- Filters or commands:
  - `Shellbags are a forensic artifact that contains details about what folders a user has accessed. If`
- Reasoning chain:
  - Recognize the goal as autopsy-driven evidence lookup.
  - Use autopsy, exiftool, mftecmd with the extracted filter/query `Shellbags are a forensic artifact that contains details about what folders a user has accessed. If` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Shadow_Plan.zip`

### Step 4: What is the password for this zip file?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use autopsy, exiftool, mftecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: autopsy, exiftool, mftecmd
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use autopsy, exiftool, mftecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Qwerty@123`

### Step 5: the zip file?

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use autopsy, exiftool, mftecmd to recover or open the referenced file and inspect its metadata fields.
- Tools: autopsy, exiftool, mftecmd
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use autopsy, exiftool, mftecmd to recover or open the referenced file and inspect its metadata fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Henry`

### Step 6: What is the correct extension of the file that has no extension in the zip folder?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use autopsy, exiftool, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: autopsy, exiftool, mftecmd
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use autopsy, exiftool, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `png`

### Step 7: What are the names of the folders that were present on the USB device? (alphabetical order)

- Route type: `autopsy-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use autopsy, exiftool, mftecmd to collect the smallest evidence slice that answers the goal.
- Tools: autopsy, exiftool, mftecmd
- Reasoning chain:
  - Recognize the goal as autopsy-driven evidence lookup.
  - Use autopsy, exiftool, mftecmd to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Critical Data TECH THM, Exfiltration Plan`

### Step 8: how many times was it executed? (YYYY-MM-DD HH:MM:SS, number of execution times)

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use autopsy, exiftool, mftecmd to align timestamps and identify the event that satisfies the question.
- Tools: autopsy, exiftool, mftecmd
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use autopsy, exiftool, mftecmd to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2025-01-29 11:26:09, 2`

### Step 9: him. What was that?

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use autopsy, exiftool, mftecmd to recover or open the referenced file and inspect its metadata fields.
- Tools: autopsy, exiftool, mftecmd
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use autopsy, exiftool, mftecmd to recover or open the referenced file and inspect its metadata fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `FLAGT{THM_TECH_DATA}`

### Step 10: Which social media site did Liam search for using his web browser? Likely to avoid suspicion, thinking somebody was watching him. (Full URL)

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use autopsy, exiftool, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: autopsy, exiftool, mftecmd
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use autopsy, exiftool, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `https://www.facebook.com`

### Step 11: What is the PowerShell command Liam executed as per the plan?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use autopsy, exiftool, mftecmd with the extracted filter/query `Answer: Get-WmiObject -Class Win32_Share | Select-Object Name, Path` and inspect the matching evidence.
- Tools: autopsy, exiftool, mftecmd
- Filters or commands:
  - `Answer: Get-WmiObject -Class Win32_Share | Select-Object Name, Path`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use autopsy, exiftool, mftecmd with the extracted filter/query `Answer: Get-WmiObject -Class Win32_Share | Select-Object Name, Path` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Get-WmiObject -Class Win32_Share | Select-Object Name, Path`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
