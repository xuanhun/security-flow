# Beta Gamer Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_beta_gamer_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, email, ids challenges.

## Input Signals

- Artifacts: disk-image, email, ids, registry, windows-events
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd
- Techniques: browser-forensics, http-analysis, privilege-escalation, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: investigation into the leaked information led us to a developer. We have created a forensic

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd to align timestamps and identify the event that satisfies the question.
- Tools: db-browser-sqlite, ftk-imager, mftecmd
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use db-browser-sqlite, ftk-imager, mftecmd to align timestamps and identify the event that satisfies the question.
  - The proof is the timestamped artifact that matches the question constraint.
- Evidence rule: The proof is the timestamped artifact that matches the question constraint.

### Step 2: Initial Access

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite, ftk-imager, mftecmd
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite, ftk-imager, mftecmd to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 3: the attacker's email address?

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd with the extracted filter/query `I started off by exporting the INBOX file, as it contains all the raw emails for this user. After` and inspect the matching evidence.
- Tools: db-browser-sqlite, ftk-imager, mftecmd
- Filters or commands:
  - `I started off by exporting the INBOX file, as it contains all the raw emails for this user. After`
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite, ftk-imager, mftecmd with the extracted filter/query `I started off by exporting the INBOX file, as it contains all the raw emails for this user. After` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `gamerhelp@mail2tor.com`

### Step 4: specify the URL from which the binary was downloaded?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd with the extracted filter/query `Within this directory is a History file, which contains the users Chrome browsing history. To` and inspect the matching evidence.
- Tools: db-browser-sqlite, ftk-imager, mftecmd
- Filters or commands:
  - `Within this directory is a History file, which contains the users Chrome browsing history. To`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, ftk-imager, mftecmd with the extracted filter/query `Within this directory is a History file, which contains the users Chrome browsing history. To` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `https://0xguts.github.io/GTAVI_Installer_x64.exe`

### Step 5: name and path of the directory created by the attacker?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\neo-gamer\AppData\GTAVI_Game_Temp`

### Step 6: provide the IP address and port used for this connection?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: db-browser-sqlite, ftk-imager, mftecmd
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use db-browser-sqlite, ftk-imager, mftecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3.147.237.39:3388`

### Step 7: scheduled task. Could you identify which tool was responsible for this action?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: db-browser-sqlite, ftk-imager, mftecmd
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use db-browser-sqlite, ftk-imager, mftecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `SharPersist.exe`

### Step 8: When a user account is created on a Windows system, Event ID 4720 is generated in the

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `MS-Defender-Admin`

### Step 9: specify the path of the script that was modified for this action?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: db-browser-sqlite, ftk-imager, mftecmd
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use db-browser-sqlite, ftk-imager, mftecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `C:\Users\neo-gamer\Documents\Dir_hash.ps1`

### Step 10: escalate privileges further?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd with the extracted filter/query `YARA is a legitimate tool, but in this case, it being executed by a regular user is suspicious (this` and inspect the matching evidence.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd
- Filters or commands:
  - `YARA is a legitimate tool, but in this case, it being executed by a regular user is suspicious (this`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd with the extracted filter/query `YARA is a legitimate tool, but in this case, it being executed by a regular user is suspicious (this` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `yara64.exe`

### Step 11: provide the specific date and time when this action occurred?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: db-browser-sqlite, ftk-imager, mftecmd
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use db-browser-sqlite, ftk-imager, mftecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2024-12-13 16:05:46`

### Step 12: When someone successfully logs in to a Windows host, an event is generated with event ID

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, ftk-imager, mftecmd
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `18.116.26.227`

### Step 13: What files were downloaded onto the system by the newly created user account?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd to align timestamps and identify the event that satisfies the question.
- Tools: db-browser-sqlite, ftk-imager, mftecmd
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use db-browser-sqlite, ftk-imager, mftecmd to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `7z2409-x64.exe, python-3.13.1-amd64.exe`

### Step 14: the directories that were archived?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, ftk-imager, mftecmd
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Thunderbird, Defender Temp Files`

### Step 15: Could you provide the name of this archive file?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, ftk-imager, mftecmd
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `dump.7z`

### Step 16: number used for this data exfiltration?

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite, ftk-imager, mftecmd
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite, ftk-imager, mftecmd to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3.147.237.39:8888`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
