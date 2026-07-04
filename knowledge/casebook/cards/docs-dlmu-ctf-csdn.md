# 大连海事大学第一届“启航杯”DLMU CTF部分题解_ℳ๓₯㎕₯㎕ζั的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `大连海事大学第一届“启航杯”DLMU CTF部分题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/大连海事大学第一届“启航杯”DLMU-CTF部分题解_ℳ๓₯㎕₯㎕ζั的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E5%A4%A7%E8%BF%9E%E6%B5%B7%E4%BA%8B%E5%A4%A7%E5%AD%A6%E7%AC%AC%E4%B8%80%E5%B1%8A%E2%80%9C%E5%90%AF%E8%88%AA%E6%9D%AF%E2%80%9DDLMU-CTF%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3_%E2%84%B3%E0%B9%93%E2%82%AF%E3%8E%95%E2%82%AF%E3%8E%95%CE%B6%E0%B8%B1%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/大连海事大学第一届“启航杯”DLMU-CTF部分题解_ℳ๓₯㎕₯㎕ζั的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for binary, ciphertext, pcap challenges.

## Input Signals

- Artifacts: binary, ciphertext, pcap, stego-media, web-app
- Tools: ida, netcat, wireshark
- Techniques: binary-exploitation, classical-crypto, command-injection, crypto-analysis, deserialization, encoding-analysis, file-inclusion, http-analysis, image-analysis, misc-analysis, network-forensics, php-tricks, qr-analysis, reverse-engineering, service-enumeration, traffic-analysis, web-exploitation

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `18`
- `docs/img/58f2abc6a4bcf4c475c4c1b861988a9c.png`
- `docs/img/5c3f2d202f606f68d2655bf30a5e4ef9.png`
- `docs/img/074128ef0087fcb4cd3e480f168dc495.png`
- `docs/img/f11490c80415e26721a7a7de9cbd61a2.png`
- `docs/img/6123aadca80502ce52214d16cdb84555.png`
- `docs/img/a0794692cadc00c83f76c97adea2322b.png`
- `docs/img/347dde27744e7b00d3b3bfe0a612592a.png`
- `docs/img/e6ac13544e9865e4bbf979d8e472e3b1.png`
- `docs/img/a3127cd7f1845929e69afb6401379b78.png`
- `docs/img/c29f0564dca0058a52ef6c28788bb3f5.png`
- `docs/img/8e2dd11876e0206258dd9c559b34fd04.png`
- `docs/img/d2b3f1e23a5500d0e7884eb1a6da4827.png`
- ... and `6` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, wireshark
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 大连海事大学第一届“启航杯”DLMU CTF部分题解_ℳ๓₯㎕₯㎕ζั的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, netcat, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, netcat, wireshark
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, netcat, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/tmmxa/article/details/111091911](https://blog.csdn.net/tmmxa/article/details/111091911)`

### Step 3: 0\. dlmuctf2020

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, wireshark
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `dlmuctf{welcome_to_dlmuctf2020}`

### Step 4: 1\. 早安，贝丝人

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query ``TVJXRzI1TERPUlRIV1NCV09aU1Y2TlM3TTRZREFaQzdNUTNIU0lMNQ==`` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - ``TVJXRzI1TERPUlRIV1NCV09aU1Y2TlM3TTRZREFaQzdNUTNIU0lMNQ==``
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query ``TVJXRzI1TERPUlRIV1NCV09aU1Y2TlM3TTRZREFaQzdNUTNIU0lMNQ==`` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `​ 很明显的Base64编码，解密后得到`MRWG25LDORTHWSBWOZSV6NS7M4YDAZC7MQ3HSIL5`,在进行Base32解码，拿到flag：`dlmuctf{H6ve_6_g00d_d6y!}``

### Step 5: 2\. lsp了

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use ida, netcat, wireshark to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: ida, netcat, wireshark
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use ida, netcat, wireshark to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `58f2abc6a4bcf4c475c4c1b861988a9c`

### Step 6: 3\. base2sth

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat, wireshark to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat, wireshark
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat, wireshark to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5c3f2d202f606f68d2655bf30a5e4ef9`

### Step 7: 4\. docz

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, wireshark
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `074128ef0087fcb4cd3e480f168dc495`

### Step 8: 5\. jigsaw

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use ida, netcat, wireshark to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: ida, netcat, wireshark
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use ida, netcat, wireshark to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `f11490c80415e26721a7a7de9cbd61a2`

### Step 9: 6\. 经典三合一

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat, wireshark to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat, wireshark
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat, wireshark to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `​ 先栅栏得`oujp{Rb_rc_anjuuh_NJBH?}`，再凯撒得到`flag{Is_it_really_EASY?}``

### Step 10: 7\. XOR

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `char a[]="DsfvD-jZ|,+p}sX.zIfvzYrh|pSvWMX'";` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `char a[]="DsfvD-jZ|,+p}sX.zIfvzYrh|pSvWMX'";`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `char a[]="DsfvD-jZ|,+p}sX.zIfvzYrh|pSvWMX'";` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a0794692cadc00c83f76c97adea2322b`

### Step 11: 8\. RSA

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat, wireshark to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat, wireshark
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat, wireshark to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `​ 把得到的16进制的明文HEX转码，拿到flag`

### Step 12: 9\. RSA_plus

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat, wireshark to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat, wireshark
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat, wireshark to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `把得到的16进制的明文HEX转码，拿到flag`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
