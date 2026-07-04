# NSSCTF 2nd-MyHurricane

## Case Metadata

- Category: `Web`
- Platform: `NSSCTF 2nd`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/NSSCTF 2nd-MyHurricane.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/NSSCTF%202nd-MyHurricane.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/NSSCTF 2nd-MyHurricane.md`
- Challenge URL: `https://www.nssctf.cn/problem/4283`

## Why This Case Matters

Use this case as a Web reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: Yakit, netcat
- Techniques: command-injection, http-analysis, ssti, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `2`
- `web/images/NSSCTF 2nd-MyHurricane-nc.png`
- `web/images/NSSCTF 2nd-MyHurricane-flag.png`

## Solve Thinking

### Step 1: 解题思路

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use Yakit, netcat to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
- Tools: Yakit, netcat
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use Yakit, netcat to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `源码直接告诉我们拦截关键词，省去了Fuzz探测的过程`

### Step 2: 过程和结果记录

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use netcat with the extracted filter/query `nc -lvp 9999` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `nc -lvp 9999`
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use netcat with the extracted filter/query `nc -lvp 9999` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `成功获取 flag 的结果如下：`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
