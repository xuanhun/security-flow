# Seized Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_seized_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for memory challenges.

## Input Signals

- Artifacts: memory
- Tools: strings, volatility
- Techniques: browser-forensics, http-analysis, malware-static, memory-forensics, service-enumeration, stego-extraction

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the CentOS version installed on the machine?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7.7.1908`

### Step 2: What is the PID of the suspicious process?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use strings, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use strings, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2854`

### Step 3: What are the attacker's IP address and the local port on the targeted machine?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use strings, volatility to align timestamps and identify the event that satisfies the question.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use strings, volatility to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.49.1:12345`

### Step 4: What is the first command that the attacker executed?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use strings, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use strings, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `python -c import pty; pty.spawn("/bin/bash")`

### Step 5: What is the name of the rootkit that the attacker used?

- Route type: `strings-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use strings, volatility to collect the smallest evidence slice that answers the goal.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as strings-driven evidence lookup.
  - Use strings, volatility to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `sysemptyrect`

### Step 6: The rootkit uses crc65 encryption. What is the key?

- Route type: `strings-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use strings, volatility to collect the smallest evidence slice that answers the goal.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as strings-driven evidence lookup.
  - Use strings, volatility to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `1337tibbartibbar`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
