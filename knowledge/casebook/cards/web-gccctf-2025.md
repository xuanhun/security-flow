# 技能五子棋

## Case Metadata

- Category: `Web`
- Platform: `GCCCTF 2025`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/[GCCCTF 2025]技能五子棋.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/%5BGCCCTF%202025%5D%E6%8A%80%E8%83%BD%E4%BA%94%E5%AD%90%E6%A3%8B.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/[GCCCTF 2025]技能五子棋.md`
- Challenge URL: `[[GCCCTF 2025]技能五子棋 | NSSCTF](https://www.nssctf.cn/problem/7165)`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app, web-service
- Tools: burp, netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, encoding-analysis, http-analysis, ssti, waf-bypass, web-exploitation, xss

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `4`
- `web/images/技能五子棋.png`
- `web/images/技能五子棋-1.png`
- `web/images/技能五子棋-2.png`
- `web/images/技能五子棋-3.png`

## Solve Thinking

### Step 1: 解题思路

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use burp, netcat with the extracted filter/query `const prohibitedPattern = /<(script|img|iframe|svg|math|object|embed|link|style|video|audio|source|meta|base|form|input|textarea|button)[^>]*>|on[a-z]+\s*=|javascript:|data:text\/html/i` and inspect the matching evidence.
- Tools: burp, netcat
- Filters or commands:
  - `const prohibitedPattern = /<(script|img|iframe|svg|math|object|embed|link|style|video|audio|source|meta|base|form|input|textarea|button)[^>]*>|on[a-z]+\s*=|javascript:|data:text\/html/i`
  - `from http.server import HTTPServer, BaseHTTPRequestHandler`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use burp, netcat with the extracted filter/query `const prohibitedPattern = /<(script|img|iframe|svg|math|object|embed|link|style|video|audio|source|meta|base|form|input|textarea|button)[^>]*>|on[a-z]+\s*=|javascript:|data:text\/html/i` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0.0.0.0`

### Step 2: 启动HTTP服务器

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0.0.0.0`

### Step 3: 发送XSS

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as xss route.
  - Use netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `return`

### Step 4: 等待结果

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat with the extracted filter/query `print(f"[+] Sending move: ({row}, {col}) | Signature: {sig[:32]}...")` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `print(f"[+] Sending move: ({row}, {col}) | Signature: {sig[:32]}...")`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat with the extracted filter/query `print(f"[+] Sending move: ({row}, {col}) | Signature: {sig[:32]}...")` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c7b846b1b997f813550589b3da164625`

### Step 5: 忽略 board 等中间消息，继续等待 gameOver

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `最终获得 flag`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
