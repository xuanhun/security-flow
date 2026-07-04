# Retracted

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `TryHackMe`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/retracted.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for ids, windows-events challenges.

## Input Signals

- Artifacts: ids, windows-events
- Tools: not detected
- Techniques: windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the full path of the text file containing the “message”?

- Route type: `evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 2: What program was used to create the text file?

- Route type: `evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `notepad.exe`

### Step 3: What is the time of execution of the process that created the text file?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use the artifact-specific tool to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use the artifact-specific tool to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `notepad.exe`

### Step 4: What is the filename of this “installer”? (including the file extension)

- Route type: `evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 5: What is the download location of this installer?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use the artifact-specific tool to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use the artifact-specific tool to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `antivirus.exe`

### Step 6: The installer reached out to an IP . What is this IP?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use the artifact-specific tool to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use the artifact-specific tool to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `source IP?`

### Step 7: which is the default RDP destination port:

- Route type: `evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 8: This other person downloaded a file and ran it. When was this file run?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use the artifact-specific tool to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use the artifact-specific tool to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `antivirus.exe`

### Step 9: A note was created on the desktop telling Sophie to check her Bitcoin.

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
  - The proof is the timestamped artifact that matches the question constraint.
- Evidence rule: The proof is the timestamped artifact that matches the question constraint.

### Step 10: We arrive on the scene to investigate.

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use the artifact-specific tool to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use the artifact-specific tool to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `out to me.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
