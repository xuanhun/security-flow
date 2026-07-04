# 深信服杯 CTF 线上 逆向题解_pipixia233333的博客-CSDN博客

## Case Metadata

- Category: `Reverse`
- Platform: `深信服杯 CTF 线上 逆向题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/深信服杯-CTF-线上-逆向题解_pipixia233333的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E6%B7%B1%E4%BF%A1%E6%9C%8D%E6%9D%AF-CTF-%E7%BA%BF%E4%B8%8A-%E9%80%86%E5%90%91%E9%A2%98%E8%A7%A3_pipixia233333%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/深信服杯-CTF-线上-逆向题解_pipixia233333的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Reverse reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: ida, netcat, z3
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, file-inclusion, reverse-engineering, symbolic-execution

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `6`
- `docs/img/4742d958a84409c4bc3b65f8fa68f278.png`
- `docs/img/1954e71542aa34d622a0f5848926a5af.png`
- `docs/img/ac5e5e42e69b1a4b3bc4b4dfc34e564b.png`
- `docs/img/0a44bbb4c141b3ef624b782209c30c9c.png`
- `docs/img/cf38ad413daabfdf7e89212f5f5fc8c6.png`
- `docs/img/fdff09d5cea3675f1de331102b9f3db0.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, z3
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 深信服杯 CTF 线上 逆向题解_pipixia233333的博客-CSDN博客

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use ida, netcat, z3 with the extracted filter/query `s.add(l[5 * i + j]!=l[5 * i + k])` and inspect the matching evidence.
- Tools: ida, netcat, z3
- Filters or commands:
  - `s.add(l[5 * i + j]!=l[5 * i + k])`
  - `s.add(l[ 5 * j + i]!=l[5 * k + i])`
  - `result = os. popen('echo ' + str(i) + '|./number_game')`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use ida, netcat, z3 with the extracted filter/query `s.add(l[5 * i + j]!=l[5 * i + k])` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4742d958a84409c4bc3b65f8fa68f278`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
