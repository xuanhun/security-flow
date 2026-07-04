# QBot Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_qbot_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for email, ids, memory challenges.

## Input Signals

- Artifacts: email, ids, memory, office-document
- Tools: strings, virustotal, volatility
- Techniques: browser-forensics, cti-enrichment, http-analysis, maldoc-analysis, malware-static, memory-forensics, stego-extraction, timeline-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: forensics skills. Those of you who enjoy memory forensics, especially Volatility, should give this

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `a go.`

### Step 2: server. Can you specify the first IP address the malware attempted to communicate with?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use strings, virustotal, volatility to extract macros, streams, embedded URLs, and decoded script content.
- Tools: strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use strings, virustotal, volatility to extract macros, streams, embedded URLs, and decoded script content.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `94.140.112.73`

### Step 3: address did the malware attempt to communicate with again?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: strings, virustotal, volatility
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `45.147.230.104`

### Step 4: name of the process that initiated the malware?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `EXCEL.EXE`

### Step 5: Can you provide its file name?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Payment.xls`

### Step 6: What is the SHA256 hash of the malware?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use virustotal, volatility to align timestamps and identify the event that satisfies the question.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use virustotal, volatility to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3cef2e4a0138eeebb94be0bffefcb55074157e6f7d774c1bbf8ab9d43fdbf6a4`

### Step 7: provide the UTC creation time of the malware file?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use virustotal, volatility to align timestamps and identify the event that satisfies the question.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use virustotal, volatility to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2015-06-05 18:17`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
