# *CTF2021部分题目解题思路及exp_liucc09的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `*CTF2021部分题目解题思路及exp`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/＊CTF2021部分题目解题思路及exp_liucc09的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%EF%BC%8ACTF2021%E9%83%A8%E5%88%86%E9%A2%98%E7%9B%AE%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF%E5%8F%8Aexp_liucc09%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/＊CTF2021部分题目解题思路及exp_liucc09的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: gdb, one-gadget, pwntools
- Techniques: binary-exploitation, crypto-analysis, encoding-analysis, ret2libc, waf-bypass

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `3`
- `docs/img/e95ac072e8d871fcac7eae6be1ca219e.png`
- `docs/img/5e99806bffe936b393dd9e8479011eec.png`
- `docs/img/17c1e371df6c415a6743fc50066f3051.png`

## Solve Thinking

### Step 1: Document

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: *CTF2021部分题目解题思路及exp_liucc09的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, one-gadget, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, one-gadget, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/liucc09/article/details/112784015](https://blog.csdn.net/liucc09/article/details/112784015)`

### Step 3: babyheap

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use gdb, one-gadget, pwntools with the extracted filter/query `gdb.attach(r,'b *{}\nset $a={}\nset $b={}\n'.format(hex(addr),hex(text_base+0x2020a0),hex(text_base+0x202060)))` and inspect the matching evidence.
- Tools: gdb, one-gadget, pwntools
- Filters or commands:
  - `gdb.attach(r,'b *{}\nset $a={}\nset $b={}\n'.format(hex(addr),hex(text_base+0x2020a0),hex(text_base+0x202060)))`
  - `gdb.attach(r,'set $a={}\nset $b={}\n'.format(hex(text_base+0x2020a0),hex(text_base+0x202060)))`
  - `gdb.attach(r,'b *{}\n'.format(hex(addr)))`
- Reasoning chain:
  - Recognize the section as timeline reconstruction.
  - Use gdb, one-gadget, pwntools with the extracted filter/query `gdb.attach(r,'b *{}\nset $a={}\nset $b={}\n'.format(hex(addr),hex(text_base+0x2020a0),hex(text_base+0x202060)))` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `52.152.231.198`

### Step 4: GuessKey2

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use pwntools to align timestamps and identify the event that satisfies the question.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as timeline reconstruction.
  - Use pwntools to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `52.163.228.53`

### Step 5: oh-my-note

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use gdb, one-gadget, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: gdb, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use gdb, one-gadget, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `e95ac072e8d871fcac7eae6be1ca219e`

### Step 6: puzzle

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, one-gadget, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, one-gadget, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5e99806bffe936b393dd9e8479011eec`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
