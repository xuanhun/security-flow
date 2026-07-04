# Trooper

## Case Metadata

- Category: `Cyber Threat Intelligence (CTI)`
- Platform: `TryHackMe`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/trooper_writuep.pdf`

## Why This Case Matters

Use this case as a Cyber Threat Intelligence (CTI) reference for email challenges.

## Input Signals

- Artifacts: email
- Tools: not detected
- Techniques: cti-enrichment

## First-Principles Route

- Extract observables first, then enrich with threat intelligence sources.
- Map hashes, domains, malware names, TTPs, and infrastructure to campaigns or actors only when evidence supports it.

## Solve Thinking

### Step 1: identify the Tactics, Techniques, and Procedures (TTPs) being used by the Threat group and

- Route type: `evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 2: What kind of phishing campaign does APT X use as part of their TTPs?

- Route type: `evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 3: What is the name of the malware used by APT X?

- Route type: `evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 4: What is the malware’s STIX ID?

- Route type: `evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ID:`

### Step 5: With the use of a USB, what technique did APT X use for initial access?

- Route type: `evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 6: What is the identity of APT X?

- Route type: `evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 7: On OpenCTI, how many Attack Pattern techniques are associated with the APT?

- Route type: `evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 8: What is the name of the tool linked to the APT?

- Route type: `evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 9: Load up the Navigator. What is the sub-technique used by the APT under Valid Accounts?

- Route type: `evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Accounts:`

### Step 10: Under what Tactics does the technique above fall?

- Route type: `evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 11: What technique is the group known for using under the tactic Collection?

- Route type: `evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
