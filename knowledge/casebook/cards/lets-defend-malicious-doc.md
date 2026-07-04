# Malicious Doc

## Case Metadata

- Category: `Malware Analysis`
- Platform: `LetsDefend`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/lets_defend_malicious_doc.pdf`

## Why This Case Matters

Use this case as a Malware Analysis reference for artifact-driven challenges.

## Input Signals

- Artifacts: not detected
- Tools: virustotal
- Techniques: cti-enrichment

## First-Principles Route

- Classify the artifact and packer/runtime before deep reversing.
- Extract strings, imports, capabilities, configuration, embedded URLs, hashes, and persistence behavior.
- Correlate static indicators with sandbox or process-monitor evidence when available.

## Solve Thinking

### Step 1: What type of exploit is running as a result of the relevant file running on the victim machine?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `rtf.exploit`

### Step 2: What is the relevant Exploit CVE code obtained as a result of the analysis?

- Route type: `virustotal-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `cve-2017-11882`

### Step 3: What is the name of the malicious software downloaded from the internet as a result of the file running?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `jan2.exe`

### Step 4: What is the IP address and port information it communicates with?

- Route type: `virustotal-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `185.36.74.48:80`

### Step 5: What is the exe name it drops to disk after it runs?

- Route type: `virustotal-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `aro.exe`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
