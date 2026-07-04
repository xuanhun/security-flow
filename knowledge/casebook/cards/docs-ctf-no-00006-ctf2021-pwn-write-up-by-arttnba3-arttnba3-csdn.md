# 【CTF题解NO.00006】*CTF2021 - pwn - write up by arttnba3_arttnba3的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `【CTF题解NO.00006】*CTF2021`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【CTF题解NO.00006】＊CTF2021---pwn---write-up-by-arttnba3_arttnba3的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90CTF%E9%A2%98%E8%A7%A3NO.00006%E3%80%91%EF%BC%8ACTF2021---pwn---write-up-by-arttnba3_arttnba3%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【CTF题解NO.00006】＊CTF2021---pwn---write-up-by-arttnba3_arttnba3的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: checksec, gdb, ida, netcat, pwntools, radare2
- Techniques: binary-exploitation, command-injection, encoding-analysis, ret2libc, reverse-engineering

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `25`
- `docs/img/8139c7aad39abfcb6d801d4a401b7d8c.png`
- `docs/img/7c0bc0fe553e6c0cbcebc46342468640.png`
- `docs/img/fd40fe36850ef2c09731268a4338d6ea.png`
- `docs/img/48fe881c6f7404282be5ceb543ffc8a1.png`
- `docs/img/44c8f428ae92f9da72fb24cf1410da14.png`
- `docs/img/cb976fe2d14b10bf2ba27e9312522d92.png`
- `docs/img/84848320ef18d496dfc97dac15fc4099.png`
- `docs/img/dfc2ebda7113221231cf83a39f68f17f.png`
- `docs/img/6c6e51cdff177e70067fac63c8412a13.png`
- `docs/img/df4eca6183df0967750719007907dafd.png`
- `docs/img/996188f67b22b9c6fd977218949ad961.png`
- `docs/img/a74b8277e38b5c61930be31a1c26b868.png`
- ... and `13` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 【CTF题解NO.00006】*CTF2021 - pwn - write up by arttnba3_arttnba3的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/arttnba3/article/details/113020297](https://blog.csdn.net/arttnba3/article/details/113020297)`

### Step 3: 【CTF题解NO.00006】*CTF2021 - pwn - write up by arttnba3

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, ida, netcat to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, ida, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `C++pwn很好玩，孩子很高兴（因为🧠已经逆炸了）`

### Step 4: 0x00.绪论

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `以及老生常谈，csdn的markdown稀烂，建议到这里阅读[github blog addr](https://arttnba3.cn/2021/01/20/CTF-0X03-STARCTF2021-PWN/)`

### Step 5: 0x01.babyheap - Use After Free + tcache poisoning

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use checksec, gdb, ida, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: checksec, gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use checksec, gdb, ida, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8139c7aad39abfcb6d801d4a401b7d8c`

### Step 6: 0x02.babygame - double free + tcache poisoning

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, gdb, ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, gdb, ida, pwntools, radare2
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, gdb, ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6c6e51cdff177e70067fac63c8412a13`

### Step 7: 0x03.babypac

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, ida, netcat to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, ida, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `[点击下载-babypac.zip](/download/starCTF2021/pwn/babypac.zip "点击此处下载原题")`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
