# HireMe Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_hireme_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, email, registry challenges.

## Input Signals

- Artifacts: disk-image, email, registry
- Tools: autopsy, cyberchef, db-browser-sqlite, ftk-imager, registry-explorer
- Techniques: browser-forensics, dns-analysis, http-analysis, registry-forensics, timeline-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the administrator's username?

- Route type: `autopsy-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use autopsy, ftk-imager, registry-explorer to collect the smallest evidence slice that answers the goal.
- Tools: autopsy, ftk-imager, registry-explorer
- Reasoning chain:
  - Recognize the goal as autopsy-driven evidence lookup.
  - Use autopsy, ftk-imager, registry-explorer to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Karen`

### Step 2: What is the OS's build number?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use ftk-imager, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: ftk-imager, registry-explorer
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use ftk-imager, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `16299`

### Step 3: What is the hostname of the computer?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `TOTALLYNOTAHACK`

### Step 4: is the name of the software?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager, registry-explorer to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager, registry-explorer
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager, registry-explorer to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Skype`

### Step 5: What is the zip code of the administrator's post?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, ftk-imager, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, ftk-imager, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, ftk-imager, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `19709`

### Step 6: What are the initials of the person who contacted the admin user from TAAUSAI?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager, registry-explorer to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager, registry-explorer
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager, registry-explorer to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `MS`

### Step 7: How much money was TAAUSAI willing to pay upfront?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager, registry-explorer to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager, registry-explorer
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager, registry-explorer to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `150000`

### Step 8: What country is the admin user meeting the hacker group in?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager, registry-explorer to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager, registry-explorer
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager, registry-explorer to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Egypt`

### Step 9: What is the machine's timezone? (Use the three-letter abbreviation)

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use ftk-imager, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: ftk-imager, registry-explorer
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use ftk-imager, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `UTC`

### Step 10: When was AlpacaCare.docx last accessed?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use ftk-imager, registry-explorer to align timestamps and identify the event that satisfies the question.
- Tools: ftk-imager, registry-explorer
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use ftk-imager, registry-explorer to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `03/17/2019 09:52 PM`

### Step 11: There was a second partition on the drive. What is the letter assigned to it?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use ftk-imager, registry-explorer to align timestamps and identify the event that satisfies the question.
- Tools: ftk-imager, registry-explorer
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use ftk-imager, registry-explorer to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `A`

### Step 12: What is the answer to the question Company's manager asked Karen?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager, registry-explorer to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager, registry-explorer
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager, registry-explorer to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `TheCardCriesNoMore`

### Step 13: What is the job position offered to Karen? (3 words, 2 spaces in between)

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `cyber security analyst`

### Step 14: When was the admin user password last changed?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use ftk-imager, registry-explorer to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: ftk-imager, registry-explorer
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use ftk-imager, registry-explorer to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `03/21/2019 19:13:09`

### Step 15: What version of Chrome is installed on the machine?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager, registry-explorer to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager, registry-explorer
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager, registry-explorer to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `72.0.3626.121`

### Step 16: What is the URL used to download Skype?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://download.skype.com/s4l/download/win/Skype-8.41.0.54.exe`

### Step 17: AlpacaCare.docx is based on?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, ftk-imager, registry-explorer to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, ftk-imager, registry-explorer
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, ftk-imager, registry-explorer to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `palominoalpacafarm.com`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
