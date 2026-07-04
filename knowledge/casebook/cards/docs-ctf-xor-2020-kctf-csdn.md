# ctf xor题_2020 KCTF秋季赛 | 第九题设计及解题思路_当下的幸福的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `ctf xor题`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/ctf-xor题_2020-KCTF秋季赛-｜-第九题设计及解题思路_当下的幸福的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/ctf-xor%E9%A2%98_2020-KCTF%E7%A7%8B%E5%AD%A3%E8%B5%9B-%EF%BD%9C-%E7%AC%AC%E4%B9%9D%E9%A2%98%E8%AE%BE%E8%AE%A1%E5%8F%8A%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF_%E5%BD%93%E4%B8%8B%E7%9A%84%E5%B9%B8%E7%A6%8F%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/ctf-xor题_2020-KCTF秋季赛-｜-第九题设计及解题思路_当下的幸福的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: checksec, gdb, netcat, pwntools, ropgadget
- Techniques: binary-exploitation, file-inclusion, http-analysis, ret2libc, stack-overflow, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `34`
- `docs/img/2ea893f94e7b4f58e947873c254e322b.png`
- `docs/img/f40133c218ac8ecaefc59e371f11f05b.png`
- `docs/img/96141b402f1ed0c412f1bde084c0767b.png`
- `docs/img/7d43fa4cb735cf9dc6a24cafe1e65972.png`
- `docs/img/ceedcd077cb2cefa4048108dfe5b993b.png`
- `docs/img/37fea20874c23942b501877fab0f5ace.png`
- `docs/img/322db74154e5a99ef04d169094c1b705.png`
- `docs/img/b35ae224f745996bdc3feacd1ed0482f.png`
- `docs/img/9d1feb51b2328bdc1ef7b69afcf9344a.png`
- `docs/img/7f440340d257ad70234f7e9690250dff.png`
- `docs/img/e60dfa39a54a79c3e89c7cf011ddc5b1.png`
- `docs/img/8f28eae322ff12ae83c5e469f07fbc8c.png`
- ... and `22` more

## Solve Thinking

### Step 1: Document

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: ctf xor题_2020 KCTF秋季赛 | 第九题设计及解题思路_当下的幸福的博客-CSDN博客

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use gdb to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: gdb
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use gdb to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `76de952b81624df920cf9ac56de8334b`

### Step 3: 看到题目后，先上checksec，可以发现题目为64位程序，未开PIE，说明代码段、数据段地址固定。

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec to collect the smallest evidence slice that answers the goal.
- Tools: checksec
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 4: 静态分析下程序，漏洞点很明显，读入0x200大小，而只memset 0x60的空间，存在栈溢出漏洞。

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, gdb, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec, gdb, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, gdb, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ff1026648113aded6dcbe1e84b388948`

### Step 5: 接下来动态调试下，可以发现一些反调试。

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 6: (cat /usr/include/x86_64-linux-gnu/asm/unistd_64.h) 查看系统调用号sub_400CA8()有ptrace反调试，patch处理掉。init_array中调用到sub_400E08()时，可以看到检查了sub_400E82()的结果，而sub_400E82()中原逻辑为返回TracerPid。如果检查不通过的话，系统调用sub_4017CC()方法将被更改...。解决方法有很多，我这边是

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use checksec, gdb, netcat, pwntools to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: checksec, gdb, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use checksec, gdb, netcat, pwntools to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `afa8a364f73a2cbd2af9d150c91770ad`

### Step 7: ROPgadget找一下：

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 8: 0x000000000040185b最长最牛，我们去他附近找找。root@ubuntu:/mnt/hgfs/ShareDir/ctf/pwn1# ROPgadget --binary pwn1 --only "pop|ret"Gadgets information============================================================0x000000000040185c : pop r12

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 9: 果然有货啊...，0x401840、0x40185A处发现通用gadget，记录下来便于后续利用。

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `cbd1d9cc4c837fb1622bd3e5b74cc4d8`

### Step 10: 栈溢出要解决的第一个问题是canary，那么如何解决呢？

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, gdb, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec, gdb, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, gdb, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `6d73b10b7498514115561a5df95f18eb`

### Step 11: 寻找梦想指针

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `f387eed2259022c9d2cb6b24eebca09d`

### Step 12: 配合上面通用gadget的方法，控制syscall(0x4017cc)，构造一个execve("/bin/sh", NULL, NULL)。

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
