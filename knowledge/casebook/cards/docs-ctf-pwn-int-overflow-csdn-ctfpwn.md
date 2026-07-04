# CTF|pwn栈溢出题目int_overflow解题思路及个人总结_一个不融化的雪人的博客-CSDN博客_ctfpwn栈溢出

## Case Metadata

- Category: `Pwn`
- Platform: `CTF|pwn栈溢出题目int`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF｜pwn栈溢出题目int_overflow解题思路及个人总结_一个不融化的雪人的博客-CSDN博客_ctfpwn栈溢出.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%EF%BD%9Cpwn%E6%A0%88%E6%BA%A2%E5%87%BA%E9%A2%98%E7%9B%AEint_overflow%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF%E5%8F%8A%E4%B8%AA%E4%BA%BA%E6%80%BB%E7%BB%93_%E4%B8%80%E4%B8%AA%E4%B8%8D%E8%9E%8D%E5%8C%96%E7%9A%84%E9%9B%AA%E4%BA%BA%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctfpwn%E6%A0%88%E6%BA%A2%E5%87%BA.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF｜pwn栈溢出题目int_overflow解题思路及个人总结_一个不融化的雪人的博客-CSDN博客_ctfpwn栈溢出.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: ida, pwntools
- Techniques: binary-exploitation, integer-overflow, reverse-engineering, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `9`
- `docs/img/c085246fdd4c910b0f6fd564798fbbbe.png`
- `docs/img/a2185f62f7d849b702a107b1492f88c1.png`
- `docs/img/649c968f087c09d6f17de8731b25612e.png`
- `docs/img/ac11672b0ccff9a1b0971c88f76a0e59.png`
- `docs/img/f0bf9ae85cd62fd73e53bd3818efe3f9.png`
- `docs/img/26228de4af2ab8b88d520b083eec4b78.png`
- `docs/img/76c5651e0dcbce4b5065a8416f3c760e.png`
- `docs/img/67765a11f27564a4619ae8068963ad9d.png`
- `docs/img/fa42d505cafb22865ae860d27f669975.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF|pwn栈溢出题目int_overflow解题思路及个人总结_一个不融化的雪人的博客-CSDN博客_ctfpwn栈溢出

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/skyattractive/article/details/106459465](https://blog.csdn.net/skyattractive/article/details/106459465)`

### Step 3: 解题思路

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `124.126.19.106`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
