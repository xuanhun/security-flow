# CrownJewel1

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `HackTheBox`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/crownjewel1.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, ids, registry challenges.

## Input Signals

- Artifacts: disk-image, ids, registry, windows-events
- Tools: evtxecmd, ida, mftecmd
- Techniques: dns-analysis, http-analysis, malware-dynamic, reverse-engineering, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: extract sensitive files like NTDS.dit to bypass security mechanisms. Identify the time when

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use evtxecmd, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: evtxecmd, mftecmd
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use evtxecmd, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2024-05-14 03:42:16`

### Step 2: When a volume shadow snapshot is created, the Volume shadow copy service validates

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use mftecmd to align timestamps and identify the event that satisfies the question.
- Tools: mftecmd
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use mftecmd to align timestamps and identify the event that satisfies the question.
  - The proof is the timestamped artifact that matches the question constraint.
- Evidence rule: The proof is the timestamped artifact that matches the question constraint.

### Step 3: When the Volume Shadow Copy Service (VSS) creates a snapshot, it performs security

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, mftecmd to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, mftecmd
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use ida, mftecmd to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Administrators, Backup Operators, DC01$`

### Step 4: Identify the Process ID (in Decimal) of the volume shadow copy service process.

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use mftecmd to enumerate processes, network sockets, injected regions, and command lines.
- Tools: mftecmd
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use mftecmd to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `4496`

### Step 5: Find the assigned Volume ID/GUID value to the Shadow copy snapshot when it was mounted.

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use mftecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: mftecmd
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use mftecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `{06c4a997-cca8-11ed-a90f-000c295644f9}`

### Step 6: Identify the full path of the dumped NTDS database on disk.

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use mftecmd to recover or open the referenced file and inspect its metadata fields.
- Tools: mftecmd
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use mftecmd to recover or open the referenced file and inspect its metadata fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\Administrator\Documents\backup_sync_Dc\Ntds.dit`

### Step 7: When was newly dumped ntds.dit created on disk?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use mftecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: mftecmd
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use mftecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2024-05-14 03:44:22`

### Step 8: dumped and what is its file size in bytes?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use mftecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: mftecmd
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use mftecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `SYSTEM, 17563648`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
