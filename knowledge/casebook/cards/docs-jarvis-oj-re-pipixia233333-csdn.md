# Jarvis OJ 刷题题解 RE_pipixia233333的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `Jarvis OJ 刷题题解 RE`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/Jarvis-OJ-刷题题解-RE_pipixia233333的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/Jarvis-OJ-%E5%88%B7%E9%A2%98%E9%A2%98%E8%A7%A3-RE_pipixia233333%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/Jarvis-OJ-刷题题解-RE_pipixia233333的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for apk-mobile, binary, ciphertext challenges.

## Input Signals

- Artifacts: apk-mobile, binary, ciphertext, web-app
- Tools: ida, netcat, radare2, z3
- Techniques: binary-exploitation, classical-crypto, crypto-analysis, dns-analysis, encoding-analysis, file-inclusion, mobile-forensics, php-tricks, reverse-engineering, symbolic-execution

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `67`
- `docs/img/faea95e3d0a2c51dd6ace25bd3bad157.png`
- `docs/img/907dc88aa1b8200c7c0e8c4a9d8b5211.png`
- `docs/img/7158c95a8efa39c24530131fa123a898.png`
- `docs/img/022a49367c8a2025c9e5f774dcf16979.png`
- `docs/img/a10bd8f4f5c5cf65a6c31aa9273233b7.png`
- `docs/img/ab0da8c4c7aca363f599c7da5c336a16.png`
- `docs/img/0d8cde2816cde61d55df88b00c88d08b.png`
- `docs/img/cc12e11a6c4ad99c871b7f5b51018909.png`
- `docs/img/f0c41dd50eb97561cf91840fae55ba52.png`
- `docs/img/3a18b723075996c8615e5eb2a2b7800c.png`
- `docs/img/cc3414433f3c2121f6c7813592daeaba.png`
- `docs/img/4c5d488c3ba7b5b483aba486ef1be980.png`
- ... and `55` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, radare2, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, radare2, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: Jarvis OJ 刷题题解 RE_pipixia233333的博客-CSDN博客

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use ida, netcat, radare2, z3 with the extracted filter/query `以前也写过几道 === 希望能把上面的题目刷个80%。。` and inspect the matching evidence.
- Tools: ida, netcat, radare2, z3
- Filters or commands:
  - `以前也写过几道 === 希望能把上面的题目刷个80%。。`
  - `这个我以前貌似看过夜影巨巨的博客 。。。。。 貌似 把这个题就做出来了====`
  - `然后就是字节数进行解密= ==`
  - `s.add((l[3] + l[2] + l[1] + l[0] )%256 == 71)`
  - `s.add((l[7] + l[6] + l[5])%256 == 3)`
  - `s.add(l[0]%256 == l[1] + 68)`
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use ida, netcat, radare2, z3 with the extracted filter/query `以前也写过几道 === 希望能把上面的题目刷个80%。。` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `faea95e3d0a2c51dd6ace25bd3bad157`

### Step 3: 输出方程的解

- Route type: `ida-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
- Tools: ida, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `print('\t', end='')`

### Step 4: 查表

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, radare2, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, radare2, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `c = p`

### Step 5: 输出flag

- Route type: `ida-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
- Tools: ida, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `print(hex(i)[2:].zfill(2).upper(), end='')`

### Step 6: 排除该解后继续求解

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use ida, netcat, radare2, z3 with the extracted filter/query `s.add(l[0] != m[l[0]].as_long())` and inspect the matching evidence.
- Tools: ida, netcat, radare2, z3
- Filters or commands:
  - `s.add(l[0] != m[l[0]].as_long())`
  - `遍历文件夹等 然后遇到docx 开始传输==`
  - `然后其实上面的脚本问题我也是吃过亏 但是还是没有长记性 == 是我太菜了，，`
  - `const-string v0, "cGhyYWNrICBjdGYgMjAxNg==" #将这个字符串给v0`
  - `const-string v0, "sSNnx1UKbYrA1+MOrdtDTA=="`
  - `这里 p0->str2 是 cGhyYWNrICBjdGYgMjAxNg== 而 "sSNnx1UKbYrA1+MOrdtDTA== 为 参数 传进了函数里面`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use ida, netcat, radare2, z3 with the extracted filter/query `s.add(l[0] != m[l[0]].as_long())` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0f73b4b4b179623d2f622751c87544fd`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
