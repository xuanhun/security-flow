# Openfire Lab

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_openfire_lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for pcap challenges.

## Input Signals

- Artifacts: pcap
- Tools: cyberchef, wireshark
- Techniques: dns-analysis, http-analysis, network-forensics, service-enumeration

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: What is the CSRF token value for the first login request?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use cyberchef, wireshark with the extracted filter/query `TLDR: Filter for POST requests made to a URI that contains “login”. You can navigate to Statistics` and inspect the matching evidence.
- Tools: cyberchef, wireshark
- Filters or commands:
  - `TLDR: Filter for POST requests made to a URI that contains “login”. You can navigate to Statistics`
  - `ip.dst==192.168.18.155 && http.request.uri contains "login" &&`
  - `http.request.method=="POST"`
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use cyberchef, wireshark with the extracted filter/query `TLDR: Filter for POST requests made to a URI that contains “login”. You can navigate to Statistics` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `tmJU6J9uym8oIOD`

### Step 2: What is the password of the first user who logged in?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use cyberchef, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: cyberchef, wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use cyberchef, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Admin@Passw0rd#@#`

### Step 3: What is the 1st username that was created by the attacker?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, wireshark with the extracted filter/query `ip.src==192.168.18.160 && http.request.method==POST` and inspect the matching evidence.
- Tools: cyberchef, wireshark
- Filters or commands:
  - `ip.src==192.168.18.160 && http.request.method==POST`
  - `ip.src==192.168.18.160 && http.request.method==GET`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, wireshark with the extracted filter/query `ip.src==192.168.18.160 && http.request.method==POST` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3536rr`

### Step 4: What is the username that the attacker used to login to the admin panel?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use cyberchef, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: cyberchef, wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use cyberchef, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a7zo4l`

### Step 5: What is the name of the plugin that the attacker uploaded?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, wireshark
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `openfire-plugin.jar`

### Step 6: What is the first command that the user executed?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, wireshark with the extracted filter/query `ip.src==192.168.18.160 && http.request.method==POST` and inspect the matching evidence.
- Tools: cyberchef, wireshark
- Filters or commands:
  - `ip.src==192.168.18.160 && http.request.method==POST`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, wireshark with the extracted filter/query `ip.src==192.168.18.160 && http.request.method==POST` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `whoami`

### Step 7: Which tool did the attacker use to get a reverse shell?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, wireshark
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `netcat`

### Step 8: Which command did the attacker execute on the server to check for network interfaces?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, wireshark with the extracted filter/query `ip.addr==192.168.18.160 && tcp.port==8888` and inspect the matching evidence.
- Tools: cyberchef, wireshark
- Filters or commands:
  - `ip.addr==192.168.18.160 && tcp.port==8888`
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, wireshark with the extracted filter/query `ip.addr==192.168.18.160 && tcp.port==8888` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ifconfig`

### Step 9: What is the CVE of the vulnerability exploited?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, wireshark with the extracted filter/query `event_type=="alert"` and inspect the matching evidence.
- Tools: cyberchef, wireshark
- Filters or commands:
  - `event_type=="alert"`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, wireshark with the extracted filter/query `event_type=="alert"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `CVE-2023-32315`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
