# 【CTF题解NO.00008】mini-LCTF 2021 official write up by arttnba3_arttnba3的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `【CTF题解NO.00008】mini`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【CTF题解NO.00008】mini-LCTF-2021-official-write-up-by-arttnba3_arttnba3的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90CTF%E9%A2%98%E8%A7%A3NO.00008%E3%80%91mini-LCTF-2021-official-write-up-by-arttnba3_arttnba3%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【CTF题解NO.00008】mini-LCTF-2021-official-write-up-by-arttnba3_arttnba3的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: checksec, netcat, one-gadget, pwntools
- Techniques: binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis, format-string, http-analysis, ret2libc, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `5`
- `docs/img/3418fa12a44c06ff8d25a12c855bb8c1.png`
- `docs/img/cb54c0511e72d407506039ad7ddbf7bb.png`
- `docs/img/3693e24155f00c4398aead5c46fae920.png`
- `docs/img/97556d3b1afc2c21ee3e77de94f878b9.png`
- `docs/img/36c450c39256665bbf778a56ee5813ac.png`

## Solve Thinking

### Step 1: Document

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, netcat, one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: checksec, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, netcat, one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 【CTF题解NO.00008】mini-LCTF 2021 official write up by arttnba3_arttnba3的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, netcat, one-gadget, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, netcat, one-gadget, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/arttnba3/article/details/116810766](https://blog.csdn.net/arttnba3/article/details/116810766)`

### Step 3: 0x00.绪论

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, netcat, one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: checksec, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, netcat, one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `点开下方查看题解👇`

### Step 4: 0x01.Baby Repeater - fmtstr + got hijack

- Route type: `format-string control path`
- Why: Format-string routes start with stack discovery and end with the smallest precise read or write.
- Probe: Use one-gadget to map readable and writable stack positions before attempting the final primitive.
- Tools: one-gadget
- Reasoning chain:
  - Recognize the section as format-string control path.
  - Use one-gadget to map readable and writable stack positions before attempting the final primitive.
  - The proof is the exact read/write effect at the intended stack or memory location.
- Evidence rule: The proof is the exact read/write effect at the intended stack or memory location.

### Step 5: 解题思路

- Route type: `format-string control path`
- Why: Format-string routes start with stack discovery and end with the smallest precise read or write.
- Probe: Use checksec, netcat, pwntools to map readable and writable stack positions before attempting the final primitive.
- Tools: checksec, netcat, pwntools
- Reasoning chain:
  - Recognize the section as format-string control path.
  - Use checksec, netcat, pwntools to map readable and writable stack positions before attempting the final primitive.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `3418fa12a44c06ff8d25a12c855bb8c1`

### Step 6: 0x02\. easytcache - Use After Free + safe-linking bypass + ORW （+ FSOP）

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, netcat, one-gadget, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, netcat, one-gadget, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-Hz2IpHD9-1621009387347)(https://i.loli.net/2021/05/15/Oqpem3yrg2UJlYC.png)]`

### Step 7: 程序分析

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use checksec, netcat, one-gadget, pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: checksec, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use checksec, netcat, one-gadget, pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `题目本身有个逻辑漏洞，在 `deleteNote()` 函数中虽然会检测堆块是否已释放，但是会在检测之前使用取反的方式改变标志位，因此可以在改变标志位后使用 edit 功能清除 tcache key，之后完成doule free`

### Step 8: 解题思路

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use one-gadget to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: one-gadget
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use one-gadget to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-fu8jXAVw-1621009387349)(https://i.loli.net/2021/04/22/EA873jmk2bIy4ca.png)]`

### Step 9: 解法一：__environ泄露栈地址在栈上构造ROP进行ORW

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use netcat, one-gadget, pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use netcat, one-gadget, pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `exp()`

### Step 10: 解法二：通过 exit() 进行FSOP构造ROP进行ORW

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use netcat, one-gadget, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use netcat, one-gadget, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `cb54c0511e72d407506039ad7ddbf7bb`

### Step 11: 非预期：

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, netcat, one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: checksec, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, netcat, one-gadget, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `3693e24155f00c4398aead5c46fae920`

### Step 12: 非预期二：

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, netcat, one-gadget, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, netcat, one-gadget, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, netcat, one-gadget, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `36c450c39256665bbf778a56ee5813ac`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
