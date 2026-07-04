# XMRig Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_xmrig_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, linux-logs, pe-malware challenges.

## Input Signals

- Artifacts: disk-image, linux-logs, pe-malware
- Tools: capa, strings, virustotal
- Techniques: browser-forensics, cti-enrichment, http-analysis, malware-static, privilege-escalation, service-enumeration, stego-extraction

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: root user over SSH. Once in the environment, the threat actor created a new user, escalated

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 2: newly created user?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use virustotal to align timestamps and identify the event that satisfies the question.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use virustotal to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `sudo usermod -aG sudo noah`

### Step 3: command the attacker used to erase evidence from the system?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use virustotal to align timestamps and identify the event that satisfies the question.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use virustotal to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `sudo rm -f /var/log/auth.log`

### Step 4: tasks to ensure the miner would run continuously?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0 * * * * /tmp/backup.elf >/dev/null 2>&1`

### Step 5: attacker with mining capabilities?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `d25208063842ebf39e092d55e033f9e2`

### Step 6: is the original name of the miner?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `xmr_linux_amd64 (3)`

### Step 7: attacker's server where the malicious miner was hosted?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use capa, strings, virustotal with the extracted filter/query `grep -r "backup.elf"` and inspect the matching evidence.
- Tools: capa, strings, virustotal
- Filters or commands:
  - `grep -r "backup.elf"`
  - `Wget and curl are commands commonly used to retrieve files from external hosts, therefore,`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use capa, strings, virustotal with the extracted filter/query `grep -r "backup.elf"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `/Tools/backup/backup.elf`

### Step 8: requiring repeated permission?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use strings, virustotal with the extracted filter/query `grep -r "/etc/sudoers"` and inspect the matching evidence.
- Tools: strings, virustotal
- Filters or commands:
  - `grep -r "/etc/sudoers"`
  - `strings recup_dir.22/f4632512.elf | grep sudoers`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use strings, virustotal with the extracted filter/query `grep -r "/etc/sudoers"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `echo 'Defaults !tty_tickets' >> /etc/sudoers`

### Step 9: the machine the attacker used to perform lateral movement to this Linux box?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use strings, virustotal with the extracted filter/query `grep -r "Accepted password"` and inspect the matching evidence.
- Tools: strings, virustotal
- Filters or commands:
  - `grep -r "Accepted password"`
  - `grep -r "authentication failure"`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use strings, virustotal with the extracted filter/query `grep -r "Accepted password"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.19.147`

### Step 10: difficult to analyze. Which bash command did they use that left this trace?

- Route type: `virustotal-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `exit`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
