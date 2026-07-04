# Kerberoasted Lab

## Case Metadata

- Category: `SIEM (ELK, Splunk, etc.)`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_kerberoasted_lab.pdf`

## Why This Case Matters

Use this case as a SIEM (ELK, Splunk, etc.) reference for registry, siem, windows-events challenges.

## Input Signals

- Artifacts: registry, siem, windows-events
- Tools: elk, john
- Techniques: dns-analysis, http-analysis, password-cracking, siem-query, timeline-analysis, windows-event-analysis

## First-Principles Route

- Translate the question into searchable fields such as host, user, process, index, sourcetype, URI, IP, hash, or event code.
- Run broad time-bounded searches first, then narrow by event type, field value, and correlation chain.
- Keep the exact query shape and the evidence field that proves each answer.

## Solve Thinking

### Step 1: Kerberos protocol uses. What encryption type is currently in use within the network?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use elk with the extracted filter/query `event.code : 4768` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `event.code : 4768`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use elk with the extracted filter/query `event.code : 4768` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `RC4-HMAC`

### Step 2: (TGS) for two distinct application services within a short timeframe?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk, john with the extracted filter/query `event.code : 4769` and inspect the matching evidence.
- Tools: elk, john
- Filters or commands:
  - `event.code : 4769`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk, john with the extracted filter/query `event.code : 4769` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `johndoe`

### Step 3: you provide the account name of the compromised service account?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use elk, john with the extracted filter/query `event.code: 4624 and @timestamp > "2023-10-16T07:37:34.740Z"` and inspect the matching evidence.
- Tools: elk, john
- Filters or commands:
  - `event.code: 4624 and @timestamp > "2023-10-16T07:37:34.740Z"`
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use elk, john with the extracted filter/query `event.code: 4624 and @timestamp > "2023-10-16T07:37:34.740Z"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `SQLService`

### Step 4: by the attacker. What is the machine's IP address?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk with the extracted filter/query `event.code: 4624 and winlog.event_data.TargetUserName : "SQLService"` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `event.code: 4624 and winlog.event_data.TargetUserName : "SQLService"`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk with the extracted filter/query `event.code: 4624 and winlog.event_data.TargetUserName : "SQLService"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `10.0.0.154`

### Step 5: account, can you specify the service name installed on the Domain Controller (DC)?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk with the extracted filter/query `event.code : "7045"` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `event.code : "7045"`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk with the extracted filter/query `event.code : "7045"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `iOOEDsXjWeGRAyGl`

### Step 6: where the attacker modified the value to enable Remote Desktop Protocol (RDP)?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 7: which logs each time a registry value is written or modified:

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use elk with the extracted filter/query `event.provider : "Microsoft-Windows-Sysmon" AND event.code : "13"` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `event.provider : "Microsoft-Windows-Sysmon" AND event.code : "13"`
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use elk with the extracted filter/query `event.provider : "Microsoft-Windows-Sysmon" AND event.code : "13"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `HKLM\System\CurrentControlSet\Control\Terminal Server\fDenyTSConnections`

### Step 8: When a user authenticates via RDP , it generates EID 4624 with logon type 10 on the target host.

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk with the extracted filter/query `event.code : 4624 AND winlog.event_data.LogonType : 10` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `event.code : 4624 AND winlog.event_data.LogonType : 10`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk with the extracted filter/query `event.code : 4624 AND winlog.event_data.LogonType : 10` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2023-10-16 07:50`

### Step 9: WMI event consumer responsible for maintaining persistence?

- Route type: `elk-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk to collect the smallest evidence slice that answers the goal.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as elk-driven evidence lookup.
  - Use elk to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Consumer is called.`

### Step 10: when an event occurs that matches the defined filter, the action specified in the consumer must occur.

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use elk with the extracted filter/query `event.provider : "Microsoft-Windows-Sysmon" AND event.code : "20"` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `event.provider : "Microsoft-Windows-Sysmon" AND event.code : "20"`
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use elk with the extracted filter/query `event.provider : "Microsoft-Windows-Sysmon" AND event.code : "20"` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Updater`

### Step 11: Which class does the WMI event subscription filter target in the WMI Event Subscription you've identified?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use elk, john with the extracted filter/query `event.provider : "Microsoft-Windows-Sysmon" AND event.code : "19"` and inspect the matching evidence.
- Tools: elk, john
- Filters or commands:
  - `event.provider : "Microsoft-Windows-Sysmon" AND event.code : "19"`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use elk, john with the extracted filter/query `event.provider : "Microsoft-Windows-Sysmon" AND event.code : "19"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Win32_NTLogEvent`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
