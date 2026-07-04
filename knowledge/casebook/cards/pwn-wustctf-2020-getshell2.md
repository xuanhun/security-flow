# [WUSTCTF 2020]getshell2

## Case Metadata

- Category: `Pwn`
- Platform: `WUSTCTF 2020`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/[WUSTCTF 2020]getshell2.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/%5BWUSTCTF%202020%5Dgetshell2.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/[WUSTCTF 2020]getshell2.md`
- Challenge URL: `https://www.nssctf.cn/problem/2003`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: IDA, ROPgadget, pwntools, checksec
- Techniques: binary-exploitation, command-injection, http-analysis, ret2libc, reverse-engineering, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `6`
- `pwn/images/WUSTCTF_2020getshell2-vulnerable.png`
- `pwn/images/WUSTCTF_2020getshell2-checksec.png`
- `pwn/images/WUSTCTF_2020getshell2-file.png`
- `pwn/images/WUSTCTF_2020getshell2-system_call.png`
- `pwn/images/WUSTCTF_2020getshell2-rop.png`
- `pwn/images/WUSTCTF_2020getshell2-find_sh.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, ida with the extracted filter/query `checksec` and inspect the matching evidence.
- Tools: checksec, ida
- Filters or commands:
  - `checksec`
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, ida with the extracted filter/query `checksec` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `文件是32位的`

### Step 2: 想到什么解题思路

- Route type: `IDA-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use IDA, ROPgadget, pwntools, checksec to collect the smallest evidence slice that answers the goal.
- Tools: IDA, ROPgadget, pwntools, checksec
- Reasoning chain:
  - Recognize the section as IDA-driven evidence lookup.
  - Use IDA, ROPgadget, pwntools, checksec to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 3: 尝试过程与结果记录

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use ida, pwntools, ropgadget with the extracted filter/query `||` and inspect the matching evidence.
- Tools: ida, pwntools, ropgadget
- Filters or commands:
  - `||`
  - `|---|`
  - `|新的ebp地址|`
  - `|system函数返回地址|`
  - `|system调用参数(shell)|`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use ida, pwntools, ropgadget with the extracted filter/query `||` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `l.interactive()`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
