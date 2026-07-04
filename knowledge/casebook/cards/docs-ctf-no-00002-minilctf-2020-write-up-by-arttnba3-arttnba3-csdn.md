# 【CTF题解NO.00002】minilCTF 2020 - write up by arttnba3_arttnba3的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `【CTF题解NO.00002】minilCTF 2020`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【CTF题解NO.00002】minilCTF-2020---write-up-by-arttnba3_arttnba3的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90CTF%E9%A2%98%E8%A7%A3NO.00002%E3%80%91minilCTF-2020---write-up-by-arttnba3_arttnba3%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【CTF题解NO.00002】minilCTF-2020---write-up-by-arttnba3_arttnba3的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, ids, web-app challenges.

## Input Signals

- Artifacts: binary, ids, web-app
- Tools: checksec, ida, netcat, pwntools, radare2
- Techniques: binary-exploitation, command-injection, http-analysis, integer-overflow, ret2libc, ret2text, reverse-engineering, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `41`
- `docs/img/580e53e1a108ae699f7c63313ecfce69.png`
- `docs/img/02650a59569e25f1d3d874b50a9164c3.png`
- `docs/img/7d66f4b9125a13ea3b1ddd99ee33c683.png`
- `docs/img/43f353cc0b8213f20585bb940ed74505.png`
- `docs/img/7462514d41aced28e34fa4d45775f7bc.png`
- `docs/img/a093318fe2bc52b2796352cbebc61bd3.png`
- `docs/img/818be54c5a209a195222a284f2aa9673.png`
- `docs/img/5074e12cdbe9c9927b3d60fba06ea2b3.png`
- `docs/img/0122bdca7fcf0a6e5d409dccacf8074b.png`
- `docs/img/3f080068b5da20f57748604c6c129528.png`
- `docs/img/e62408ab1a0f027c794e9c12d4143622.png`
- `docs/img/f56cee7328efc0086317d710efd7dadb.png`
- ... and `29` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, ida, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 【CTF题解NO.00002】minilCTF 2020 - write up by arttnba3_arttnba3的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, ida, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/arttnba3/article/details/108068265](https://blog.csdn.net/arttnba3/article/details/108068265)`

### Step 3: 0x00.绪论

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, ida, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 注：所有题目在[archive.lctf.online](https://archive.lctf.online)上都有部署`

### Step 4: Starting Point

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, ida, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `点进页面就可以直接获得flag了`

### Step 5: hello - ret2text + ret2shellcode

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, ida to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec, ida
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, ida to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `580e53e1a108ae699f7c63313ecfce69`

### Step 6: ret2text执行过程：

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, ida, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec, ida, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, ida, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `接下来就是ret2shellcode的：`

### Step 7: ret2shellcode修正过程：

- Route type: `radare2-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use radare2 to collect the smallest evidence slice that answers the goal.
- Tools: radare2
- Reasoning chain:
  - Recognize the section as radare2-driven evidence lookup.
  - Use radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `7462514d41aced28e34fa4d45775f7bc`

### Step 8: 高阶解法：栈迁移

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, ida, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: checksec, ida, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, ida, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `sellcraft.sh`

### Step 9: ezsc - Alphanumeric Shellcode

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec to collect the smallest evidence slice that answers the goal.
- Tools: checksec
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `a093318fe2bc52b2796352cbebc61bd3`

### Step 10: 程序分析

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `818be54c5a209a195222a284f2aa9673`

### Step 11: Alphanumeric Shelllcode

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5074e12cdbe9c9927b3d60fba06ea2b3`

### Step 12: easycpp - Use After Free

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec to collect the smallest evidence slice that answers the goal.
- Tools: checksec
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `3f080068b5da20f57748604c6c129528`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
