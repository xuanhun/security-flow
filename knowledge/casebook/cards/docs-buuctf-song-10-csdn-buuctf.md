# buuctf解题记录_song-10的博客-CSDN博客_buuctf解题

## Case Metadata

- Category: `Pwn`
- Platform: `buuctf解题记录`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/buuctf解题记录_song-10的博客-CSDN博客_buuctf解题.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/buuctf%E8%A7%A3%E9%A2%98%E8%AE%B0%E5%BD%95_song-10%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_buuctf%E8%A7%A3%E9%A2%98.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/buuctf解题记录_song-10的博客-CSDN博客_buuctf解题.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: checksec, netcat, pwntools
- Techniques: binary-exploitation, command-injection, encoding-analysis, file-inclusion, integer-overflow, ret2libc, stack-overflow, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Solve Thinking

### Step 1: Document

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: checksec, netcat, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: buuctf解题记录_song-10的博客-CSDN博客_buuctf解题

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `文中所用到的程序文件：[bin file](https://github.com/song-10/write-up)`

### Step 3: 相似题目：Hgame 2020 findyourself

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use checksec, netcat, pwntools with the extracted filter/query `if ( (unsigned int)check1(&command) != -1 )` and inspect the matching evidence.
- Tools: checksec, netcat, pwntools
- Filters or commands:
  - `if ( (unsigned int)check1(&command) != -1 )`
  - `if ( (a1[i] <= 96 || a1[i] > 122) && (a1[i] <= 64 || a1[i] > 90) && a1[i] != 47 && a1[i] != 32 && a1[i] != 45 )`
  - `if ( strstr(a1, "sh") || strstr(a1, "cat") || strstr(a1, "flag") || strstr(a1, "pwd") || strstr(a1, "export") )`
  - `if ( (unsigned int)check2(&s1, 20LL) == -1 )`
  - `|| strstr(a1, "sh")`
  - `|| strstr(a1, "cat")`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use checksec, netcat, pwntools with the extracted filter/query `if ( (unsigned int)check1(&command) != -1 )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `cat /flag`

### Step 4: rci

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag{5fcd2cea-5330-4d33-b21a-291eec874be3}`

### Step 5: 另开的终端，获取文件夹名

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat with the extracted filter/query `nop@nop-pwn:~$ nc node3.buuoj.cn 29623 | grep 18631212` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `nop@nop-pwn:~$ nc node3.buuoj.cn 29623 | grep 18631212`
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat with the extracted filter/query `nop@nop-pwn:~$ nc node3.buuoj.cn 29623 | grep 18631212` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `p.send('/tmp/'+addr_current_dir)`

### Step 6: [BJDCTF 2nd]secret

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use checksec, pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: checksec, pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use checksec, pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `way2()`

### Step 7: [BJDCTF 2nd]test

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `||strstr(cmd, "e")` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `||strstr(cmd, "e")`
  - `||strstr(cmd, "p")`
  - `||strstr(cmd, "b")`
  - `||strstr(cmd, "u")`
  - `||strstr(cmd, "s")`
  - `||strstr(cmd, "h")`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `||strstr(cmd, "e")` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `$`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
