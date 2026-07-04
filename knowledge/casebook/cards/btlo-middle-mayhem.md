# Middle Mayhem

## Case Metadata

- Category: `SIEM (ELK, Splunk, etc.)`
- Platform: `BTLO`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/btlo_middle_mayhem.pdf`

## Why This Case Matters

Use this case as a SIEM (ELK, Splunk, etc.) reference for siem challenges.

## Input Signals

- Artifacts: siem
- Tools: elk, splunk
- Techniques: http-analysis, service-enumeration, siem-query

## First-Principles Route

- Translate the question into searchable fields such as host, user, process, index, sourcetype, URI, IP, hash, or event code.
- Run broad time-bounded searches first, then narrow by event type, field value, and correlation chain.
- Keep the exact query shape and the evidence field that proves each answer.

## Solve Thinking

### Step 1: Find the relevant HTTP header in the SIEM logs that indicates CVE exploitation. Provide the header name.

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk, splunk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk, splunk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk, splunk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `X-Middleware-Subrequest`

### Step 2: What interesting URI did the attacker access after exploiting the CVE?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use elk to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use elk to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `/api/upload`

### Step 3: Identify the user account that achieved successful lateral movement to another server.

- Route type: `elk-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk to collect the smallest evidence slice that answers the goal.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as elk-driven evidence lookup.
  - Use elk to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `dbserv`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
