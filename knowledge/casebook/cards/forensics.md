# Forensics

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `TryHackMe`
- Difficulty: `Hard`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/forensics.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for memory, registry challenges.

## Input Signals

- Artifacts: memory, registry
- Tools: strings, virustotal, volatility
- Techniques: browser-forensics, cti-enrichment, malware-static, memory-forensics, stego-extraction

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the Operating System of this Dump file? (OS name)

- Route type: `strings-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use strings, volatility to collect the smallest evidence slice that answers the goal.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as strings-driven evidence lookup.
  - Use strings, volatility to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Windows`

### Step 2: What is the PID of SearchIndexer?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2180`

### Step 3: What is the last directory accessed by the user? (The last folder name as it is?)

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use strings, volatility to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use strings, volatility to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `deleted_files`

### Step 4: which they are? (ANSWER format: Pid1;Pid2;Pid3)

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use strings, virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use strings, virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1860;1820;2464`

### Step 5: *** .233. *** (Write full IP)

- Route type: `strings-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use strings, volatility to collect the smallest evidence slice that answers the goal.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as strings-driven evidence lookup.
  - Use strings, volatility to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `202.107.233.211`

### Step 6: What is the unique environmental variable of PID 2464?

- Route type: `strings-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use strings, volatility to collect the smallest evidence slice that answers the goal.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as strings-driven evidence lookup.
  - Use strings, volatility to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `OANOCACHE`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
