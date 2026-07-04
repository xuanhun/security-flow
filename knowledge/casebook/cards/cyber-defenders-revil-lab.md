# REvil Lab

## Case Metadata

- Category: `SIEM (ELK, Splunk, etc.)`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_revil_lab.pdf`

## Why This Case Matters

Use this case as a SIEM (ELK, Splunk, etc.) reference for siem, windows-events challenges.

## Input Signals

- Artifacts: siem, windows-events
- Tools: cyberchef, elk, splunk, virustotal
- Techniques: cti-enrichment, dns-analysis, http-analysis, siem-query, windows-event-analysis

## First-Principles Route

- Translate the question into searchable fields such as host, user, process, index, sourcetype, URI, IP, hash, or event code.
- Run broad time-bounded searches first, then narrow by event type, field value, and correlation chain.
- Keep the exact query shape and the evidence field that proves each answer.

## Solve Thinking

### Step 1: origin. Where can we find the ransomware's executable file?

- Route type: `elk-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk to collect the smallest evidence slice that answers the goal.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as elk-driven evidence lookup.
  - Use elk to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `C:\Users\Administrator\Downloads\facebook assistant.exe`

### Step 2: command that was used for this purpose?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use cyberchef, elk, virustotal with the extracted filter/query `event.provider : "Microsoft-Windows-Sysmon" AND event.code : 1 AND` and inspect the matching evidence.
- Tools: cyberchef, elk, virustotal
- Filters or commands:
  - `event.provider : "Microsoft-Windows-Sysmon" AND event.code : 1 AND`
  - `Answer: Get-WmiObject Win32_Shadowcopy | ForEach-Object {$_.Delete();}`
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use cyberchef, elk, virustotal with the extracted filter/query `event.provider : "Microsoft-Windows-Sysmon" AND event.code : 1 AND` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Get-WmiObject Win32_Shadowcopy | ForEach-Object {$_.Delete();}`

### Step 3: ransomware author's onion domain?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `aplebzu47wgazapdqks6vrcv6zcnjppkbxbr6wketf56nf6aq2nmyoyd.onion`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
