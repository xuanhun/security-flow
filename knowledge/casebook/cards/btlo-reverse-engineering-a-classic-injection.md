# Reverse Engineering - A Classic Injection

## Case Metadata

- Category: `Malware Analysis`
- Platform: `BTLO`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/btlo_reverse_engineering_a_classic_injection.pdf`

## Why This Case Matters

Use this case as a Malware Analysis reference for pe-malware challenges.

## Input Signals

- Artifacts: pe-malware
- Tools: cutter, cyberchef, detect-it-easy, ida, pestudio, strings
- Techniques: malware-dynamic, malware-static, reverse-engineering, stego-extraction

## First-Principles Route

- Classify the artifact and packer/runtime before deep reversing.
- Extract strings, imports, capabilities, configuration, embedded URLs, hashes, and persistence behavior.
- Correlate static indicators with sandbox or process-monitor evidence when available.

## Solve Thinking

### Step 1: What is the name of the compiler used to generate the EXE?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, pestudio to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, pestudio
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, pestudio to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 2: The malware, when executed, sleeps for some time. What is the sleep time in minutes?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cutter, cyberchef, detect-it-easy, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cutter, cyberchef, detect-it-easy, ida, pestudio, strings
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cutter, cyberchef, detect-it-easy, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `function executes.`

### Step 3: After the sleep time, it prompts for user password, what is the correct password?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, pestudio to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, pestudio
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, pestudio to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 4: What is the size of the shellcode?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, pestudio to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, pestudio
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, pestudio to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `CreateRemoteThread.`

### Step 5: What is the name of the victim process?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, pestudio to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, pestudio
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, pestudio to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `nslookup.exe`

### Step 6: What is the file created by the sample

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, pestudio to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, pestudio
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, pestudio to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `powershell.exe`

### Step 7: What is the message in the created file

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, pestudio to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, pestudio
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, pestudio to locate strings, comparisons, and control-flow decisions relevant to the input.
  - The proof is the code path, comparison, constant, or decoded data that explains the answer.
- Evidence rule: The proof is the code path, comparison, constant, or decoded data that explains the answer.

### Step 8: What is the program that the shellcode used to create and write this file?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, pestudio to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, pestudio
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, pestudio to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `powershell.exe`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
