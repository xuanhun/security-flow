# [NSSRound#13]TimeTrcer

## Case Metadata

- Category: `Web`
- Platform: `NSSRound#13`
- Difficulty: `困难`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/NSSRound#13TimeTrcer.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/NSSRound%2313TimeTrcer.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/NSSRound#13TimeTrcer.md`
- Challenge URL: `https://www.nssctf.cn/problem/4081`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: 无, netcat
- Techniques: command-injection, crypto-analysis, http-analysis, web-exploitation, xss

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `5`
- `web/images/3-19题目wp_index-2.png`
- `web/images/3-19题目wp_hint.png`
- `web/images/3-19题目wp_js.png`
- `web/images/3-19题目wp_note.png`
- `web/images/3-19题目wp_report.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use 无, netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
- Tools: 无, netcat
- Reasoning chain:
  - Recognize the section as xss route.
  - Use 无, netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `代码处理笔记的创建和访问，涉及hash和privateKey。`

### Step 2: 想到什么解题思路

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use 无, netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
- Tools: 无, netcat
- Reasoning chain:
  - Recognize the section as xss route.
  - Use 无, netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `在首页的note中构造相应的xss的payload来尝试去获取高权限（admin）的私钥`

### Step 3: 尝试过程和结果记录

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use netcat with the extracted filter/query `if(fetched == false){` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if(fetched == false){`
- Reasoning chain:
  - Recognize the section as xss route.
  - Use netcat with the extracted filter/query `if(fetched == false){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `};" />`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
