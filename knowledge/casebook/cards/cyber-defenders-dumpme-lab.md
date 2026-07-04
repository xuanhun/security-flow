# DumpMe Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_dumpme_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, memory challenges.

## Input Signals

- Artifacts: disk-image, memory
- Tools: virustotal, volatility
- Techniques: cti-enrichment, malware-dynamic, memory-forensics, registry-forensics, service-enumeration, timeline-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the SHA1 hash of Triage-Memory.mem (memory dump)?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c95e8cc8c946f95a109ea8e47a6800de10a27abd`

### Step 2: What volatility profile is the most appropriate for this machine? (ex: Win10x86_14393)

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Win7SP1x64`

### Step 3: What was the process ID of notepad.exe?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `3032`

### Step 4: What was the IP address of the machine at the time the RAM dump was created?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use virustotal to align timestamps and identify the event that satisfies the question.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use virustotal to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `10.0.0.101`

### Step 5: Based on the answer regarding the infected PID, can you determine the IP of the attacker?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `10.0.0.106`

### Step 6: How many processes are associated with VCRUNTIME140.dll?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use virustotal to align timestamps and identify the event that satisfies the question.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use virustotal to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5`

### Step 7: After dumping the infected process, what is its md5 hash?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `UWkpjFjDzM.exe`

### Step 8: Where -p specifies the PID and -D specifies the dump directory. We can then utilise the md5sum utility to generate the MD5 hash for the dumped process:

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `690ea20bc3bdfb328e23005d9a80c290`

### Step 9: What is the LM hash of Bob's account?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `aad3b435b51404eeaad3b435b51404ee`

### Step 10: What memory protection constants does the VAD node at 0xfffffa800577ba10 have?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `PAGE_READONLY`

### Step 11: What memory protection did the VAD starting at 0x00000000033c0000 and ending at 0x00000000033dffff have?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `PAGE_NOACCESS`

### Step 12: An application was run at 2019-03-07 23:06:58 UTC. What is the name of the program?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use virustotal, volatility to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use virustotal, volatility to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Skype.exe`

### Step 13: What was written in notepad.exe at the time when the memory dump was captured?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use virustotal to align timestamps and identify the event that satisfies the question.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use virustotal to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `flag<REDBULL_IS_LIFE>`

### Step 14: What is the short name of the file at file record 59045?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `EMPLOY~1.XLS`

### Step 15: This box was exploited and is running meterpreter. What was the infected PID?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3496`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
