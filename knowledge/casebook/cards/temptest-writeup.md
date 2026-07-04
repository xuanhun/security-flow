# Tempest

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/temptest_writeup.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for email, pcap, registry challenges.

## Input Signals

- Artifacts: email, pcap, registry, windows-events
- Tools: cyberchef, john, strings, virustotal, wireshark
- Techniques: cti-enrichment, dns-analysis, email-header-analysis, http-analysis, malware-static, network-forensics, password-cracking, privilege-escalation, stego-extraction, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the SHA256 hash of the capture.pcapng file?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 2: What is the SHA256 hash of the sysmon.evtx file?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use cyberchef, virustotal, wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use cyberchef, virustotal, wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Repeat the process used in the previous question:`

### Step 3: What is the SHA256 hash of the windows.evtx file?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use cyberchef, virustotal, wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use cyberchef, virustotal, wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Repeat the process used in the previous question:`

### Step 4: name of the document?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use cyberchef, virustotal, wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use cyberchef, virustotal, wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Viewer or in Timeline Explorer like I have:`

### Step 5: What is the name of the compromised user and machine?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, virustotal, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, virustotal, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `benimaru-TEMPEST.`

### Step 6: What is the PID of the Microsoft Word process that opened the malicious document?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `the Word process that opened the malicious document:`

### Step 7: the previous question?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use cyberchef, virustotal, wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use cyberchef, virustotal, wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - The proof is the event record and correlated timestamp/user/process fields.
- Evidence rule: The proof is the event record and correlated timestamp/user/process fields.

### Step 8: which shows all DNS Query logs. To filter the results even further, you can search for

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `167.71.199.191`

### Step 9: What is the base64 encoded string in the malicious payload executed by the document?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use cyberchef, virustotal, wireshark with the extracted filter/query `C47IHJtIHVwZGF0ZS56aXA7Cg==` and inspect the matching evidence.
- Tools: cyberchef, virustotal, wireshark
- Filters or commands:
  - `C47IHJtIHVwZGF0ZS56aXA7Cg==`
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use cyberchef, virustotal, wireshark with the extracted filter/query `C47IHJtIHVwZGF0ZS56aXA7Cg==` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `C47IHJtIHVwZGF0ZS56aXA7Cg==`

### Step 10: What is the CVE number of the exploit used by the attacker to achieve a remote code execution?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use cyberchef, john, virustotal, wireshark to enumerate processes, network sockets, injected regions, and command lines.
- Tools: cyberchef, john, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use cyberchef, john, virustotal, wireshark to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `CVE-2022-30190`

### Step 11: path of the payload?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use cyberchef, virustotal, wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use cyberchef, virustotal, wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\benimaru\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

### Step 12: command upon a successful login of the compromised user?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use cyberchef, virustotal, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use cyberchef, virustotal, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `explorer.exe`

### Step 13: domain and port used by the attacker?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `first.exe`

### Step 14: What is the URL of the malicious payload embedded in the document?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Therefore the answer is http[:]//phishteam.xyz/02dcf07/index.html.`

### Step 15: What is the encoding used by the attacker on the c2 connection?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, virustotal, wireshark with the extracted filter/query `The malicious c2 binary sends a payload using a parameter that contains the executed` and inspect the matching evidence.
- Tools: cyberchef, virustotal, wireshark
- Filters or commands:
  - `The malicious c2 binary sends a payload using a parameter that contains the executed`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, virustotal, wireshark with the extracted filter/query `The malicious c2 binary sends a payload using a parameter that contains the executed` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 16: command results. What is the parameter used by the binary?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 17: What is the URL used by the binary?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Base64 encoded results.`

### Step 18: What is the HTTP method used by the binary? GET:

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The programming language used appears to be nim.`

### Step 19: the password discovered on the aforementioned file?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use cyberchef, strings, virustotal, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: cyberchef, strings, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use cyberchef, strings, virustotal, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - The proof is the authentication field or stream showing the credential value.
- Evidence rule: The proof is the authentication field or stream showing the credential value.

### Step 20: listening port that could provide a remote shell inside the machine?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `first.exe`

### Step 21: What is the SHA256 hash of the binary used by the attacker to establish the reverse socks proxy connection?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use cyberchef, virustotal, wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use cyberchef, virustotal, wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ch.exe`

### Step 22: What is the name of the tool used by the attacker based on the SHA256 hash?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use cyberchef, virustotal, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use cyberchef, virustotal, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The tool is called chisel.`

### Step 23: use to authenticate?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8524FBC0D73E711E69D60C64F1F1B7BEF35C986705880643DD4D5E17779E586D`

### Step 24: Based on the SHA256 hash of the binary, what is the name of the tool?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 25: find the name of the tool:

- Route type: `cyberchef-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, virustotal, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, virustotal, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The name of the tool is printspoofer.`

### Step 26: The tool exploits a specific privilege owned by the user . What is the name of the privilege?

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use cyberchef, virustotal, wireshark to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use cyberchef, virustotal, wireshark to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - The proof is the service enumeration result and the exact access or escalation condition.
- Evidence rule: The proof is the service enumeration result and the exact access or escalation condition.

### Step 27: What is the name of the binary?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use cyberchef, virustotal, wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use cyberchef, virustotal, wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `spf.exe`

### Step 28: The binary connects to a different port from the first c2 connection. What is the port used?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `first.exe`

### Step 29: failed in the creation attempt. What is the missing option that made the attempt fail?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use cyberchef, virustotal, wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use cyberchef, virustotal, wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - The proof is the event record and correlated timestamp/user/process fields.
- Evidence rule: The proof is the event record and correlated timestamp/user/process fields.

### Step 30: ID that indicates the account creation activity?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `creation.`

### Step 31: command used by the attacker?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use cyberchef, virustotal, wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use cyberchef, virustotal, wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `net.exe`

### Step 32: What is the event ID that indicates the addition to a sensitive local group?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `answer.`

### Step 33: administrative access. What is the command executed by the attacker to achieve this?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use cyberchef, virustotal, wireshark to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use cyberchef, virustotal, wireshark to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `sc.exe`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
