# unctf2019 pwn部分题解_NoOneGroup的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `unctf2019 pwn部分题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/unctf2019-pwn部分题解_NoOneGroup的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/unctf2019-pwn%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3_NoOneGroup%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/unctf2019-pwn部分题解_NoOneGroup的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-service challenges.

## Input Signals

- Artifacts: binary, web-service
- Tools: burp, gdb, ida, netcat, one-gadget, pwntools
- Techniques: binary-exploitation, classical-crypto, command-injection, encoding-analysis, integer-overflow, ret2libc, reverse-engineering, symbolic-execution, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `4`
- `docs/img/9b3c36e3a3021c4c1d623ce9812b185f.png`
- `docs/img/c915429d5d316337be94a36e32f7b7d5.png`
- `docs/img/93d5184e9b71fb14135a318eeb79041c.png`
- `docs/img/8a207b7e8161d4550136d2a1c5d7b9ed.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use burp, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: burp, gdb, ida, netcat, one-gadget
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use burp, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: unctf2019 pwn部分题解_NoOneGroup的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, gdb, ida, netcat, one-gadget
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/u010334666/article/details/103889663](https://blog.csdn.net/u010334666/article/details/103889663)`

### Step 3: unctf2019 pwn部分题解

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, gdb, ida, netcat, one-gadget
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `[新博客链接](https://noone-hub.github.io/)`

### Step 4: babyheap

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use gdb, pwntools with the extracted filter/query `text_base = int(os.popen("pmap {}| awk '{{print $1}}'".format(io.pid)).readlines()[1], 16)` and inspect the matching evidence.
- Tools: gdb, pwntools
- Filters or commands:
  - `text_base = int(os.popen("pmap {}| awk '{{print $1}}'".format(io.pid)).readlines()[1], 16)`
  - `gdb.attach(io,'b *{}'.format(hex(text_base+addr)))`
  - `gdb.attach(io,"b *{}".format(hex(addr)))`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use gdb, pwntools with the extracted filter/query `text_base = int(os.popen("pmap {}| awk '{{print $1}}'".format(io.pid)).readlines()[1], 16)` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `127.0.0.1`

### Step 5: babyrop

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use gdb, pwntools with the extracted filter/query `text_base = int(os.popen("pmap {}| awk '{{print $1}}'".format(io.pid)).readlines()[1], 16)` and inspect the matching evidence.
- Tools: gdb, pwntools
- Filters or commands:
  - `text_base = int(os.popen("pmap {}| awk '{{print $1}}'".format(io.pid)).readlines()[1], 16)`
  - `gdb.attach(io,'b *{}'.format(hex(text_base+addr)))`
  - `gdb.attach(io,"b *{}".format(hex(addr)))`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use gdb, pwntools with the extracted filter/query `text_base = int(os.popen("pmap {}| awk '{{print $1}}'".format(io.pid)).readlines()[1], 16)` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `192.25.1.3`

### Step 6: soeasypwn

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use gdb, pwntools with the extracted filter/query `text_base = int(os.popen("pmap {}| awk '{{print $1}}'".format(io.pid)).readlines()[1], 16)` and inspect the matching evidence.
- Tools: gdb, pwntools
- Filters or commands:
  - `text_base = int(os.popen("pmap {}| awk '{{print $1}}'".format(io.pid)).readlines()[1], 16)`
  - `gdb.attach(io,'b *{}'.format(hex(text_base+addr)))`
  - `gdb.attach(io,"b *{}".format(hex(addr)))`
  - `sa("(1.hello|2.byebye):", payload)`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use gdb, pwntools with the extracted filter/query `text_base = int(os.popen("pmap {}| awk '{{print $1}}'".format(io.pid)).readlines()[1], 16)` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `101.71.29.5`

### Step 7: 漏洞点

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use burp, gdb, ida, netcat with the extracted filter/query `size == 0 ，这个时候等同于free` and inspect the matching evidence.
- Tools: burp, gdb, ida, netcat, one-gadget
- Filters or commands:
  - `size == 0 ，这个时候等同于free`
  - `realloc_ptr == 0 && size > 0 ， 这个时候等同于malloc`
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use burp, gdb, ida, netcat with the extracted filter/query `size == 0 ，这个时候等同于free` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这就是double free`

### Step 8: 漏洞利用

- Route type: `one-gadget-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use one-gadget to collect the smallest evidence slice that answers the goal.
- Tools: one-gadget
- Reasoning chain:
  - Recognize the section as one-gadget-driven evidence lookup.
  - Use one-gadget to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 9: 准备工作

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use burp, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: burp, gdb, ida, netcat, one-gadget
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use burp, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `c(4)`

### Step 10: 泄露libc地址

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这里就是IO_FILE攻击，不清楚的可以自己学下，这里我学到个新操作。。我调试的时候要生要死的，没想到抛出异常，多亏大佬博客了，还有自己复现的时候用ida把前面一段打开文件那部分patch掉吧，不然感觉效率太慢了。。。`

### Step 11: double free

- Route type: `one-gadget-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use one-gadget to collect the smallest evidence slice that answers the goal.
- Tools: one-gadget
- Reasoning chain:
  - Recognize the section as one-gadget-driven evidence lookup.
  - Use one-gadget to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这里常规操作，接下来的才是重头戏`

### Step 12: one_gadget失败

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use gdb, netcat, one-gadget with the extracted filter/query `gdb.attach(io)` and inspect the matching evidence.
- Tools: gdb, netcat, one-gadget
- Filters or commands:
  - `gdb.attach(io)`
  - `rax == NULL`
  - `[rsp+0x30] == NULL`
  - `[rsp+0x50] == NULL`
  - `[rsp+0x70] == NULL`
  - `gdb-peda$ x/10gx $rsp+0x30-0x20`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use gdb, netcat, one-gadget with the extracted filter/query `gdb.attach(io)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `9b3c36e3a3021c4c1d623ce9812b185f`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
