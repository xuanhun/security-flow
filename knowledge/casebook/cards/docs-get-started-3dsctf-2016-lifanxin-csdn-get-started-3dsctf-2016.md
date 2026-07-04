# get_started_3dsctf_2016 题解___lifanxin的博客-CSDN博客_get_started_3dsctf_2016

## Case Metadata

- Category: `Pwn`
- Platform: `get`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/get_started_3dsctf_2016-题解___lifanxin的博客-CSDN博客_get_started_3dsctf_2016.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/get_started_3dsctf_2016-%E9%A2%98%E8%A7%A3___lifanxin%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_get_started_3dsctf_2016.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/get_started_3dsctf_2016-题解___lifanxin的博客-CSDN博客_get_started_3dsctf_2016.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: ida, pwntools
- Techniques: binary-exploitation, classical-crypto, reverse-engineering, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `5`
- `docs/img/6aa6f2b58caf58775634096a66cea1f0.png`
- `docs/img/42cac89907be4f3443487f33d9ce3de6.png`
- `docs/img/0597b92dbfc3c9c7008929b8e4c35d4a.png`
- `docs/img/70fdc6209a30c5a9cb93c986d59daa7f.png`
- `docs/img/5d0ac19750abfc36e42bee27e3a06835.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: get_started_3dsctf_2016 题解___lifanxin的博客-CSDN博客_get_started_3dsctf_2016

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/A951860555/article/details/111030289](https://blog.csdn.net/A951860555/article/details/111030289)`

### Step 3: 知识点关键字

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `栈溢出，ROP + shellcode`

### Step 4: 样本

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `[get_started_3dsctf_2016样本下载](https://download.csdn.net/download/A951860555/13650960)`

### Step 5: 运行

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec to collect the smallest evidence slice that answers the goal.
- Tools: checksec
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `6aa6f2b58caf58775634096a66cea1f0`

### Step 6: 静态分析

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use ida to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: ida
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use ida to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0597b92dbfc3c9c7008929b8e4c35d4a`

### Step 7: 本地可以运行，远端不行的解法

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5d0ac19750abfc36e42bee27e3a06835`

### Step 8: 简单解法 – 利用后门函数

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `q.recvline()`

### Step 9: ROP解法 – 直接获取shell

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `shellcraft.sh`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
