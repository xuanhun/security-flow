# [SWPUCTF 2021 新生赛]gift_pwn

## Case Metadata

- Category: `Pwn`
- Platform: `SWPUCTF 2021 新生赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/[SWPUCTF 2021 新生赛]gift_pwn.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/%5BSWPUCTF%202021%20%E6%96%B0%E7%94%9F%E8%B5%9B%5Dgift_pwn.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/[SWPUCTF 2021 新生赛]gift_pwn.md`
- Challenge URL: `https://www.nssctf.cn/problem/390`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: ida, pwntools
- Techniques: binary-exploitation, command-injection, http-analysis, ret2libc, ret2text, reverse-engineering, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `4`
- `pwn/images/SWPUCTF_2021_gift_pwn-file.png`
- `pwn/images/SWPUCTF_2021_gift_pwn-vuln.png`
- `pwn/images/SWPUCTF_2021_gift_pwn-gift.png`
- `pwn/images/SWPUCTF_2021_gift_pwn-getshell.png`

## Solve Thinking

### Step 1: 附件分析

- Route type: `ida-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 无栈保护 无PIE保护`

### Step 2: IDA 反编译

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use ida, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use ida, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `![gift](./images/SWPUCTF_2021_gift_pwn-gift.png)`

### Step 3: 想到什么解题思路

- Route type: `ida-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 覆盖返回地址 `0x4005b6``

### Step 4: Payload

- Route type: `pwntools-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use pwntools to collect the smallest evidence slice that answers the goal.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as pwntools-driven evidence lookup.
  - Use pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `![getshell](./images/SWPUCTF_2021_gift_pwn-getshell.png)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
