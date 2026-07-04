# Bruteforce

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `BTLO`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/btlo_bruteforce.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for windows-events challenges.

## Input Signals

- Artifacts: windows-events
- Tools: evtxecmd
- Techniques: http-analysis, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: How many Audit Failure events are there? (Format: Count of Events)

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd with the extracted filter/query `Turns out, the evtx file only contains one event for failed logon, so let’s take a look at the` and inspect the matching evidence.
- Tools: evtxecmd
- Filters or commands:
  - `Turns out, the evtx file only contains one event for failed logon, so let’s take a look at the`
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd with the extracted filter/query `Turns out, the evtx file only contains one event for failed logon, so let’s take a look at the` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3103`

### Step 2: What is the username of the local account that is being targeted? (Format: Username)

- Route type: `evtxecmd-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use evtxecmd to collect the smallest evidence slice that answers the goal.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as evtxecmd-driven evidence lookup.
  - Use evtxecmd to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `administrator`

### Step 3: What is the failure reason related to the Audit Failure logs? (Format: String)

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use evtxecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use evtxecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Unknown user name or bad password.`

### Step 4: What is the Windows Event ID associated with these logon failures? (Format: ID)

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `4625`

### Step 5: What is the source IP conducting this attack? (Format: X.X.X.X)

- Route type: `evtxecmd-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use evtxecmd to collect the smallest evidence slice that answers the goal.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as evtxecmd-driven evidence lookup.
  - Use evtxecmd to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `113.161.192.227`

### Step 6: What country is this IP address associated with? (Format: Country)

- Route type: `evtxecmd-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use evtxecmd to collect the smallest evidence slice that answers the goal.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as evtxecmd-driven evidence lookup.
  - Use evtxecmd to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Vietnam`

### Step 7: What is the range of source ports that were used by the attacker to make these login requests? (LowestPort-HighestPort - Ex: 100-541)

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use evtxecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use evtxecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `49162-65534`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
