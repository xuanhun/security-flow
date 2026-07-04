# Boogeyman 1

## Case Metadata

- Category: `Network Forensics`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/boogeyman1_writeup.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for email, windows-events challenges.

## Input Signals

- Artifacts: email, windows-events
- Tools: cyberchef, wireshark
- Techniques: dns-analysis, email-header-analysis, http-analysis, network-forensics, windows-event-analysis

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: What is the email address used to send the phishing email?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `sender email address:`

### Step 2: What is the email address of the victim?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `question:`

### Step 3: DKIM-Signature and List-Unsubscribe headers?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `I decided to examine the source manually:`

### Step 4: What is the name of the file inside the encrypted attachment?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Invoice_20230103.lnk.`

### Step 5: What is the password of the encrypted attachment?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 6: Command Line Argument field?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `string>” | base64 -d:`

### Step 7: What are the domains used by the attacker for file hosting and C2? Provide the domains in alphabetical order .

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use wireshark with the extracted filter/query `cat powershell.json | jq -s -c 'sort_by(.Timestamp) | .[]'| jq '{ScriptBlockText}'| sort | uniq` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `cat powershell.json | jq -s -c 'sort_by(.Timestamp) | .[]'| jq '{ScriptBlockText}'| sort | uniq`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use wireshark with the extracted filter/query `cat powershell.json | jq -s -c 'sort_by(.Timestamp) | .[]'| jq '{ScriptBlockText}'| sort | uniq` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `field, and remove duplicated field names:`

### Step 8: What is the name of the enumeration tool downloaded by the attacker?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 9: What is the file accessed by the attacker using the downloaded sq3.exe binary? Provide

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `sq3.exe`

### Step 10: What is the name of the exfiltrated file?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `167.71.211.113`

### Step 11: What type of file uses the .kdbx file extension?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 12: What is the encoding used during the exfiltration attempt of the sensitive file?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 13: What software is used by the attacker to host its presumed file/payload server?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Python is hosting the web server:`

### Step 14: What HTTP method is used by the C2 for the output of the commands executed by the attacker?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 15: What is the protocol used during the exfiltration activity?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use wireshark with the extracted filter/query `therefore the protocol used is DNS.` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `therefore the protocol used is DNS.`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use wireshark with the extracted filter/query `therefore the protocol used is DNS.` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `therefore the protocol used is DNS.`

### Step 16: What is the password of the exfiltrated file?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark with the extracted filter/query `attacker using the sq3.exe binary. Therefore, we can use the ‘http contains “sq3.exe”’ filter to` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `attacker using the sq3.exe binary. Therefore, we can use the ‘http contains “sq3.exe”’ filter to`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark with the extracted filter/query `attacker using the sq3.exe binary. Therefore, we can use the ‘http contains “sq3.exe”’ filter to` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `sq3.exe`

### Step 17: find the password:

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use cyberchef, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: cyberchef, wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use cyberchef, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- %p9^3!lL^Mz47E2GaT^y`

### Step 18: What is the credit card number stored inside the exfiltrated file?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
