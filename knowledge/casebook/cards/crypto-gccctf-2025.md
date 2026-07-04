# [GCCCTF 2025]密钥危机

## Case Metadata

- Category: `Crypto`
- Platform: `GCCCTF 2025`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `crypto/[GCCCTF 2025]密钥危机.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/crypto/%5BGCCCTF%202025%5D%E5%AF%86%E9%92%A5%E5%8D%B1%E6%9C%BA.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/crypto/[GCCCTF 2025]密钥危机.md`

## Why This Case Matters

Use this case as a Crypto reference for binary, ciphertext challenges.

## Input Signals

- Artifacts: binary, ciphertext
- Tools: ida, netcat
- Techniques: crypto-analysis, encoding-analysis, reverse-engineering

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Solve Thinking

### Step 1: 看到什么

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这是一个RSA共享质因子攻击题目。题目给出了10个RSA密钥和对应的密文。`

### Step 2: 想到什么解题思路

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `对所有RSA模数进行两两GCD计算，然后共享质因子攻击`

### Step 3: 尝试过程和结果记录

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 4: EXP

- Route type: `ida-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, netcat to collect the smallest evidence slice that answers the goal.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `#!/usr/bin/env python3`

### Step 5: python find_shared_pairs.py data.json

- Route type: `ida-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, netcat to collect the smallest evidence slice that answers the goal.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `#`

### Step 6: - 将结果保存到 candidates.txt 供后续攻击使用

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `1. 相等模数对: n1 == n2 (共模攻击候选)` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `1. 相等模数对: n1 == n2 (共模攻击候选)`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `1. 相等模数对: n1 == n2 (共模攻击候选)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `n_to_idxs = {} # 模数 -> 索引列表的映射`

### Step 7: 构建模数到索引的映射，便于检测重复

- Route type: `ida-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, netcat to collect the smallest evidence slice that answers the goal.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `n_to_idxs.setdefault(key, []).append(idx)`

### Step 8: 检查每个模数值，如果对应多个索引，说明有相同模数

- Route type: `ida-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, netcat to collect the smallest evidence slice that answers the goal.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `if len(idxs) > 1: # 如果有多个密钥使用相同模数`

### Step 9: 生成所有可能的密钥对组合

- Route type: `ida-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, netcat to collect the smallest evidence slice that answers the goal.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `equal_pairs.append((idxs[i], idxs[j], mpz(key)))`

### Step 10: 获取所有模数及其索引

- Route type: `ida-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, netcat to collect the smallest evidence slice that answers the goal.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `N = len(n_list)`

### Step 11: 逐一比较所有密钥对的模数

- Route type: `ida-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, netcat with the extracted filter/query `if n_i == n_j: # 跳过相同模数的对 (已在步骤1处理)` and inspect the matching evidence.
- Tools: ida, netcat
- Filters or commands:
  - `if n_i == n_j: # 跳过相同模数的对 (已在步骤1处理)`
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, netcat with the extracted filter/query `if n_i == n_j: # 跳过相同模数的对 (已在步骤1处理)` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `continue`

### Step 12: 计算两个模数的最大公约数

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat with the extracted filter/query `if g != 1: # 如果gcd > 1，说明有共享质因子` and inspect the matching evidence.
- Tools: ida, netcat
- Filters or commands:
  - `if g != 1: # 如果gcd > 1，说明有共享质因子`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat with the extracted filter/query `if g != 1: # 如果gcd > 1，说明有共享质因子` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `"""`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
