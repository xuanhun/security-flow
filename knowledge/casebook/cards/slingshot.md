# SlingShot

## Case Metadata

- Category: `SIEM (ELK, Splunk, etc.)`
- Platform: `TryHackMe`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/slingshot.pdf`

## Why This Case Matters

Use this case as a SIEM (ELK, Splunk, etc.) reference for siem, web-service challenges.

## Input Signals

- Artifacts: siem, web-service
- Tools: cyberchef, elk, gobuster, hydra, nmap, strings
- Techniques: dns-analysis, http-analysis, malware-static, password-cracking, service-enumeration, siem-query, stego-extraction, timeline-analysis, web-enumeration

## First-Principles Route

- Translate the question into searchable fields such as host, user, process, index, sourcetype, URI, IP, hash, or event code.
- Run broad time-bounded searches first, then narrow by event type, field value, and correlation chain.
- Keep the exact query shape and the evidence field that proves each answer.

## Solve Thinking

### Step 1: What was the attacker’s IP?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use cyberchef, elk to align timestamps and identify the event that satisfies the question.
- Tools: cyberchef, elk
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use cyberchef, elk to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `10.0.2.15`

### Step 2: What was the first scanner that the attacker ran against the web server?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, elk, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, elk, nmap
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, elk, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 3: which is the answer:

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use cyberchef, elk, nmap to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: cyberchef, elk, nmap
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use cyberchef, elk, nmap to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - The proof is the service enumeration result and the exact access or escalation condition.
- Evidence rule: The proof is the service enumeration result and the exact access or escalation condition.

### Step 4: What was the User Agent of the directory enumeration tool that the attacker used on the web server?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, elk, gobuster with the extracted filter/query `Gobuster is a popular directory and file brute forcing tool, and it is the answer.` and inspect the matching evidence.
- Tools: cyberchef, elk, gobuster
- Filters or commands:
  - `Gobuster is a popular directory and file brute forcing tool, and it is the answer.`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, elk, gobuster with the extracted filter/query `Gobuster is a popular directory and file brute forcing tool, and it is the answer.` and inspect the matching evidence.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 5: In total, how many requested resources on the web served did the attacker fail to find?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `requested resources.`

### Step 6: What is the flag under the interesting directory the attacker found?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 7: What login page did the attacker discover using the directory enumeration tool?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - The proof is the DNS packet, resolver, queried domain, or response record.
- Evidence rule: The proof is the DNS packet, resolver, queried domain, or response record.

### Step 8: What was the user agent of the brute-force tool that the attacker used on the admin panel?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, elk, hydra to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, elk, hydra
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, elk, hydra to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `is a popular brute-force tool:`

### Step 9: What username:password combination did the attacker use to gain access to the admin page?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use cyberchef, elk, hydra to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: cyberchef, elk, hydra
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use cyberchef, elk, hydra to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `event:`

### Step 10: What flag was included in the file that the attacker uploaded from the admin directory?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 11: What was the first command the attacker ran on the web shell?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, elk, strings with the extracted filter/query `This looks for all HTTP traffic with the response code 200 and contains the strings cmd,` and inspect the matching evidence.
- Tools: cyberchef, elk, strings
- Filters or commands:
  - `This looks for all HTTP traffic with the response code 200 and contains the strings cmd,`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, elk, strings with the extracted filter/query `This looks for all HTTP traffic with the response code 200 and contains the strings cmd,` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `down to 4 results:`

### Step 12: When we were looking at what the attacker uploaded to the admin directory, we could also see

- Route type: `cyberchef-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, elk to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, elk
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, elk to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `config-db.php`

### Step 13: What directory did the attacker use to access the database manger?

- Route type: `cyberchef-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, elk to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, elk
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, elk to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 14: What was the name of the database that the attacker exported?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `export.php`

### Step 15: What flag does the attacker insert into the database?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `import.php`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
