# [HZNUCTF 2023 final]虽然他送了我玫瑰花

## Case Metadata

- Category: `Reverse`
- Platform: `HZNUCTF 2023 final`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `reverse/[HZNUCTF 2023 final]虽然他送了我玫瑰花.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/reverse/%5BHZNUCTF%202023%20final%5D%E8%99%BD%E7%84%B6%E4%BB%96%E9%80%81%E4%BA%86%E6%88%91%E7%8E%AB%E7%91%B0%E8%8A%B1.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/reverse/[HZNUCTF 2023 final]虽然他送了我玫瑰花.md`

## Why This Case Matters

Use this case as a Reverse reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: netcat
- Techniques: reverse-engineering

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Solve Thinking

### Step 1: [HZNUCTF 2023 final]虽然他送了我玫瑰花

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `---`

### Step 2: 考点

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `---`

### Step 3: 思路

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `由此可以推断出**flag{Wh4t_@_6eaut1fu1_$lower}**`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
