# Crownjewel-2

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `HackTheBox`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/crownjewewl2.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for ids, windows-events challenges.

## Input Signals

- Artifacts: ids, windows-events
- Tools: evtxecmd, ida
- Techniques: dns-analysis, http-analysis, reverse-engineering, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: When utilizing ntdsutil.exe to dump NTDS on disk, it simultaneously employs the Microsoft

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use evtxecmd to align timestamps and identify the event that satisfies the question.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use evtxecmd to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 2: the running state, signifying the possible initiation of the NTDS dumping process?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use evtxecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use evtxecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2024-05-15 05:39:55`

### Step 3: Identify the full path of the dumped NTDS file.

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `C:\Windows\Temp\dump_tmp\Active Directory\ntds.dit`

### Step 4: When was the database dump created on the disk?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use evtxecmd to align timestamps and identify the event that satisfies the question.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use evtxecmd to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2024-05-15 05:39:56`

### Step 5: When was the newly dumped database considered complete and ready for use?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2024-05-15 05:39:58`

### Step 6: source provides database status data like creation and detachment?

- Route type: `evtxecmd-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use evtxecmd to collect the smallest evidence slice that answers the goal.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as evtxecmd-driven evidence lookup.
  - Use evtxecmd to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ESENT`

### Step 7: When ntdsutil.exe is used to dump the database, it enumerates certain user groups to validate the privileges of the account being used. Which two groups are enumerated by the

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use evtxecmd to enumerate processes, network sockets, injected regions, and command lines.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use evtxecmd to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ntdsutil.exe`

### Step 8: When a security-enabled local group membership is enumerated, event ID 4799 is logged. We

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use evtxecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use evtxecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Administrators, Backup Operators`

### Step 9: find the Time when the user logon session started.

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use evtxecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use evtxecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2024-05-15 05:36:31`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
