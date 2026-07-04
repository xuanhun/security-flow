# Anonymous

## Case Metadata

- Category: `Pentesting`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/anonymous_writeup.pdf`

## Why This Case Matters

Use this case as a Pentesting reference for web-service challenges.

## Input Signals

- Artifacts: web-service
- Tools: nmap, strings
- Techniques: http-analysis, malware-static, privilege-escalation, service-enumeration, stego-extraction

## First-Principles Route

- Begin with service discovery and directory/application enumeration.
- Map each exposed service to default credentials, known CVEs, misconfiguration, or content leaks.
- After initial access, enumerate local privilege escalation paths before exploitation.

## Solve Thinking

### Step 1: Enumeration:

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `o FTP service with anonymous login enabled`

### Step 2: Service Enumeration

- Route type: `nmap-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use nmap to collect the smallest evidence slice that answers the goal.
- Tools: nmap
- Reasoning chain:
  - Recognize the goal as nmap-driven evidence lookup.
  - Use nmap to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 3: Accessing SMB Share:

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use nmap, strings to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: nmap, strings
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use nmap, strings to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 4: where data is hidden within images (such as in the Exif data, etc).

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use nmap, strings to recover or open the referenced file and inspect its metadata fields.
- Tools: nmap, strings
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use nmap, strings to recover or open the referenced file and inspect its metadata fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 5: Exploring FTP

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - The proof is the authentication field or stream showing the credential value.
- Evidence rule: The proof is the authentication field or stream showing the credential value.

### Step 6: Analysing the downloaded files

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use nmap to align timestamps and identify the event that satisfies the question.
- Tools: nmap
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use nmap to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `clean.sh`

### Step 7: Gaining a Reverse Shell:

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use nmap to align timestamps and identify the event that satisfies the question.
- Tools: nmap
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use nmap to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `clean.sh`

### Step 8: Privilege Escalation:

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use nmap to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: nmap
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use nmap to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Questions Answered:`

### Step 9: There’s a share on the user’s computer. What’s it called?

- Route type: `nmap-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use nmap to collect the smallest evidence slice that answers the goal.
- Tools: nmap
- Reasoning chain:
  - Recognize the goal as nmap-driven evidence lookup.
  - Use nmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `o pics`

### Step 10: user.txt

- Route type: `nmap-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use nmap to collect the smallest evidence slice that answers the goal.
- Tools: nmap
- Reasoning chain:
  - Recognize the goal as nmap-driven evidence lookup.
  - Use nmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `90d6f992585815ff991e68748c414740`

### Step 11: root.txt

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use nmap to enumerate processes, network sockets, injected regions, and command lines.
- Tools: nmap
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use nmap to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `4d930091c31a622a7ed10f27999af363`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
