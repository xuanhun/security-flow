# Injector Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_injector_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, memory, registry challenges.

## Input Signals

- Artifacts: disk-image, memory, registry
- Tools: cyberchef, ftk-imager, registry-explorer, strings, volatility
- Techniques: http-analysis, malware-static, memory-forensics, registry-forensics, stego-extraction

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the computer's name?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use ftk-imager, registry-explorer, volatility to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: ftk-imager, registry-explorer, volatility
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use ftk-imager, registry-explorer, volatility to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `WIN-L0ZZQ76PMUF`

### Step 2: What is the Timezone of the compromised machine? Format: UTC+0 (no-space)

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use ftk-imager, registry-explorer, volatility to align timestamps and identify the event that satisfies the question.
- Tools: ftk-imager, registry-explorer, volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use ftk-imager, registry-explorer, volatility to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `UTC-7`

### Step 3: What was the first vulnerability the attacker was able to exploit?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager, registry-explorer, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager, registry-explorer, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager, registry-explorer, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `XSS`

### Step 4: What is the OS build number?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager, registry-explorer, volatility to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager, registry-explorer, volatility
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager, registry-explorer, volatility to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6001`

### Step 5: How many users are on the compromised machine?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use ftk-imager, registry-explorer, volatility to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: ftk-imager, registry-explorer, volatility
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use ftk-imager, registry-explorer, volatility to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4`

### Step 6: What is the webserver package installed on the machine?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager, registry-explorer, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager, registry-explorer, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager, registry-explorer, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `xampp`

### Step 7: What is the name of the vulnerable web app installed on the webserver?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager, registry-explorer, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager, registry-explorer, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager, registry-explorer, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `dvwa`

### Step 8: What is the user agent used in the HTTP requests sent by the SQL injection attack tool?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager, registry-explorer, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager, registry-explorer, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager, registry-explorer, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `sqlmap/1.0-dev-nongit-20150902`

### Step 9: configuration. What is the filename?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager, registry-explorer, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager, registry-explorer, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager, registry-explorer, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `hosts`

### Step 10: of the type parameter in the executed command?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use ftk-imager, registry-explorer, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: ftk-imager, registry-explorer, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use ftk-imager, registry-explorer, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 11: determine that the type parameter is remotedesktop.

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager, registry-explorer, volatility to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager, registry-explorer, volatility
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager, registry-explorer, volatility to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `remotedesktop`

### Step 12: How many users were added by the attacker?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use ftk-imager, registry-explorer, volatility to align timestamps and identify the event that satisfies the question.
- Tools: ftk-imager, registry-explorer, volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use ftk-imager, registry-explorer, volatility to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2`

### Step 13: When did the attacker create the first user?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use ftk-imager, registry-explorer, volatility to align timestamps and identify the event that satisfies the question.
- Tools: ftk-imager, registry-explorer, volatility
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use ftk-imager, registry-explorer, volatility to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2015-09-02 09:05:06 UTC`

### Step 14: What is the NThash of the user's password set by the attacker?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use ftk-imager, registry-explorer, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: ftk-imager, registry-explorer, volatility
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use ftk-imager, registry-explorer, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `817875ce4794a9262159186413772644`

### Step 15: What is The MITRE ID corresponding to the technique used to keep persistence?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager, registry-explorer, volatility to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager, registry-explorer, volatility
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager, registry-explorer, volatility to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `T1136.001`

### Step 16: the name of the URL parameter used to execute commands?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager, registry-explorer, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager, registry-explorer, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager, registry-explorer, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 17: determine that the URL parameter used to execute commands is cmd:

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager, registry-explorer, volatility with the extracted filter/query `Within this zip file, you can right click the webshell.pfp file to export the hash, which contains` and inspect the matching evidence.
- Tools: ftk-imager, registry-explorer, volatility
- Filters or commands:
  - `Within this zip file, you can right click the webshell.pfp file to export the hash, which contains`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager, registry-explorer, volatility with the extracted filter/query `Within this zip file, you can right click the webshell.pfp file to export the hash, which contains` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `cmd`

### Step 18: Group. Provide the IP address that was part of the executed command?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use ftk-imager, registry-explorer, strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: ftk-imager, registry-explorer, strings, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use ftk-imager, registry-explorer, strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `192.168.56.102`

### Step 19: for a specific version of PHP . Provide the PHP version number?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, ftk-imager, registry-explorer, volatility to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, ftk-imager, registry-explorer, volatility
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, ftk-imager, registry-explorer, volatility to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `4.1.0`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
