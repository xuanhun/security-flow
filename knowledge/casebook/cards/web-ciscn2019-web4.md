# [CISCN 2019华东南]Web4

## Case Metadata

- Category: `Web`
- Platform: `CISCN 2019华东南`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/CISCN2019华东南-Web4.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/CISCN2019%E5%8D%8E%E4%B8%9C%E5%8D%97-Web4.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/CISCN2019华东南-Web4.md`
- Challenge URL: `https://www.nssctf.cn/problem/6`

## Why This Case Matters

Use this case as a Web reference for binary, disk-image, web-app challenges.

## Input Signals

- Artifacts: binary, disk-image, web-app
- Tools: python2 环境, netcat
- Techniques: crypto-analysis, encoding-analysis, http-analysis, ssti, timeline-analysis, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `2`
- `web/images/CISCN2019华东南-Web4-getCookie.png`
- `web/images/CISCN2019华东南-Web4-setCookie.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use python2 环境, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: python2 环境, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use python2 环境, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- `Set-Cookie: session=eyJ1c2VybmFtZSI6eyIgYiI6ImQzZDNMV1JoZEdFPSJ9fQ.Z43Fcg.EOpviRtmep0wOvhzQYCWy-rJ7oA; HttpOnly; Path=/``

### Step 2: 想到什么解题思路

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use python2 环境, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: python2 环境, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use python2 环境, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 3: 尝试过程和结果记录

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use python2 环境, netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: python2 环境, netcat
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use python2 环境, netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `/proc/self/loginuid`

### Step 4: 4294967295

- Route type: `python2 环境-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use python2 环境, netcat to collect the smallest evidence slice that answers the goal.
- Tools: python2 环境, netcat
- Reasoning chain:
  - Recognize the section as python2 环境-driven evidence lookup.
  - Use python2 环境, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `/proc/self/environ`

### Step 5: HOME=/app

- Route type: `python2 环境-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use python2 环境, netcat to collect the smallest evidence slice that answers the goal.
- Tools: python2 环境, netcat
- Reasoning chain:
  - Recognize the section as python2 环境-driven evidence lookup.
  - Use python2 环境, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `/proc/self/cmdline`

### Step 6: /usr/local/bin/python /app/app.py

- Route type: `python2 环境-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use python2 环境, netcat to collect the smallest evidence slice that answers the goal.
- Tools: python2 环境, netcat
- Reasoning chain:
  - Recognize the section as python2 环境-driven evidence lookup.
  - Use python2 环境, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ````python`

### Step 7: encoding:utf-8

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use python2 环境, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: python2 环境, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use python2 环境, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0.0.0.0`

### Step 8: encoding:utf-8

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use python2 环境, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: python2 环境, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use python2 环境, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0.0.0.0`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
