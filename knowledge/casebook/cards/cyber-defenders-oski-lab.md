# Oski Lab

## Case Metadata

- Category: `Cyber Threat Intelligence (CTI)`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_oski_lab.pdf`

## Why This Case Matters

Use this case as a Cyber Threat Intelligence (CTI) reference for email, registry challenges.

## Input Signals

- Artifacts: email, registry
- Tools: virustotal
- Techniques: cti-enrichment, dns-analysis, http-analysis, malware-dynamic

## First-Principles Route

- Extract observables first, then enrich with threat intelligence sources.
- Map hashes, domains, malware names, TTPs, and infrastructure to campaigns or actors only when evidence supports it.

## Solve Thinking

### Step 1: the time of malware creation?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2022-09-28 17:40`

### Step 2: primary objectives. What is the first library that the malware requests post-infection?

- Route type: `virustotal-driven evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `sqlite3.dll`

### Step 3: its base64-encoded string?

- Route type: `virustotal-driven evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `5329514621441247975720749009`

### Step 4: user’s password.

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `T1555`

### Step 5: does the malware target for the deletion of all DLL files?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\ProgramData\`

### Step 6: user's data, how many seconds does it take for the malware to self-delete?

- Route type: `virustotal-driven evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `5`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
