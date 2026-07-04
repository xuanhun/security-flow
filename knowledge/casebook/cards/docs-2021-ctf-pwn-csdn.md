# 砰砰砰！2021美团CTF决赛PWN题详解_代码熬夜敲的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `砰砰砰！2021美团CTF决赛PWN题详解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/砰砰砰！2021美团CTF决赛PWN题详解_代码熬夜敲的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E7%A0%B0%E7%A0%B0%E7%A0%B0%EF%BC%812021%E7%BE%8E%E5%9B%A2CTF%E5%86%B3%E8%B5%9BPWN%E9%A2%98%E8%AF%A6%E8%A7%A3_%E4%BB%A3%E7%A0%81%E7%86%AC%E5%A4%9C%E6%95%B2%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/砰砰砰！2021美团CTF决赛PWN题详解_代码熬夜敲的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, stego-media, web-app challenges.

## Input Signals

- Artifacts: binary, stego-media, web-app
- Tools: gdb, ida, netcat, pwntools, radare2
- Techniques: binary-exploitation, command-injection, encoding-analysis, format-string, ret2libc, reverse-engineering, symbolic-execution, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `13`
- `docs/img/39cf3066a230a2d3068a715f4cec1228.png`
- `docs/img/08ef85c9e235990bbd33c405afb9f0ee.png`
- `docs/img/29dc04b8e27d4803e1cb5f4c459da24b.png`
- `docs/img/0088b4410b0277f99438e133eb60d042.png`
- `docs/img/a00887dc5a96e4caaee5d229072118cf.png`
- `docs/img/7ccc30928586c82fe4f45ddbc2ab5aad.png`
- `docs/img/5b07469378abd056abcbdd4a5ffe631e.png`
- `docs/img/6020894d538e887185d8b80dca2b918a.png`
- `docs/img/55cff50bb4c980ecebdce1451a6ce8a8.png`
- `docs/img/6bd83fe0ed8c60b0b5d124844833bdca.png`
- `docs/img/60cab557166e3520b2b9bf7cec28afa0.png`
- `docs/img/836190a8f2ee301c638bfc2b8996e333.png`
- ... and `1` more

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

### Step 2: 砰砰砰！2021美团CTF决赛PWN题详解_代码熬夜敲的博客-CSDN博客

- Route type: `format-string control path`
- Why: Format-string routes start with stack discovery and end with the smallest precise read or write.
- Probe: Use gdb, ida, netcat, pwntools to map readable and writable stack positions before attempting the final primitive.
- Tools: gdb, ida, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as format-string control path.
  - Use gdb, ida, netcat, pwntools to map readable and writable stack positions before attempting the final primitive.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `39cf3066a230a2d3068a715f4cec1228`

### Step 3: coding=utf-8

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use ida, netcat, pwntools, radare2 with the extracted filter/query `if(len(sys.argv)==1): #local` and inspect the matching evidence.
- Tools: ida, netcat, pwntools, radare2
- Filters or commands:
  - `if(len(sys.argv)==1): #local`
  - `rax == NULL`
  - `[rsp+0x30] == NULL`
  - `[rsp+0x50] == NULL`
  - `[rsp+0x70] == NULL`
  - `if (((param_1[iVar7] == param_1[iVar7 + iVar4 + -1]) &&`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use ida, netcat, pwntools, radare2 with the extracted filter/query `if(len(sys.argv)==1): #local` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `114.215.144.240`

### Step 4: coding=utf-8

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, netcat, pwntools with the extracted filter/query `if(len(sys.argv)==1): #local` and inspect the matching evidence.
- Tools: gdb, netcat, pwntools
- Filters or commands:
  - `if(len(sys.argv)==1): #local`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, netcat, pwntools with the extracted filter/query `if(len(sys.argv)==1): #local` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `114.215.144.240`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
