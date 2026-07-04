# off by one --- Asis CTF 2016 b00ks题解_coco##的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `off by one`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/off-by-one-----Asis-CTF-2016-b00ks题解_coco##的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/off-by-one-----Asis-CTF-2016-b00ks%E9%A2%98%E8%A7%A3_coco%23%23%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/off-by-one-----Asis-CTF-2016-b00ks题解_coco##的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: checksec, gdb, ida, one-gadget, pwntools, radare2
- Techniques: binary-exploitation, encoding-analysis, ret2libc, reverse-engineering, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `3`
- `docs/img/87bb73a65f574918bb8480970c0ee77c.png`
- `docs/img/be7af86fd6616dc0c356b048be985b11.png`
- `docs/img/5d9c45caa3dcdd8333ade2c69048ac08.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, gdb, ida, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: off by one --- Asis CTF 2016 b00ks题解_coco##的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, gdb, ida, one-gadget to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, gdb, ida, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, gdb, ida, one-gadget to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_38419913/article/details/103124592](https://blog.csdn.net/weixin_38419913/article/details/103124592)`

### Step 3: 确定漏洞点

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `87bb73a65f574918bb8480970c0ee77c`

### Step 4: create 函数

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, gdb, ida, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `并注意其中的每个字段都占8个字节，虽然int类型本身是四个字节，但是struct结构中为了内存对齐进行了padding`

### Step 5: delete函数

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, gdb, ida, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
  - The proof is the code path, comparison, constant, or decoded data that explains the answer.
- Evidence rule: The proof is the code path, comparison, constant, or decoded data that explains the answer.

### Step 6: edit函数

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, gdb, ida, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `根据index选择一个book修改其description内容，大小限制在description size`

### Step 7: print detail函数

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, gdb, ida, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `遍历index，根据book struct中指针信息，打印出name和description内容。最后打印出author name`

### Step 8: change author name

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, gdb, ida, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `改变author name，这里有一个null off by one漏洞，输入32个字符会向内存里多写入一个\x00`

### Step 9: 内存布局

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, gdb, ida, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0x55b6aab2f1a0: 0x0000000000000000 0x0000000000020e61 <-- top chunk size`

### Step 10: 泄漏堆上的地址

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, gdb, ida, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `由于printf一个字符串是一直到\x00为止，所以打印出name的同时也能泄漏出了堆上的地址`

### Step 11: 利用NULL OFF BY ONE

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, gdb, ida, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
  - The proof is the code path, comparison, constant, or decoded data that explains the answer.
- Evidence rule: The proof is the code path, comparison, constant, or decoded data that explains the answer.

### Step 12: 泄漏libc基址

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, gdb, ida, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, gdb, ida, one-gadget to locate strings, comparisons, and control-flow decisions relevant to the input.
  - The proof is the code path, comparison, constant, or decoded data that explains the answer.
- Evidence rule: The proof is the code path, comparison, constant, or decoded data that explains the answer.

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
