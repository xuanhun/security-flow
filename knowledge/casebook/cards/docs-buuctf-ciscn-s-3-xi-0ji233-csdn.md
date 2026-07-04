# buuctf:ciscn_s_3题解_xi@0ji233的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `buuctf:ciscn`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/buuctf：ciscn_s_3题解_xi@0ji233的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/buuctf%EF%BC%9Aciscn_s_3%E9%A2%98%E8%A7%A3_xi%400ji233%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/buuctf：ciscn_s_3题解_xi@0ji233的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app, web-service challenges.

## Input Signals

- Artifacts: binary, web-app, web-service
- Tools: gdb, ida, netcat, nmap, pwntools, z3
- Techniques: binary-exploitation, classical-crypto, file-inclusion, http-analysis, ret2libc, reverse-engineering, service-enumeration, stack-overflow, symbolic-execution, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `2`
- `docs/img/839b1ec8abd7ad2d7eeb50b65ed7ce80.png`
- `docs/img/9ef96f43fcddc5e2542c2063c4f96a85.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat, nmap to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat, nmap, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat, nmap to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: buuctf:ciscn_s_3题解_xi@0ji233的博客-CSDN博客

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat, nmap to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat, nmap
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat, nmap to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `839b1ec8abd7ad2d7eeb50b65ed7ce80`

### Step 3: 分析程序

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use ida to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: ida
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use ida to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - The proof is the controlled return or call path, plus the program behavior that reaches the target win path.
- Evidence rule: The proof is the controlled return or call path, plus the program behavior that reaches the target win path.

### Step 4: 寻找漏洞

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use gdb, ida, netcat, nmap to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: gdb, ida, netcat, nmap, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use gdb, ida, netcat, nmap to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这一个可以说很明显的一个栈溢出漏洞了，`read` `0x400`字节的数据，且缓冲区特别小。`

### Step 5: 第一次溢出

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use gdb, netcat, z3 to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: gdb, netcat, z3
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use gdb, netcat, z3 to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `那么第一次溢出完美的构造了`/bin/sh`字符串并且获得了它的地址。`

### Step 6: 第二次溢出

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat, nmap to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat, nmap, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat, nmap to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `第二次溢出要准备的东西就有点多了。`

### Step 7: 寻找gadget

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, ida, netcat, nmap to collect the smallest evidence slice that answers the goal.
- Tools: gdb, ida, netcat, nmap, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, ida, netcat, nmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `9ef96f43fcddc5e2542c2063c4f96a85`

### Step 8: exp

- Route type: `pwntools-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use pwntools to collect the smallest evidence slice that answers the goal.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as pwntools-driven evidence lookup.
  - Use pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `p.interactive()`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
