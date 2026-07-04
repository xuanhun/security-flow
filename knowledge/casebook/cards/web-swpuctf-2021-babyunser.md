# [SWPUCTF 2021 新生赛]babyunser

## Case Metadata

- Category: `Web`
- Platform: `SWPUCTF 2021 新生赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/[SWPUCTF 2021 新生赛]babyunser.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/%5BSWPUCTF%202021%20%E6%96%B0%E7%94%9F%E8%B5%9B%5Dbabyunser.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/[SWPUCTF 2021 新生赛]babyunser.md`
- Challenge URL: `http://node5.anna.nssctf.cn:27981`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: PHP环境, hackbar, netcat
- Techniques: command-injection, crypto-analysis, deserialization, file-upload, http-analysis, misc-analysis, php-tricks, ret2libc, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `2`
- `web/images/[SWPUCTF 2021 新生赛]babyunser-php.png`
- `web/images/[SWPUCTF 2021 新生赛]babyunser-flag.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `PHP环境-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use PHP环境, hackbar, netcat to collect the smallest evidence slice that answers the goal.
- Tools: PHP环境, hackbar, netcat
- Reasoning chain:
  - Recognize the section as PHP环境-driven evidence lookup.
  - Use PHP环境, hackbar, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `**题目关键信息列表**：`

### Step 2: 想到什么解题思路

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use PHP环境, hackbar, netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: PHP环境, hackbar, netcat
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use PHP环境, hackbar, netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `upload.php`

### Step 3: 尝试过程和结果记录

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6d2151e639ecf66fd66d1b8c51c78c12`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
