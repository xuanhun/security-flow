# MrRobot Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_mrrobot_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, email, ids challenges.

## Input Signals

- Artifacts: disk-image, email, ids, memory, pe-malware, registry
- Tools: capa, strings, virustotal, volatility
- Techniques: browser-forensics, cti-enrichment, dns-analysis, http-analysis, malware-static, memory-forensics, service-enumeration, stego-extraction, timeline-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: Machine:Target1 What is the filename that was delivered in the email?

- Route type: `strings-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use strings, virustotal, volatility to collect the smallest evidence slice that answers the goal.
- Tools: strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as strings-driven evidence lookup.
  - Use strings, virustotal, volatility to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `AnyConnectInstaller.exe`

### Step 2: Machine:Target1 What is the name of the rat's family used by the attacker?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Use strings, virustotal, volatility with the extracted filter/query `profile=Win7SP1x86_23418 -g 0x82765be8 filescan | Select-String -` and inspect the matching evidence.
- Tools: strings, virustotal, volatility
- Filters or commands:
  - `profile=Win7SP1x86_23418 -g 0x82765be8 filescan | Select-String -`
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Use strings, virustotal, volatility with the extracted filter/query `profile=Win7SP1x86_23418 -g 0x82765be8 filescan | Select-String -` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `xtremerat`

### Step 3: of the process that is injected?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use strings, virustotal, volatility with the extracted filter/query `profile=Win7SP1x86_23418 -g 0x82765be8 malfind | Select-String -` and inspect the matching evidence.
- Tools: strings, virustotal, volatility
- Filters or commands:
  - `profile=Win7SP1x86_23418 -g 0x82765be8 malfind | Select-String -`
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use strings, virustotal, volatility with the extracted filter/query `profile=Win7SP1x86_23418 -g 0x82765be8 malfind | Select-String -` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2996`

### Step 4: runs on the system. What is the unique name the malware is using?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use strings, virustotal, volatility with the extracted filter/query `profile=Win7SP1x86_23418 -g 0x82765be8 filescan | grep -i "users"` and inspect the matching evidence.
- Tools: strings, virustotal, volatility
- Filters or commands:
  - `profile=Win7SP1x86_23418 -g 0x82765be8 filescan | grep -i "users"`
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use strings, virustotal, volatility with the extracted filter/query `profile=Win7SP1x86_23418 -g 0x82765be8 filescan | grep -i "users"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `fsociety0.dat`

### Step 5: Machine:Target1 What is the NTLM password hash for the administrator account?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use strings, virustotal, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use strings, virustotal, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `79402b7671c317877b8b954b3311fa82`

### Step 6: front desk host. How many tools did the attacker move?

- Route type: `tls handshake inspection`
- Why: TLS questions usually require filtering the specific handshake and reading the requested field directly.
- Probe: Use capa, strings, virustotal, volatility to filter the relevant TLS handshake and inspect session, random, key, or certificate fields.
- Tools: capa, strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as tls handshake inspection.
  - Use capa, strings, virustotal, volatility to filter the relevant TLS handshake and inspect session, random, key, or certificate fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3`

### Step 7: Machine:Target1 What is the password for the front desk local administrator account?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use strings, virustotal, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use strings, virustotal, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flagadmin@1234`

### Step 8: Machine:Target1 What is the std create data timestamp for the nbtscan.exe tool?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use strings, virustotal, volatility with the extracted filter/query `profile=Win7SP1x86_23418 -g 0x82765be8 mftparser | grep` and inspect the matching evidence.
- Tools: strings, virustotal, volatility
- Filters or commands:
  - `profile=Win7SP1x86_23418 -g 0x82765be8 mftparser | grep`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use strings, virustotal, volatility with the extracted filter/query `profile=Win7SP1x86_23418 -g 0x82765be8 mftparser | grep` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2015-10-09 10:45:12 UTC`

### Step 9: in a text file on a disk called nbs.txt. What is the IP address of the first machine in that file?

- Route type: `strings-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use strings, virustotal, volatility to collect the smallest evidence slice that answers the goal.
- Tools: strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as strings-driven evidence lookup.
  - Use strings, virustotal, volatility to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `10.1.1.2`

