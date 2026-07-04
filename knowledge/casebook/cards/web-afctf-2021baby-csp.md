# [AFCTF 2021]BABY_CSP

## Case Metadata

- Category: `Web`
- Platform: `AFCTF 2021`
- Difficulty: `简单`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/AFCTF 2021BABY_CSP.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/AFCTF%202021BABY_CSP.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/AFCTF 2021BABY_CSP.md`
- Challenge URL: `https://www.nssctf.cn/problem/1409`

## Why This Case Matters

Use this case as a Web reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: 无, netcat
- Techniques: http-analysis, waf-bypass, web-exploitation, xss

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `3`
- `web/images/3-19题目wp_index-1.png`
- `web/images/3-19题目wp_source.png`
- `web/images/3-19题目wp_flag-1.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use 无, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: 无, netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use 无, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `查看网页源代码：`

### Step 2: 想到什么解题思路

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 3: 尝试过程和结果记录

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `提交后查看页面源代码，成功获取flag：`

### Step 4: 参考链接：

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use 无, netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: 无, netcat
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use 无, netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- [CSP绕过技巧](https://blog.csdn.net/weixin_42478365/article/details/116597764)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
