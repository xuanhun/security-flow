# unctf2020部分题解_tansty_zh的博客-CSDN博客

## Case Metadata

- Category: `Misc`
- Platform: `unctf2020部分题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/unctf2020部分题解_tansty_zh的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/unctf2020%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3_tansty_zh%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/unctf2020部分题解_tansty_zh的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Misc reference for binary, ciphertext, linux-logs challenges.

## Input Signals

- Artifacts: binary, ciphertext, linux-logs, pcap, stego-media, web-app
- Tools: ida, john, netcat, pwntools, radare2, tshark
- Techniques: binary-exploitation, classical-crypto, command-injection, crypto-analysis, dns-analysis, encoding-analysis, http-analysis, image-analysis, misc-analysis, network-forensics, password-cracking, qr-analysis, ret2libc, reverse-engineering, sql-injection, traffic-analysis, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `48`
- `docs/img/fb688046bb9658355ce91ca5a7da3598.png`
- `docs/img/c076957c12abf6db0602da55e161fa75.png`
- `docs/img/36b1be8c75838b1ac5600866062801ee.png`
- `docs/img/2f37129165e3818f5a13fe523380f37d.png`
- `docs/img/9f195dfebe51d3516af80e00a2c656d0.png`
- `docs/img/24923882326c94f70034e0ebc7a8a988.png`
- `docs/img/7c5301f0149e8f91ab2b16c218dfad7f.png`
- `docs/img/6dad787e43575bf0fc1be54cba12e5f8.png`
- `docs/img/13248c7a088d42fc3861717e8491b810.png`
- `docs/img/6e7e1e2f209d3d694bf261902097bc5e.png`
- `docs/img/909fc3bd93f195d1f92490163a36e20e.png`
- `docs/img/470f541d44e2af4d0a32bfeec5bcf58e.png`
- ... and `36` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, john, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, john, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, john, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: unctf2020部分题解_tansty_zh的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, john, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, john, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, john, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/tansty_zh/article/details/109707327](https://blog.csdn.net/tansty_zh/article/details/109707327)`

### Step 3: ⭐unctf2020

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `**友链：https://www.cnblogs.com/Jlay/p/unctf_2020.html**`

### Step 4: baba_is_you

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `fb688046bb9658355ce91ca5a7da3598`

### Step 5: 阴阳人编码

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, john, netcat, pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, john, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, john, netcat, pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c076957c12abf6db0602da55e161fa75`

### Step 6: 爷的历险记

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2f37129165e3818f5a13fe523380f37d`

### Step 7: YLB’s CAPTCHA - 签到题

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `13248c7a088d42fc3861717e8491b810`

### Step 8: 躲猫猫

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `dW5jdGYlN0I3MzgzYjY3ZGU5MTA2YTZmMTBmZGJlNGU4ZWJjNjRjZSU3RA==` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `dW5jdGYlN0I3MzgzYjY3ZGU5MTA2YTZmMTBmZGJlNGU4ZWJjNjRjZSU3RA==`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `dW5jdGYlN0I3MzgzYjY3ZGU5MTA2YTZmMTBmZGJlNGU4ZWJjNjRjZSU3RA==` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6e7e1e2f209d3d694bf261902097bc5e`

### Step 9: 网络深处1

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use ida, john, netcat, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: ida, john, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use ida, john, netcat, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `909fc3bd93f195d1f92490163a36e20e`

### Step 10: Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use ida, netcat with the extracted filter/query `flag{Y29pbA==}` and inspect the matching evidence.
- Tools: ida, netcat
- Filters or commands:
  - `flag{Y29pbA==}`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use ida, netcat with the extracted filter/query `flag{Y29pbA==}` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `043b36b25b1894f6062d141d89372787`

### Step 11: 被删除的flag

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6e7882b5e071c2b9f19fa959861863f3`

### Step 12: 你能破解我的密码吗

- Route type: `incident timeline reconstruction`
- Why: Incident-response cases become reusable when every claim is anchored to timestamped artifact correlation.
- Probe: Use john, netcat with the extracted filter/query `john --show shadow` and inspect the matching evidence.
- Tools: john, netcat
- Filters or commands:
  - `john --show shadow`
- Reasoning chain:
  - Recognize the section as incident timeline reconstruction.
  - Use john, netcat with the extracted filter/query `john --show shadow` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `804080a27e16f9509e06e9591421214e`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
