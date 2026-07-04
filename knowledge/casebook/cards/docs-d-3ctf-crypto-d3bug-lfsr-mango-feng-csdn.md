# D^3CTF(Crypto-D3bug详解 LFSR题目）_Mango|Feng的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `D^3CTF(Crypto`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/D^3CTF(Crypto-D3bug详解-LFSR题目）_Mango｜Feng的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/D%5E3CTF%28Crypto-D3bug%E8%AF%A6%E8%A7%A3-LFSR%E9%A2%98%E7%9B%AE%EF%BC%89_Mango%EF%BD%9CFeng%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/D^3CTF(Crypto-D3bug详解-LFSR题目）_Mango｜Feng的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: z3
- Techniques: crypto-analysis, http-analysis, symbolic-execution, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Solve Thinking

### Step 1: Document

- Route type: `z3-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use z3 to collect the smallest evidence slice that answers the goal.
- Tools: z3
- Reasoning chain:
  - Recognize the section as z3-driven evidence lookup.
  - Use z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: D^3CTF(Crypto-D3bug详解 LFSR题目）_Mango|Feng的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: z3
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/ZoeMG/article/details/123499857](https://blog.csdn.net/ZoeMG/article/details/123499857)`

### Step 3: 题目

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `在复现的时候，查看许多write up里只有一个关键词:`爆破` (头都看大了好吧，主要还说是一个签到题)`

### Step 4: (lfsr_MyCode)step by step：

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use z3 with the extracted filter/query `当 l a s t b i t ( n ) = = 0 时 ： 对 l a s t b i t ( n + 1 ) 产 生 无 影 响 ， 因 为 0 ⊕ 0 = 0 ， 0 ⊕ 1 = 1 当lastbit(n)==0时：对lastbit(n+1)产生无影响，因为0\oplus 0=0，0\oplus1=1 当lastbit(n)==0时：对lastbit(n+1)产生无影响，因为0⊕0=0，0⊕1=1` and inspect the matching evidence.
- Tools: z3
- Filters or commands:
  - `当 l a s t b i t ( n ) = = 0 时 ： 对 l a s t b i t ( n + 1 ) 产 生 无 影 响 ， 因 为 0 ⊕ 0 = 0 ， 0 ⊕ 1 = 1 当lastbit(n)==0时：对lastbit(n+1)产生无影响，因为0\oplus 0=0，0\oplus1=1 当lastbit(n)==0时：对lastbit(n+1)产生无影响，因为0⊕0=0，0⊕1=1`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use z3 with the extracted filter/query `当 l a s t b i t ( n ) = = 0 时 ： 对 l a s t b i t ( n + 1 ) 产 生 无 影 响 ， 因 为 0 ⊕ 0 = 0 ， 0 ⊕ 1 = 1 当lastbit(n)==0时：对lastbit(n+1)产生无影响，因为0\oplus 0=0，0\oplus1=1 当lastbit(n)==0时：对lastbit(n+1)产生无影响，因为0⊕0=0，0⊕1=1` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `00100110001000110001101010101001001`

### Step 5: lfsr_CopiedfromInternet()

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: z3
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0100110001000110001101010101001001`

### Step 6: 需要注意的是：

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 with the extracted filter/query `"""so.add(a[1]^a[3]^a[6]^a[13]^a[21]^a[25]^a[28]^a[30]^a[33]^a[35]^a[38]^a[45]^a[53]^a[57]^a[60]^a[62]==0)` and inspect the matching evidence.
- Tools: z3
- Filters or commands:
  - `"""so.add(a[1]^a[3]^a[6]^a[13]^a[21]^a[25]^a[28]^a[30]^a[33]^a[35]^a[38]^a[45]^a[53]^a[57]^a[60]^a[62]==0)`
  - `so.add(a[2]^a[4]^a[7]^a[14]^a[22]^a[26]^a[29]^a[31]^a[34]^a[36]^a[39]^a[46]^a[54]^a[58]^a[61]^a[63]==1)`
  - `so.add(a[3]^a[5]^a[8]^a[15]^a[23]^a[27]^a[30]^a[32]^a[35]^a[37]^a[40]^a[47]^a[55]^a[59]^a[62]^a[64]==1)`
  - `so.add(a[4]^a[6]^a[9]^a[16]^a[24]^a[28]^a[31]^a[33]^a[36]^a[38]^a[41]^a[48]^a[56]^a[60]^a[63]^b[1]==1)`
  - `so.add(a[5]^a[7]^a[10]^a[17]^a[25]^a[29]^a[32]^a[34]^a[37]^a[39]^a[42]^a[49]^a[57]^a[61]^a[64]^b[2]==1)`
  - `so.add(a[6]^a[8]^a[11]^a[18]^a[26]^a[30]^a[33]^a[35]^a[38]^a[40]^a[43]^a[50]^a[58]^a[62]^b[1]^b[3]==1)`
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 with the extracted filter/query `"""so.add(a[1]^a[3]^a[6]^a[13]^a[21]^a[25]^a[28]^a[30]^a[33]^a[35]^a[38]^a[45]^a[53]^a[57]^a[60]^a[62]==0)` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0100110001000110001101010101001001`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
