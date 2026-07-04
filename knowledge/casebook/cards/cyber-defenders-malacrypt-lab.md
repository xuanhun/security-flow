# MalaCrypt Lab

## Case Metadata

- Category: `Malware Analysis`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_malacrypt_lab.pdf`

## Why This Case Matters

Use this case as a Malware Analysis reference for pe-malware, registry challenges.

## Input Signals

- Artifacts: pe-malware, registry
- Tools: capa, cutter, cyberchef, floss, ida, pestudio, strings, virustotal
- Techniques: cti-enrichment, dns-analysis, http-analysis, malware-dynamic, malware-static, reverse-engineering, stego-extraction

## First-Principles Route

- Classify the artifact and packer/runtime before deep reversing.
- Extract strings, imports, capabilities, configuration, embedded URLs, hashes, and persistence behavior.
- Correlate static indicators with sandbox or process-monitor evidence when available.

## Solve Thinking

### Step 1: being used. What architecture is this binary built for?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use capa, cutter, cyberchef, floss to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: capa, cutter, cyberchef, floss, pestudio, strings, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use capa, cutter, cyberchef, floss to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `x64`

### Step 2: purpose. What is the original name of the executable?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use capa, cutter, cyberchef, floss to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: capa, cutter, cyberchef, floss, pestudio, strings, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use capa, cutter, cyberchef, floss to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `DefaultViewer.exe`

### Step 3: to manipulate the Windows Registry?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use capa, cutter, cyberchef, floss to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: capa, cutter, cyberchef, floss, pestudio, strings, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use capa, cutter, cyberchef, floss to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ADVAPI32.dll`

### Step 4: messaging app discovered in the basic static analysis?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use capa, cutter, cyberchef, floss with the extracted filter/query `floss <binary_to_analyse>` and inspect the matching evidence.
- Tools: capa, cutter, cyberchef, floss, pestudio, strings, virustotal
- Filters or commands:
  - `floss <binary_to_analyse>`
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use capa, cutter, cyberchef, floss with the extracted filter/query `floss <binary_to_analyse>` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `WeChat`

### Step 5: destroy previously generated encryption keys?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use capa, cutter, cyberchef, floss to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: capa, cutter, cyberchef, floss, pestudio, strings, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use capa, cutter, cyberchef, floss to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `CryptDestroyKey`

### Step 6: to Hong Kong?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use capa, cutter, cyberchef, floss with the extracted filter/query `strings .\malware.exe > strings.txt` and inspect the matching evidence.
- Tools: capa, cutter, cyberchef, floss, pestudio, strings, virustotal
- Filters or commands:
  - `strings .\malware.exe > strings.txt`
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use capa, cutter, cyberchef, floss with the extracted filter/query `strings .\malware.exe > strings.txt` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `154.82.85.12`

### Step 7: activities, What message is displayed on the screen when the binary is executed?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use capa, cutter, cyberchef, floss to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: capa, cutter, cyberchef, floss, pestudio, strings, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use capa, cutter, cyberchef, floss to locate strings, comparisons, and control-flow decisions relevant to the input.
  - The proof is the code path, comparison, constant, or decoded data that explains the answer.
- Evidence rule: The proof is the code path, comparison, constant, or decoded data that explains the answer.

### Step 8: When executing this binary, we can immediately see a popup that displays “Error”:

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use capa, cutter, cyberchef, floss to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: capa, cutter, cyberchef, floss, pestudio, strings, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use capa, cutter, cyberchef, floss to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Error`

### Step 9: What is the name of the first DLL file that is loaded after the binary is executed?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use capa, cutter, cyberchef, floss to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: capa, cutter, cyberchef, floss, pestudio, strings, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use capa, cutter, cyberchef, floss to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ntdll.dll`

### Step 10: call made from the function that is called from the main function?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use capa, cutter, cyberchef, floss to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: capa, cutter, cyberchef, floss, pestudio, strings, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use capa, cutter, cyberchef, floss to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `GetEnvironmentVariableA`

### Step 11: the attacker's intent. What is the name of the company embedded in the binary?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use capa, cutter, cyberchef, floss to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: capa, cutter, cyberchef, floss, pestudio, strings, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use capa, cutter, cyberchef, floss to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Zeon Corporation`

### Step 12: VirtualAlloc as identified in the Capa rules related to this technique?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use capa, cutter, cyberchef, floss with the extracted filter/query `Capa is a tool developed by Mandiant that detects capabilities in executable files. To run Capa` and inspect the matching evidence.
- Tools: capa, cutter, cyberchef, floss, ida, pestudio, strings, virustotal
- Filters or commands:
  - `Capa is a tool developed by Mandiant that detects capabilities in executable files. To run Capa`
  - `capa -vv malware.exe`
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use capa, cutter, cyberchef, floss with the extracted filter/query `Capa is a tool developed by Mandiant that detects capabilities in executable files. To run Capa` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0x140004A31`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
