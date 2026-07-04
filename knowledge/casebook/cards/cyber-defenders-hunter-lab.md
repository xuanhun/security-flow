# Hunter Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_hunter_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, email, ids challenges.

## Input Signals

- Artifacts: disk-image, email, ids, pe-malware, registry, web-service, windows-events
- Tools: burp, db-browser-sqlite, evtxecmd, ftk-imager, nmap, pecmd, registry-explorer
- Techniques: browser-forensics, dns-analysis, http-analysis, registry-forensics, service-enumeration, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the computer name of the suspect machine?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `4ORENSICS`

### Step 2: What is the computer IP?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `10.0.2.15`

### Step 3: What was the DHCP LeaseObtainedTime?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to align timestamps and identify the event that satisfies the question.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `21/06/2016 02:24:12 UTC`

### Step 4: What is the computer SID?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `S-1-5-21-2489440558-2754304563-710705792`

### Step 5: What is the Operating System(OS) version?

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `8.1`

### Step 6: What was the computer timezone?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to align timestamps and identify the event that satisfies the question.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `UTC-07:00`

### Step 7: How many times did this user log on to the computer?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `3`

### Step 8: When was the last login time for the discovered account? Format: one-space between date and time

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, nmap, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2016-06-21 01:42:40`

### Step 9: When did the port scan end? (Example: Sat Jan 23 hh:mm:ss 2016)

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, nmap with the extracted filter/query `Zenmap. In the home directory of ‘Hunter’ we can see a directory for zenmap that likely contains` and inspect the matching evidence.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, nmap, pecmd, registry-explorer
- Filters or commands:
  - `Zenmap. In the home directory of ‘Hunter’ we can see a directory for zenmap that likely contains`
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, nmap with the extracted filter/query `Zenmap. In the home directory of ‘Hunter’ we can see a directory for zenmap that likely contains` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Tue Jun 21 05:12:09 2016`

### Step 10: How many ports were scanned?

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1000`

### Step 11: What ports were found "open"?(comma-separated, ascending)

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, nmap to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, nmap, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, nmap to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - The proof is the service enumeration result and the exact access or escalation condition.
- Evidence rule: The proof is the service enumeration result and the exact access or escalation condition.

### Step 12: find the following open ports:

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `22,80,9929,31337`

### Step 13: What was the version of the network scanner running on this computer?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, nmap with the extracted filter/query `folder. Here we can find a folder called ‘zenmap_version’ that contains the version of zenmap` and inspect the matching evidence.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, nmap, pecmd, registry-explorer
- Filters or commands:
  - `folder. Here we can find a folder called ‘zenmap_version’ that contains the version of zenmap`
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, nmap with the extracted filter/query `folder. Here we can find a folder called ‘zenmap_version’ that contains the version of zenmap` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7.12`

### Step 14: username of the other party?

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `linux-rul3z`

### Step 15: provide remote access for the external attacker in their Skype conversation?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `teamviewer`

### Step 16: What is the Gmail email address of the suspect employee?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ehptmsgs@gmail.com`

### Step 17: external attacker. What is the file name of the deleted diagram?

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `home-network-design-networking-for-a-single-family-home-case-house-arkko-1433-x-`

### Step 18: techniques. What is the name of the file?

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Ryan_VanAntwerp_thesis.pdf`

### Step 19: What was the name of the Disk Encryption application Installed on the victim system? (two words space separated)

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd with the extracted filter/query `On Windows, the Program Files folder is a system folder that contains installed programs. If we` and inspect the matching evidence.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Filters or commands:
  - `On Windows, the Program Files folder is a system folder that contains installed programs. If we`
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd with the extracted filter/query `On Windows, the Program Files folder is a system folder that contains installed programs. If we` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Crypto Swap`

### Step 20: What are the serial numbers of the two identified USB storage?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `07B20C03C80830A9,AAI6UXDKZDV8E9OU`

### Step 21: One of the installed applications is a file shredder. What is the name of the application?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to align timestamps and identify the event that satisfies the question.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Jetico BCWipe`

### Step 22: How many prefetch files were discovered on the system?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to align timestamps and identify the event that satisfies the question.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `174`

### Step 23: How many times was the file shredder application executed?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, nmap to align timestamps and identify the event that satisfies the question.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, nmap, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, nmap to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5`

### Step 24: of the file?

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use burp, db-browser-sqlite, evtxecmd, ftk-imager to recover or open the referenced file and inspect its metadata fields.
- Tools: burp, db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use burp, db-browser-sqlite, evtxecmd, ftk-imager to recover or open the referenced file and inspect its metadata fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\Hunter\Downloads\Burpsuite_free_v1.7.03.jar`

### Step 25: the name of the suspected attachment?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to align timestamps and identify the event that satisfies the question.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Pictures.7z`

### Step 26: exfiltrate. What is the full path of that folder?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\Hunter\Pictures\Exfil`

### Step 27: the file name that has the resolution of 1920x1200?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to align timestamps and identify the event that satisfies the question.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ws_small_cute_kitty_1920x1200.jpg`

### Step 28: automatically by the system) is stored?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, pecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `AutomaticDestinations`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
