# NerisBot Lab

## Case Metadata

- Category: `SIEM (ELK, Splunk, etc.)`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_nerisbot_lab.pdf`

## Why This Case Matters

Use this case as a SIEM (ELK, Splunk, etc.) reference for ids, pcap, siem challenges.

## Input Signals

- Artifacts: ids, pcap, siem
- Tools: splunk, strings, suricata, virustotal, zeek
- Techniques: cti-enrichment, dns-analysis, http-analysis, malware-static, network-forensics, siem-query, stego-extraction

## First-Principles Route

- Translate the question into searchable fields such as host, user, process, index, sourcetype, URI, IP, hash, or event code.
- Run broad time-bounded searches first, then narrow by event type, field value, and correlation chain.
- Keep the exact query shape and the evidence field that proves each answer.

## Solve Thinking

### Step 1: What is the IP address from which the initial unauthorized access originated?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use splunk, strings, suricata, virustotal with the extracted filter/query `All unique http.http_user_agent strings` and inspect the matching evidence.
- Tools: splunk, strings, suricata, virustotal, zeek
- Filters or commands:
  - `All unique http.http_user_agent strings`
  - `All unique http.uri values`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use splunk, strings, suricata, virustotal with the extracted filter/query `All unique http.http_user_agent strings` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `147.32.84.165`

### Step 2: which is atypical for a user-agent string.

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use splunk, suricata, virustotal, zeek to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: splunk, suricata, virustotal, zeek
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use splunk, suricata, virustotal, zeek to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `195.88.191.59`

### Step 3: attacks. What is the domain name of the attacker server?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use splunk, suricata, virustotal, zeek with the extracted filter/query `one, we can add the http.hostname field to the original query and filter for the specific source` and inspect the matching evidence.
- Tools: splunk, suricata, virustotal, zeek
- Filters or commands:
  - `one, we can add the http.hostname field to the original query and filter for the specific source`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use splunk, suricata, virustotal, zeek with the extracted filter/query `one, we can add the http.hostname field to the original query and filter for the specific source` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `nocomcom.com`

### Step 4: could potentially be malicious?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use splunk, suricata, virustotal, zeek to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: splunk, suricata, virustotal, zeek
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use splunk, suricata, virustotal, zeek to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `client.exe`

### Step 5: determine the behaviour of these executables.

- Route type: `splunk-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use splunk, suricata, virustotal, zeek to collect the smallest evidence slice that answers the goal.
- Tools: splunk, suricata, virustotal, zeek
- Reasoning chain:
  - Recognize the goal as splunk-driven evidence lookup.
  - Use splunk, suricata, virustotal, zeek to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `5`

### Step 6: What is the SHA256 hash of the malicious file disguised as a .txt file?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: splunk, suricata, virustotal, zeek
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - The proof is the locally extracted indicator plus the enrichment source result.
- Evidence rule: The proof is the locally extracted indicator plus the enrichment source result.

### Step 7: which gave this super long query:

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use splunk, suricata, virustotal, zeek to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: splunk, suricata, virustotal, zeek
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use splunk, suricata, virustotal, zeek to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6fbc4d506f4d4e0a64ca09fd826408d3103c1a258c370553583a07a4cb9a6530`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
