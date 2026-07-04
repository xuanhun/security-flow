# Brave

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_brave_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for memory challenges.

## Input Signals

- Artifacts: memory
- Tools: john, volatility
- Techniques: browser-forensics, dns-analysis, http-analysis, memory-forensics, password-cracking

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What time was the RAM image acquired according to the suspect system? (YYYY-MM-DD HH:MM:SS)

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use volatility to align timestamps and identify the event that satisfies the question.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use volatility to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The image was taken at: 2021-04-30 17:52:19`

### Step 2: What is the SHA256 hash value of the RAM image?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 3: What is the process ID of “brave.exe”?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `brave.exe`

### Step 4: How many established network connections were there at the time of acquisition? (number)

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 5: What FQDN does Chrome have an established network connection with?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use volatility to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use volatility to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `185.70.41.130`

### Step 6: What is the MD5 hash value of process executable for PID 6988?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - The proof is the locally extracted indicator plus the enrichment source result.
- Evidence rule: The proof is the locally extracted indicator plus the enrichment source result.

### Step 7: What is the word starting at offset 0x45BE876 with a length of 6 bytes?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use volatility to enumerate processes, network sockets, injected regions, and command lines.
  - The proof is the memory plugin output tied to process/socket/module evidence.
- Evidence rule: The proof is the memory plugin output tied to process/socket/module evidence.

### Step 8: What is the creation date and time of the parent process of “powershell.exe”? (YYYY-MM- DD HH:MM:SS)

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use volatility to align timestamps and identify the event that satisfies the question.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use volatility to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `powershell.exe`

### Step 9: How long did the suspect use Brave browser? (hh:mm:ss)

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use volatility to align timestamps and identify the event that satisfies the question.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use volatility to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The answer is 04:01:54.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
