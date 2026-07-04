# Akira Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefedners`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_akira_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for memory, registry, windows-events challenges.

## Input Signals

- Artifacts: memory, registry, windows-events
- Tools: evtxecmd, memprocfs, radare2, strings, volatility
- Techniques: dns-analysis, http-analysis, malware-static, memory-forensics, stego-extraction, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: to which the infected machine is joined?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use evtxecmd, memprocfs, strings, volatility with the extracted filter/query `python .\vol.py -f "C:\Users\Administrator\Desktop\Start` and inspect the matching evidence.
- Tools: evtxecmd, memprocfs, strings, volatility
- Filters or commands:
  - `python .\vol.py -f "C:\Users\Administrator\Desktop\Start`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use evtxecmd, memprocfs, strings, volatility with the extracted filter/query `python .\vol.py -f "C:\Users\Administrator\Desktop\Start` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Cydef.enterprise`

### Step 2: local path of the file that was shared on the file server?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use evtxecmd, memprocfs, strings, volatility with the extracted filter/query `python .\vol.py -f "C:\Users\Administrator\Desktop\Start` and inspect the matching evidence.
- Tools: evtxecmd, memprocfs, strings, volatility
- Filters or commands:
  - `python .\vol.py -f "C:\Users\Administrator\Desktop\Start`
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use evtxecmd, memprocfs, strings, volatility with the extracted filter/query `python .\vol.py -f "C:\Users\Administrator\Desktop\Start` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `z:\Shares\data`

### Step 3: machine that attempted to connect to the file server?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, memprocfs, strings, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: evtxecmd, memprocfs, strings, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, memprocfs, strings, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.60.129`

### Step 4: perform malicious activities on the compromised FileServer?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use evtxecmd, memprocfs, strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: evtxecmd, memprocfs, strings, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use evtxecmd, memprocfs, strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - The proof is the memory plugin output tied to process/socket/module evidence.
- Evidence rule: The proof is the memory plugin output tied to process/socket/module evidence.

### Step 5: This plugin can identify processes, even hidden ones, that were present at the time of the

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use evtxecmd, memprocfs, strings, volatility with the extracted filter/query `python .\vol.py -f "C:\Users\Administrator\Desktop\Start` and inspect the matching evidence.
- Tools: evtxecmd, memprocfs, strings, volatility
- Filters or commands:
  - `python .\vol.py -f "C:\Users\Administrator\Desktop\Start`
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use evtxecmd, memprocfs, strings, volatility with the extracted filter/query `python .\vol.py -f "C:\Users\Administrator\Desktop\Start` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `PSEXESVC.exe`

### Step 6: enumeration?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, memprocfs, strings, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: evtxecmd, memprocfs, strings, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, memprocfs, strings, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `tasklist`

### Step 7: What is the name of the registry value that was added or modified under HKLM\SOFTWARE\Policies\Microsoft\Windows Defender?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use evtxecmd, memprocfs, strings, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: evtxecmd, memprocfs, strings, volatility
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use evtxecmd, memprocfs, strings, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `DisableAntiSpyware`

### Step 8: that the attacker created?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, memprocfs, strings, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: evtxecmd, memprocfs, strings, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, memprocfs, strings, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ITadmin_2`

### Step 9: communication and accessing the attacker's chat?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use evtxecmd, memprocfs, radare2, strings with the extracted filter/query `strings.exe .\memory.dmp > strings.txt` and inspect the matching evidence.
- Tools: evtxecmd, memprocfs, radare2, strings, volatility
- Filters or commands:
  - `strings.exe .\memory.dmp > strings.txt`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use evtxecmd, memprocfs, radare2, strings with the extracted filter/query `strings.exe .\memory.dmp > strings.txt` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `https://akiralkzxzq2dsrzsrvbr2xgbbu2wgsmxryd4csgfameg52n7efvr2id.onion`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
