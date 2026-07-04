# Snort Challenge live attacks

## Case Metadata

- Category: `IDS/IPS`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/snort_challenge_live_attacks.pdf`

## Why This Case Matters

Use this case as a IDS/IPS reference for ids challenges.

## Input Signals

- Artifacts: ids
- Tools: snort
- Techniques: service-enumeration

## First-Principles Route

- Start from alerts/signatures, then validate them against packet context and endpoint/network indicators.
- Tune signatures only after confirming the malicious flow and payload boundaries.

## Solve Thinking

### Step 1: What is the used protocol/port in the attack? TCP/22

- Route type: `snort-driven evidence lookup`
- Why: For IDS/IPS, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use snort to collect the smallest evidence slice that answers the goal.
- Tools: snort
- Reasoning chain:
  - Recognize the goal as snort-driven evidence lookup.
  - Use snort to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Let’s now add the following rule:`

### Step 2: What tool is highly associated with this specific port number? Metasploit is the answer.

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use snort to align timestamps and identify the event that satisfies the question.
- Tools: snort
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use snort to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `first time.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
