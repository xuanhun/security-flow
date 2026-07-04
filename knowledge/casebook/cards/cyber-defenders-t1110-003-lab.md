# T1110-003 Lab

## Case Metadata

- Category: `SIEM (ELK, Splunk, etc.)`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_t1110_003_lab.pdf`

## Why This Case Matters

Use this case as a SIEM (ELK, Splunk, etc.) reference for email, siem challenges.

## Input Signals

- Artifacts: email, siem
- Tools: elk, splunk
- Techniques: dns-analysis, http-analysis, service-enumeration, siem-query, windows-event-analysis

## First-Principles Route

- Translate the question into searchable fields such as host, user, process, index, sourcetype, URI, IP, hash, or event code.
- Run broad time-bounded searches first, then narrow by event type, field value, and correlation chain.
- Keep the exact query shape and the evidence field that proves each answer.

## Solve Thinking

### Step 1: when brute forcing a single account with many passwords. [1]

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use elk with the extracted filter/query `SSH (22/TCP)` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `SSH (22/TCP)`
  - `FTP (21/TCP)`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use elk with the extracted filter/query `SSH (22/TCP)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `email applications, such as Office 365.[2]`

### Step 2: Who was the last logged-in user?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk with the extracted filter/query `event.code : 4624` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `event.code : 4624`
  - `event.code : 4624 AND winlog.event_data.LogonType : 2`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk with the extracted filter/query `event.code : 4624` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Administrator`

### Step 3: What is the logon type of the failed logons?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use elk with the extracted filter/query `event.code : 4625` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `event.code : 4625`
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use elk with the extracted filter/query `event.code : 4625` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3`

### Step 4: What is the protocol the attacker tried to bruteforce?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use elk with the extracted filter/query `event.code : 261` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `event.code : 261`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use elk with the extracted filter/query `event.code : 261` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `RDP`

### Step 5: When you look at the failed authentication attempts, they were mostly coming from

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk with the extracted filter/query `event.code : 4624 AND winlog.event_data.IpAddress : 192.168.1.60 AND` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `event.code : 4624 AND winlog.event_data.IpAddress : 192.168.1.60 AND`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk with the extracted filter/query `event.code : 4624 AND winlog.event_data.IpAddress : 192.168.1.60 AND` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6`

### Step 6: According to Microsoft. What is the description of the "Sub Status" code for event id 4625?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk with the extracted filter/query `event.code : 4625 AND winlog.event_data.IpAddress : 192.168.1.60 AND` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `event.code : 4625 AND winlog.event_data.IpAddress : 192.168.1.60 AND`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk with the extracted filter/query `event.code : 4625 AND winlog.event_data.IpAddress : 192.168.1.60 AND` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `User logon with misspelled or bad password`

### Step 7: How long did the bruteforce last? MM:SS

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `05:48`

### Step 8: How many minutes passed before the attacker logged into the machine again?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk with the extracted filter/query `event.code : 4624 AND winlog.event_data.IpAddress : 192.168.1.60 AND` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `event.code : 4624 AND winlog.event_data.IpAddress : 192.168.1.60 AND`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk with the extracted filter/query `event.code : 4624 AND winlog.event_data.IpAddress : 192.168.1.60 AND` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `11`

### Step 9: What is the name of the policy used to lock the account after a certain number of failed login attempts?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use elk to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use elk to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Account Lockout`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
