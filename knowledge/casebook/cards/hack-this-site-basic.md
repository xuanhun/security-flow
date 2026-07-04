# Basic

## Case Metadata

- Category: `Pentesting`
- Platform: `HackThisSite`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/hack_this_site_basic.pdf`

## Why This Case Matters

Use this case as a Pentesting reference for email, web-service challenges.

## Input Signals

- Artifacts: email, web-service
- Tools: burp, dirb, ida, john
- Techniques: http-analysis, password-cracking, reverse-engineering, web-enumeration

## First-Principles Route

- Begin with service discovery and directory/application enumeration.
- Map each exposed service to default credentials, known CVEs, misconfiguration, or content leaks.
- After initial access, enumerate local privilege escalation paths before exploitation.

## Solve Thinking

### Step 1: decode the logic and got the password “d489a490”. Level 7: Remote Code Execution (RCE)

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use burp, dirb, ida, john with the extracted filter/query `7 | P a g e` and inspect the matching evidence.
- Tools: burp, dirb, ida, john
- Filters or commands:
  - `7 | P a g e`
  - `8 | P a g e`
  - `9 | P a g e`
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use burp, dirb, ida, john with the extracted filter/query `7 | P a g e` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `index.php`

### Step 2: Access Control: Implement secure access control mechanisms to minimise exposure of

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use burp with the extracted filter/query `10 | P a g e` and inspect the matching evidence.
- Tools: burp
- Filters or commands:
  - `10 | P a g e`
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use burp with the extracted filter/query `10 | P a g e` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `10 | P a g e`

### Step 3: Sanitise User Input: Sanitise and escape user inputs, especially those that make system

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use burp to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: burp
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use burp to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `calls.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
