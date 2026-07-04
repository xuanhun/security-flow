# Phishing Analysis

## Case Metadata

- Category: `Email Analysis`
- Platform: `BTLO`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/btlo_phishing_analysis.pdf`

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

### Step 1: Who is the primary recipient of this email?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `kinnar1975@yahoo.co.uk`

### Step 2: What is the subject of this email?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Undeliverable: Website contact form submission`

### Step 3: What is the date and time the email was sent?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `18 March 2021 04:14`

### Step 4: What is the Originating IP?

- Route type: `evidence lookup`
- Why: For Email Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `103.9.171.10`

### Step 5: Perform reverse DNS on this IP address, what is the resolved host?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use the artifact-specific tool to filter DNS traffic and pivot from source host to queried domain or resolver.
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use the artifact-specific tool to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `c5s2-1e-syd.hosting-services.net.auD`

### Step 6: What is the name of the attached file?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Website contact form submission.eml`

### Step 7: What is the URL found inside the attachment?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://35000usdperwwekpodf.blogspot.sg/?p=9swghttps://35000usdperwwekpodf.blogspot.c`

### Step 8: What service is this webpage hosted on?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `blogspot`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
