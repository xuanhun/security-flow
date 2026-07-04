# REvil Corp

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/revil_corp.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for memory challenges.

## Input Signals

- Artifacts: memory
- Tools: john, radare2, virustotal, volatility
- Techniques: browser-forensics, cti-enrichment, http-analysis, memory-forensics, password-cracking, timeline-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the compromised employee's full name?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal to enumerate processes, network sockets, injected regions, and command lines.
  - The proof is the memory plugin output tied to process/socket/module evidence.
- Evidence rule: The proof is the memory plugin output tied to process/socket/module evidence.

### Step 2: find the compromised username:

- Route type: `john-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use john, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: john, virustotal
- Reasoning chain:
  - Recognize the goal as john-driven evidence lookup.
  - Use john, virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `John Coleman`

### Step 3: What is the operating system of the compromised host?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Windows 7 Home Premium 7601 Service Pack 1`

### Step 4: What is the name of the malicious executable that the user opened?

- Route type: `radare2-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use radare2, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: radare2, virustotal
- Reasoning chain:
  - Recognize the goal as radare2-driven evidence lookup.
  - Use radare2, virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `WinRAR2021.exe`

### Step 5: What is the full URL that the user visited to download the malicious binary? (include the binary as well)

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use radare2, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: radare2, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use radare2, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `http://192.168.75.129:4748/Documents/WinRAR2021.exe`

### Step 6: What is the MD5 hash of the binary?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `890a58f200dfff23165df9e1b088e58f`

### Step 7: What is the size of the binary in kilobytes?

- Route type: `virustotal-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `164`

### Step 8: What is the extension to which the user's files got renamed?

- Route type: `virustotal-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `.t48s39la`

### Step 9: What is the number of files that got renamed and changed to that extension?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use virustotal to align timestamps and identify the event that satisfies the question.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use virustotal to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `48`

### Step 10: What is the full path to the wallpaper that got changed by an attacker, including the image name?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use john, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: john, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use john, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\John Coleman\AppData\Local\Temp\hk8.bmp`

### Step 11: What are some three names associated with the malware which infected this host? (enter the names in alphabetical order)

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `REvil,Sodin,Sodinokibi`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
