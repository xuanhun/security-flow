# Andromeda Bot Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_andromeda_bot_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for memory, registry, windows-events challenges.

## Input Signals

- Artifacts: memory, registry, windows-events
- Tools: evtxecmd, memprocfs, virustotal
- Techniques: cti-enrichment, dns-analysis, http-analysis, memory-forensics, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: analysis revealed defence evasion techniques by disabling Windows Defender protections and

- Route type: `evtxecmd-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use evtxecmd, memprocfs, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: evtxecmd, memprocfs, virustotal
- Reasoning chain:
  - Recognize the goal as evtxecmd-driven evidence lookup.
  - Use evtxecmd, memprocfs, virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `dropped payloads including an executable and multiple DLLs.`

### Step 2: your investigation. What is the serial number of the inserted USB device?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, memprocfs, virustotal with the extracted filter/query `Here we can find a text file called usb_storage that contains information about connected usb` and inspect the matching evidence.
- Tools: evtxecmd, memprocfs, virustotal
- Filters or commands:
  - `Here we can find a text file called usb_storage that contains information about connected usb`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, memprocfs, virustotal with the extracted filter/query `Here we can find a text file called usb_storage that contains information about connected usb` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7095411056659025437&0`

### Step 3: which disables Windows Defender protections and executes a binary called “Trusted

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use evtxecmd, memprocfs, virustotal to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: evtxecmd, memprocfs, virustotal
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use evtxecmd, memprocfs, virustotal to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `E:\hidden\Trusted Installer.exe`

### Step 4: threat intelligence reports, what URL does the bot use to download its C&C file?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use evtxecmd, memprocfs, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: evtxecmd, memprocfs, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use evtxecmd, memprocfs, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `http://anam0rph.su/in.php`

### Step 5: dropped .exe file?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, memprocfs, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: evtxecmd, memprocfs, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, memprocfs, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7FE00CC4EA8429629AC0AC610DB51993`

### Step 6: of the first DLL dropped by the malware sample?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd, memprocfs, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd, memprocfs, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd, memprocfs, virustotal to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\Tomy\AppData\Local\Temp\Gozekeneka.dll`

### Step 7: APT group reactivated this malware for use in its campaigns?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use evtxecmd, memprocfs, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: evtxecmd, memprocfs, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use evtxecmd, memprocfs, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Turla`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
