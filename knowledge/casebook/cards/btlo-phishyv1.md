# Phishy v1

## Case Metadata

- Category: `Email Analysis`
- Platform: `BTLO`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/btlo_phishyv1.pdf`

## Why This Case Matters

Use this case as a Email Analysis reference for email challenges.

## Input Signals

- Artifacts: email
- Tools: not detected
- Techniques: dns-analysis, http-analysis

## First-Principles Route

- Inspect headers first: sender path, SPF/DKIM/DMARC, received chain, reply-to, attachments, and URLs.
- Decode attachments, URLs, and embedded payloads in an isolated workflow.
- Enrich domains, IPs, and hashes only after extracting them locally.

## Solve Thinking

### Step 1: What is the full URL of the background image which is on the phishing landing page?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use the artifact-specific tool to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use the artifact-specific tool to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `http://securedocument.net/secure/L0GIN/protected/login/portal/axCBhIt.png`

### Step 2: What is the name of the php page which will process the stolen credentials?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use the artifact-specific tool to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use the artifact-specific tool to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `jeff.php`

### Step 3: What is the SHA256 of the phishing kit in ZIP format? (Provide the last 6 characters)

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `fa5b48`

### Step 4: What email address is setup to receive the phishing credential logs?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use the artifact-specific tool to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use the artifact-specific tool to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `boris.smets@tfl-uk.co`

### Step 5: What is the function called to produce the PHP variable which appears in the index1.html URL?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `getTime()`

### Step 6: What is the domain of the website which should appear once credentials are entered?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use the artifact-specific tool to filter DNS traffic and pivot from source host to queried domain or resolver.
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use the artifact-specific tool to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Office.com`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
