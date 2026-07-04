# 2021dasctf七月赛 pwn题解复现（strdup,md5,protect,setcontext)_N1ch0l4s的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `2021dasctf`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/2021dasctf七月赛-pwn题解复现（strdup,md5,protect,setcontext)_N1ch0l4s的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/2021dasctf%E4%B8%83%E6%9C%88%E8%B5%9B-pwn%E9%A2%98%E8%A7%A3%E5%A4%8D%E7%8E%B0%EF%BC%88strdup%2Cmd5%2Cprotect%2Csetcontext%29_N1ch0l4s%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/2021dasctf七月赛-pwn题解复现（strdup,md5,protect,setcontext)_N1ch0l4s的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: gdb, ida, pwntools
- Techniques: binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis, php-tricks, ret2libc, ret2text, reverse-engineering, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `13`
- `docs/img/a97c6514ac3f36e26aa4ac0308796280.png`
- `docs/img/999483292af8731e499893bca87d9da1.png`
- `docs/img/19a97769476fb3fcddbccf996cdffa0a.png`
- `docs/img/f6f8dd76ed0e3fe812370493cef84775.png`
- `docs/img/349ad2dab38a7d8ee969950478e1317f.png`
- `docs/img/bb58e4cbe151ff6dbee6a140a2f5c4ba.png`
- `docs/img/a60172570d27f1a50fc7f41104f0f849.png`
- `docs/img/3295a1f00b6cdb65280958db09fc4aba.png`
- `docs/img/410046493da9582dc2b6d8e67190cfec.png`
- `docs/img/d95cafa84fb3b2ec33127f6e19491109.png`
- `docs/img/16bc6cee5d7918d4c083c9e8bb18cf28.png`
- `docs/img/3a3689c4b903d602b029d9e886f83adc.png`
- ... and `1` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 2021dasctf七月赛 pwn题解复现（strdup,md5,protect,setcontext)_N1ch0l4s的博客-CSDN博客

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use gdb, ida, pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: gdb, ida, pwntools
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use gdb, ida, pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `[https://kr0emer.com/2021/08/04/DASCTF%20July%20X%20CBCTF%204th%20pwn/](https://kr0emer.com/2021/08/04/DASCTF%20July%20X%20CBCTF%204th%20pwn/)`

### Step 3: Easyheap

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `a97c6514ac3f36e26aa4ac0308796280`

### Step 4: 漏洞点

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `19a97769476fb3fcddbccf996cdffa0a`

### Step 5: 解法1：写入mmap，常规解法

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use gdb, pwntools with the extracted filter/query `gdb.attach(io,"brva 0xC18")` and inspect the matching evidence.
- Tools: gdb, pwntools
- Filters or commands:
  - `gdb.attach(io,"brva 0xC18")`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use gdb, pwntools with the extracted filter/query `gdb.attach(io,"brva 0xC18")` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `io.interactive()`

### Step 6: 解法2：调用mprotect

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use gdb, pwntools with the extracted filter/query `frame.rsp=free_hook+0x10` and inspect the matching evidence.
- Tools: gdb, pwntools
- Filters or commands:
  - `frame.rsp=free_hook+0x10`
  - `frame.rdi=shellcode_addr`
  - `frame.rsi=0x1000`
  - `frame.rdx=7`
  - `frame.rip=libc.sym['mprotect']+libc_addr`
  - `gdb.attach(io,"brva 0xC18")`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use gdb, pwntools with the extracted filter/query `frame.rsp=free_hook+0x10` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `f6f8dd76ed0e3fe812370493cef84775`

### Step 7: RealNoOutput

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use gdb, pwntools with the extracted filter/query `gdb.attach(io,"brva 0x1861")` and inspect the matching evidence.
- Tools: gdb, pwntools
- Filters or commands:
  - `gdb.attach(io,"brva 0x1861")`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use gdb, pwntools with the extracted filter/query `gdb.attach(io,"brva 0x1861")` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `349ad2dab38a7d8ee969950478e1317f`

### Step 8: canary3

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use ida, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use ida, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `d95cafa84fb3b2ec33127f6e19491109`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
