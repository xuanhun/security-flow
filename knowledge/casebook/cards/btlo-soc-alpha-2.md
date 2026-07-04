# SOC Alpha 2

## Case Metadata

- Category: `SIEM (ELK, Splunk, etc.)`
- Platform: `BTLO`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/btlo_soc_alpha_2.pdf`

## Why This Case Matters

Use this case as a SIEM (ELK, Splunk, etc.) reference for siem, windows-events challenges.

## Input Signals

- Artifacts: siem, windows-events
- Tools: elk, virustotal
- Techniques: cti-enrichment, dns-analysis, siem-query, windows-event-analysis

## First-Principles Route

- Translate the question into searchable fields such as host, user, process, index, sourcetype, URI, IP, hash, or event code.
- Run broad time-bounded searches first, then narrow by event type, field value, and correlation chain.
- Keep the exact query shape and the evidence field that proves each answer.

## Solve Thinking

### Step 1: investigation is slightly more difficult, although in my opinion, is way more enjoyable. You get

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use elk to align timestamps and identify the event that satisfies the question.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use elk to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `frames, and alert context.`

### Step 2: Hunt 1 (1/3) - What is the IP address from which the suspicious brute force traffic is seen?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use elk to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use elk to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `(Format: X.X.X.X)`

### Step 3: In order to look for any brute force attempt, we can filter for this event ID and focus on the

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use elk to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use elk to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Event_EvebtData_UpAddress field:`

### Step 4: user nightmare.

- Route type: `elk-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk to collect the smallest evidence slice that answers the goal.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as elk-driven evidence lookup.
  - Use elk to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `192.168.1.20`

### Step 5: When a user attempts to authenticate to a Windows host, the generated log includes a field for logon type. Logon type indicates the way the user attempts to authenticate to the host

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Network`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
