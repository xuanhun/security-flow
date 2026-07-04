# [NISACTF 2022]popchains

## Case Metadata

- Category: `Web`
- Platform: `NISACTF 2022`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/NISACTF2022-popchains.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/NISACTF2022-popchains.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/NISACTF2022-popchains.md`
- Challenge URL: `https://www.nssctf.cn/problem/2099`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: PHP环境, hackbar, netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, deserialization, encoding-analysis, file-inclusion, http-analysis, php-tricks, ret2libc, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

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

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag.php`

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
- Result: `flag.php`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
