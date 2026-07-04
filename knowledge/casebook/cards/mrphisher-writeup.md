# Mr. Phisher

## Case Metadata

- Category: `Malware Analysis`
- Platform: `TryHackMe`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/mrphisher_writeup.pdf`

## Why This Case Matters

Use this case as a Malware Analysis reference for email, office-document challenges.

## Input Signals

- Artifacts: email, office-document
- Tools: olevba
- Techniques: maldoc-analysis

## First-Principles Route

- Classify the artifact and packer/runtime before deep reversing.
- Extract strings, imports, capabilities, configuration, embedded URLs, hashes, and persistence behavior.
- Correlate static indicators with sandbox or process-monitor evidence when available.

## Solve Thinking

### Step 1: Apply the case-level route for Mr. Phisher

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use olevba with the extracted filter/query `Olevba which are great for analysing Macro enabled documents, however, in this room we aren’t` and inspect the matching evidence.
- Tools: olevba
- Filters or commands:
  - `Olevba which are great for analysing Macro enabled documents, however, in this room we aren’t`
- Reasoning chain:
  - Recognize the case as maldoc analysis.
  - Use olevba with the extracted filter/query `Olevba which are great for analysing Macro enabled documents, however, in this room we aren’t` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `performs the same operations as the VB code:`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
