# [FSCTF 2023]加速加速

## Case Metadata

- Category: `Web`
- Platform: `FSCTF 2023`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/[FSCTF 2023]加速加速.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/%5BFSCTF%202023%5D%E5%8A%A0%E9%80%9F%E5%8A%A0%E9%80%9F.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/[FSCTF 2023]加速加速.md`
- Challenge URL: `https://www.nssctf.cn/problem/4629`

## Why This Case Matters

Use this case as a Web reference for web-app, web-service challenges.

## Input Signals

- Artifacts: web-app, web-service
- Tools: yakit, burp, netcat
- Techniques: command-injection, file-inclusion, file-upload, http-analysis, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `7`
- `web/images/[FSCTF 2023]加速加速-上传图片.png`
- `web/images/[FSCTF 2023]加速加速-上传php.png`
- `web/images/[FSCTF 2023]加速加速-重复上传php.png`
- `web/images/[FSCTF 2023]加速加速-查看php.png`
- `web/images/[FSCTF 2023]加速加速-成功上传.png`
- `web/images/[FSCTF 2023]加速加速-蚁剑连接.png`
- `web/images/[FSCTF 2023]加速加速-获取flag.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use yakit, burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: yakit, burp, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use yakit, burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `**题目关键信息列表**：`

### Step 2: 想到什么解题思路

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use yakit, burp, netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: yakit, burp, netcat
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use yakit, burp, netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - The proof is the blocked primitive working through the filter path, not just a payload variation that reflects.
- Evidence rule: The proof is the blocked primitive working through the filter path, not just a payload variation that reflects.

### Step 3: 尝试过程和结果记录

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use burp, netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use burp, netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2.php`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
