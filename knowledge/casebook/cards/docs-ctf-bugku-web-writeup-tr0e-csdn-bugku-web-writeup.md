# CTF解题-Bugku_Web_WriteUp (上）_Tr0e的博客-CSDN博客_bugku web writeup

## Case Metadata

- Category: `Web`
- Platform: `CTF解题`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF解题-Bugku_Web_WriteUp-(上）_Tr0e的博客-CSDN博客_bugku-web-writeup.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%E8%A7%A3%E9%A2%98-Bugku_Web_WriteUp-%28%E4%B8%8A%EF%BC%89_Tr0e%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_bugku-web-writeup.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF解题-Bugku_Web_WriteUp-(上）_Tr0e的博客-CSDN博客_bugku-web-writeup.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, email, web-app challenges.

## Input Signals

- Artifacts: ciphertext, email, web-app, web-service
- Tools: burp, detect-it-easy, netcat, sqlmap
- Techniques: classical-crypto, command-injection, crypto-analysis, deserialization, email-header-analysis, encoding-analysis, file-inclusion, file-upload, http-analysis, php-tricks, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `101`
- `docs/img/2ccdd07c1c7d954f8663a005ea591f09.png`
- `docs/img/615063739a671bdd63f73063c3a5e162.png`
- `docs/img/f4335079cf03152117f16207572366e7.png`
- `docs/img/8abd72b65fc605fa26729d43abfc920a.png`
- `docs/img/fb253c5591e6c83104c54f23e0f3d6ab.png`
- `docs/img/f9c1b0add8cc5a5ef2061d6b88a78dba.png`
- `docs/img/3fcc7ef158922d077896e29b5eea8243.png`
- `docs/img/ec9d5e19f726f62a776ff4556324470c.png`
- `docs/img/7d221167584abef750d445f67f09c86f.png`
- `docs/img/92111ffd461554ef68d0acf2c90b5d5e.png`
- `docs/img/4c22f7a379a16e37979610a6153bfee4.png`
- `docs/img/c5449702bb64e3daf52724c8d754307d.png`
- ... and `89` more

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, sqlmap
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF解题-Bugku_Web_WriteUp (上）_Tr0e的博客-CSDN博客_bugku web writeup

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, netcat, sqlmap
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2ccdd07c1c7d954f8663a005ea591f09`

### Step 3: N0.1 前端信息泄露

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, sqlmap
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `f4335079cf03152117f16207572366e7`

### Step 4: No.2 绕过前端限制

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use burp, detect-it-easy, netcat, sqlmap to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: burp, detect-it-easy, netcat, sqlmap
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use burp, detect-it-easy, netcat, sqlmap to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `f9c1b0add8cc5a5ef2061d6b88a78dba`

### Step 5: No.3 GET传参

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, sqlmap
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3fcc7ef158922d077896e29b5eea8243`

### Step 6: No.4 POST传参

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, sqlmap
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7d221167584abef750d445f67f09c86f`

### Step 7: No.5 科学计数法

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, sqlmap
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `4c22f7a379a16e37979610a6153bfee4`

### Step 8: No.6 Unicode转码

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, sqlmap
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1a5306ef35da6899c7f5fe3a2a0195a4`

### Step 9: No.7 本地域名解析

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, netcat, sqlmap
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `17c0fb1049b3d677efe5c42a9c75f919`

### Step 10: No.8 数据包重放

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, sqlmap
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `9f6051c10be0891fa0fa142963be78b7`

### Step 11: No.9 本地包含

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, sqlmap
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `题目有问题……`

### Step 12: No.10 PHP全局变量

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, sqlmap
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `cfc03aadeafb54c47262c418324362a4`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
