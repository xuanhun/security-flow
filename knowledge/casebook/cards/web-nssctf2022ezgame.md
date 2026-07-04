# [NSSCTF 2022]ezgame

## Case Metadata

- Category: `Web`
- Platform: `NSSCTF 2022`
- Difficulty: `轻松`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/NSSCTF2022ezgame.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/NSSCTF2022ezgame.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/NSSCTF2022ezgame.md`
- Challenge URL: `https://www.nssctf.cn/problem/2074`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: 无
- Techniques: http-analysis, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `2`
- `web/images/3-19题目wp_sources_code.png`
- `web/images/3-19题目wp_flag.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use 无 to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: 无
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use 无 to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `查看index源码，发现如下内容：`

### Step 2: 想到什么解题思路

- Route type: `无-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use 无 to collect the smallest evidence slice that answers the goal.
- Tools: 无
- Reasoning chain:
  - Recognize the section as 无-driven evidence lookup.
  - Use 无 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- ~~打游戏通关~~`

### Step 3: 尝试过程和结果记录

- Route type: `无-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use 无 to collect the smallest evidence slice that answers the goal.
- Tools: 无
- Reasoning chain:
  - Recognize the section as 无-driven evidence lookup.
  - Use 无 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `scorePoint = 1000000; // 设置分数高于65`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
