# ”BUUCTF之pwn题解（一些栈题+程序分析）_swedsn的博客-CSDN博客_buuctf pwn

## Case Metadata

- Category: `Pwn`
- Platform: `”BUUCTF之pwn题解（一些栈题+程序分析）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/”BUUCTF之pwn题解（一些栈题+程序分析）_swedsn的博客-CSDN博客_buuctf-pwn.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E2%80%9DBUUCTF%E4%B9%8Bpwn%E9%A2%98%E8%A7%A3%EF%BC%88%E4%B8%80%E4%BA%9B%E6%A0%88%E9%A2%98%2B%E7%A8%8B%E5%BA%8F%E5%88%86%E6%9E%90%EF%BC%89_swedsn%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_buuctf-pwn.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/”BUUCTF之pwn题解（一些栈题+程序分析）_swedsn的博客-CSDN博客_buuctf-pwn.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: gdb, ida, netcat, pwntools, ropgadget, strings
- Techniques: binary-exploitation, command-injection, encoding-analysis, format-string, integer-overflow, malware-static, ret2libc, ret2text, reverse-engineering, stack-overflow, stego-extraction, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `64`
- `docs/img/4cda432a56a909cd888e66c6f9781841.png`
- `docs/img/a53f8aa95f165cc5b2f0848cc95105cf.png`
- `docs/img/ef7e3b24511eb6e011d979f5dc3e22d8.png`
- `docs/img/24af28fb55dfffae19cf7e16d98dddb6.png`
- `docs/img/6ebd31bc349117e70789f2120235bd11.png`
- `docs/img/314bff8af4c1de82a2a8296509074028.png`
- `docs/img/4e8aea1a8476b68ea7f630e9d84c6712.png`
- `docs/img/b3c4795b46c5008e3f8f20b90da803eb.png`
- `docs/img/36353b1ee181a267bb9e2302b4c66b6b.png`
- `docs/img/f675e520bacff08f6938416f662025f3.png`
- `docs/img/9affa12237f68970dfb764266fe9dbfc.png`
- `docs/img/a132f0257b613d4116dfb863d0496b1d.png`
- ... and `52` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: ”BUUCTF之pwn题解（一些栈题+程序分析）_swedsn的博客-CSDN博客_buuctf pwn

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, ida, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_51032807/article/details/112545011](https://blog.csdn.net/qq_51032807/article/details/112545011)`

### Step 3: 前言

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use gdb, ida, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: gdb, ida, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use gdb, ida, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `（3）[PWN题型之栈迁移](https://blog.csdn.net/qq_51032807/article/details/119211154?spm=1001.2014.3001.5502)`

### Step 4: 0x01 ：test_your_n

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use ida, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use ida, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `4cda432a56a909cd888e66c6f9781841`

### Step 5: 0x02 ：rip

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a53f8aa95f165cc5b2f0848cc95105cf`

### Step 6: coding: utf-8    #python2.7中文注释

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `r.interactive() #远程交互`

### Step 7: 0x03 ：warmup_csaw_2016

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6ebd31bc349117e70789f2120235bd11`

### Step 8: coding: utf-8

- Route type: `pwntools-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use pwntools to collect the smallest evidence slice that answers the goal.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as pwntools-driven evidence lookup.
  - Use pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `r.interactive()`

### Step 9: 0x04 ：pwn1_sctf_2016

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use ida to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: ida
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use ida to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `b3c4795b46c5008e3f8f20b90da803eb`

### Step 10: coding: utf-8

- Route type: `pwntools-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use pwntools to collect the smallest evidence slice that answers the goal.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as pwntools-driven evidence lookup.
  - Use pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `payload = offset*'I' +'aaaa'+ p32(0x08048F13)`

### Step 11: 20个‘I’ -> 20个 ‘you’ 就会有60个字节，就会覆盖到ebp，然后再加上4字节，覆盖到返回地址。

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, ida, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, ida, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, ida, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `.`

### Step 12: 0x05 ：ciscn_2019_n_1

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use ida to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: ida
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use ida to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `9affa12237f68970dfb764266fe9dbfc`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
