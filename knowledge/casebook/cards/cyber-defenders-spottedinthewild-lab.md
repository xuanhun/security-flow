# SpottedInTheWild Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Hard`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_spottedinthewild_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, pe-malware, registry challenges.

## Input Signals

- Artifacts: disk-image, pe-malware, registry, windows-events
- Tools: capa, cyberchef, evtxecmd, ftk-imager, mftecmd, pecmd, strings, virustotal
- Techniques: cti-enrichment, http-analysis, malware-static, registry-forensics, stego-extraction, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: entry point for the attack. Which application was used to download the malicious file?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use cyberchef, evtxecmd, ftk-imager, mftecmd with the extracted filter/query `After exploring this rar archive using FTK Imager, I can see that it contains a folder called SANS` and inspect the matching evidence.
- Tools: cyberchef, evtxecmd, ftk-imager, mftecmd, pecmd, strings
- Filters or commands:
  - `After exploring this rar archive using FTK Imager, I can see that it contains a folder called SANS`
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use cyberchef, evtxecmd, ftk-imager, mftecmd with the extracted filter/query `After exploring this rar archive using FTK Imager, I can see that it contains a folder called SANS` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Telegram`

### Step 2: suspicious file was first downloaded?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use cyberchef, evtxecmd, mftecmd, pecmd to align timestamps and identify the event that satisfies the question.
- Tools: cyberchef, evtxecmd, mftecmd, pecmd, strings
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use cyberchef, evtxecmd, mftecmd, pecmd to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 3: which acts as a detailed metadata repository for that object.

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use cyberchef, evtxecmd, mftecmd, pecmd to recover or open the referenced file and inspect its metadata fields.
- Tools: cyberchef, evtxecmd, mftecmd, pecmd, strings
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use cyberchef, evtxecmd, mftecmd, pecmd to recover or open the referenced file and inspect its metadata fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2024-02-03 07:33:20`

### Step 4: identifier of the vulnerability used in this attack?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, evtxecmd, mftecmd, pecmd to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, evtxecmd, mftecmd, pecmd, strings
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, evtxecmd, mftecmd, pecmd to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `CVE-2023-38831`

### Step 5: it might be malicious. What is the name of this file?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, evtxecmd, mftecmd, pecmd to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, evtxecmd, mftecmd, pecmd, strings
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, evtxecmd, mftecmd, pecmd to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `SANS SEC401.pdf .cmd`

### Step 6: used. What is the URL used by the attacker to download the second stage of the malware?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, evtxecmd, ftk-imager, mftecmd with the extracted filter/query `strings -n 15 '.\SANS SEC401.pdf .cmd' > strings.txt` and inspect the matching evidence.
- Tools: cyberchef, evtxecmd, ftk-imager, mftecmd, pecmd, strings, virustotal
- Filters or commands:
  - `strings -n 15 '.\SANS SEC401.pdf .cmd' > strings.txt`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, evtxecmd, ftk-imager, mftecmd with the extracted filter/query `strings -n 15 '.\SANS SEC401.pdf .cmd' > strings.txt` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `http://172.18.35.10:8000/amanwhogetsnorest.jpg`

### Step 7: tamper with the event logs. What is the script name?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use cyberchef, evtxecmd, mftecmd, pecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: cyberchef, evtxecmd, mftecmd, pecmd, strings
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use cyberchef, evtxecmd, mftecmd, pecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Eventlogs.ps1`

### Step 8: the UTC timestamp for when the script that tampered with event logs was run?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use cyberchef, evtxecmd, mftecmd, pecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: cyberchef, evtxecmd, mftecmd, pecmd, strings
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use cyberchef, evtxecmd, mftecmd, pecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2024-02-03 07:38:01`

### Step 9: command used by the attacker for persistence?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: cyberchef, evtxecmd, mftecmd, pecmd, strings
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 10: analysis report. In that report, we can see that schtasks.exe was used to create a scheduled

- Route type: `cyberchef-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, evtxecmd, mftecmd, pecmd to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, evtxecmd, mftecmd, pecmd, strings
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, evtxecmd, mftecmd, pecmd to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `schtasks /create /sc minute /mo 3 /tn "whoisthebaba" /tr C:\Windows\Temp\run.bat /RL`

### Step 11: attacker's tools in preparation for data exfiltration?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, evtxecmd, mftecmd, pecmd with the extracted filter/query `If you locate this file within the mounted image, you can see that it contains a base64 encoded` and inspect the matching evidence.
- Tools: cyberchef, evtxecmd, mftecmd, pecmd, strings
- Filters or commands:
  - `If you locate this file within the mounted image, you can see that it contains a base64 encoded`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, evtxecmd, mftecmd, pecmd with the extracted filter/query `If you locate this file within the mounted image, you can see that it contains a base64 encoded` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\Administrator\AppData\Local\Temp\BL4356.txt`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
