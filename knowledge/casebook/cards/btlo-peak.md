# Peak

## Case Metadata

- Category: `SIEM (ELK, Splunk, etc.)`
- Platform: `BTLO`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/btlo_peak.pdf`

## Why This Case Matters

Use this case as a SIEM (ELK, Splunk, etc.) reference for linux-logs, siem challenges.

## Input Signals

- Artifacts: linux-logs, siem
- Tools: elk, hydra
- Techniques: dns-analysis, http-analysis, password-cracking, privilege-escalation, service-enumeration, siem-query

## First-Principles Route

- Translate the question into searchable fields such as host, user, process, index, sourcetype, URI, IP, hash, or event code.
- Run broad time-bounded searches first, then narrow by event type, field value, and correlation chain.
- Keep the exact query shape and the evidence field that proves each answer.

## Solve Thinking

### Step 1: What is the hostname of the infected server?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use elk to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use elk to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `APPSERV-Chicago`

### Step 2: What is the tool to crack the password that he possibly used?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use elk, hydra to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: elk, hydra
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use elk, hydra to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Hydra`

### Step 3: What is the first command executed by the attacker?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ls`

### Step 4: the file he downloads?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `raw.githubusercontent.com, linpeas.sh`

### Step 5: the vulnerability he attempts to exploit?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `sudo, CVE-2021–3156`

### Step 6: Attacker executes the downloaded script. What is the URL that the script connects to?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://134430fcb321.ngrok.io/upload`

### Step 7: What are the local files that have been downloaded in the malicious activity?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `/etc/passwd, /tmp/btlo.zip`

### Step 8: How many files did the attacker delete?

- Route type: `elk-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk to collect the smallest evidence slice that answers the goal.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as elk-driven evidence lookup.
  - Use elk to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
