# Ramnit

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_ramnit_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for memory, pe-malware challenges.

## Input Signals

- Artifacts: memory, pe-malware
- Tools: capa, virustotal, volatility
- Techniques: browser-forensics, cti-enrichment, dns-analysis, malware-static, memory-forensics, timeline-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: name of the suspicious process?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use virustotal, volatility to align timestamps and identify the event that satisfies the question.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use virustotal, volatility to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ChomeSetup.exe`

### Step 2: To eradicate the malware, what is the exact file path of the process executable?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ChromeSetup.exe`

### Step 3: communication strategy. What is the IP address it attempted to connect to?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `58.64.204.181`

### Step 4: address the malware communicated with?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: capa, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `58.64.204.181`

### Step 5: machines. What is the SHA1 hash of the malware’s executable?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use virustotal, volatility to align timestamps and identify the event that satisfies the question.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use virustotal, volatility to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `280C9D36039F9432433893DEE6126D72B9112AD2`

### Step 6: What is the compilation UTC timestamp of the malware?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, volatility to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, volatility to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 7: network. Can you provide the domain related to the malware?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, volatility to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, volatility to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
