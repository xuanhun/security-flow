# IcedID 2 Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_icedid_2_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for memory, registry challenges.

## Input Signals

- Artifacts: memory, registry
- Tools: memprocfs, virustotal, volatility
- Techniques: browser-forensics, cti-enrichment, http-analysis, memory-forensics, timeline-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: determine how it executed, and understand its progression through the system.

- Route type: `memprocfs-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use memprocfs, virustotal, volatility to collect the smallest evidence slice that answers the goal.
- Tools: memprocfs, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memprocfs-driven evidence lookup.
  - Use memprocfs, virustotal, volatility to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 2: you specify the filename of the .iso file that was used to deliver the malicious payload?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use memprocfs, virustotal, volatility with the extracted filter/query `python .\vol.py -f .\memory.dmp filescan > filescan_out.txt` and inspect the matching evidence.
- Tools: memprocfs, virustotal, volatility
- Filters or commands:
  - `python .\vol.py -f .\memory.dmp filescan > filescan_out.txt`
  - `python .\vol.py -f .\memory.dmp filescan | Select-String -Pattern "\.iso$"`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use memprocfs, virustotal, volatility with the extracted filter/query `python .\vol.py -f .\memory.dmp filescan > filescan_out.txt` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `docs_invoice_173.iso`

### Step 3: the link used to view the malicious malware?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use memprocfs, virustotal, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: memprocfs, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use memprocfs, virustotal, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `https://drive.google.com/file/d/1WsffqUcaojZchwIOcVTr-E__j1971Qh0/view`

### Step 4: located on the workstation?

- Route type: `layer-2 endpoint identification`
- Why: MAC/OUI questions should start from the relevant endpoint conversation, then verify the address in Ethernet fields.
- Probe: Use memprocfs, virustotal, volatility to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
- Tools: memprocfs, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as layer-2 endpoint identification.
  - Use memprocfs, virustotal, volatility to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\admin\Downloads`

### Step 5: the intrusion. What is the malicious command that triggered this malicious behaviour?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use memprocfs, virustotal, volatility with the extracted filter/query `python .\vol.py -f .\memory.dmp windows.cmdline > cmdline_out.txt` and inspect the matching evidence.
- Tools: memprocfs, virustotal, volatility
- Filters or commands:
  - `python .\vol.py -f .\memory.dmp windows.cmdline > cmdline_out.txt`
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use memprocfs, virustotal, volatility with the extracted filter/query `python .\vol.py -f .\memory.dmp windows.cmdline > cmdline_out.txt` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `rundll32.exe dar.dll,DllRegisterServer`

### Step 6: SHA256 hash of the DLL associated with the last execution of the malware?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Use memprocfs, virustotal, volatility with the extracted filter/query `python .\vol.py -f .\memory.dmp dlllist --pid 3312` and inspect the matching evidence.
- Tools: memprocfs, virustotal, volatility
- Filters or commands:
  - `python .\vol.py -f .\memory.dmp dlllist --pid 3312`
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Use memprocfs, virustotal, volatility with the extracted filter/query `python .\vol.py -f .\memory.dmp dlllist --pid 3312` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `D90B4EE7E8ADF2D7AA5FCFF2C017C1FA4E99143FDCD9CD3D1BD7827AE59D9A05`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
