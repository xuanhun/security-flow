# 【CTF题解NO.00009】CISCN2021-初赛-pwn write up by arttnba3_arttnba3的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `【CTF题解NO.00009】CISCN2021`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【CTF题解NO.00009】CISCN2021-初赛-pwn-write-up-by-arttnba3_arttnba3的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90CTF%E9%A2%98%E8%A7%A3NO.00009%E3%80%91CISCN2021-%E5%88%9D%E8%B5%9B-pwn-write-up-by-arttnba3_arttnba3%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【CTF题解NO.00009】CISCN2021-初赛-pwn-write-up-by-arttnba3_arttnba3的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: ida, netcat, one-gadget, pwntools
- Techniques: binary-exploitation, crypto-analysis, encoding-analysis, image-analysis, ret2libc, reverse-engineering, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, one-gadget, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, one-gadget, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 【CTF题解NO.00009】CISCN2021-初赛-pwn write up by arttnba3_arttnba3的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, netcat, one-gadget, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, netcat, one-gadget, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/arttnba3/article/details/117097191](https://blog.csdn.net/arttnba3/article/details/117097191)`

### Step 3: 0x00.绪论

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, netcat, one-gadget, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, netcat, one-gadget, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `以下 write up 主要摘自比赛当天队内的协作文档，~~以及👴感觉pwn好没用啊，还不如早点转web算了~~`

### Step 4: pwny | Done

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, one-gadget, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, one-gadget, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `124.71.239.124`

### Step 5: lonelywolf | Done

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `124.71.239.124`

### Step 6: channel

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use ida, netcat, one-gadget, pwntools to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: ida, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use ida, netcat, one-gadget, pwntools to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `简单看了一下应该是个堆，但是👴的 qemu-aarch64 跑不起来就离谱，后面也没心思看题了，等过段时间再复现，简单看了一下 fmyy 师傅的解法，好像也不是特别难的题，~~但是那天下午👴实在是太困了去睡觉了，惭愧~~`

### Step 7: silverwolf | Done

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `124.71.239.124`

### Step 8: game

- Route type: `ida-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, netcat, one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: ida, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, netcat, one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `🛏💤`

### Step 9: satool

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, one-gadget, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, one-gadget, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `🛏💤`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
