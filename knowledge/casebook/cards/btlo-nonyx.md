# Nonyx

## Case Metadata

- Category: `Malware Analysis`
- Platform: `BTLO`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/btlo_nonyx.pdf`

## Why This Case Matters

Use this case as a Malware Analysis reference for memory challenges.

## Input Signals

- Artifacts: memory
- Tools: strings, volatility
- Techniques: malware-static, memory-forensics, stego-extraction

## First-Principles Route

- Classify the artifact and packer/runtime before deep reversing.
- Extract strings, imports, capabilities, configuration, embedded URLs, hashes, and persistence behavior.
- Correlate static indicators with sandbox or process-monitor evidence when available.

## Solve Thinking

### Step 1: Apply the case-level route for Nonyx

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use strings, volatility with the extracted filter/query `Q1) Which process most likely contains injected code, providing its name, PID, and` and inspect the matching evidence.
- Tools: strings, volatility
- Filters or commands:
  - `Q1) Which process most likely contains injected code, providing its name, PID, and`
  - `and filtering out legitimate SSDT entries using egrep -v '(ntoskrnl|win32k)'? (Format: XX,`
- Reasoning chain:
  - Recognize the case as http evidence extraction.
  - Use strings, volatility with the extracted filter/query `Q1) Which process most likely contains injected code, providing its name, PID, and` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `12b0407d9298e1a7154f5196db4a716052ca3acc70becf2d5489efd35f6c6ec8`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
