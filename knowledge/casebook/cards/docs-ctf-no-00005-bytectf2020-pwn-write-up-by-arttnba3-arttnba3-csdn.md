# 【CTF题解NO.00005】ByteCTF2020 - pwn - write up by arttnba3_arttnba3的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `【CTF题解NO.00005】ByteCTF2020`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【CTF题解NO.00005】ByteCTF2020---pwn---write-up-by-arttnba3_arttnba3的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90CTF%E9%A2%98%E8%A7%A3NO.00005%E3%80%91ByteCTF2020---pwn---write-up-by-arttnba3_arttnba3%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【CTF题解NO.00005】ByteCTF2020---pwn---write-up-by-arttnba3_arttnba3的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: checksec, gdb, ida, netcat, one-gadget, pwntools, radare2
- Techniques: binary-exploitation, encoding-analysis, ret2libc, reverse-engineering

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `14`
- `docs/img/c2632503476891f11a7a08aa216d2586.png`
- `docs/img/9a18120f6c72b7301d5f37e9caca74a9.png`
- `docs/img/34b3e4ea68cbb2325c468a6d4d787553.png`
- `docs/img/aecfa29ec32cf711411e32b299fb537b.png`
- `docs/img/cd2a01059b5e120dc91b4ddf2daa69bf.png`
- `docs/img/92821f8deab8810c2471766e6f033b4a.png`
- `docs/img/308f8996ff2e32f38d09f9d7d39d0b4e.png`
- `docs/img/614854a9df390817bf3e4d4aad9187bc.png`
- `docs/img/24b292c677652b24dc1588ff4063db9d.png`
- `docs/img/4fedbdc953c3f8d12dc4e0b5c83e6e22.png`
- `docs/img/b8ff9950839d10930ad35478132bc698.png`
- `docs/img/6f3383f42db6799a2d56374616e86ec0.png`
- ... and `2` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, gdb, ida, netcat, one-gadget
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 【CTF题解NO.00005】ByteCTF2020 - pwn - write up by arttnba3_arttnba3的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, gdb, ida, netcat, one-gadget
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/arttnba3/article/details/112854031](https://blog.csdn.net/arttnba3/article/details/112854031)`

### Step 3: 【CTF题解NO.00005】ByteCTF2020 - pwn - write up by arttnba3

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, gdb, ida, netcat, one-gadget
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 推荐到这里进行阅读：[github pages address](https://arttnba3.cn/2020/11/23/CTF-0X01-ByteCTF2020-pwn/)`

### Step 4: 0x00.绪论

- Route type: `radare2-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use radare2 to collect the smallest evidence slice that answers the goal.
- Tools: radare2
- Reasoning chain:
  - Recognize the section as radare2-driven evidence lookup.
  - Use radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `题目的质量都很高，以及逆向量十分巨大，比赛当天把我给看晕了（当然主要还是因为我太菜了Or2`

### Step 5: 0x00.easy_heap - null by any address + tcache poisoning

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `c2632503476891f11a7a08aa216d2586`

### Step 6: 漏洞：任意地址写0

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use gdb, netcat, pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use gdb, netcat, pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `aecfa29ec32cf711411e32b299fb537b`

### Step 7: 0x01.gun - Use After Free + ORW

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `24b292c677652b24dc1588ff4063db9d`

### Step 8: 0x00.diary - Use After Free + tcache poisoning +

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use netcat, one-gadget, pwntools, radare2 to enumerate processes, network sockets, injected regions, and command lines.
- Tools: netcat, one-gadget, pwntools, radare2
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use netcat, one-gadget, pwntools, radare2 to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `exp()`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
