# [SDCTF 2022]jawt that down!

## Case Metadata

- Category: `Web`
- Platform: `SDCTF 2022`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/[SDCTF 2022]jawt that down!.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/%5BSDCTF%202022%5Djawt%20that%20down%21.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/[SDCTF 2022]jawt that down!.md`
- Challenge URL: `https://www.nssctf.cn/problem/2352`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: python环境, netcat, radare2
- Techniques: browser-forensics, crypto-analysis, http-analysis, jwt-analysis, osint, sql-injection, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `2`
- `web/images/0528wp_leak_passwd.png`
- `web/images/0528wp_de_jwt.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use python环境, netcat, radare2 to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: python环境, netcat, radare2
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use python环境, netcat, radare2 to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `扫目录看到一些路由，about里面都是一些人的unsplash主页，此外还有一个login的接口`

### Step 2: 想到什么解题思路

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use python环境, netcat, radare2 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: python环境, netcat, radare2
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use python环境, netcat, radare2 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `猜想这道题会不会是社工题，或者用about里面那些人的信息来登录，或者获取那些人的cookie等来登录，或者是sql注入`

### Step 3: 尝试过程和结果记录

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use python环境, netcat, radare2 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: python环境, netcat, radare2
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use python环境, netcat, radare2 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `import requests`

### Step 4: 目标URL

- Route type: `jwt trust-boundary abuse`
- Why: JWT cases hinge on understanding what the server actually trusts: signature, claim, header, or backend lookup.
- Probe: Use netcat, radare2 to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as jwt trust-boundary abuse.
  - Use netcat, radare2 to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `136.0.0.0`

### Step 5: 登录并获取JWT token，禁止自动重定向

- Route type: `jwt trust-boundary abuse`
- Why: JWT cases hinge on understanding what the server actually trusts: signature, claim, header, or backend lookup.
- Probe: Use python环境, netcat, radare2 to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
- Tools: python环境, netcat, radare2
- Reasoning chain:
  - Recognize the section as jwt trust-boundary abuse.
  - Use python环境, netcat, radare2 to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `login_response = requests.post(login_url, headers=login_headers, data=login_data, allow_redirects=False)`

### Step 6: 提取JWT token

- Route type: `jwt trust-boundary abuse`
- Why: JWT cases hinge on understanding what the server actually trusts: signature, claim, header, or backend lookup.
- Probe: Use python环境, netcat, radare2 to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
- Tools: python环境, netcat, radare2
- Reasoning chain:
  - Recognize the section as jwt trust-boundary abuse.
  - Use python环境, netcat, radare2 to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `return None`

### Step 7: 设置请求头部

- Route type: `jwt trust-boundary abuse`
- Why: JWT cases hinge on understanding what the server actually trusts: signature, claim, header, or backend lookup.
- Probe: Use netcat to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as jwt trust-boundary abuse.
  - Use netcat to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `136.0.0.0`

### Step 8: 目标URL

- Route type: `jwt trust-boundary abuse`
- Why: JWT cases hinge on understanding what the server actually trusts: signature, claim, header, or backend lookup.
- Probe: Use netcat, radare2 to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as jwt trust-boundary abuse.
  - Use netcat, radare2 to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `136.0.0.0`

### Step 9: 登录并获取JWT token，禁止自动重定向

- Route type: `jwt trust-boundary abuse`
- Why: JWT cases hinge on understanding what the server actually trusts: signature, claim, header, or backend lookup.
- Probe: Use python环境, netcat, radare2 to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
- Tools: python环境, netcat, radare2
- Reasoning chain:
  - Recognize the section as jwt trust-boundary abuse.
  - Use python环境, netcat, radare2 to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `login_response = requests.post(login_url, headers=login_headers, data=login_data, allow_redirects=False)`

### Step 10: 提取JWT token

- Route type: `jwt trust-boundary abuse`
- Why: JWT cases hinge on understanding what the server actually trusts: signature, claim, header, or backend lookup.
- Probe: Use python环境, netcat, radare2 to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
- Tools: python环境, netcat, radare2
- Reasoning chain:
  - Recognize the section as jwt trust-boundary abuse.
  - Use python环境, netcat, radare2 to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `return None`

### Step 11: 设置请求头部

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `136.0.0.0`

### Step 12: 开始获取flag

- Route type: `python环境-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use python环境, netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: python环境, netcat, radare2
- Reasoning chain:
  - Recognize the section as python环境-driven evidence lookup.
  - Use python环境, netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `print(f"当前路径: {flag}")`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
