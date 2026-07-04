# [SWPUCTF 2021 新生赛]easyupload1.0

## Case Metadata

- Category: `Web`
- Platform: `SWPUCTF 2021 新生赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/SWPUCTF2021新生赛-easyupload1.0.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/SWPUCTF2021%E6%96%B0%E7%94%9F%E8%B5%9B-easyupload1.0.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/SWPUCTF2021新生赛-easyupload1.0.md`
- Challenge URL: `https://www.nssctf.cn/problem/388`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: Yakit, 蚁剑
- Techniques: command-injection, file-upload, http-analysis, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `4`
- `web/<images/[SWPUCTF 2021 新生赛]easyupload1.0-yakit.jpg>`
- `web/<images/[SWPUCTF 2021 新生赛]easyupload1.0-antsword-connect.jpg>`
- `web/<images/[SWPUCTF 2021 新生赛]easyupload1.0-find_flag.jpg>`
- `web/<images/[SWPUCTF 2021 新生赛]easyupload1.0-env.jpg>`

## Solve Thinking

### Step 1: 看到什么

- Route type: `Yakit-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use Yakit, 蚁剑 to collect the smallest evidence slice that answers the goal.
- Tools: Yakit, 蚁剑
- Reasoning chain:
  - Recognize the section as Yakit-driven evidence lookup.
  - Use Yakit, 蚁剑 to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 2: 想到什么解题思路

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use Yakit, 蚁剑 to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: Yakit, 蚁剑
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use Yakit, 蚁剑 to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 3: 尝试过程和结果记录

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use antsword, yakit to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: antsword, yakit
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use antsword, yakit to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `![alt text](<images/[SWPUCTF 2021 新生赛]easyupload1.0-env.jpg>)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
