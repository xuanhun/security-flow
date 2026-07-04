# BUUCTF ciscn_2019_c_1__N1rvana_的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `BUUCTF ciscn`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF-ciscn_2019_c_1__N1rvana_的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF-ciscn_2019_c_1__N1rvana_%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF-ciscn_2019_c_1__N1rvana_的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: checksec, netcat, pwntools, ropgadget
- Techniques: binary-exploitation, crypto-analysis, encoding-analysis, http-analysis, stack-overflow, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `5`
- `docs/img/d38a281638320df9048c204cd6bac953.png`
- `docs/img/6c76f6be81ac84f479be426665895ab7.png`
- `docs/img/68c3d785289a1ff2efc116e997aa0e05.png`
- `docs/img/66807dd23a8f548815b25d4c1e4443bf.png`
- `docs/img/4dfa01048c5e21251edd026fef5cf068.png`

## Solve Thinking

### Step 1: Document

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, netcat, pwntools, ropgadget to collect the smallest evidence slice that answers the goal.
- Tools: checksec, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, netcat, pwntools, ropgadget to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BUUCTF ciscn_2019_c_1__N1rvana_的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, netcat, pwntools, ropgadget to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, netcat, pwntools, ropgadget to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这道题是BUUCTF上的ciscn_2019_c_1。标准的64位ROP流程，我也就分享一下自己的坎坷心路历程。`

### Step 3: 代码审计

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec to collect the smallest evidence slice that answers the goal.
- Tools: checksec
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `d38a281638320df9048c204cd6bac953`

### Step 4: 关键函数:encrypt()

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, netcat, pwntools, ropgadget to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, netcat, pwntools, ropgadget to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `68c3d785289a1ff2efc116e997aa0e05`

### Step 5: 通过gets（）函数构造ROP链：

- Route type: `ropgadget-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ropgadget to collect the smallest evidence slice that answers the goal.
- Tools: ropgadget
- Reasoning chain:
  - Recognize the section as ropgadget-driven evidence lookup.
  - Use ropgadget to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `66807dd23a8f548815b25d4c1e4443bf`

### Step 6: 方法一：

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `现在在网上基本上很难找到不同的解法了，感觉大家都流水线过一遍，也不想去思考或者也不愿意去分享自己更好的做法了。很可惜，李杜诗篇万口传，至今已觉不新鲜。`

### Step 7: 方法二：

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, netcat, pwntools, ropgadget to collect the smallest evidence slice that answers the goal.
- Tools: checksec, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, netcat, pwntools, ropgadget to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `payload = b'a'*0x58+p64(pop_rdi_addr)+p64(puts_got)+p64(puts_plt)+p64(main_addr)`

### Step 8: 方法三：

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, netcat, pwntools, ropgadget to collect the smallest evidence slice that answers the goal.
- Tools: checksec, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, netcat, pwntools, ropgadget to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `payload = b'\x00'+b'a'*0x57+p64(pop_rdi_addr)+p64(puts_got)+p64(puts_plt)+p64(main_addr)`

### Step 9: 最终exp:

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `r.interactive()`

### Step 10: 没收到puts真实地址

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `4dfa01048c5e21251edd026fef5cf068`

### Step 11: 依然GOT EOF

- Route type: `ropgadget-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ropgadget to collect the smallest evidence slice that answers the goal.
- Tools: ropgadget
- Reasoning chain:
  - Recognize the section as ropgadget-driven evidence lookup.
  - Use ropgadget to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `payload1 = b'\x00'+b'a'*0x57+p64(ret)+p64(pop_rdi_addr)+p64(bin_sh)+p64(system_addr)`

### Step 12: 关于我的字符串前面都带一个b

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `查看链接网址后提示在每个字符串前面加上b即不会出现错误警告`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
