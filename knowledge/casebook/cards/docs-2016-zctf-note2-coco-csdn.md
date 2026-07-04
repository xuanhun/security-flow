# 2016 ZCTF note2 题解_coco##的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `2016 ZCTF note2 题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/2016-ZCTF-note2-题解_coco##的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/2016-ZCTF-note2-%E9%A2%98%E8%A7%A3_coco%23%23%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/2016-ZCTF-note2-题解_coco##的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: one-gadget, pwntools
- Techniques: binary-exploitation, encoding-analysis, integer-overflow, ret2libc, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `5`
- `docs/img/bab33be6a98d29a56cb807efd409bd69.png`
- `docs/img/29d3285511a921cb86ce4fd0e2ed50d4.png`
- `docs/img/89bb4a860d8b6fef833ec00fb694fd72.png`
- `docs/img/bb2800c609e783a50901ac17bf0a2b94.png`
- `docs/img/cabf38d664a87a07dc322b858a6683e8.png`

## Solve Thinking

### Step 1: Document

- Route type: `one-gadget-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as one-gadget-driven evidence lookup.
  - Use one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 2016 ZCTF note2 题解_coco##的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use one-gadget, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use one-gadget, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_38419913/article/details/103333195](https://blog.csdn.net/weixin_38419913/article/details/103333195)`

### Step 3: 程序分析

- Route type: `one-gadget-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as one-gadget-driven evidence lookup.
  - Use one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `bab33be6a98d29a56cb807efd409bd69`

### Step 4: new note函数

- Route type: `integer-overflow bypass`
- Why: Numeric edge cases matter when they alter a length, signedness, allocation, or control-flow boundary.
- Probe: Use one-gadget, pwntools to verify the numeric edge case and how it changes the downstream size or bounds check.
- Tools: one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as integer-overflow bypass.
  - Use one-gadget, pwntools to verify the numeric edge case and how it changes the downstream size or bounds check.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `29d3285511a921cb86ce4fd0e2ed50d4`

### Step 5: show note

- Route type: `one-gadget-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as one-gadget-driven evidence lookup.
  - Use one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `bb2800c609e783a50901ac17bf0a2b94`

### Step 6: edit note

- Route type: `one-gadget-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as one-gadget-driven evidence lookup.
  - Use one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `重新编辑note中的内容，但是不能超过之前规定的size限制。`

### Step 7: delete note

- Route type: `one-gadget-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as one-gadget-driven evidence lookup.
  - Use one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `free note的堆块，并且把指向堆块的指针置空并且把size也置为0。`

### Step 8: 利用思路

- Route type: `one-gadget-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use one-gadget to collect the smallest evidence slice that answers the goal.
- Tools: one-gadget
- Reasoning chain:
  - Recognize the section as one-gadget-driven evidence lookup.
  - Use one-gadget to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `cabf38d664a87a07dc322b858a6683e8`

### Step 9: 完整的exp

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use one-gadget, pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use one-gadget, pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `io.interactive()`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
