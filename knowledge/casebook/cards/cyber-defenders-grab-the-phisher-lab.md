# GrabThePhiser

## Case Metadata

- Category: `Cyber Threat Intelligence (CTI)`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_grab_the_phisher_lab.pdf`

## Why This Case Matters

Use this case as a Cyber Threat Intelligence (CTI) reference for email challenges.

## Input Signals

- Artifacts: email
- Tools: not detected
- Techniques: http-analysis

## First-Principles Route

- Extract observables first, then enrich with threat intelligence sources.
- Map hashes, domains, malware names, TTPs, and infrastructure to campaigns or actors only when evidence supports it.

## Solve Thinking

### Step 1: What is the file name that has the code for the phishing kit?

- Route type: `evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `metamask.php`

### Step 2: In which language was the kit written?

- Route type: `evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 3: What service does the kit use to retrieve the victim’s machine information?

- Route type: `evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `The answer being sypex geo.`

### Step 4: How many seed phrases were already collected?

- Route type: `evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool with the extracted filter/query `In the pankewk/log directory you can find a log,txt file that contains 3 seed phrases (each line` and inspect the matching evidence.
- Filters or commands:
  - `In the pankewk/log directory you can find a log,txt file that contains 3 seed phrases (each line`
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool with the extracted filter/query `In the pankewk/log directory you can find a log,txt file that contains 3 seed phrases (each line` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `represents a seed phrase):`

### Step 5: Write down the seed phrase of the most recent phishing incident?

- Route type: `evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 6: Which medium had been used for credential dumping?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use the artifact-specific tool to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use the artifact-specific tool to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `metamask.php`

### Step 7: What is the token for the channel?

- Route type: `evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 8: What is the chat ID of the phisher’s channel?

- Route type: `evidence lookup`
- Why: For Cyber Threat Intelligence (CTI), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Can be seen above the token variable:`

### Step 9: What is the full name of the Phish Actor?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `dMessage?chat_id=5442785564&text=yo`

### Step 10: What is the username of the Phish Actor?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
  - The proof is the timestamped artifact that matches the question constraint.
- Evidence rule: The proof is the timestamped artifact that matches the question constraint.

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
