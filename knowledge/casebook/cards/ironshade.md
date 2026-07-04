# IronShade

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/ironshade.pdf`

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

### Step 1: forensics; therefore, this challenge was relatively difficult, however, with enough patience, you

- Route type: `evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `can easily complete this challenge.`

### Step 2: What is the Machine ID of the machine we are investigating?

- Route type: `evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `dc7c8ac5c09a4bbfaf3d09d399f10d96`

### Step 3: What backdoor user account was created on the server?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `microservice`

### Step 4: What is the cronjob that was set up by the attacker for persistence?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `@reboot /home/mircoservice/printer_app`

### Step 5: hidden process from the backdoor account?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use the artifact-specific tool with the extracted filter/query `sudo ps auxf | grep "home"` and inspect the matching evidence.
- Filters or commands:
  - `sudo ps auxf | grep "home"`
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use the artifact-specific tool with the extracted filter/query `sudo ps auxf | grep "home"` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `.strokes`

### Step 6: How many processes are found to be running from the backdoor account’s directory?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use the artifact-specific tool to enumerate processes, network sockets, injected regions, and command lines.
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use the artifact-specific tool to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2`

### Step 7: What is the name of the hidden file in memory from the root directory?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use the artifact-specific tool to enumerate processes, network sockets, injected regions, and command lines.
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use the artifact-specific tool to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `.systmd`

### Step 8: What suspicious services were installed on the server? Format is service a, service b in alphabetical order.

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use the artifact-specific tool to enumerate processes, network sockets, injected regions, and command lines.
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use the artifact-specific tool to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `backup.service, strokes.service`

### Step 9: Examine the logs; when was the backdoor account created on this infected system?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use the artifact-specific tool with the extracted filter/query `grep -a "mircoservice" /var/log/auth*` and inspect the matching evidence.
- Filters or commands:
  - `grep -a "mircoservice" /var/log/auth*`
  - `grep -a "ssh.*mircoservice" /var/log/auth*`
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use the artifact-specific tool with the extracted filter/query `grep -a "mircoservice" /var/log/auth*` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Aug 5 22:05:33`

### Step 10: How many failed SSH login attempts were observed on the backdoor account?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use the artifact-specific tool with the extracted filter/query `grep -a "Failed password.*mircoservice" /var/log/auth*` and inspect the matching evidence.
- Filters or commands:
  - `grep -a "Failed password.*mircoservice" /var/log/auth*`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use the artifact-specific tool with the extracted filter/query `grep -a "Failed password.*mircoservice" /var/log/auth*` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8`

### Step 11: Which malicious package was installed on the host?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool with the extracted filter/query `grep "install" /var/log/dpkg.log` and inspect the matching evidence.
- Filters or commands:
  - `grep "install" /var/log/dpkg.log`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use the artifact-specific tool with the extracted filter/query `grep "install" /var/log/dpkg.log` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `pscanner`

### Step 12: What is the secret code found in the metadata of the suspicious package?

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use the artifact-specific tool to recover or open the referenced file and inspect its metadata fields.
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use the artifact-specific tool to recover or open the referenced file and inspect its metadata fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `{_tRy_Hack_ME_}`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
