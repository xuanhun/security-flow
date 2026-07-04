# [NSSRound#30 Duo]hack_the_world!

## Case Metadata

- Category: `Web`
- Platform: `NSSRound#30 Duo`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/[NSSRound#30 Duo]hack_the_world!.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/%5BNSSRound%2330%20Duo%5Dhack_the_world%21.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/[NSSRound#30 Duo]hack_the_world!.md`
- Challenge URL: `https://www.nssctf.cn/problem/6672`

## Why This Case Matters

Use this case as a Web reference for ids, web-app, web-service challenges.

## Input Signals

- Artifacts: ids, web-app, web-service
- Tools: python环境, flask-unsign, burpsuite, yakit, burp, netcat
- Techniques: dns-analysis, http-analysis, jwt-analysis, ssti, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `2`
- `web/images/0528wp_dejwt.png`
- `web/images/0528wp_fuzzing.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use python环境, flask-unsign, burpsuite, yakit to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
- Tools: python环境, flask-unsign, burpsuite, yakit, burp
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use python环境, flask-unsign, burpsuite, yakit to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `下载附件后得到flask源码，进行代码审计，发现有ssti漏洞，不过有其他限制：session认证机制和一些过滤机制`

### Step 2: 想到什么解题思路

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use python环境, flask-unsign, burpsuite, yakit to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
- Tools: python环境, flask-unsign, burpsuite, yakit, burp
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use python环境, flask-unsign, burpsuite, yakit to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `针对于ssti漏洞可以尝试用fenjing在本地搭建的靶场来测试获得payload然后获得flag`

### Step 3: 尝试过程和结果记录

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use burp, netcat, yakit to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: burp, netcat, yakit
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use burp, netcat, yakit to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `然后发送后可以在前端的js文件中得到flag`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
