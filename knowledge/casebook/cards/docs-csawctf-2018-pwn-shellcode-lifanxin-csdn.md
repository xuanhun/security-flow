# CSAWCTF-2018-pwn-shellcode 题解___lifanxin的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `CSAWCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CSAWCTF-2018-pwn-shellcode-题解___lifanxin的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CSAWCTF-2018-pwn-shellcode-%E9%A2%98%E8%A7%A3___lifanxin%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CSAWCTF-2018-pwn-shellcode-题解___lifanxin的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: checksec, gdb, netcat, pwntools
- Techniques: binary-exploitation, command-injection, encoding-analysis, ret2libc, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `7`
- `docs/img/d18428125ef821f0e7af03ad9266f153.png`
- `docs/img/672fd41f03cb20713cba60245dd4bdb6.png`
- `docs/img/a8c036469c8d6f4cb0318877a288e72b.png`
- `docs/img/85d92fba859765e7a1cdfbcd6e2caa68.png`
- `docs/img/b409e96e3123ee8cff62404a28fa933b.png`
- `docs/img/8423a4d11aa5c141b240e063242c5e42.png`
- `docs/img/ba9a60fcdd62511ff4d90b22ed8d54b6.png`

## Solve Thinking

### Step 1: Document

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CSAWCTF-2018-pwn-shellcode 题解___lifanxin的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, gdb, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, gdb, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/A951860555/article/details/110350773](https://blog.csdn.net/A951860555/article/details/110350773)`

### Step 3: 知识点关键字

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, gdb, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec, gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, gdb, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `栈溢出，shellcode拆分+组装`

### Step 4: 样本

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, gdb, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, gdb, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `样本来自2018年CSAWCTF的pwn题目shellcode`

### Step 5: 运行

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, gdb to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec, gdb
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, gdb to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `d18428125ef821f0e7af03ad9266f153`

### Step 6: 静态分析

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `672fd41f03cb20713cba60245dd4bdb6`

### Step 7: 程序逻辑

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use checksec, gdb, netcat, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: checksec, gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use checksec, gdb, netcat, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `由于无法生成小于15字节的shellcode脚本来执行系统调用函数system("/bin/sh")，所以利用程序所给出的三个小节点分开存储shellcode然后链接起来运行，其中节点不连续需要使用跳转指令进行链接。`

### Step 8: 一些细节：

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `5、将“/bin/sh"压到栈中时，最后一个字节是"\x00"，刚好作为读取字符串的停止符。`

### Step 9: wp_shellcode.py

- Route type: `pwntools-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use pwntools to collect the smallest evidence slice that answers the goal.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as pwntools-driven evidence lookup.
  - Use pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `127.0.0.1`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
