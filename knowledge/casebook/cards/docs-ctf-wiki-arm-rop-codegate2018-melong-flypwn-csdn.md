# ctf-wiki ARM ROP Codegate2018_Melong题解_flypwn的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `ctf`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/ctf-wiki-ARM-ROP-Codegate2018_Melong题解_flypwn的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/ctf-wiki-ARM-ROP-Codegate2018_Melong%E9%A2%98%E8%A7%A3_flypwn%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/ctf-wiki-ARM-ROP-Codegate2018_Melong题解_flypwn的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: checksec, gdb, ghidra, netcat, pwntools, ropgadget
- Techniques: binary-exploitation, classical-crypto, command-injection, encoding-analysis, image-analysis, ret2libc, reverse-engineering, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `2`
- `docs/img/444eca59e16f9523c089d2c0534b8569.png`
- `docs/img/ef2293a720a506721842b412e714e8e5.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, gdb, ghidra, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, gdb, ghidra, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, gdb, ghidra, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: ctf-wiki ARM ROP Codegate2018_Melong题解_flypwn的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, gdb, ghidra, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, gdb, ghidra, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, gdb, ghidra, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_42016744/article/details/118517898](https://blog.csdn.net/weixin_42016744/article/details/118517898)`

### Step 3: 写在前面

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, gdb, ghidra, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, gdb, ghidra, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, gdb, ghidra, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ctf-wiki关于arm pwn的[arm - ROP](https://ctf-wiki.org/pwn/linux/arm/arm_rop/#arm-rop "Permanent link")中的例题是Codegate2018_Melong，但在网上一直没找到write up，这里跟着官方解给出的exp调试记录。`

### Step 4: 确定保护

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec, netcat
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2c55e75a072020303e7c802d32a5b82432f329e9`

### Step 5: 静态分析

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use checksec, gdb, ghidra, netcat with the extracted filter/query `可以看到若想到达case 4中的write_diary函数，首先需要变量local_18[0]!=0才行。` and inspect the matching evidence.
- Tools: checksec, gdb, ghidra, netcat, pwntools, ropgadget
- Filters or commands:
  - `可以看到若想到达case 4中的write_diary函数，首先需要变量local_18[0]!=0才行。`
  - `if (local_10 == exc2) {`
  - `这里没明白local_10==exc2中的exc2是什么意思。但是经测试输入-1时，在菜单4中可以写入，猜测这里是可能的溢出点。`
  - `栈溢出==>puts(elf.got[‘function_name’])<mark>>计算libc基址</mark>>跳回main==>跳转到system("/bin/sh")`
  - `============================================================`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use checksec, gdb, ghidra, netcat with the extracted filter/query `可以看到若想到达case 4中的write_diary函数，首先需要变量local_18[0]!=0才行。` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `444eca59e16f9523c089d2c0534b8569`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
