# [HNCTF 2022 WEEK4]checker

## Case Metadata

- Category: `Pwn`
- Platform: `HNCTF 2022 WEEK4`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/checker.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/checker.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/checker.md`
- Challenge URL: `https://www.nssctf.cn/problem/3106`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: 无, netcat
- Techniques: binary-exploitation, crypto-analysis, http-analysis, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `4`
- `pwn/images/HNCTF_2022_WEEK4checker-html.png`
- `pwn/images/HNCTF_2022_WEEK4checker-code_info.png`
- `pwn/images/HNCTF_2022_WEEK4checker-encode.png`
- `pwn/images/HNCTF_2022_WEEK4checker-flag.png`

## Solve Thinking

### Step 1: 第一轮

- Route type: `无-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use 无, netcat to collect the smallest evidence slice that answers the goal.
- Tools: 无, netcat
- Reasoning chain:
  - Recognize the section as 无-driven evidence lookup.
  - Use 无, netcat to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 2: 第一轮

- Route type: `无-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use 无, netcat to collect the smallest evidence slice that answers the goal.
- Tools: 无, netcat
- Reasoning chain:
  - Recognize the section as 无-driven evidence lookup.
  - Use 无, netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 3: 第一轮

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `核心算法就是将b64形式的密码解码后与密钥流逐位异或（二元加法流密码）`

### Step 4: 本地工具环境配置

- Route type: `无-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use 无, netcat to collect the smallest evidence slice that answers the goal.
- Tools: 无, netcat
- Reasoning chain:
  - Recognize the section as 无-driven evidence lookup.
  - Use 无, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `无`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
