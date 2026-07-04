# [BJDCTF 2020]babystack2.0

## Case Metadata

- Category: `Pwn`
- Platform: `BJDCTF 2020`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/[BJDCTF 2020]babystack2.0.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/%5BBJDCTF%202020%5Dbabystack2.0.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/[BJDCTF 2020]babystack2.0.md`
- Challenge URL: `https://www.nssctf.cn/problem/709`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: IDA, checksec, pwntools
- Techniques: binary-exploitation, command-injection, http-analysis, integer-overflow, ret2libc, ret2text, reverse-engineering, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `5`
- `pwn/images/BJDCTF_2020babystack2.0-checksec.png`
- `pwn/images/BJDCTF_2020babystack2.0-reverse.png`
- `pwn/images/BJDCTF_2020babystack2.0-64bit.png`
- `pwn/images/BJDCTF_2020babystack2.0-find_sh.png`
- `pwn/images/BJDCTF_2020babystack2.0-success_get_flag.png`

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
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `程序是64位的`

### Step 2: 想到什么解题思路

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use IDA, checksec, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: IDA, checksec, pwntools
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use IDA, checksec, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- 如果没有，就需要借助`system`函数等`syscall`函数，在栈溢出后`system("/bin/sh")`覆盖`

### Step 3: 尝试过程与结果记录

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use ida, pwntools with the extracted filter/query `||` and inspect the matching evidence.
- Tools: ida, pwntools
- Filters or commands:
  - `||`
  - `|---|`
  - `|栈顶|`
  - `|新的rbp|`
  - `|执行完成后要返回的地址|`
  - `|buf(大小:0x10)|`
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use ida, pwntools with the extracted filter/query `||` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `cat flag`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
