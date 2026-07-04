# Seccon-ctf-2016-pwn-cheer_msg 题解___lifanxin的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `Seccon`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/Seccon-ctf-2016-pwn-cheer_msg-题解___lifanxin的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/Seccon-ctf-2016-pwn-cheer_msg-%E9%A2%98%E8%A7%A3___lifanxin%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/Seccon-ctf-2016-pwn-cheer_msg-题解___lifanxin的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: pwntools
- Techniques: binary-exploitation, command-injection, encoding-analysis, ret2libc, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `3`
- `docs/img/51db4e32b5a4d14dbabb26117b9ff3c6.png`
- `docs/img/f5f231861c393072d6cd3eb15ca1fc33.png`
- `docs/img/0be5af79c044b41df8c68b6b9eff6a23.png`

## Solve Thinking

### Step 1: Document

- Route type: `pwntools-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use pwntools to collect the smallest evidence slice that answers the goal.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as pwntools-driven evidence lookup.
  - Use pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: Seccon-ctf-2016-pwn-cheer_msg 题解___lifanxin的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/A951860555/article/details/114011564](https://blog.csdn.net/A951860555/article/details/114011564)`

### Step 3: 文件信息

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `51db4e32b5a4d14dbabb26117b9ff3c6`

### Step 4: 漏洞定位

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `f5f231861c393072d6cd3eb15ca1fc33`

### Step 5: 利用分析

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - The proof is the returned command output or filesystem effect from the injected command.
- Evidence rule: The proof is the returned command output or filesystem effect from the injected command.

### Step 6: wp

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use pwntools with the extracted filter/query `print("=============", addr, hex(addr))` and inspect the matching evidence.
- Tools: pwntools
- Filters or commands:
  - `print("=============", addr, hex(addr))`
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use pwntools with the extracted filter/query `print("=============", addr, hex(addr))` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `p.interactive()`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
