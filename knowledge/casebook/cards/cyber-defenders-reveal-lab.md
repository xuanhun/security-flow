# Reveal

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_reveal_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for ids, memory challenges.

## Input Signals

- Artifacts: ids, memory
- Tools: virustotal, volatility
- Techniques: cti-enrichment, http-analysis, memory-forensics, timeline-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: attack. What is the name of the malicious process?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use virustotal, volatility to align timestamps and identify the event that satisfies the question.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use virustotal, volatility to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `powershell.exe`

### Step 2: malware uses to execute the second-stage payload?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `powershell.exe`

### Step 3: stage payload using a Windows utility to run the malicious file?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `3435.dll`

### Step 4: process runs under?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `powershell.exe`

### Step 5: forensics challenges involving Volatility and I really enjoy them. Hopefully this writeup proves

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `useful for someone out there.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
