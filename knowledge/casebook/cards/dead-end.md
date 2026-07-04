# Dead End?

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `TryHackMe`
- Difficulty: `Hard`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/dead_end.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, memory, registry challenges.

## Input Signals

- Artifacts: disk-image, memory, registry
- Tools: ftk-imager, virustotal, volatility
- Techniques: cti-enrichment, memory-forensics

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: TryHackMe: Dead End?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use ftk-imager, virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: ftk-imager, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use ftk-imager, virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `recommend checking out this writeup.`

### Step 2: What binary gives the most apparent sign of suspicious activity in the given memory image?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use ftk-imager, virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: ftk-imager, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use ftk-imager, virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - The proof is the memory plugin output tied to process/socket/module evidence.
- Evidence rule: The proof is the memory plugin output tied to process/socket/module evidence.

### Step 3: When investigating a memory image, I like to start by listing all the running processes by using the pslist plugin:

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager, virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager, virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Tools\svchost.exe`

### Step 4: .txt file - what is the full path of this .txt file?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager, virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager, virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\Bobby\Documents\tmp\part2.txt`

### Step 5: What binary gives the most apparent sign of suspicious activity in the given disk image?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: ftk-imager, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Tools\windows-networking-tools-master\windows-networking-tools-`

### Step 6: What is the full registry path where the existence of the binary above is confirmed?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use ftk-imager, virustotal, volatility to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: ftk-imager, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use ftk-imager, virustotal, volatility to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Key Path`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
