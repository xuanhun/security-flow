# Amadey Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_amadey_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for ids, memory challenges.

## Input Signals

- Artifacts: ids, memory
- Tools: strings, volatility
- Techniques: http-analysis, malware-static, memory-forensics, stego-extraction

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: triggered this malicious behavior?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use volatility to align timestamps and identify the event that satisfies the question.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use volatility to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `lssass.exe`

### Step 2: which is the PID of wininit.exe:

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `lssass.exe`

### Step 3: about its nature and source. Where is this process housed on the workstation?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\0XSH3R~1\AppData\Local\Temp\925e7e99c5\lssass.exe`

### Step 4: modules. How many distinct files is it trying to bring onto the compromised workstation?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use strings, volatility to align timestamps and identify the event that satisfies the question.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use strings, volatility to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2`

### Step 5: process is initiated by the malware to execute these files?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `rundll32.exe`

### Step 6: ensuring its consistent presence?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `\Windows\System32\Tasks\lssass.exe`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
