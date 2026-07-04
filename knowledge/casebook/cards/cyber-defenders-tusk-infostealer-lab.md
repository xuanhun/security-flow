# Tusk Infostealer Lab

## Case Metadata

- Category: `Cyber Threat Intelligence (CTI)`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_tusk_infostealer_lab.pdf`

## Why This Case Matters

Use this case as a Cyber Threat Intelligence (CTI) reference for artifact-driven challenges.

## Input Signals

- Artifacts: not detected
- Tools: virustotal
- Techniques: cti-enrichment

## First-Principles Route

- Extract observables first, then enrich with threat intelligence sources.
- Map hashes, domains, malware names, TTPs, and infrastructure to campaigns or actors only when evidence supports it.

## Solve Thinking

### Step 1: In KB, what is the size of the malicious file?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use virustotal to align timestamps and identify the event that satisfies the question.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use virustotal to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `921.36`

### Step 2: name of an ancient hunted creature?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Mammoth`

### Step 3: both macOS and Windows OS versions?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use virustotal with the extracted filter/query `The malicious executable contains a configuration file that includes base64-encoded URLs` and inspect the matching evidence.
- Tools: virustotal
- Filters or commands:
  - `The malicious executable contains a configuration file that includes base64-encoded URLs`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use virustotal with the extracted filter/query `The malicious executable contains a configuration file that includes base64-encoded URLs` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `DropBox`

### Step 4: stage payloads. What is the password for decompression found in this configuration file?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `newfile2024`

### Step 5: What is the name of the function responsible for retrieving the field archive from the configuration file?

- Route type: `virustotal-driven evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `downloadAndExtractArchive`

### Step 6: the malicious translator created by the attackers?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `yous.ai, voico.io`

### Step 7: StealC C2 servers used in the campaign?

- Route type: `virustotal-driven evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `46.8.238.240, 23.94.225.177`

### Step 8: What is the address of the Ethereum cryptocurrency wallet used in this campaign?

- Route type: `virustotal-driven evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0xaf0362e215Ff4e004F30e785e822F7E20b99723A`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
