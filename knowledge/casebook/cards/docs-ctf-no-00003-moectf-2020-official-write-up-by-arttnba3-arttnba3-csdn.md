# 【CTF题解NO.00003】moeCTF 2020 - official write up by arttnba3_arttnba3的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `【CTF题解NO.00003】moeCTF 2020`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【CTF题解NO.00003】moeCTF-2020---official-write-up-by-arttnba3_arttnba3的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90CTF%E9%A2%98%E8%A7%A3NO.00003%E3%80%91moeCTF-2020---official-write-up-by-arttnba3_arttnba3%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【CTF题解NO.00003】moeCTF-2020---official-write-up-by-arttnba3_arttnba3的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, ciphertext, ids challenges.

## Input Signals

- Artifacts: binary, ciphertext, ids, web-app
- Tools: checksec, gdb, ida, netcat, pwntools, radare2, ropgadget, z3
- Techniques: binary-exploitation, classical-crypto, command-injection, crypto-analysis, encoding-analysis, http-analysis, misc-analysis, osint, qr-analysis, ret2libc, ret2text, reverse-engineering, stack-overflow, symbolic-execution, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `51`
- `docs/img/50a3693fde525f6e3caf1228a570fc78.png`
- `docs/img/8d232bfd2565c31de5b7580a2ef98f2a.png`
- `docs/img/4a6bbc779b882ab3b4e962125019ae8c.png`
- `docs/img/fe73480c53253c37295b765f2e7adb3f.png`
- `docs/img/e77d923bfe828aca7c6c6b7c4dc3f2f6.png`
- `docs/img/fcefe54b71a30a14be8d9880e0cd01c2.png`
- `docs/img/c5ec951a8fc8b7ae3e2fe2c12c7a013d.png`
- `docs/img/9acca1972b6a92b5d15f83cff209d1e0.png`
- `docs/img/aacfe7f0b535ff8a443f76a8289d623f.png`
- `docs/img/85d6e0cbb544e6b6127faab58bd1601c.png`
- `docs/img/f9a341544b7be1aa7b9e49a18f5d6d4d.png`
- `docs/img/1d2cfcd5313bd8cecc3aa1e5ec0da923.png`
- ... and `39` more

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

### Step 2: 【CTF题解NO.00003】moeCTF 2020 - official write up by arttnba3_arttnba3的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/arttnba3/article/details/109847659](https://blog.csdn.net/arttnba3/article/details/109847659)`

### Step 3: 0x00.绪论

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 注：原题皆可在本页面直接下载`

### Step 4: Pwn从入门到入狱

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, ida, netcat to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, ida, netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `50a3693fde525f6e3caf1228a570fc78`

### Step 5: Welcome

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use netcat with the extracted filter/query `nc，提示`Please fill me up`，考虑到栈溢出，直接输出一长串随机字符串获得flag` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `nc，提示`Please fill me up`，考虑到栈溢出，直接输出一长串随机字符串获得flag`
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use netcat with the extracted filter/query `nc，提示`Please fill me up`，考虑到栈溢出，直接输出一长串随机字符串获得flag` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8d232bfd2565c31de5b7580a2ef98f2a`

### Step 6: Baby Pwn - ret2text

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `4a6bbc779b882ab3b4e962125019ae8c`

### Step 7: Baby Shellcode - shellcode

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `fcefe54b71a30a14be8d9880e0cd01c2`

### Step 8: unusual shellcode - Alphanumeric Shellcode

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, ida, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c5ec951a8fc8b7ae3e2fe2c12c7a013d`

### Step 9: ROP1 - ret2text

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use checksec, gdb, ida, pwntools with the extracted filter/query `> $ ROPgadget --binary rop1 --only 'pop|ret'` and inspect the matching evidence.
- Tools: checksec, gdb, ida, pwntools, ropgadget
- Filters or commands:
  - `> $ ROPgadget --binary rop1 --only 'pop|ret'`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use checksec, gdb, ida, pwntools with the extracted filter/query `> $ ROPgadget --binary rop1 --only 'pop|ret'` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `85d6e0cbb544e6b6127faab58bd1601c`

### Step 10: ROP2 - ret2text

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, ida, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, ida, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `9161807db31e1532e9880a520e72c62f`

### Step 11: baby migration - stack migration + ret2shellcode

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec, ida, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `b2546df5976b6aa6720ab16d51674c53`

### Step 12: Hard shellcode - ret2shellcode

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, ida, pwntools, ropgadget to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec, ida, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, ida, pwntools, ropgadget to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `9c2c41e1115220e6239ea61637c859ca`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
