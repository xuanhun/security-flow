# 【CTF WriteUp】UTCTF 2020部分题解_零食商人的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `【CTF WriteUp】UTCTF 2020部分题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【CTF-WriteUp】UTCTF-2020部分题解_零食商人的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90CTF-WriteUp%E3%80%91UTCTF-2020%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3_%E9%9B%B6%E9%A3%9F%E5%95%86%E4%BA%BA%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【CTF-WriteUp】UTCTF-2020部分题解_零食商人的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app, web-service
- Tools: burp, netcat, pwntools, radare2, z3
- Techniques: binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis, http-analysis, image-analysis, php-tricks, qr-analysis, symbolic-execution, web-exploitation

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `3`
- `docs/img/4e0f456fbc101dc30728319a78888932.png`
- `docs/img/d3a7d3996bd69e189173bca3b8369a03.png`
- `docs/img/1fd60791523c93138352450435e584f5.png`

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat, pwntools, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat, pwntools, radare2, z3
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat, pwntools, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 【CTF WriteUp】UTCTF 2020部分题解_零食商人的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat, pwntools, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat, pwntools, radare2, z3
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat, pwntools, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `看大佬们不屑于写这种比赛的WP，那就我这个菜鸡来献丑了`

### Step 3: [basics] crypto

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use netcat, radare2, z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use netcat, radare2, z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `utflag{n0w_th4ts_wh4t_i_c4ll_crypt0}`

### Step 4: One True Problem

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp, netcat, pwntools, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: burp, netcat, pwntools, radare2, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp, netcat, pwntools, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `utflag{tw0_tim3_p4ds}`

### Step 5: Hill

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp, netcat, pwntools, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: burp, netcat, pwntools, radare2, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp, netcat, pwntools, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `utflag{d4nger0us_c1pherText_qq}`

### Step 6: Galois

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4e0f456fbc101dc30728319a78888932`

### Step 7: Random ECB

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp, netcat, pwntools, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: burp, netcat, pwntools, radare2, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp, netcat, pwntools, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `#!/usr/bin/env python`

### Step 8: -*- coding: utf-8 -*-

- Route type: `pwntools-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use pwntools to collect the smallest evidence slice that answers the goal.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as pwntools-driven evidence lookup.
  - Use pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `s = r.recvline()`

### Step 9: print 'RECEIVE: %s %s' % (s.strip(), str(len(s.strip())))

- Route type: `burp-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat, pwntools, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat, pwntools, radare2, z3
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat, pwntools, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `return s.strip()`

### Step 10: Step 1: find length of flag

- Route type: `burp-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat, pwntools, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat, pwntools, radare2, z3
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat, pwntools, radare2 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flaglength = 30`

### Step 11: Step2: get result of different padding A

- Route type: `burp-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat, pwntools, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat, pwntools, radare2, z3
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat, pwntools, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `break`

### Step 12: Step 3: begin to burp 1~15 digit

- Route type: `burp-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat, pwntools, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat, pwntools, radare2, z3
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat, pwntools, radare2 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4.flag的16-30位方法类似，由于ECB各段不干扰的特型，我们直接比对第二个128位即可`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
