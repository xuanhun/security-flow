# Lookup

## Case Metadata

- Category: `Pentesting`
- Platform: `TryHackMe`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/lookup.pdf`

## Why This Case Matters

Use this case as a Pentesting reference for web-service challenges.

## Input Signals

- Artifacts: web-service
- Tools: hydra, nmap
- Techniques: dns-analysis, password-cracking, privilege-escalation, service-enumeration

## First-Principles Route

- Begin with service discovery and directory/application enumeration.
- Map each exposed service to default credentials, known CVEs, misconfiguration, or content leaks.
- After initial access, enumerate local privilege escalation paths before exploitation.

## Solve Thinking

### Step 1: When we enter these credentials into the login portal, we get an error because we need to add

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use hydra, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: hydra, nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use hydra, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `module:`

### Step 2: Privilege Escalation

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use hydra, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: hydra, nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use hydra, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `We can now retrieve the user flag:`

### Step 3: Root Privilege Escalation

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use hydra, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: hydra, nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use hydra, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `entering:`

### Step 4: What is the user flag?

- Route type: `hydra-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use hydra, nmap to collect the smallest evidence slice that answers the goal.
- Tools: hydra, nmap
- Reasoning chain:
  - Recognize the goal as hydra-driven evidence lookup.
  - Use hydra, nmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `38375fb4dd8baa2b2039ac03d92b820e`

### Step 5: What is the root flag?

- Route type: `hydra-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use hydra, nmap to collect the smallest evidence slice that answers the goal.
- Tools: hydra, nmap
- Reasoning chain:
  - Recognize the goal as hydra-driven evidence lookup.
  - Use hydra, nmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `5a285a9f257e45c68bb6c9f9f57d18e8`

### Step 6: Conclusion

- Route type: `hydra-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use hydra, nmap to collect the smallest evidence slice that answers the goal.
- Tools: hydra, nmap
- Reasoning chain:
  - Recognize the goal as hydra-driven evidence lookup.
  - Use hydra, nmap to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `beginners out there.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
