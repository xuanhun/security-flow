# NetX-Support Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_netx_support_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, registry, windows-events challenges.

## Input Signals

- Artifacts: disk-image, registry, windows-events
- Tools: cyberchef, db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, pecmd, registry-explorer, strings
- Techniques: browser-forensics, dns-analysis, http-analysis, malware-static, registry-forensics, service-enumeration, stego-extraction, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the URL from which the malicious ZIP file was downloaded?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd with the extracted filter/query `Within this directory is a "History” file, which contains the users Edge browsing history. To export` and inspect the matching evidence.
- Tools: cyberchef, db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer
- Filters or commands:
  - `Within this directory is a "History” file, which contains the users Edge browsing history. To export`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd with the extracted filter/query `Within this directory is a "History” file, which contains the users Edge browsing history. To export` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `https://limewire.com/d/S785F#bBSxZAx5HH`

### Step 2: When did the employee download the malicious ZIP file?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to align timestamps and identify the event that satisfies the question.
- Tools: cyberchef, db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2025-05-05 08:51:35`

### Step 3: triggered the attack chain. What is the name of this JavaScript file?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, db-browser-sqlite, evtxecmd, ftk-imager to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, db-browser-sqlite, evtxecmd, ftk-imager to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5645_M.js`

### Step 4: tool with the OriginalFileName client32.exe?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\Alpha\AppData\Roaming\IRomvWG3\presentationhost.exe`

### Step 5: identified in the previous question?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2025-05-05 13:10`

### Step 6: earlier. What is the name of that registry value?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `SoftwareUpdater`

### Step 7: attacker created to maintain system access?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `WDAGUtilityAccount2`

### Step 8: privileged groups. Which groups were they?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Administrators, Remote Desktop Users`

### Step 9: server on a schedule and automatically restart it if it stops?

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to recover or open the referenced file and inspect its metadata fields.
- Tools: cyberchef, db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer, strings
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to recover or open the referenced file and inspect its metadata fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\ProgramData\sshd\sshd.exe -f C:\ProgramData\sshd\config\sshd_config`

### Step 10: remote IP address were used to establish the reverse SSH tunnel?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `root@185.206.146.129`

### Step 11: What is the IP address of the target host to which the attacker attempted lateral movement via RDP?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Within the Microsoft-Windows-TerminalServices-RDPClient%4Operational.evtx logs you can`

### Step 12: find Event ID 1102 (Connection Establish). This log is created when an RDP connection has

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `192.168.159.201`

### Step 13: activity, what is the full UNC path to the shared folder?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, db-browser-sqlite, ftk-imager, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `\\ALPH7-W3S-H3R3\Users\Alpha\Downloads\Important\Secrets.txt`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
