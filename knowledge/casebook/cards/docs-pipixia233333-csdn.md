# 实验吧 部分逆向题解_pipixia233333的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `实验吧 部分逆向题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/实验吧-部分逆向题解_pipixia233333的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E5%AE%9E%E9%AA%8C%E5%90%A7-%E9%83%A8%E5%88%86%E9%80%86%E5%90%91%E9%A2%98%E8%A7%A3_pipixia233333%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/实验吧-部分逆向题解_pipixia233333的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: ida, netcat
- Techniques: binary-exploitation, classical-crypto, command-injection, crypto-analysis, encoding-analysis, file-inclusion, http-analysis, integer-overflow, qr-analysis, ret2libc, reverse-engineering, siem-query, symbolic-execution

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `58`
- `docs/img/7118dc63eec9a5c1f96be17df02fb72b.png`
- `docs/img/1e6f40410195aa2e132287b9c29ffa9f.png`
- `docs/img/2c3367184c9aafa98fb059c9f77191d3.png`
- `docs/img/e0548087b31ef39549fae9cf5d42728f.png`
- `docs/img/b5d5163faf49848d317a4c93f629d05c.png`
- `docs/img/96565fd2516b46281d0b70ad1d11701d.png`
- `docs/img/4c017e71fd118932936ff271c0ad8788.png`
- `docs/img/31fcb5b0ee661a2f09682d85459290e8.png`
- `docs/img/92a0a0315cf2492a02ce78207720015f.png`
- `docs/img/1eecfbd402ce9f7c0dafff1a634f91ec.png`
- `docs/img/c6f2a4f433171f5f0e56092fcfd0783a.png`
- `docs/img/8f1e4aa3cba6f66e4328639a901322ff.png`
- ... and `46` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 实验吧 部分逆向题解_pipixia233333的博客-CSDN博客

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use ida, netcat with the extracted filter/query `if(flag==1)` and inspect the matching evidence.
- Tools: ida, netcat
- Filters or commands:
  - `if(flag==1)`
  - `if(fg==NULL)`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use ida, netcat with the extracted filter/query `if(flag==1)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7118dc63eec9a5c1f96be17df02fb72b`

### Step 3: -*- coding:utf-8 -*-

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use ida, netcat with the extracted filter/query `ret=os. popen('echo "'+ss +'" |./tlc')` and inspect the matching evidence.
- Tools: ida, netcat
- Filters or commands:
  - `ret=os. popen('echo "'+ss +'" |./tlc')`
  - `putchar(((unsigned __int8)j >> 4) | 16 * j);`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use ida, netcat with the extracted filter/query `ret=os. popen('echo "'+ss +'" |./tlc')` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6c12a0bd7f9346bcf34cafdc8430761d`

### Step 4: catalyst-system

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c525fce0737c8ab6aff613b2b38f3004`

### Step 5: defcamp

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `e57276daaa5f3124b6b5239c6fd6252d`

### Step 6: reversemeplz

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `if ( (v1 & 0x3F) != 38 )` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if ( (v1 & 0x3F) != 38 )`
  - `v3 = v2 | (v1 << 8) | 9 * ((v1 & 0x5F) == 86);`
  - `if ( (v1 & 0x77) != 116 )`
  - `v5 = v4 | v3;`
  - `if ( (v1 & 0x3F) != 39 )`
  - `v7 = v6 | v5;`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `if ( (v1 & 0x3F) != 38 )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `46b861c858e0b0cecf7bb6b6351e397c`

### Step 7: bitwise

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat with the extracted filter/query `#255 ==11111111 最后结果取 8个二进制 那么` and inspect the matching evidence.
- Tools: ida, netcat
- Filters or commands:
  - `#255 ==11111111 最后结果取 8个二进制 那么`
  - `temp=((i>>5)|(i<<3))&255`
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat with the extracted filter/query `#255 ==11111111 最后结果取 8个二进制 那么` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `7dd8144871bbfd0c644b79483d6b5dec`

### Step 8: 逆向观察

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use ida to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: ida
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use ida to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6f16c2bf66205b6fb5f4d508cb44cb9f`

### Step 9: 迷路

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use ida, netcat with the extracted filter/query `if((j*5+28)%26==s[i]-temp)` and inspect the matching evidence.
- Tools: ida, netcat
- Filters or commands:
  - `if((j*5+28)%26==s[i]-temp)`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use ida, netcat with the extracted filter/query `if((j*5+28)%26==s[i]-temp)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `63c42bc80bebcd8a6da77aa2378ea029`

### Step 10: NSCTF Reverse 400

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use ida, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use ida, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a7b4e8dd9c8d102f99c6cf0e19ee0133`

### Step 11: encoding: utf-8

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `91202e7b5634276aff68e9caf7c39781`

### Step 12: Keylead（ASIS CTF 2015）

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4c97bf2dc4d2cee4bd0a3123f5f5b6d3`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
