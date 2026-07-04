# The Crime lab

## Case Metadata

- Category: `Mobile Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_the_crime_lab.pdf`

## Why This Case Matters

Use this case as a Mobile Forensics reference for apk-mobile, ids challenges.

## Input Signals

- Artifacts: apk-mobile, ids
- Tools: not detected
- Techniques: http-analysis, mobile-forensics

## First-Principles Route

- Inventory app/database artifacts, timestamps, media, account records, and package metadata.
- Extract SQLite, plist/XML/JSON, and app-specific records before guessing behavior.

## Solve Thinking

### Step 1: primarily used on his phone?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use the artifact-specific tool with the extracted filter/query `Once completed, ALEAP creates a directory that contains all the extracted information. I am` and inspect the matching evidence.
- Filters or commands:
  - `Once completed, ALEAP creates a directory that contains all the extracted information. I am`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use the artifact-specific tool with the extracted filter/query `Once completed, ALEAP creates a directory that contains all the extracted information. I am` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4f168a772350f283a1c49e78c1548d7c2c6c05106d8b9feb825fdc3466e9df3c`

### Step 2: repay now" . How much does the victim owe this person?

- Route type: `evidence lookup`
- Why: For Mobile Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `250000`

### Step 3: What is the name of the person to whom the victim owes money?

- Route type: `evidence lookup`
- Why: For Mobile Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Shady Wahab`

### Step 4: victim located at that moment?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use the artifact-specific tool to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use the artifact-specific tool to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `The Nile Ritz-Carlton`

### Step 5: extract two messages, one being a reply containing a location to meet:

- Route type: `evidence lookup`
- Why: For Mobile Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The Mob Museum`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
