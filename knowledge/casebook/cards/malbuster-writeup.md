# MalBuster

## Case Metadata

- Category: `Malware Analysis`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/malbuster_writeup.pdf`

## Why This Case Matters

Use this case as a Malware Analysis reference for pe-malware challenges.

## Input Signals

- Artifacts: pe-malware
- Tools: capa, detect-it-easy, floss, pestudio, strings, virustotal
- Techniques: cti-enrichment, malware-dynamic, malware-static, stego-extraction

## First-Principles Route

- Classify the artifact and packer/runtime before deep reversing.
- Extract strings, imports, capabilities, configuration, embedded URLs, hashes, and persistence behavior.
- Correlate static indicators with sandbox or process-monitor evidence when available.

## Solve Thinking

### Step 1: Based on the ARCHITECTURE of the binary, is malbuster_1 a 32-bit or a 64-bit application?

- Route type: `capa-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use capa, detect-it-easy, floss, pestudio to collect the smallest evidence slice that answers the goal.
- Tools: capa, detect-it-easy, floss, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as capa-driven evidence lookup.
  - Use capa, detect-it-easy, floss, pestudio to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 2: What is the MD5 hash of malbuster_1?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: capa, detect-it-easy, floss, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 3: Using the hash, what is the number of detections of malbuster_1 in VirusT otal?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: capa, detect-it-easy, floss, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `mscoree.dll`

### Step 4: Based on the VS_VERSION_INFO header , what is the original name of malbuster_2?

- Route type: `capa-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use capa, detect-it-easy, floss, pestudio to collect the smallest evidence slice that answers the goal.
- Tools: capa, detect-it-easy, floss, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as capa-driven evidence lookup.
  - Use capa, detect-it-easy, floss, pestudio to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 5: Using the hash of malbuster_3, what is its malware signature based on abuse.ch?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: capa, detect-it-easy, floss, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `9da8a5a0b5957db6112e927b607a8fd062b870f2132c4ae3442eb63235f789e1`

### Step 6: Using the hash of malbuster_4, what is its malware signature based on abuse.ch?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: capa, detect-it-easy, floss, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - The proof is the locally extracted indicator plus the enrichment source result.
- Evidence rule: The proof is the locally extracted indicator plus the enrichment source result.

### Step 7: What is the message found in the DOS_STUB of malbuster_4?

- Route type: `capa-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use capa, detect-it-easy, floss, pestudio to collect the smallest evidence slice that answers the goal.
- Tools: capa, detect-it-easy, floss, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as capa-driven evidence lookup.
  - Use capa, detect-it-easy, floss, pestudio to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `shell32.dll`

### Step 8: Using capa, how man anti-VM instructions were identified in malbuster_1?

- Route type: `capa-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use capa, detect-it-easy, floss, pestudio to collect the smallest evidence slice that answers the goal.
- Tools: capa, detect-it-easy, floss, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as capa-driven evidence lookup.
  - Use capa, detect-it-easy, floss, pestudio to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The answer is 3.`

### Step 9: Using capa, which binary can log keystrokes?

- Route type: `capa-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use capa, detect-it-easy, floss, pestudio to collect the smallest evidence slice that answers the goal.
- Tools: capa, detect-it-easy, floss, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as capa-driven evidence lookup.
  - Use capa, detect-it-easy, floss, pestudio to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `keystrokes as seen here:`

### Step 10: Using capa, what is the MITRE ID of the discovery technique used by malbuster_4?

- Route type: `capa-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use capa, detect-it-easy, floss, pestudio to collect the smallest evidence slice that answers the goal.
- Tools: capa, detect-it-easy, floss, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as capa-driven evidence lookup.
  - Use capa, detect-it-easy, floss, pestudio to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The technique is T1083.`

### Step 11: Which binary contains the string GodMode?

- Route type: `capa-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use capa, detect-it-easy, floss, pestudio to collect the smallest evidence slice that answers the goal.
- Tools: capa, detect-it-easy, floss, pestudio, strings, virustotal
- Reasoning chain:
  - Recognize the goal as capa-driven evidence lookup.
  - Use capa, detect-it-easy, floss, pestudio to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 12: Which binary contains the string Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)?

- Route type: `capa-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use capa, detect-it-easy, floss, pestudio to collect the smallest evidence slice that answers the goal.
- Tools: capa, detect-it-easy, floss, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as capa-driven evidence lookup.
  - Use capa, detect-it-easy, floss, pestudio to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
