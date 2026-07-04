# Investigating with Splunk

## Case Metadata

- Category: `SIEM (ELK, Splunk, etc.)`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/investigating_with_splunk.pdf`

## Why This Case Matters

Use this case as a SIEM (ELK, Splunk, etc.) reference for ids, registry, siem challenges.

## Input Signals

- Artifacts: ids, registry, siem, windows-events
- Tools: cyberchef, john, splunk
- Techniques: dns-analysis, http-analysis, password-cracking, siem-query, windows-event-analysis

## First-Principles Route

- Translate the question into searchable fields such as host, user, process, index, sourcetype, URI, IP, hash, or event code.
- Run broad time-bounded searches first, then narrow by event type, field value, and correlation chain.
- Keep the exact query shape and the evidence field that proves each answer.

## Solve Thinking

### Step 1: How many events were collected and ingested in the index main?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use splunk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: splunk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use splunk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 2: What is the new username?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use splunk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: splunk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use splunk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `checking out the User field:`

### Step 3: What is the command used to add a backdoor user from a remote computer?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use splunk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: splunk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use splunk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 4: investigation.

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use splunk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: splunk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use splunk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `login from the A1berto user.`

### Step 5: What is the name of the infected host on which suspicious PowerShell commands were executed?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use splunk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: splunk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use splunk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 6: malicious PowerShell execution?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, splunk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, splunk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, splunk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `10.10.10.5`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
