# SOC Alpha 3

## Case Metadata

- Category: `SIEM (ELK, Splunk, etc.)`
- Platform: `BTLO`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/btlo_soc_alpha_3.pdf`

## Why This Case Matters

Use this case as a SIEM (ELK, Splunk, etc.) reference for ids, registry, siem challenges.

## Input Signals

- Artifacts: ids, registry, siem, windows-events
- Tools: elk, virustotal
- Techniques: cti-enrichment, dns-analysis, http-analysis, siem-query, windows-event-analysis

## First-Principles Route

- Translate the question into searchable fields such as host, user, process, index, sourcetype, URI, IP, hash, or event code.
- Run broad time-bounded searches first, then narrow by event type, field value, and correlation chain.
- Keep the exact query shape and the evidence field that proves each answer.

## Solve Thinking

### Step 1: What program is used for compression?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `C:\Program Files\WinRAR\WinRAR.exe`

### Step 2: What is the name of the compressed file?

- Route type: `elk-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: elk, virustotal
- Reasoning chain:
  - Recognize the goal as elk-driven evidence lookup.
  - Use elk, virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `gatherings.rar`

### Step 3: What is the name of the file that has been added to the registry?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use elk, virustotal to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: elk, virustotal
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use elk, virustotal to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `C:\Windows\Temp\process.exe`

### Step 4: What is the RegValue?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use elk, virustotal to enumerate processes, network sockets, injected regions, and command lines.
- Tools: elk, virustotal
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use elk, virustotal to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `WindowsProcess`

### Step 5: When Windows event logs are cleared, Event IDs 104 and 1102 are logged. Event ID 104

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2021/05/28T00:26:29`

### Step 6: value in the log?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `winevent-security, Event_System_EventID=1102`

### Step 7: What is the program used for adding the firewall rule?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `netsh.exe`

### Step 8: What is the rulename?

- Route type: `elk-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: elk, virustotal
- Reasoning chain:
  - Recognize the goal as elk-driven evidence lookup.
  - Use elk, virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Zoop TCP Port 80`

### Step 9: What is the program used for downloading the suspicious file?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use elk, virustotal to enumerate processes, network sockets, injected regions, and command lines.
- Tools: elk, virustotal
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use elk, virustotal to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `bitsadmin.exe`

### Step 10: What is the URL from which the file is downloaded?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://pastebin.com/raw/AGdtReXJ0`

### Step 11: Hunt for the darkside ransomware sample and what is the MD5 hash of the sample?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `9d418ecc0f3bf45029263b0944236884`

### Step 12: There is an event to delete the malware from the system. Can you find the full command?

- Route type: `elk-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: elk, virustotal
- Reasoning chain:
  - Recognize the goal as elk-driven evidence lookup.
  - Use elk, virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `C:\Windows\system32\cmd.exe" /C DEL /F /Q`

### Step 13: What is the username of the mining server used?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use elk, virustotal to enumerate processes, network sockets, injected regions, and command lines.
- Tools: elk, virustotal
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use elk, virustotal to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `42PkwcWLCjheUAaXy2h6CndY9DoKvv4pQ6QogCxgnFFF268ueYNb2FXiLCgQeds64jAytuaXzFT`

### Step 14: What is the version of the miner?

- Route type: `elk-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: elk, virustotal
- Reasoning chain:
  - Recognize the goal as elk-driven evidence lookup.
  - Use elk, virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `6.12.1`

### Step 15: What is the full command attempted to stop the windows defender?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use elk, virustotal to align timestamps and identify the event that satisfies the question.
- Tools: elk, virustotal
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use elk, virustotal to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `C:\Windows\system32\net.exe STOP WinDefend`

### Step 16: are the services in alphabetical order?

- Route type: `elk-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: elk, virustotal
- Reasoning chain:
  - Recognize the goal as elk-driven evidence lookup.
  - Use elk, virustotal to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `spooler, WbioSrvc, wlidsvc`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
