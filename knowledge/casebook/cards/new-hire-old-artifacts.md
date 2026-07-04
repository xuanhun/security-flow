# New Hire Old Artifacts

## Case Metadata

- Category: `SIEM (ELK, Splunk, etc.)`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/new_hire_old_artifacts.pdf`

## Why This Case Matters

Use this case as a SIEM (ELK, Splunk, etc.) reference for ids, pe-malware, registry challenges.

## Input Signals

- Artifacts: ids, pe-malware, registry, siem, windows-events
- Tools: capa, cyberchef, elk, splunk
- Techniques: dns-analysis, http-analysis, malware-static, siem-query, windows-event-analysis

## First-Principles Route

- Translate the question into searchable fields such as host, user, process, index, sourcetype, URI, IP, hash, or event code.
- Run broad time-bounded searches first, then narrow by event type, field value, and correlation chain.
- Keep the exact query shape and the evidence field that proves each answer.

## Solve Thinking

### Step 1: investigation was never conducted. Your manager has tasked you to sift through the events of

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use elk, splunk to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: elk, splunk
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use elk, splunk to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `the binary? Enter the full path.`

### Step 2: What is listed as the company name?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - The proof is the DNS packet, resolver, queried domain, or response record.
- Evidence rule: The proof is the DNS packet, resolver, queried domain, or response record.

### Step 3: What was the name of the binary? What is listed as its original filename? (format: file.xyz,file.xyz)

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `IonicLarge.exe`

### Step 4: The same binary made some change to a registry key. What was the key path?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use elk to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use elk to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - The proof is the event record and correlated timestamp/user/process fields.
- Evidence rule: The proof is the event record and correlated timestamp/user/process fields.

### Step 5: which logs changes to a registry value:

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `WvmIOrcfsuILdX6SNwIRmGOJ.exe`

### Step 6: location. What was the full path to the binary?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `AppData location:`

### Step 7: What were the DLLs that were loaded from the binary from the previous question. Enter the

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use capa, elk, splunk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: capa, elk, splunk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use capa, elk, splunk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `file1.dll`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
