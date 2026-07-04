# PWN dragon echo1 echo2 [pwnable.kr]CTF writeup题解系列16_3riC5r的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `PWN dragon echo1 echo2`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/PWN-dragon-echo1-echo2-[pwnable.kr]CTF-writeup题解系列16_3riC5r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/PWN-dragon-echo1-echo2-%5Bpwnable.kr%5DCTF-writeup%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%9716_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/PWN-dragon-echo1-echo2-[pwnable.kr]CTF-writeup题解系列16_3riC5r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: checksec, ida, netcat
- Techniques: binary-exploitation, format-string, integer-overflow, reverse-engineering, stack-overflow

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: PWN dragon echo1 echo2 [pwnable.kr]CTF writeup题解系列16_3riC5r的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, ida, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 3: 0x01 dragon

- Route type: `integer-overflow bypass`
- Why: Numeric edge cases matter when they alter a length, signedness, allocation, or control-flow boundary.
- Probe: Use ida, netcat with the extracted filter/query `if ( nPersonType == 1 )` and inspect the matching evidence.
- Tools: ida, netcat
- Filters or commands:
  - `if ( nPersonType == 1 )`
  - `if ( nPersonType != 2 )`
- Reasoning chain:
  - Recognize the section as integer-overflow bypass.
  - Use ida, netcat with the extracted filter/query `if ( nPersonType == 1 )` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `}`

### Step 4: 0x02 echo1

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec, netcat
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2、或者泄漏got表函数地址，然后根据got表地址查找libc的system、binsh，再继续溢出执行system`

### Step 5: 0x03 echo2

- Route type: `format-string control path`
- Why: Format-string routes start with stack discovery and end with the smallest precise read or write.
- Probe: Use checksec, ida, netcat to map readable and writable stack positions before attempting the final primitive.
- Tools: checksec, ida, netcat
- Reasoning chain:
  - Recognize the section as format-string control path.
  - Use checksec, ida, netcat to map readable and writable stack positions before attempting the final primitive.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `可以泄漏got表，然后根据got表地址查找libc的system、binsh，再继续溢出执行system`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
