# Phishing Analysis 2

## Case Metadata

- Category: `Email Analysis`
- Platform: `BTLO`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/btlo_phishing_analysis_2.pdf`

## Why This Case Matters

Use this case as a Email Analysis reference for email challenges.

## Input Signals

- Artifacts: email
- Tools: cyberchef
- Techniques: http-analysis

## First-Principles Route

- Inspect headers first: sender path, SPF/DKIM/DMARC, received chain, reply-to, attachments, and URLs.
- Decode attachments, URLs, and embedded payloads in an isolated workflow.
- Enrich domains, IPs, and hashes only after extracting them locally.

## Solve Thinking

### Step 1: What is the sending email address?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Email Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `amazon@zyevantoby.cn`

### Step 2: What is the recipient email address?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Email Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `saintington73@outlook.com`

### Step 3: What is the subject line of the email?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Email Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Your Account has been locked`

### Step 4: What company is the attacker trying to imitate?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Email Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Amazon`

### Step 5: What is the date and time the email was sent? (As copied from a text editor)

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use cyberchef to align timestamps and identify the event that satisfies the question.
- Tools: cyberchef
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use cyberchef to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Wed, 14 Jul 2021 01:40:32 +0900`

### Step 6: What is the URL of the main call-to-action button?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://emea01.safelinks.protection.outlook.com/?url=https%3A%2F%2Famaozn.zzyuchengzh`

### Step 7: When looking at the main body content in a text editor, what encoding scheme is being used?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Email Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `base64`

### Step 8: What is the URL used to retrieve the company's logo in the email?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef with the extracted filter/query `For some unknown reason one of the URLs contains a Facebook profile URL. What is the` and inspect the matching evidence.
- Tools: cyberchef
- Filters or commands:
  - `For some unknown reason one of the URLs contains a Facebook profile URL. What is the`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef with the extracted filter/query `For some unknown reason one of the URLs contains a Facebook profile URL. What is the` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `https://images.squarespace-`

### Step 9: username (not necessarily the display name) of this account, based on the URL?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `amir.boyka.7`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
