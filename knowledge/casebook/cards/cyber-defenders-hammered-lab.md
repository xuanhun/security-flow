# Hammered Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_hammered_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for ids, linux-logs, web-service challenges.

## Input Signals

- Artifacts: ids, linux-logs, web-service
- Tools: exiftool, nmap, strings
- Techniques: dns-analysis, http-analysis, malware-static, service-enumeration, stego-extraction

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: Which service did the attackers use to gain access to the system?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use exiftool, nmap, strings with the extracted filter/query `grep -i "authentication failure" auth.log | cut -d ' ' -f4,6,7,8,13,14 |` and inspect the matching evidence.
- Tools: exiftool, nmap, strings
- Filters or commands:
  - `grep -i "authentication failure" auth.log | cut -d ' ' -f4,6,7,8,13,14 |`
  - `sort | uniq -c | sort -nr`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use exiftool, nmap, strings with the extracted filter/query `grep -i "authentication failure" auth.log | cut -d ' ' -f4,6,7,8,13,14 |` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ssh`

### Step 2: What is the operating system version of the targeted system?

- Route type: `exiftool-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use exiftool, nmap, strings to collect the smallest evidence slice that answers the goal.
- Tools: exiftool, nmap, strings
- Reasoning chain:
  - Recognize the goal as exiftool-driven evidence lookup.
  - Use exiftool, nmap, strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `4.2.4-1ubuntu3`

### Step 3: What is the name of the compromised account?

- Route type: `exiftool-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use exiftool, nmap, strings to collect the smallest evidence slice that answers the goal.
- Tools: exiftool, nmap, strings
- Reasoning chain:
  - Recognize the goal as exiftool-driven evidence lookup.
  - Use exiftool, nmap, strings to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 4: extract another field, you can see that bulk of these failed authentication attempts are targeting the root user:

- Route type: `exiftool-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use exiftool, nmap, strings with the extracted filter/query `grep -i "authentication failure" auth.log | cut -d ' ' -f10 | sort | uniq -` and inspect the matching evidence.
- Tools: exiftool, nmap, strings
- Filters or commands:
  - `grep -i "authentication failure" auth.log | cut -d ' ' -f10 | sort | uniq -`
  - `c | sort -nr`
- Reasoning chain:
  - Recognize the goal as exiftool-driven evidence lookup.
  - Use exiftool, nmap, strings with the extracted filter/query `grep -i "authentication failure" auth.log | cut -d ' ' -f10 | sort | uniq -` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `root`

### Step 5: access the system after initial failed attempts?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use exiftool, nmap, strings with the extracted filter/query `comm -12 <(grep "Failed password for root" auth.log | awk` and inspect the matching evidence.
- Tools: exiftool, nmap, strings
- Filters or commands:
  - `comm -12 <(grep "Failed password for root" auth.log | awk`
  - `'{for(i=1;i<=NF;i++) if($i=="from") print $(i+1)}' | sort | uniq)`
  - `<(grep "Accepted password for root" auth.log | awk '{for(i=1;i<=NF;i++)`
  - `if($i=="from") print $(i+1)}' | sort | uniq)`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use exiftool, nmap, strings with the extracted filter/query `comm -12 <(grep "Failed password for root" auth.log | awk` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `if($i=="from") print $(i+1)}' | sort | uniq)`

### Step 6: root user after conducting a brute force attack.

- Route type: `exiftool-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use exiftool, nmap, strings to collect the smallest evidence slice that answers the goal.
- Tools: exiftool, nmap, strings
- Reasoning chain:
  - Recognize the goal as exiftool-driven evidence lookup.
  - Use exiftool, nmap, strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `6`

### Step 7: Which attacker's IP address successfully logged into the system the most number of times?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use exiftool, nmap, strings with the extracted filter/query `grep -i "accepted password for root" auth.log | cut -d ' ' -f11 | sort |` and inspect the matching evidence.
- Tools: exiftool, nmap, strings
- Filters or commands:
  - `grep -i "accepted password for root" auth.log | cut -d ' ' -f11 | sort |`
  - `uniq -c | sort -nr`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use exiftool, nmap, strings with the extracted filter/query `grep -i "accepted password for root" auth.log | cut -d ' ' -f11 | sort |` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `219.150.161.20`

### Step 8: How many requests were sent to the Apache Server?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use exiftool, nmap, strings with the extracted filter/query `cat www-access.log | wc -l` and inspect the matching evidence.
- Tools: exiftool, nmap, strings
- Filters or commands:
  - `cat www-access.log | wc -l`
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use exiftool, nmap, strings with the extracted filter/query `cat www-access.log | wc -l` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `365`

### Step 9: How many rules have been added to the firewall?

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use nmap with the extracted filter/query `grep -i COMMAND auth.log` and inspect the matching evidence.
- Tools: nmap
- Filters or commands:
  - `grep -i COMMAND auth.log`
  - `grep -i iptables auth.log`
  - `grep nmap dpkg.log`
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use nmap with the extracted filter/query `grep -i COMMAND auth.log` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6`

### Step 10: When was the last login from the attacker with IP 219.150.161.20? Format: MM/DD/YYYY HH:MM:SS AM

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use exiftool with the extracted filter/query `grep -i "accepted password" auth.log | grep 219.150.161.20` and inspect the matching evidence.
- Tools: exiftool
- Filters or commands:
  - `grep -i "accepted password" auth.log | grep 219.150.161.20`
  - `exiftool auth.log`
  - `grep -i "sql" daemon.log | grep -i "warning"`
  - `contains 2 root accounts without password!`
  - `Answer: mysql.user contains 2 root accounts without password!`
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use exiftool with the extracted filter/query `grep -i "accepted password" auth.log | grep 219.150.161.20` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2010-04-19 05:56`

### Step 11: 26 at 04:43:15?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use exiftool, nmap, strings with the extracted filter/query `grep -i useradd auth.log` and inspect the matching evidence.
- Tools: exiftool, nmap, strings
- Filters or commands:
  - `grep -i useradd auth.log`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use exiftool, nmap, strings with the extracted filter/query `grep -i useradd auth.log` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `wind3str0y`

### Step 12: used by this proxy?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use strings with the extracted filter/query `cat www-access.log | cut -d ' ' -f12 | sort | uniq -c | sort -nr` and inspect the matching evidence.
- Tools: strings
- Filters or commands:
  - `cat www-access.log | cut -d ' ' -f12 | sort | uniq -c | sort -nr`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use strings with the extracted filter/query `cat www-access.log | cut -d ' ' -f12 | sort | uniq -c | sort -nr` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `pxyscand/2.1`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
