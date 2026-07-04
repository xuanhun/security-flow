# Sysinternals

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_sysinternals_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, registry challenges.

## Input Signals

- Artifacts: disk-image, registry
- Tools: autopsy, virustotal
- Techniques: browser-forensics, cti-enrichment, dns-analysis, registry-forensics, timeline-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What was the malicious executable file name that the user downloaded?

- Route type: `autopsy-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use autopsy, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: autopsy, virustotal
- Reasoning chain:
  - Recognize the goal as autopsy-driven evidence lookup.
  - Use autopsy, virustotal to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 2: When was the last time the malicious executable file was modified? 12-hour format

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use autopsy, virustotal to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: autopsy, virustotal
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use autopsy, virustotal to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `directory:`

### Step 3: Where --csv . indicates that I want the output to be saved in the current directory and -f is the file path to the SYSTEM hive. We can now import this csv into Excel or something like Timeline

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use autopsy, virustotal to align timestamps and identify the event that satisfies the question.
- Tools: autopsy, virustotal
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use autopsy, virustotal to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `PM.`

### Step 4: What is the SHA1 hash value of the malware?

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use autopsy, virustotal to recover or open the referenced file and inspect its metadata fields.
- Tools: autopsy, virustotal
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use autopsy, virustotal to recover or open the referenced file and inspect its metadata fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `file:`

### Step 5: What is the malware’s family?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: autopsy, virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 6: What is the first mapped domain's Fully Qualified Domain Name (FQDN)?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use autopsy, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: autopsy, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use autopsy, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 7: The mapped domain is linked to an IP address. What is that IP address?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use autopsy, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: autopsy, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use autopsy, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.15.10`

### Step 8: What is the name of the executable dropped by the first-stage executable?

- Route type: `autopsy-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use autopsy, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: autopsy, virustotal
- Reasoning chain:
  - Recognize the goal as autopsy-driven evidence lookup.
  - Use autopsy, virustotal to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `sysinternals.exe`

### Step 9: What is the name of the service installed by the 2nd stage executable?

- Route type: `autopsy-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use autopsy, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: autopsy, virustotal
- Reasoning chain:
  - Recognize the goal as autopsy-driven evidence lookup.
  - Use autopsy, virustotal to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `start the VMwareIOHelperService.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
