# [NSSRound#18]门酱想玩什么呢

## Case Metadata

- Category: `Web`
- Platform: `NSSRound#18`
- Difficulty: `中等`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/NSSRound#18门酱想玩什么呢.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/NSSRound%2318%E9%97%A8%E9%85%B1%E6%83%B3%E7%8E%A9%E4%BB%80%E4%B9%88%E5%91%A2.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/NSSRound#18门酱想玩什么呢.md`
- Challenge URL: `https://www.nssctf.cn/problem/5123`

## Why This Case Matters

Use this case as a Web reference for stego-media, web-app challenges.

## Input Signals

- Artifacts: stego-media, web-app
- Tools: 无, netcat
- Techniques: dns-analysis, http-analysis, waf-bypass, web-exploitation, xss

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `5`
- `web/images/3-19题目wp_index.png`
- `web/images/3-19题目wp_baidu.com.png`
- `web/images/3-19题目wp_message_pad.png`
- `web/images/3-19题目wp_test.png`
- `web/images/3-19题目wp_3xss.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as xss route.
  - Use netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `这是一个典型的留言板系统，通常是存储型XSS的常见目标。`

### Step 2: 想到什么解题思路

- Route type: `无-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use 无, netcat to collect the smallest evidence slice that answers the goal.
- Tools: 无, netcat
- Reasoning chain:
  - Recognize the section as 无-driven evidence lookup.
  - Use 无, netcat to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 3: 尝试过程和结果记录

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use 无, netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
- Tools: 无, netcat
- Reasoning chain:
  - Recognize the section as xss route.
  - Use 无, netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `"门酱"访问后会被重定向到元梦之星，我们获得flag。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
