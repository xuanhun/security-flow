# Injection Series Part 3

## Case Metadata

- Category: `Malware Analysis`
- Platform: `BTLO`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/btlo_injection_series_part_3.pdf`

## Why This Case Matters

Use this case as a Malware Analysis reference for artifact-driven challenges.

## Input Signals

- Artifacts: not detected
- Tools: cutter, cyberchef, ida
- Techniques: http-analysis, reverse-engineering

## First-Principles Route

- Classify the artifact and packer/runtime before deep reversing.
- Extract strings, imports, capabilities, configuration, embedded URLs, hashes, and persistence behavior.
- Correlate static indicators with sandbox or process-monitor evidence when available.

## Solve Thinking

### Step 1: How many arguments does the sample take?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cutter, cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cutter, cyberchef, ida
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cutter, cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `one argument:`

### Step 2: Again, what is the size of the shellcode?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cutter, cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cutter, cyberchef, ida
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cutter, cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `for the shellcode:`

### Step 3: In VirtualAlloc what does the flAllocationType value represents?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cutter, cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cutter, cyberchef, ida
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cutter, cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `value represents MEM_COMMIT:`

### Step 4: What is the argument required by the sample to run the shellcode?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cutter, cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cutter, cyberchef, ida
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cutter, cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 5: What is the payload in Metasploit that would have been used to generate the shellcode?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cutter, cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cutter, cyberchef, ida
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cutter, cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - The proof is the code path, comparison, constant, or decoded data that explains the answer.
- Evidence rule: The proof is the code path, comparison, constant, or decoded data that explains the answer.

### Step 6: What is the API used to create a wait object?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cutter, cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cutter, cyberchef, ida
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cutter, cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `wait object”, therefore the answer is CreateThreadpoolWait.`

### Step 7: What is the library function used to copy shellcode between memory blocks?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cutter, cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cutter, cyberchef, ida
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cutter, cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 8: What argument to the sample invokes powershell process?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cutter, cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cutter, cyberchef, ida
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cutter, cyberchef, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `PowerShell, security, and system.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
