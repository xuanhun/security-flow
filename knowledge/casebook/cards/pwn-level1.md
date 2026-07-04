# [WUSTCTF 2020]level1

## Case Metadata

- Category: `Pwn`
- Platform: `WUSTCTF 2020`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/level1.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/level1.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/level1.md`
- Challenge URL: `https://www.nssctf.cn/problem/1996`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: IDA pro, ida
- Techniques: binary-exploitation, http-analysis, reverse-engineering, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `2`
- `pwn/images/WUSTCTF_2020level1-ida_1.png`
- `pwn/images/WUSTCTF_2020level1-F5.png`

## Solve Thinking

### Step 1: 第一轮

- Route type: `IDA pro-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use IDA pro, ida to collect the smallest evidence slice that answers the goal.
- Tools: IDA pro, ida
- Reasoning chain:
  - Recognize the section as IDA pro-driven evidence lookup.
  - Use IDA pro, ida to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 2: 第一轮

- Route type: `IDA pro-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use IDA pro, ida to collect the smallest evidence slice that answers the goal.
- Tools: IDA pro, ida
- Reasoning chain:
  - Recognize the section as IDA pro-driven evidence lookup.
  - Use IDA pro, ida to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 3: 第一轮

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - The proof is the code path, comparison, constant, or decoded data that explains the answer.
- Evidence rule: The proof is the code path, comparison, constant, or decoded data that explains the answer.

### Step 4: 第二轮

- Route type: `IDA pro-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use IDA pro, ida to collect the smallest evidence slice that answers the goal.
- Tools: IDA pro, ida
- Reasoning chain:
  - Recognize the section as IDA pro-driven evidence lookup.
  - Use IDA pro, ida to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: ````python`

### Step 5: list.py

- Route type: `IDA pro-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use IDA pro, ida to collect the smallest evidence slice that answers the goal.
- Tools: IDA pro, ida
- Reasoning chain:
  - Recognize the section as IDA pro-driven evidence lookup.
  - Use IDA pro, ida to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `输出得到flag。`

### Step 6: IDA Pro

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `因为自己用的是某不可信小站版本的ida，所以这里就不分享链接了，如有需求请自行搜索~`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
