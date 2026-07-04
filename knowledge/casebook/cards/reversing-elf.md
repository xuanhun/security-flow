# Reversing ELF

## Case Metadata

- Category: `Reverse Engineering`
- Platform: `TryHackMe`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/reversing_elf.pdf`

## Why This Case Matters

Use this case as a Reverse Engineering reference for artifact-driven challenges.

## Input Signals

- Artifacts: not detected
- Tools: radare2, strings
- Techniques: malware-static, reverse-engineering, stego-extraction

## First-Principles Route

- Identify file type, architecture, symbols, strings, imports, and obvious validation routines.
- Work from observable input/output behavior into static control flow and comparison points.

## Solve Thinking

### Step 1: Apply the case-level route for Reversing ELF

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use radare2, strings with the extracted filter/query `Therefore, the answer/input is OfdlDSA|3tXb32~X3tX@sX`4tXtz` and inspect the matching evidence.
- Tools: radare2, strings
- Filters or commands:
  - `Therefore, the answer/input is OfdlDSA|3tXb32~X3tX@sX`4tXtz`
- Reasoning chain:
  - Recognize the case as reverse engineering.
  - Use radare2, strings with the extracted filter/query `Therefore, the answer/input is OfdlDSA|3tXb32~X3tX@sX`4tXtz` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Crackme8`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
