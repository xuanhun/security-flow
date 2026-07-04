# Memory Analysis

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `LetsDefend`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/lets_defend_memory_analysis.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for ids, memory challenges.

## Input Signals

- Artifacts: ids, memory
- Tools: hashcat, john, virustotal, volatility
- Techniques: cti-enrichment, dns-analysis, memory-forensics, password-cracking, privilege-escalation

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What was the date and time when Memory from the compromised endpoint was acquired?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use virustotal, volatility to align timestamps and identify the event that satisfies the question.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use virustotal, volatility to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2022-07-26 18:16:32`

### Step 2: What was the suspicious process running on the system? (Format: name.extension)

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `explorer.exe`

### Step 3: Which User Account was compromised? Format (DomainName/USERNAME)

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, volatility to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, volatility to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `display a processes environment variables:`

### Step 4: What is the compromised user password?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use hashcat, john, virustotal, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: hashcat, john, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use hashcat, john, virustotal, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `evil.exe`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
