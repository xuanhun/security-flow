# Injection Series Part 4

## Case Metadata

- Category: `Malware Analysis`
- Platform: `BTLO`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/btlo_ijection_series_part_4.pdf`

## Why This Case Matters

Use this case as a Malware Analysis reference for web-service challenges.

## Input Signals

- Artifacts: web-service
- Tools: cyberchef, ida, nmap, strings
- Techniques: dns-analysis, malware-static, reverse-engineering, service-enumeration, stego-extraction

## First-Principles Route

- Classify the artifact and packer/runtime before deep reversing.
- Extract strings, imports, capabilities, configuration, embedded URLs, hashes, and persistence behavior.
- Correlate static indicators with sandbox or process-monitor evidence when available.

## Solve Thinking

### Step 1: What is the process that would be first spawned by the sample? And what is the API used? (Format: Format: process, APICall)

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, ida
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `notepad.exe`

### Step 2: The value 4 has been pushed as a parameter to this API, what does that

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, ida
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `CREATE_SUSPENDED:`

### Step 3: What is the domain that the malware tries to connect? (Format: domain.tld)

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, ida, strings to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, ida, strings
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, ida, strings to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `command:`

### Step 4: What is the cmdlet used to download the file and what is the path of the file stored? (Format: CMDLET, path)

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, ida
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `exp.exe`

### Step 5: Just after the file download instructions, a function from ntdll has been loaded

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, ida, nmap to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, ida, nmap
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, ida, nmap to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `NtUnmapViewOfSection`

### Step 6: What are the 2 APIs used to update the entry point and resume the thread? (Format: API, API)

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, ida
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `thread:`

### Step 7: What is the MITRE ID for this technique implemented in this sample? (Format: TXXXX.XXX)

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, ida, nmap to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, ida, nmap
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, ida, nmap to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- Resuming execution.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
