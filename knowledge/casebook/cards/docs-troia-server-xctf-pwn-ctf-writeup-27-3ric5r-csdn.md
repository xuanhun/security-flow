# troia_server [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列27(未完待续）_3riC5r的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `troia`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/troia_server-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列27(未完待续）_3riC5r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/troia_server-%5BXCTF-PWN%5D%5B%E9%AB%98%E6%89%8B%E8%BF%9B%E9%98%B6%E5%8C%BA%5DCTF-writeup%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%9727%28%E6%9C%AA%E5%AE%8C%E5%BE%85%E7%BB%AD%EF%BC%89_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/troia_server-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列27(未完待续）_3riC5r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, ciphertext challenges.

## Input Signals

- Artifacts: binary, ciphertext
- Tools: gdb, ida, netcat, pwntools
- Techniques: binary-exploitation, crypto-analysis, integer-overflow, reverse-engineering, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `3`
- `docs/img/14b4ca04ae65f6954a3e679ad1e19a01.png`
- `docs/img/38f5b43947fe83092879b130f9ec178e.png`
- `docs/img/7fc684ba388110e415f2f08c493cd02d.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: troia_server [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列27(未完待续）_3riC5r的博客-CSDN博客

- Route type: `integer-overflow bypass`
- Why: Numeric edge cases matter when they alter a length, signedness, allocation, or control-flow boundary.
- Probe: Use ida, netcat, pwntools with the extracted filter/query `if ( nInputSize < 0 || nInputSize > nSize2 )` and inspect the matching evidence.
- Tools: ida, netcat, pwntools
- Filters or commands:
  - `if ( nInputSize < 0 || nInputSize > nSize2 )`
  - `if ( (unsigned __int16)sum_buf_byte((__int64)ptr, nInputSize) != v3 )`
- Reasoning chain:
  - Recognize the section as integer-overflow bypass.
  - Use ida, netcat, pwntools with the extracted filter/query `if ( nInputSize < 0 || nInputSize > nSize2 )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `14b4ca04ae65f6954a3e679ad1e19a01`

### Step 3: elf = ELF(process_name)

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use gdb, ida, netcat, pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use gdb, ida, netcat, pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `p.send(p32(len(payload)))`

### Step 4: pause()

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `return payload2`

### Step 5: print(0x63+0x9c)

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, ida, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, ida, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `send_payload(a)`

### Step 6: p.send('\x00'*2)

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, ida, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, ida, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `payload = 'I\'m coming'`

### Step 7: payload = 'abc'

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `send_payload(encode(payload))`

### Step 8: p.send(payload+'\x08\x90')

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `send_payload(encode('\x00'))`

### Step 9: p.recv()

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `p.recv()`

### Step 10: sh_cmd('ls')

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb to collect the smallest evidence slice that answers the goal.
- Tools: gdb
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `38f5b43947fe83092879b130f9ec178e`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
