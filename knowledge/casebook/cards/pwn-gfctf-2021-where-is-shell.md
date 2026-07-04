# [GFCTF 2021]where_is_shell

## Case Metadata

- Category: `Pwn`
- Platform: `GFCTF 2021`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/[GFCTF 2021]where_is_shell.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/%5BGFCTF%202021%5Dwhere_is_shell.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/[GFCTF 2021]where_is_shell.md`
- Challenge URL: `https://www.nssctf.cn/problem/889`

## Why This Case Matters

Use this case as a Pwn reference for binary, ids, web-app challenges.

## Input Signals

- Artifacts: binary, ids, web-app
- Tools: IDA, pwntools, ROPgadget, checksec
- Techniques: binary-exploitation, http-analysis, ret2libc, ret2text, reverse-engineering, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `8`
- `pwn/images/GFCTF_2021where_is_shell-file.png`
- `pwn/images/GFCTF_2021where_is_shell-checksec.png`
- `pwn/images/GFCTF_2021where_is_shell-main.png`
- `pwn/images/GFCTF_2021where_is_shell-tips.png`
- `pwn/images/GFCTF_2021where_is_shell-systemcall.png`
- `pwn/images/GFCTF_2021where_is_shell-ret.png`
- `pwn/images/GFCTF_2021where_is_shell-pop_rdi.png`
- `pwn/images/GFCTF_2021where_is_shell-getflag.png`

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
- Result: `因为实在找不到有什么能够代表`sh`的了，根据题目提示，字符串可能在`.text`代码段上，所以有可能这个标红的位置是`shell`的字符串(可尝试一下)`

### Step 2: 想到什么解题思路

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use IDA, pwntools, ROPgadget, checksec to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: IDA, pwntools, ROPgadget, checksec
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use IDA, pwntools, ROPgadget, checksec to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - The proof is the controlled return or call path, plus the program behavior that reaches the target win path.
- Evidence rule: The proof is the controlled return or call path, plus the program behavior that reaches the target win path.

### Step 3: 尝试过程与结果记录

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use ida, pwntools, ropgadget with the extracted filter/query `|地址|栈顶|` and inspect the matching evidence.
- Tools: ida, pwntools, ropgadget
- Filters or commands:
  - `|地址|栈顶|`
  - `|--|--|`
  - `|···|···|`
  - `|0x1000|即将退出的rbp|`
  - `|0x1008|返回地址|`
  - `|0x1008|指向ret指令的地址|`
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use ida, pwntools, ropgadget with the extracted filter/query `|地址|栈顶|` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `成功获得flag`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
