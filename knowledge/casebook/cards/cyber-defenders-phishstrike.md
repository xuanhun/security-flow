# PhishStrike Lab

## Case Metadata

- Category: `Cyber Threat Intelligence (CTI)`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_phishstrike.pdf`

## Why This Case Matters

Use this case as a Cyber Threat Intelligence (CTI) reference for email, registry challenges.

## Input Signals

- Artifacts: email, registry
- Tools: urlhaus, virustotal
- Techniques: cti-enrichment, dns-analysis, email-header-analysis, http-analysis

## First-Principles Route

- Extract observables first, then enrich with threat intelligence sources.
- Map hashes, domains, malware names, TTPs, and infrastructure to campaigns or actors only when evidence supports it.

## Solve Thinking

### Step 1: When analysing emails manually, I enjoy using sublime text with the email header syntax created by 13Cubed.

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use urlhaus, virustotal to align timestamps and identify the event that satisfies the question.
- Tools: urlhaus, virustotal
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use urlhaus, virustotal to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `18.208.22.104`

### Step 2: return path specified in this email?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use urlhaus, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: urlhaus, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use urlhaus, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `erikajohana.lopez@uptc.edu.co`

### Step 3: Which malware family is responsible for cryptocurrency mining?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use urlhaus, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: urlhaus, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use urlhaus, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 4: which is a platform from abuse.ch and Spamhaus that shares malicious URLs being used for

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use urlhaus, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: urlhaus, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use urlhaus, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `CoinMiner`

### Step 5: malware sample, what does this malware request the URL?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use urlhaus, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: urlhaus, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use urlhaus, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `http://ripley.studio/loader/uploads/Qanjttrbv.jpeg`

### Step 6: what is the executable's name in the first value added to the registry auto-run key?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use urlhaus, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: urlhaus, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use urlhaus, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Jzwvix.exe`

### Step 7: hash of the file previously downloaded and added to the autorun keys?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use urlhaus, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: urlhaus, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use urlhaus, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `bf7628695c2df7a3020034a065397592a1f8850e59f9a448b555bc1c8c639539`

### Step 8: analysis?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use urlhaus, virustotal with the extracted filter/query `Within this report is a Network section that contains the network requests that were made by` and inspect the matching evidence.
- Tools: urlhaus, virustotal
- Filters or commands:
  - `Within this report is a Network section that contains the network requests that were made by`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use urlhaus, virustotal with the extracted filter/query `Within this report is a Network section that contains the network requests that were made by` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `50`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
