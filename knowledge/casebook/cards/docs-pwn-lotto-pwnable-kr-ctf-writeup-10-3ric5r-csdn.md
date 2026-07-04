# PWN lotto [pwnable.kr]CTF writeup题解系列10_3riC5r的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `PWN lotto [pwnable.kr]CTF writeup题解系列10`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/PWN-lotto-[pwnable.kr]CTF-writeup题解系列10_3riC5r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/PWN-lotto-%5Bpwnable.kr%5DCTF-writeup%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%9710_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/PWN-lotto-[pwnable.kr]CTF-writeup题解系列10_3riC5r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: gdb, netcat, pwntools, radare2
- Techniques: binary-exploitation, browser-forensics, command-injection, file-inclusion, http-analysis, integer-overflow, privilege-escalation, ret2libc, service-enumeration, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `3`
- `docs/img/61c2f4edbf7527251d4c2d2d70027a0b.png`
- `docs/img/a0a25e334ecce7d656b242b184883884.png`
- `docs/img/53f599e72f87a24d5b7924a2c026cf68.png`

## Solve Thinking

### Step 1: Document

- Route type: `gdb-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, netcat, pwntools, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: gdb, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, netcat, pwntools, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: PWN lotto [pwnable.kr]CTF writeup题解系列10_3riC5r的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, netcat, pwntools, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, netcat, pwntools, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 3: 0x01题目

- Route type: `gdb-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, netcat, pwntools, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: gdb, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, netcat, pwntools, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `61c2f4edbf7527251d4c2d2d70027a0b`

### Step 4: 0x02解题思路

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use gdb, netcat, pwntools, radare2 with the extracted filter/query `| \| |__| || \ / || \ | | / _] | |/ ]| \` and inspect the matching evidence.
- Tools: gdb, netcat, pwntools, radare2
- Filters or commands:
  - `| \| |__| || \ / || \ | | / _] | |/ ]| \`
  - `| o ) | | || _ || o || o )| | / [_ | ' / | D )`
  - `| _/| | | || | || || || |___ | _] | \ | /`
  - `| | | ` ' || | || _ || O || || [_ __ | \| \`
  - `| | \ / | | || | || || || || || . || . \`
  - `|__| \_/\_/ |__|__||__|__||_____||_____||_____||__||__|\_||__|\_|`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use gdb, netcat, pwntools, radare2 with the extracted filter/query `| \| |__| || \ / || \ | | / _] | |/ ]| \` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `64.43.135.184`

### Step 5: 0x03题解

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `process_name = './lotto'`

### Step 6: p = process([process_name], env={'LD_LIBRARY_PATH':'./'})

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gdb, netcat, pwntools, radare2 to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gdb, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use gdb, netcat, pwntools, radare2 to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `p = s.process(executable='/home/lotto/lotto')`

### Step 7: elf = ELF(process_name)

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use gdb, netcat, pwntools, radare2 to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: gdb, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use gdb, netcat, pwntools, radare2 to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `pass`

### Step 8: This is used for locating apport core dumps

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

### Step 9: Attempt to dump ALL core file regions

- Route type: `gdb-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, netcat, pwntools, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: gdb, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, netcat, pwntools, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `pass`

### Step 10: Assume that the user would prefer to have core dumps.

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `root@mypwn:/ctf/work/pwnable.kr#`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
