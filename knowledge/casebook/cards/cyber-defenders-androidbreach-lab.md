# AndroidBreach Lab

## Case Metadata

- Category: `Mobile Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_androidbreach_lab.pdf`

## Why This Case Matters

Use this case as a Mobile Forensics reference for apk-mobile, email challenges.

## Input Signals

- Artifacts: apk-mobile, email
- Tools: cyberchef, jadx
- Techniques: browser-forensics, http-analysis, mobile-forensics

## First-Principles Route

- Inventory app/database artifacts, timestamps, media, account records, and package metadata.
- Extract SQLite, plist/XML/JSON, and app-specific records before guessing behavior.

## Solve Thinking

### Step 1: investigation?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, jadx to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, jadx
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, jadx to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `https://ufile.io/57rdyncx`

### Step 2: What is the name of the downloaded APK?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Mobile Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, jadx to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, jadx
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, jadx to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Discord_nitro_Mod.apk`

### Step 3: What is the malicious package name found in the APK?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Mobile Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, jadx to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, jadx
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, jadx to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `names.`

### Step 4: When going through the AndroidManifest.xml file, which is a critical configuration file in every

- Route type: `cyberchef-driven evidence lookup`
- Why: For Mobile Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, jadx to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, jadx
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, jadx to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `com.example.keylogger`

### Step 5: Which port was used to exfiltrate the data?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Mobile Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, jadx to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, jadx
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, jadx to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `465`

### Step 6: What is the service platform name the attacker utilized to receive the data being exfiltrated?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Mobile Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, jadx to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, jadx
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, jadx to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `mailtrap.io`

### Step 7: What email was used by the attacker when exfiltrating data?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use cyberchef, jadx to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: cyberchef, jadx
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use cyberchef, jadx to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `APThreat@gmail.com`

### Step 8: exfiltrate it. Based on the data, can you retrieve the credentials found in the leak?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use cyberchef, jadx to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: cyberchef, jadx
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use cyberchef, jadx to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `hany.tarek@brightwave.com:HTarek@9711$QTPO309`

### Step 9: encryption key used by the malware to encrypt these images?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Mobile Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, jadx to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, jadx
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, jadx to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 10: determine that it is used for encrypting data using AES:

- Route type: `cyberchef-driven evidence lookup`
- Why: For Mobile Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, jadx to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, jadx
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, jadx to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `9bY$wQ7!cTz465TX`

### Step 11: information. What is the CVC of the credit card stored?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Mobile Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, jadx to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, jadx
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, jadx to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `128`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
