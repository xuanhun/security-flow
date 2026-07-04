# Browser Forensics - Cryptominer

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `BTLO`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/btlo_browser_forensics_cryptominer.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image challenges.

## Input Signals

- Artifacts: disk-image
- Tools: ftk-imager
- Techniques: browser-forensics

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: How many browser-profiles are present in Google Chrome?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2`

### Step 2: What is the name of the browser theme installed on Google Chrome?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `earth in space`

### Step 3: Identify the Extension ID and Extension Name of the cryptominer

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `egnfmleidkolminhjlkaomjefheafbbb, DFP Cryptocurrency Miner`

### Step 4: What is the description text of this extension?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Allows staff members to mine cryptocurrency in the background of their web browser`

### Step 5: What is the name of the specific javascript web miner used in the browser extension?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `cryptoloot`

### Step 6: How many hashes is the crypto miner calculating per second?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: ftk-imager
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `20`

### Step 7: What is the public key associated with this mining activity?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `b23efb4650150d5bc5b2de6f05267272cada06d985a0`

### Step 8: What is the URL of the official Twitter page of the javascript web miner?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `twitter.com/cryptolootminer`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
