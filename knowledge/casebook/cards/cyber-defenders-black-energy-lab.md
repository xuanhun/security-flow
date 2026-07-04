# BlackEnergy Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_black_energy_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for memory challenges.

## Input Signals

- Artifacts: memory
- Tools: strings, virustotal, volatility
- Techniques: cti-enrichment, http-analysis, malware-static, memory-forensics, stego-extraction, timeline-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: How many processes were running when the image was acquired?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `There were 19 processes running.`

### Step 2: What is the process ID of cmd.exe?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `cmd.exe`

### Step 3: What is the name of the most suspicious process?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `rootkit.exe`

### Step 4: Which process shows the highest likelihood of code injection?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use strings, virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use strings, virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `svchost.exe`

### Step 5: What is the name of the injected dll file loaded from the recent process?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `svchost.exe`

### Step 6: When looking at the output, msxml3r.dll stands out as very suspicious:

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `msxml3r.dll`

### Step 7: What is the base address of the injected dll?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal, volatility with the extracted filter/query `volatility, I highly recommend completing this room.` and inspect the matching evidence.
- Tools: virustotal, volatility
- Filters or commands:
  - `volatility, I highly recommend completing this room.`
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal, volatility with the extracted filter/query `volatility, I highly recommend completing this room.` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `volatility, I highly recommend completing this room.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
