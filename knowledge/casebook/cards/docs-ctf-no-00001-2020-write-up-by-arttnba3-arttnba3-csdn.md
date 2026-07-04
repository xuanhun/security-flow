# 【CTF题解NO.00001】西安电子科技大学网络与信息安全学院2020年网络空间安全专业实验班选拔考试 - write up by arttnba3_arttnba3的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `docs`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【CTF题解NO.00001】西安电子科技大学网络与信息安全学院2020年网络空间安全专业实验班选拔考试---write-up-by-arttnba3_arttnba3的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90CTF%E9%A2%98%E8%A7%A3NO.00001%E3%80%91%E8%A5%BF%E5%AE%89%E7%94%B5%E5%AD%90%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6%E7%BD%91%E7%BB%9C%E4%B8%8E%E4%BF%A1%E6%81%AF%E5%AE%89%E5%85%A8%E5%AD%A6%E9%99%A22020%E5%B9%B4%E7%BD%91%E7%BB%9C%E7%A9%BA%E9%97%B4%E5%AE%89%E5%85%A8%E4%B8%93%E4%B8%9A%E5%AE%9E%E9%AA%8C%E7%8F%AD%E9%80%89%E6%8B%94%E8%80%83%E8%AF%95---write-up-by-arttnba3_arttnba3%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【CTF题解NO.00001】西安电子科技大学网络与信息安全学院2020年网络空间安全专业实验班选拔考试---write-up-by-arttnba3_arttnba3的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, ciphertext, pe-malware challenges.

## Input Signals

- Artifacts: binary, ciphertext, pe-malware
- Tools: checksec, dnspy, ida, netcat, pwntools
- Techniques: binary-exploitation, classical-crypto, dns-analysis, encoding-analysis, format-string, misc-analysis, reverse-engineering, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `10`
- `docs/img/80907fbd153462d35bf2e90c87acbe2b.png`
- `docs/img/784a30c18d27046489f9c7635f1a5443.png`
- `docs/img/244221c10cae2eb1f0bd4c8866ead908.png`
- `docs/img/e81308405c5602666aad015c1c981765.png`
- `docs/img/a68314b9cb6bbb93c19bd7ffe530b60b.png`
- `docs/img/f1833087ca6f2eda60f7ba94cd8ec84a.png`
- `docs/img/792feeab75af8c1a2c3e235dd91174dd.png`
- `docs/img/6e6d5e787f60c69bd261cbe316e2092f.png`
- `docs/img/092c01e3de1b75eef1e0e834bbc3c1e4.png`
- `docs/img/669461cd71756465e768897171bccde6.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, dnspy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, dnspy, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, dnspy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 【CTF题解NO.00001】西安电子科技大学网络与信息安全学院2020年网络空间安全专业实验班选拔考试 - write up by arttnba3_arttnba3的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, dnspy, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, dnspy, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, dnspy, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/arttnba3/article/details/108068170](https://blog.csdn.net/arttnba3/article/details/108068170)`

### Step 3: 【CTF题解NO.00001】西安电子科技大学网络与信息安全学院2020年网络空间安全专业实验班选拔考试 - write up by arttnba3

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, dnspy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, dnspy, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, dnspy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 4: 0x00.绪论

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, dnspy, ida, netcat to collect the smallest evidence slice that answers the goal.
- Tools: checksec, dnspy, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, dnspy, ida, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 5: 0x01.PWN (AK)

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, dnspy, ida, netcat to collect the smallest evidence slice that answers the goal.
- Tools: checksec, dnspy, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, dnspy, ida, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 6: cmcc_stack

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, ida, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `80907fbd153462d35bf2e90c87acbe2b`

### Step 7: pwn_canary

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use checksec, ida, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: checksec, ida, pwntools
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use checksec, ida, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a68314b9cb6bbb93c19bd7ffe530b60b`

### Step 8: 0x02.reverse

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, dnspy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, dnspy, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, dnspy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 9: Babyre

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use dnspy to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: dnspy
- Reasoning chain:
  - Recognize the section as dns pivot.
  - Use dnspy to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `669461cd71756465e768897171bccde6`

### Step 10: 0x03.misc

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, dnspy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, dnspy, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, dnspy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 11: hello

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use checksec, dnspy, ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: checksec, dnspy, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use checksec, dnspy, ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `* * *`

### Step 12: encrypt

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `其他的题都不会写了XDDDD果然我还是太菜了QAQ`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
