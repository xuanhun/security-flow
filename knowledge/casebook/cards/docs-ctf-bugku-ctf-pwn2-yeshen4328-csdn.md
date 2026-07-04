# ctf.bugku ctf题目详解——pwn2_yeshen4328的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `ctf.bugku ctf题目详解——pwn2`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/ctf.bugku-ctf题目详解——pwn2_yeshen4328的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/ctf.bugku-ctf%E9%A2%98%E7%9B%AE%E8%AF%A6%E8%A7%A3%E2%80%94%E2%80%94pwn2_yeshen4328%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/ctf.bugku-ctf题目详解——pwn2_yeshen4328的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: gdb, ida, netcat
- Techniques: binary-exploitation, reverse-engineering, stack-overflow

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `9`
- `docs/img/58ca31766ccdb78a5f582204bf1e8a58.png`
- `docs/img/7acf4298599ec34ac20191f25854f73e.png`
- `docs/img/b8fa281866db2c31a3dc89e0d845d25d.png`
- `docs/img/3040074f2781bc6b9f7fd47e5efe9a1a.png`
- `docs/img/bc12581f3479a5185b72cfd507ffd64b.png`
- `docs/img/51f319863f0b9600e1ebd52b45a2a508.png`
- `docs/img/b42e08200a1da4e12874b795df748d07.png`
- `docs/img/1c5010734636886a9a14e14cac14bf08.png`
- `docs/img/1d9ec202a64071b6c9208c0f3798925c.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: ctf.bugku ctf题目详解——pwn2_yeshen4328的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, ida, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/yeshen4328/article/details/106363576](https://blog.csdn.net/yeshen4328/article/details/106363576)`

### Step 3: 题目

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use ida to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: ida
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use ida to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `58ca31766ccdb78a5f582204bf1e8a58`

### Step 4: x64函数调用规则

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `栈底指针（帧指针）：rbp`

### Step 5: 栈结构

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `b8fa281866db2c31a3dc89e0d845d25d`

### Step 6: 其他指令

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `以上是解本题可能用到的知识`

### Step 7: 解题

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb to collect the smallest evidence slice that answers the goal.
- Tools: gdb
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `3040074f2781bc6b9f7fd47e5efe9a1a`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
