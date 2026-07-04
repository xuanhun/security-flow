# IcedID

## Case Metadata

- Category: `Cyber Threat Intelligence (CTI)`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_icedid_lab.pdf`

## Why This Case Matters

Use this case as a Cyber Threat Intelligence (CTI) reference for email, office-document challenges.

## Input Signals

- Artifacts: email, office-document
- Tools: malpedia, malwarebazaar, virustotal
- Techniques: cti-enrichment, dns-analysis, http-analysis

## First-Principles Route

- Extract observables first, then enrich with threat intelligence sources.
- Map hashes, domains, malware names, TTPs, and infrastructure to campaigns or actors only when evidence supports it.

## Solve Thinking

### Step 1: What is the name of the file associated with the given hash?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: malpedia, virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `document-1982481273.xlsm`

### Step 2: Can you identify the filename of the GIF file that was deployed?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use malpedia, virustotal with the extracted filter/query `dropped contains a list of all files that were created and written during execution.` and inspect the matching evidence.
- Tools: malpedia, virustotal
- Filters or commands:
  - `dropped contains a list of all files that were created and written during execution.`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use malpedia, virustotal with the extracted filter/query `dropped contains a list of all files that were created and written during execution.` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3003.gif`

### Step 3: How many domains does the malware look to download the additional payload file in Q2?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use malpedia, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: malpedia, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use malpedia, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `5`

### Step 4: the Registrar INC?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use malpedia, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: malpedia, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use malpedia, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `NameCheap`

### Step 5: Could you specify the threat actor linked to the sample provided?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: malpedia, malwarebazaar, virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `GOLD CABIN`

### Step 6: onto the system?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use malpedia, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: malpedia, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use malpedia, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `URLDownloadToFileA`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
