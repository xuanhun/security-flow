# BSides Delhi CTF 2018部分pwn题题解_Peanuts_CTF的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `BSides Delhi CTF 2018部分pwn题题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BSides-Delhi-CTF-2018部分pwn题题解_Peanuts_CTF的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BSides-Delhi-CTF-2018%E9%83%A8%E5%88%86pwn%E9%A2%98%E9%A2%98%E8%A7%A3_Peanuts_CTF%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BSides-Delhi-CTF-2018部分pwn题题解_Peanuts_CTF的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: gdb, ida, netcat, pwntools, radare2
- Techniques: binary-exploitation, ret2libc, reverse-engineering, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `9`
- `docs/img/bc965afd8390c2efc1b18a4006e43fb5.png`
- `docs/img/a6d1dd329ed2a202dcb49a43cf6d51b9.png`
- `docs/img/686bb81672f23ac1f293e86ec2321dd9.png`
- `docs/img/360742597f6dabc11af468be2f51262e.png`
- `docs/img/fb0ff29377bd68ac0ad3ab2ef43afa56.png`
- `docs/img/54f0711681d7efdadf869922f2b486e5.png`
- `docs/img/d5619ed8b6356a7a78913cb38ba97ac4.png`
- `docs/img/b60828ead82149198787236747f57b23.png`
- `docs/img/db3993cf24571ffd723b6cf7c4766c04.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BSides Delhi CTF 2018部分pwn题题解_Peanuts_CTF的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, ida, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这个是一个比较基础的国际赛，做完之后的感觉就是其中有些题目很有价值，可以顺便补充一些信号机制、uaf使用的知识。`

### Step 3: canary

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `p.interactive()`

### Step 4: easypeasy

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use netcat, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use netcat, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `singal()函数声明 void (signal(int sig, void (func)(int)))(int) ，第一个参数为要处理的信号，第二个参数为处理方法`

### Step 5: 程序功能分析

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `bc965afd8390c2efc1b18a4006e43fb5`

### Step 6: exp：

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0x6010A0 + 0x20,0x0,0x0, u64('/bin/ sh\x00'),0,0)`

### Step 7: data_bank

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `题目的名字叫做data*bank，是一个比较简单的国际赛的题但是利用这个题可以复习一下uaf关于泄漏地址和改写malloc*hook的知识。`

### Step 8: 程序功能分析

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `fb0ff29377bd68ac0ad3ab2ef43afa56`

### Step 9: 思路分析

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use gdb to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: gdb
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use gdb to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `国际赛里还是有很多对入坑不久的人很友善的比赛的，不是所有比赛都像hitcon，secon一样的。。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
