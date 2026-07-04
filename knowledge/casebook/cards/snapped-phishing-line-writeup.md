# Snapped Phish-ing Line

## Case Metadata

- Category: `Email Analysis`
- Platform: `TryHackMe`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/snapped_phishing_line_writeup.pdf`

## Why This Case Matters

Use this case as a Email Analysis reference for email challenges.

## Input Signals

- Artifacts: email
- Tools: cyberchef, virustotal
- Techniques: browser-forensics, cti-enrichment, dns-analysis

## First-Principles Route

- Inspect headers first: sender path, SPF/DKIM/DMARC, received chain, reply-to, attachments, and URLs.
- Decode attachments, URLs, and embedded payloads in an isolated workflow.
- Enrich domains, IPs, and hashes only after extracting them locally.

## Solve Thinking

### Step 1: Analysing the phishing URL(s) by browsing it using Firefox.

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 2: Using CTI-related tooling to gather more information about the adversary.

- Route type: `virustotal-driven evidence lookup`
- Why: For Email Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 3: Who is the individual who received an email attachment containing a PDF?

- Route type: `virustotal-driven evidence lookup`
- Why: For Email Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal with the extracted filter/query `After exploring all emails, you discover that the Quote for Services Rendered eml file contains` and inspect the matching evidence.
- Tools: virustotal
- Filters or commands:
  - `After exploring all emails, you discover that the Quote for Services Rendered eml file contains`
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal with the extracted filter/query `After exploring all emails, you discover that the Quote for Services Rendered eml file contains` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `the pdf:`

### Step 4: What email address was used by the adversary to send the phishing emails?

- Route type: `virustotal-driven evidence lookup`
- Why: For Email Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Accounts.Payable@groupmarketingonline.icu:`

### Step 5: What is the redirection URL to the phishing page for the individual Zoe Duncan?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `40e7baa2f826a57fcf04e5202526f8bd`

### Step 6: What is the URL to the .zip archive of the phishing kit? (defanged format)

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `you the answer:`

### Step 7: What is the SHA256 hash of the phishing kit archive?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 8: When was the phishing kit archive first submitted?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 9: When was the SSL certificate the phishing domain used to host the phishing kit archive first logged?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Lookup.`

### Step 10: What was the email address of the user who submitted their password twice?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 11: What was the email address used by the adversary to collect compromised credentials?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use virustotal to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `submit.php`

### Step 12: address that ends in “@gmail.com”?

- Route type: `virustotal-driven evidence lookup`
- Why: For Email Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 13: What is the hidden flag?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `terminal:`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
