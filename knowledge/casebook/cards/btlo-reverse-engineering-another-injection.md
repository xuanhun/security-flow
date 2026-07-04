# Reverse Engineering - Another Injection

## Case Metadata

- Category: `Malware Analysis`
- Platform: `BTLO`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/btlo_reverse_engineering_another_injection.pdf`

## Why This Case Matters

Use this case as a Malware Analysis reference for pe-malware challenges.

## Input Signals

- Artifacts: pe-malware
- Tools: cyberchef, detect-it-easy, floss, ida, strings
- Techniques: malware-static, reverse-engineering, stego-extraction

## First-Principles Route

- Classify the artifact and packer/runtime before deep reversing.
- Extract strings, imports, capabilities, configuration, embedded URLs, hashes, and persistence behavior.
- Correlate static indicators with sandbox or process-monitor evidence when available.

## Solve Thinking

### Step 1: What is the language the program is written?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, strings
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 2: What is the build id?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, strings
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `9ah0QEvz1OTFcq`

### Step 3: What is the dependency package the sample uses for invoking windows APIs

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, strings
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Therefore, the answer is github.com/TheTitanrain/w32`

### Step 4: What is the victim process?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, strings
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `notepad.exe`

### Step 5: What is the process invoked from the shellcode?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, strings
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `powershell.exe`

### Step 6: What is the name of the created file?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, strings
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `change.ps1`

### Step 7: What is the name of the actual tool executed?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, strings
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `change the EventLog audit policy (T1562.002).`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
