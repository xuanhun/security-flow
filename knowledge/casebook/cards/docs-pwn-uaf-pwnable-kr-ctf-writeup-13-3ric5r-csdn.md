# PWN uaf [pwnable.kr]CTF writeup题解系列13_3riC5r的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `PWN uaf [pwnable.kr]CTF writeup题解系列13`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/PWN-uaf-[pwnable.kr]CTF-writeup题解系列13_3riC5r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/PWN-uaf-%5Bpwnable.kr%5DCTF-writeup%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%9713_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/PWN-uaf-[pwnable.kr]CTF-writeup题解系列13_3riC5r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: gdb, ida, netcat, pwntools
- Techniques: binary-exploitation, browser-forensics, classical-crypto, command-injection, file-inclusion, integer-overflow, privilege-escalation, ret2libc, reverse-engineering, service-enumeration, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `2`
- `docs/img/c81f1a95510ed93c52fa7bcc59757eb4.png`
- `docs/img/7bc024950fb608326f812e1a00cdda68.png`

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

### Step 2: PWN uaf [pwnable.kr]CTF writeup题解系列13_3riC5r的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 3: 0x01题目

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `c81f1a95510ed93c52fa7bcc59757eb4`

### Step 4: 0x02解题思路

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use gdb, ida, netcat, pwntools with the extracted filter/query `| \| |__| || \ / || \ | | / _] | |/ ]| \` and inspect the matching evidence.
- Tools: gdb, ida, netcat, pwntools
- Filters or commands:
  - `| \| |__| || \ / || \ | | / _] | |/ ]| \`
  - `| o ) | | || _ || o || o )| | / [_ | ' / | D )`
  - `| _/| | | || | || || || |___ | _] | \ | /`
  - `| | | ` ' || | || _ || O || || [_ __ | \| \`
  - `| | \ / | | || | || || || || || . || . \`
  - `|__| \_/\_/ |__|__||__|__||_____||_____||_____||__||__|\_||__|\_|`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use gdb, ida, netcat, pwntools with the extracted filter/query `| \| |__| || \ / || \ | | / _] | |/ ]| \` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `220.116.190.78`

### Step 5: 0x03题解

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use pwntools to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use pwntools to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `p.sendlineafter('free\n', '1')`

### Step 6: p.recv()

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use gdb, ida, netcat, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use gdb, ida, netcat, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `pass`

### Step 7: This is used for locating apport core dumps

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat with the extracted filter/query `os.open(newfd, os.O_RDONLY if fd == 0 else (os.O_RDWR|os.O_CREAT))` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `os.open(newfd, os.O_RDONLY if fd == 0 else (os.O_RDWR|os.O_CREAT))`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat with the extracted filter/query `os.open(newfd, os.O_RDONLY if fd == 0 else (os.O_RDWR|os.O_CREAT))` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))`

### Step 8: Attempt to dump ALL core file regions

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `pass`

### Step 9: Assume that the user would prefer to have core dumps.

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `$`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
