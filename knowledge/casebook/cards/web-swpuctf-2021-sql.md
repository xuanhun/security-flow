# [SWPUCTF 2021 新生赛]sql

## Case Metadata

- Category: `Web`
- Platform: `SWPUCTF 2021 新生赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/[SWPUCTF 2021 新生赛]sql.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/%5BSWPUCTF%202021%20%E6%96%B0%E7%94%9F%E8%B5%9B%5Dsql.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/[SWPUCTF 2021 新生赛]sql.md`
- Challenge URL: `https://www.nssctf.cn/problem/442`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: Hackbar
- Techniques: dns-analysis, http-analysis, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Solve Thinking

### Step 1: 解题思路

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use Hackbar to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: Hackbar
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use Hackbar to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 2: 解题过程

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use Hackbar to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: Hackbar
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use Hackbar to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `最后拼接出 flag 是 `NSSCTF{1a1b08f7-39b2-4430-8d17-d315180fdae9}`。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
