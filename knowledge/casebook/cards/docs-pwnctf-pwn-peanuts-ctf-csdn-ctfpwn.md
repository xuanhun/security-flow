# PWNctf的pwn题解析_Peanuts_CTF的博客-CSDN博客_ctfpwn题

## Case Metadata

- Category: `Pwn`
- Platform: `PWNctf的pwn题解析`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/PWNctf的pwn题解析_Peanuts_CTF的博客-CSDN博客_ctfpwn题.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/PWNctf%E7%9A%84pwn%E9%A2%98%E8%A7%A3%E6%9E%90_Peanuts_CTF%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctfpwn%E9%A2%98.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/PWNctf的pwn题解析_Peanuts_CTF的博客-CSDN博客_ctfpwn题.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: gdb, ida, netcat, pwntools
- Techniques: binary-exploitation, encoding-analysis, ret2libc, reverse-engineering, stack-overflow, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `11`
- `docs/img/1931e67524d3b214e3f39a13fc7fbca8.png`
- `docs/img/f8d280205b7dbd5951b06990e8850e62.png`
- `docs/img/6900ab4f008ee08ae44753b52d6fb085.png`
- `docs/img/05808ce748f53dc0ac61bf0c7a5b7ce1.png`
- `docs/img/10561ad0a4c417b4e1b7473eae3f6e30.png`
- `docs/img/512031e67a9b87bd1231712196eac0d0.png`
- `docs/img/042671d686c3b4115c722b690d2dfb69.png`
- `docs/img/52aad8746ad107ba1bbb7ce47a684fdb.png`
- `docs/img/10eb720662072443d05f0eff0b287b27.png`
- `docs/img/6a21f8a266a7d1dfbfc14ff540fb9230.png`
- `docs/img/2a39ad86a726097813f6551afadd34ef.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: PWNctf的pwn题解析_Peanuts_CTF的博客-CSDN博客_ctfpwn题

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/w12315q/article/details/83869439](https://blog.csdn.net/w12315q/article/details/83869439)`

### Step 3: importantservice

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这个题目比较简单，保护开的很多多到我怀疑自己是不是把题目想的太简单了，结果果然是这么简单的。。`

### Step 4: 程序功能分析

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use gdb, ida, netcat, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use gdb, ida, netcat, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `1931e67524d3b214e3f39a13fc7fbca8`

### Step 5: 调试程序

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use gdb, ida to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: gdb, ida
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use gdb, ida to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `05808ce748f53dc0ac61bf0c7a5b7ce1`

### Step 6: 思路分析

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use gdb, ida, netcat, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use gdb, ida, netcat, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `二、开了pie，可以利用地址的低位覆盖让程序覆盖到我们想要的getshell地址（刚开始做题目的时候，四位定式了，对开了pie的题目第一步就是想到要进行地址泄漏，发现怎么也泄漏不出地址所以卡了好久。最后柳暗花明了，忘记了最简单的绕过方法。）`

### Step 7: exp:

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `p.interactive()`

### Step 8: exploitClass

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use gdb, ida, netcat, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use gdb, ida, netcat, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这道题目考查的是数组越界和canary的绕过，我个人觉得是质量非常高的一个题目，题目本身不难但是很有做的价值`

### Step 9: 程序功能分析

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `10561ad0a4c417b4e1b7473eae3f6e30`

### Step 10: 调试过程

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, ida, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, ida, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `10eb720662072443d05f0eff0b287b27`

### Step 11: 思路分析

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, ida, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, ida, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `二、覆盖函数的ret进行一个ROP链的利用，关于ROP的利用就不多说了，坑点无非就是这里是一个64位的程序不是直接引用栈的。`

### Step 12: exp:

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `p.interactive()`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
