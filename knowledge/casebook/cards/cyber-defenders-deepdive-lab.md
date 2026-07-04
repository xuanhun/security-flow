# DeepDive Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Hard`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_deepdive_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for memory challenges.

## Input Signals

- Artifacts: memory
- Tools: john, virustotal, volatility
- Techniques: cti-enrichment, http-analysis, memory-forensics, password-cracking, service-enumeration

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What profile should you use for this memory sample?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Win7SP1x64_24000`

### Step 2: What is the KDBG virtual address of the memory sample?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0xf80002bef120`

### Step 3: There is a malicious process running, but it's hidden. What's its name?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Use virustotal, volatility with the extracted filter/query `detect hidden processes by comparing what PsActiveProcessHead contains with what is` and inspect the matching evidence.
- Tools: virustotal, volatility
- Filters or commands:
  - `detect hidden processes by comparing what PsActiveProcessHead contains with what is`
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Use virustotal, volatility with the extracted filter/query `detect hidden processes by comparing what PsActiveProcessHead contains with what is` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `vds_ps.exe`

### Step 4: What is the physical offset of the malicious process?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0x000000007d336950`

### Step 5: What is the full path (including executable name) of the hidden executable?

- Route type: `john-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use john, virustotal, volatility to collect the smallest evidence slice that answers the goal.
- Tools: john, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as john-driven evidence lookup.
  - Use john, virustotal, volatility to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\john\AppData\Local\api-ms-win-service-management-l2-1-0\vds_ps.exe`

### Step 6: Which malware is this?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Use virustotal, volatility with the extracted filter/query `Vad that contains the largest injected PE? Answer in hex, like: 0xABC` and inspect the matching evidence.
- Tools: virustotal, volatility
- Filters or commands:
  - `Vad that contains the largest injected PE? Answer in hex, like: 0xABC`
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Use virustotal, volatility with the extracted filter/query `Vad that contains the largest injected PE? Answer in hex, like: 0xABC` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Emotet`

### Step 7: What is the pooltag of the malicious process in ascii? (HINT: use volshell)

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `R0ot`

### Step 8: What is the physical address of the hidden executable's pooltag? (HINT: use volshell)

- Route type: `virustotal-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal, volatility to collect the smallest evidence slice that answers the goal.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal, volatility to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0x7D3368F4`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
