# NintendoHunt Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Hard`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_nintendohunt_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, memory, registry challenges.

## Input Signals

- Artifacts: disk-image, memory, registry
- Tools: strings, volatility
- Techniques: http-analysis, malware-static, memory-forensics, service-enumeration, stego-extraction, timeline-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the process ID of the currently running malicious process?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use strings, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use strings, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8560`

### Step 2: What is the md5 hash hidden in the malicious process memory?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3a19697f29095bc289a96e4504679680`

### Step 3: What is the process name of the malicious process parent?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `explorer.exe`

### Step 4: What is the MAC address of this machine's default gateway?

- Route type: `layer-2 endpoint identification`
- Why: MAC/OUI questions should start from the relevant endpoint conversation, then verify the address in Ethernet fields.
- Probe: Use strings, volatility to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as layer-2 endpoint identification.
  - Use strings, volatility to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `00:50:56:fe:d8:07`

### Step 5: What is the name of the file that is hidden in the alternative data stream?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use strings, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use strings, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `yes.txt`

### Step 6: What is the full path of the browser cache created when the user visited "www.13cubed.com" ?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use strings, volatility to align timestamps and identify the event that satisfies the question.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use strings, volatility to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\CTF\AppData\Local\Packages\MICROS~1.MIC\AC\#!001\MICROS~1\Cache\AHF2CO`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
