# 【CTF题解NO.00007】VNCTF2021 - pwn - write up by arttnba3_arttnba3的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `【CTF题解NO.00007】VNCTF2021`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【CTF题解NO.00007】VNCTF2021---pwn---write-up-by-arttnba3_arttnba3的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90CTF%E9%A2%98%E8%A7%A3NO.00007%E3%80%91VNCTF2021---pwn---write-up-by-arttnba3_arttnba3%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【CTF题解NO.00007】VNCTF2021---pwn---write-up-by-arttnba3_arttnba3的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: checksec, ida, netcat, pwntools
- Techniques: binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis, http-analysis, ret2libc, reverse-engineering, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `20`
- `docs/img/5e6212e61673938bc72f10c178484656.png`
- `docs/img/7b356db041ac66b42d67c039924aeafc.png`
- `docs/img/69fdd4828a7d0efbf5ee76023c386af7.png`
- `docs/img/1364f190df2cbe4ca0a77c22803432fd.png`
- `docs/img/2befbba7a3ecf8937c5c0a3b94aac65b.png`
- `docs/img/a1ec79ad916a2e9aa317c0f50835cd94.png`
- `docs/img/b5c9252f9a1fd41d2623524dfe5b275b.png`
- `docs/img/7552abc407219aa5578b71a3a6303d15.png`
- `docs/img/be720ee084ac0b9bb1c52c4f651dfac6.png`
- `docs/img/20d0dbe3a511a1529270b1a5072eb0aa.png`
- `docs/img/545e50ff27730c9032cdd78bb4088ace.png`
- `docs/img/2474881b3be3f00a56268bd5327e9037.png`
- ... and `8` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 【CTF题解NO.00007】VNCTF2021 - pwn - write up by arttnba3_arttnba3的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/arttnba3/article/details/115447496](https://blog.csdn.net/arttnba3/article/details/115447496)`

### Step 3: VNCTF2021 - Pwn

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `太棒了，我逐渐理解一切.jpg`

### Step 4: [VNCTF 2021]White_Give_Flag - read out of bounds

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, ida, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, ida, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5e6212e61673938bc72f10c178484656`

### Step 5: [VNCTF 2021]ff - tcache poisoning + IO_FILE hijack

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use checksec, ida, netcat, pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use checksec, ida, netcat, pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a1ec79ad916a2e9aa317c0f50835cd94`

### Step 6: [VNCTF 2021]LittleRedFlower

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, ida, netcat, pwntools with the extracted filter/query `#define NARENAS_FROM_NCORES(n) ((n) * (sizeof (long) == 4 ? 2 : 8))` and inspect the matching evidence.
- Tools: checksec, ida, netcat, pwntools
- Filters or commands:
  - `#define NARENAS_FROM_NCORES(n) ((n) * (sizeof (long) == 4 ? 2 : 8))`
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, ida, netcat, pwntools with the extracted filter/query `#define NARENAS_FROM_NCORES(n) ((n) * (sizeof (long) == 4 ? 2 : 8))` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2474881b3be3f00a56268bd5327e9037`

### Step 7: 个人感受

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `3682894c64ca69eed416d4c536ad6da1`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
