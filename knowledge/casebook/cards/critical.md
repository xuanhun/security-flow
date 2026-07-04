# Critical

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `TryHackMe`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/critical.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, memory challenges.

## Input Signals

- Artifacts: disk-image, memory
- Tools: strings, volatility
- Techniques: dns-analysis, http-analysis, malware-static, memory-forensics, stego-extraction, timeline-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: Environment

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use strings, volatility to align timestamps and identify the event that satisfies the question.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use strings, volatility to align timestamps and identify the event that satisfies the question.
  - The proof is the timestamped artifact that matches the question constraint.
- Evidence rule: The proof is the timestamped artifact that matches the question constraint.

### Step 2: Gathering target information

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `windows.info plugin:`

### Step 3: Is the architecture of the machine x64 (64 bit)?

- Route type: `strings-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use strings, volatility to collect the smallest evidence slice that answers the goal.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as strings-driven evidence lookup.
  - Use strings, volatility to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Y:`

### Step 4: Searching for suspicious activity

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `their child or parent processes, etc):`

### Step 5: connection on port 80?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - The proof is the memory plugin output tied to process/socket/module evidence.
- Evidence rule: The proof is the memory plugin output tied to process/socket/module evidence.

### Step 6: through port 80?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `msedge.exe`

### Step 7: What is the time stamp for the process with the truncated name critical_updat?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use strings, volatility to align timestamps and identify the event that satisfies the question.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use strings, volatility to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 8: Finding interesting data

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use strings, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use strings, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `updater.exe`

### Step 9: Analysing the “windows.filescan” output, what is the full path and name for critical_updat?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use strings, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use strings, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `critical_update.exe`

### Step 10: determine the server used by the attacker?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use strings, volatility to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use strings, volatility to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `updater.exe`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