### Step 10: Machine:Target1 What is the full IP address and the port was the attacker's malware using?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use strings, virustotal, volatility with the extracted filter/query `profile=Win7SP1x86_23418 -g 0x82765be8 netscan | grep "iexplore"` and inspect the matching evidence.
- Tools: strings, virustotal, volatility
- Filters or commands:
  - `profile=Win7SP1x86_23418 -g 0x82765be8 netscan | grep "iexplore"`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use strings, virustotal, volatility with the extracted filter/query `profile=Win7SP1x86_23418 -g 0x82765be8 netscan | grep "iexplore"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `180.76.254.120:22`

### Step 11: software. What is the name of the running process?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use strings, virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use strings, virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `TeamViewer.exe`

### Step 12: IP address did they connect to?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use strings, virustotal, volatility to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use strings, virustotal, volatility to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `10.1.1.21`

### Step 13: password did they use?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use strings, virustotal, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use strings, virustotal, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123qwe!@#`

### Step 14: Machine:Target2 What was the name of the RAR file created by the attackers?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use strings, virustotal, volatility to align timestamps and identify the event that satisfies the question.
- Tools: strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use strings, virustotal, volatility to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `crownjewlez.rar`

### Step 15: Machine:Target2 How many files did the attacker add to the RAR archive?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use strings, virustotal, volatility with the extracted filter/query `we can examine the memory dump of conhost.exe (PID 3048) which contains relevant` and inspect the matching evidence.
- Tools: strings, virustotal, volatility
- Filters or commands:
  - `we can examine the memory dump of conhost.exe (PID 3048) which contains relevant`
  - `strings 3048.dmp | grep "crownjewlez.rar" -A 10 -B 10`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use strings, virustotal, volatility with the extracted filter/query `we can examine the memory dump of conhost.exe (PID 3048) which contains relevant` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3`

### Step 16: machine. What is the name of the file associated with the scheduled task?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use strings, virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use strings, virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1.bat`

### Step 17: Machine:POS What is the malware CNC's server?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use strings, virustotal, volatility with the extracted filter/query `profile=Win7SP1x86_23418 -g 0x82765be8 malfind | grep "Process:"` and inspect the matching evidence.
- Tools: strings, virustotal, volatility
- Filters or commands:
  - `profile=Win7SP1x86_23418 -g 0x82765be8 malfind | grep "Process:"`
  - `profile=Win7SP1x86_23418 -g 0x82765be8 netscan | grep "iexplore.exe"`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use strings, virustotal, volatility with the extracted filter/query `profile=Win7SP1x86_23418 -g 0x82765be8 malfind | grep "Process:"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `54.84.237.92`

### Step 18: Machine:POS What is the common name of the malware used to infect the POS system?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Use strings, virustotal, volatility with the extracted filter/query `strings "process.0x83f324d8.0x50000.dmp" | grep ".exe"` and inspect the matching evidence.
- Tools: strings, virustotal, volatility
- Filters or commands:
  - `strings "process.0x83f324d8.0x50000.dmp" | grep ".exe"`
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Use strings, virustotal, volatility with the extracted filter/query `strings "process.0x83f324d8.0x50000.dmp" | grep ".exe"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Dexter`

### Step 19: Machine:POS What is the name of the file the malware was initially launched from?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use strings, virustotal, volatility with the extracted filter/query `profile=Win7SP1x86_23418 -g 0x82765be8 filescan | grep` and inspect the matching evidence.
- Tools: strings, virustotal, volatility
- Filters or commands:
  - `profile=Win7SP1x86_23418 -g 0x82765be8 filescan | grep`
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use strings, virustotal, volatility with the extracted filter/query `profile=Win7SP1x86_23418 -g 0x82765be8 filescan | grep` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `allsafe_update.exe`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
