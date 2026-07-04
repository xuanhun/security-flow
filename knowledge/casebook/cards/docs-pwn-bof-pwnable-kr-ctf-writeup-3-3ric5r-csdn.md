# PWN bof [pwnable.kr]CTF writeup题解系列3_3riC5r的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `PWN bof [pwnable.kr]CTF writeup题解系列3`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/PWN-bof-[pwnable.kr]CTF-writeup题解系列3_3riC5r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/PWN-bof-%5Bpwnable.kr%5DCTF-writeup%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%973_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/PWN-bof-[pwnable.kr]CTF-writeup题解系列3_3riC5r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: gdb, netcat, pwntools
- Techniques: binary-exploitation, command-injection, crypto-analysis, file-inclusion, http-analysis, ret2libc, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `2`
- `docs/img/0699bf3e9dbda28270eb535860086715.png`
- `docs/img/106e20253367f688b20c7fee7f15cba8.png`

## Solve Thinking

### Step 1: Document

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: PWN bof [pwnable.kr]CTF writeup题解系列3_3riC5r的博客-CSDN博客

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use gdb, netcat, pwntools with the extracted filter/query `Connecting to pwnable.kr (pwnable.kr)|128.61.240.205|:80... connected.` and inspect the matching evidence.
- Tools: gdb, netcat, pwntools
- Filters or commands:
  - `Connecting to pwnable.kr (pwnable.kr)|128.61.240.205|:80... connected.`
  - `bof.c 100%[=================================================>] 308 --.-KB/s in 0s`
  - `bof 100%[=================================================>] 7.18K --.-KB/s in 0s`
  - `if(key == 0xcafebabe){`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use gdb, netcat, pwntools with the extracted filter/query `Connecting to pwnable.kr (pwnable.kr)|128.61.240.205|:80... connected.` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `128.61.240.205`

### Step 3: p = process([process_name], env={'LD_LIBRARY_PATH':'./'})

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use gdb, netcat, pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use gdb, netcat, pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `p = remote('pwnable.kr', 9000)`

### Step 4: elf = ELF(process_name)

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use gdb, netcat, pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use gdb, netcat, pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `简单溢出题，没什么特别好说的。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
