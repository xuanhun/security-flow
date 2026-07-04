# DarkCrystal Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_darkcrystal_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for memory, windows-events challenges.

## Input Signals

- Artifacts: memory, windows-events
- Tools: evtxecmd, strings, volatility
- Techniques: http-analysis, malware-static, memory-forensics, stego-extraction, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: and initiates the chain of malicious activities?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, volatility to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, volatility
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, volatility to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `services.exe`

### Step 2: identified in the previous question?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, volatility to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, volatility
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, volatility to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1313.exe`

### Step 3: launched as a result of their execution?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `providerBrowser.exe`

### Step 4: using a LOLBin?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use volatility with the extracted filter/query `python .\vol.py -f .\memory.dmp windows.pstree > pstree_out.csv` and inspect the matching evidence.
- Tools: volatility
- Filters or commands:
  - `python .\vol.py -f .\memory.dmp windows.pstree > pstree_out.csv`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use volatility with the extracted filter/query `python .\vol.py -f .\memory.dmp windows.pstree > pstree_out.csv` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `SandeLLoCHECKER_Installer.msi`

### Step 5: of the parent process linked to the legitimate LOLBin mentioned in the previous question?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use volatility with the extracted filter/query `python .\vol.py -f .\memory.dmp windows.netscan` and inspect the matching evidence.
- Tools: volatility
- Filters or commands:
  - `python .\vol.py -f .\memory.dmp windows.netscan`
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use volatility with the extracted filter/query `python .\vol.py -f .\memory.dmp windows.netscan` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2964`

### Step 6: two local ports the malware uses to connect to its C&C servers?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `49948, 49949`

### Step 7: exfiltrate data. What is the name of the script retrieved in this case?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use strings, volatility with the extracted filter/query `python .\vol.py -f .\memory.dmp windows.memmap --pid 10956 --dump` and inspect the matching evidence.
- Tools: strings, volatility
- Filters or commands:
  - `python .\vol.py -f .\memory.dmp windows.memmap --pid 10956 --dump`
  - `strings .\pid.10956.dmp | Select-String "77.222.47.117"`
  - `strings .\pid.10956.dmp | Select-String "VideoPipeProcessorDefault"`
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use strings, volatility with the extracted filter/query `python .\vol.py -f .\memory.dmp windows.memmap --pid 10956 --dump` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `VideoPipeProcessorDefault.php`

### Step 8: this malware sample?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use volatility to align timestamps and identify the event that satisfies the question.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use volatility to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Trojan:Win32/DCRat.MQ!MTB`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
