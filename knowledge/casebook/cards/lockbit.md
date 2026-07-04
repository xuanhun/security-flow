# Lockbit

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `LetsDefend`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/lockbit.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for memory, registry challenges.

## Input Signals

- Artifacts: memory, registry
- Tools: virustotal, volatility
- Techniques: cti-enrichment, http-analysis, memory-forensics, privilege-escalation

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the name of the ransomware family responsible for the attack?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Its clearly LockBit.`

### Step 2: What file extension is appended to the encrypted files by the ransomware?

- Route type: `virustotal-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal, volatility to collect the smallest evidence slice that answers the goal.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal, volatility to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 3: What is the TLSH (Trend Micro Locality Sensitive Hash) of the ransomware?

- Route type: `tls handshake inspection`
- Why: TLS questions usually require filtering the specific handshake and reading the requested field directly.
- Probe: Use virustotal, volatility to filter the relevant TLS handshake and inspect session, random, key, or certificate fields.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as tls handshake inspection.
  - Use virustotal, volatility to filter the relevant TLS handshake and inspect session, random, key, or certificate fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `answer.`

### Step 4: Which MITRE ATT&CK technique ID was used by the ransomware to perform privilege escalation?

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use virustotal, volatility to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use virustotal, volatility to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - The proof is the service enumeration result and the exact access or escalation condition.
- Evidence rule: The proof is the service enumeration result and the exact access or escalation condition.

### Step 5: What is the SHA256 hash of the ransom note dropped by the malware?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `67c6784a5296658ac4d633f4e8c0914ecc783b1cf2f6431818c4e2f3cdcce91f`

### Step 6: persistence on the infected system?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use virustotal, volatility to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use virustotal, volatility to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `section in the behaviour tab on VirusTotal.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
