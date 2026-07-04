# Eli Lab

## Case Metadata

- Category: `Mobile Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_denfenders_eli_lab.pdf`

## Why This Case Matters

Use this case as a Mobile Forensics reference for email, ids challenges.

## Input Signals

- Artifacts: email, ids
- Tools: not detected
- Techniques: browser-forensics, http-analysis

## First-Principles Route

- Inventory app/database artifacts, timestamps, media, account records, and package metadata.
- Extract SQLite, plist/XML/JSON, and app-specific records before guessing behavior.

## Solve Thinking

### Step 1: The folder to store all your data in - How many files are in Eli's downloads directory?

- Route type: `evidence lookup`
- Why: For Mobile Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2021 CTF - Chromebook.tar\decrypted\mount\user\Downloads`

### Step 2: user has downloaded via a browser, etc.

- Route type: `evidence lookup`
- Why: For Mobile Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `6`

### Step 3: Smile for the camera - What is the MD5 hash of the user's profile photo?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5DDD4FE0041839DEB0A4B0252002127B`

### Step 4: Road Trip! - What city was Eli's destination in?

- Route type: `evidence lookup`
- Why: For Mobile Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Plattsburgh`

### Step 5: Promise Me - How many promises does Wickr make?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `9`

### Step 6: Key-ty Cat - What are the last five characters of the key for the Tabby Cat extension?

- Route type: `evidence lookup`
- Why: For Mobile Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool with the extracted filter/query `directory. Once you find the folder for this extension, open the manifest.json file, which contains` and inspect the matching evidence.
- Filters or commands:
  - `directory. Once you find the folder for this extension, open the manifest.json file, which contains`
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool with the extracted filter/query `directory. Once you find the folder for this extension, open the manifest.json file, which contains` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `DAQAB`

### Step 7: Time to jam out - How many songs does Eli have downloaded?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2`

### Step 8: Autofill, roll out - Which word was Autofilled the most?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `email`

### Step 9: Dress for success - What is this bird's image's logical size in bytes?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `46791`

### Step 10: Repeat customer - What was Eli's top-visited site?

- Route type: `evidence lookup`
- Why: For Mobile Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `protonmail.com`

### Step 11: Vroom Vroom, What is the name of the car-related theme?

- Route type: `evidence lookup`
- Why: For Mobile Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Lamborghini Cherry`

### Step 12: You got mail - How many emails were received from notification@service.tiktok.com?

- Route type: `evidence lookup`
- Why: For Mobile Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the goal as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2021 CTF - Takeout\Takeout\Mail`

### Step 13: how many emails were received by notification@service.tiktok.com. There are tools that can

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6`

### Step 14: Who defines essential? - What was searched on Mar 4, 2021, at 4:09:35 AM EDT?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use the artifact-specific tool with the extracted filter/query `The first video this user watched was called “The BEST Clips of 2020 | Lacrosse Highlights ECD` and inspect the matching evidence.
- Filters or commands:
  - `The first video this user watched was called “The BEST Clips of 2020 | Lacrosse Highlights ECD`
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use the artifact-specific tool with the extracted filter/query `The first video this user watched was called “The BEST Clips of 2020 | Lacrosse Highlights ECD` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `is travelling to get chicken essential travel`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
