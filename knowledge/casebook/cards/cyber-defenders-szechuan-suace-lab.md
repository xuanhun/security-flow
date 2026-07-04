# Szechuan Sauce Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_szechuan_suace_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, ids, memory challenges.

## Input Signals

- Artifacts: disk-image, ids, memory, pcap, registry, windows-events
- Tools: evtxecmd, ftk-imager, radare2, registry-explorer, virustotal, volatility, wireshark
- Techniques: cti-enrichment, dns-analysis, http-analysis, memory-forensics, network-forensics, registry-forensics, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What’s the Operating System version of the Server? (two words)

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use evtxecmd, ftk-imager, radare2, registry-explorer with the extracted filter/query `python .\vol.py -f citadeldc01.mem windows.registry.hivelist –dump` and inspect the matching evidence.
- Tools: evtxecmd, ftk-imager, radare2, registry-explorer, virustotal, volatility, wireshark
- Filters or commands:
  - `python .\vol.py -f citadeldc01.mem windows.registry.hivelist –dump`
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use evtxecmd, ftk-imager, radare2, registry-explorer with the extracted filter/query `python .\vol.py -f citadeldc01.mem windows.registry.hivelist –dump` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2012 R2`

### Step 2: What’s the Operating System of the Desktop? (four words separated by spaces)

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Windows 10 Enterprise Evaluation`

### Step 3: What was the IP address assigned to the domain controller?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `10.42.85.10`

### Step 4: What was the timezone of the Server?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal to align timestamps and identify the event that satisfies the question.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `UTC-6`

### Step 5: What was the initial entry vector (how did they get in)?. Provide protocol name.

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `EvtxECmd.exe`

### Step 6: What immediately stands out are successful logons from a remote host named “Kali” , likely

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `RDP`

### Step 7: What was the malicious process used by the malware? (one word)

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal with the extracted filter/query `python .\vol.py -f citadeldc01.mem windows.pstree.PsTree` and inspect the matching evidence.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Filters or commands:
  - `python .\vol.py -f citadeldc01.mem windows.pstree.PsTree`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal with the extracted filter/query `python .\vol.py -f citadeldc01.mem windows.pstree.PsTree` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `coreupdater`

### Step 8: Which process did malware migrate to after the initial compromise? (one word)

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal with the extracted filter/query `python .\vol.py -f citadeldc01.mem windows.malfind.Malfind` and inspect the matching evidence.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Filters or commands:
  - `python .\vol.py -f citadeldc01.mem windows.malfind.Malfind`
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal with the extracted filter/query `python .\vol.py -f citadeldc01.mem windows.malfind.Malfind` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `• python .\vol.py -f citadeldc01.mem windows.malfind.Malfind`

### Step 9: What immediately stands out is the MZ file header for spoolsv.exe:

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal with the extracted filter/query `python .\vol.py -f citadeldc01.mem windows.memmap --dump --pid 3724` and inspect the matching evidence.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Filters or commands:
  - `python .\vol.py -f citadeldc01.mem windows.memmap --dump --pid 3724`
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal with the extracted filter/query `python .\vol.py -f citadeldc01.mem windows.memmap --dump --pid 3724` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `spoolsv`

### Step 10: Identify the IP Address that delivered the payload.

- Route type: `evtxecmd-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Reasoning chain:
  - Recognize the goal as evtxecmd-driven evidence lookup.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `194.61.24.102`

### Step 11: What IP Address was the malware calling to?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal with the extracted filter/query `python .\vol.py -f citadeldc01.mem windows.netscan > dc01-net.txt` and inspect the matching evidence.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Filters or commands:
  - `python .\vol.py -f citadeldc01.mem windows.netscan > dc01-net.txt`
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal with the extracted filter/query `python .\vol.py -f citadeldc01.mem windows.netscan > dc01-net.txt` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `203.78.103.109`

### Step 12: Where did the malware reside on the disk?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal with the extracted filter/query `python3 vol.py -f "citadeldc01.mem" windows.filescan | grep` and inspect the matching evidence.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Filters or commands:
  - `python3 vol.py -f "citadeldc01.mem" windows.filescan | grep`
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal with the extracted filter/query `python3 vol.py -f "citadeldc01.mem" windows.filescan | grep` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Windows\System32\coreupdater.exe`

### Step 13: What's the name of the attack tool you think this malware belongs to? (one word)

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal to enumerate processes, network sockets, injected regions, and command lines.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Metasploit`

### Step 14: One of the involved malicious IP's is based in Thailand. What was the IP?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 15: Another malicious IP once resolved to klient-293.xyz . What is this IP?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal with the extracted filter/query `ip.addr==194.61.24.102` and inspect the matching evidence.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Filters or commands:
  - `ip.addr==194.61.24.102`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal with the extracted filter/query `ip.addr==194.61.24.102` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `194.61.24.102`

### Step 16: environment via RDP . What is the hostname of that system?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal with the extracted filter/query `ip.src==10.42.85.10 && rdp` and inspect the matching evidence.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Filters or commands:
  - `ip.src==10.42.85.10 && rdp`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal with the extracted filter/query `ip.src==10.42.85.10 && rdp` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `DESKTOP-SDN1RPT`

### Step 17: What was the password for "jerrysmith" account?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `!BETHEYBOO12!`

### Step 18: What was the original filename for Beth’s secrets?

- Route type: `evtxecmd-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Reasoning chain:
  - Recognize the goal as evtxecmd-driven evidence lookup.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `SECRET_beth.txt`

### Step 19: What was the content of Beth’s secret file? ( six words, spaces in between)

- Route type: `evtxecmd-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Reasoning chain:
  - Recognize the goal as evtxecmd-driven evidence lookup.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Earth beth is the real beth.`

### Step 20: persistence. What is the corresponding MITRE technique ID?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, ftk-imager, registry-explorer, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, ftk-imager, registry-explorer, virustotal, volatility, wireshark
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, ftk-imager, registry-explorer, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `T1543.003`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
