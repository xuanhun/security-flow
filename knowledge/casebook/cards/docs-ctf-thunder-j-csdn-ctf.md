# CTF-安卓逆向入门题目_Thunder_J的博客-CSDN博客_ctf 安卓逆向

## Case Metadata

- Category: `Reverse`
- Platform: `CTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF-安卓逆向入门题目_Thunder_J的博客-CSDN博客_ctf-安卓逆向.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF-%E5%AE%89%E5%8D%93%E9%80%86%E5%90%91%E5%85%A5%E9%97%A8%E9%A2%98%E7%9B%AE_Thunder_J%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctf-%E5%AE%89%E5%8D%93%E9%80%86%E5%90%91.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF-安卓逆向入门题目_Thunder_J的博客-CSDN博客_ctf-安卓逆向.md`

## Why This Case Matters

Use this case as a Reverse reference for apk-mobile, binary, ciphertext challenges.

## Input Signals

- Artifacts: apk-mobile, binary, ciphertext, web-app
- Tools: netcat, radare2
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, http-analysis, mobile-forensics, web-exploitation

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `19`
- `docs/img/cff67bbe25bdb9b1e9a216312bbbd83d.png`
- `docs/img/8bc577915c0ea02cd97fe8fee88e2081.png`
- `docs/img/b3763e07e8c89654160b26163bdc93a8.png`
- `docs/img/fd7656035f58a317b2638876175a8d46.png`
- `docs/img/f77ce2e884305ff0b2daf177b8b68ca4.png`
- `docs/img/51753d75d4474db3ab1a0e1284fd4440.png`
- `docs/img/648946db540a233ad2feda30a9b1b1a8.png`
- `docs/img/6cbbeff34bdfb18c945face0b2a91ab9.png`
- `docs/img/ca27bdfc020de859894b53845f2e0203.png`
- `docs/img/fd2d0b349eb8d0516472d2b7ed685e27.png`
- `docs/img/e912a2f839c0c3c1e216a49d1241a0cd.png`
- `docs/img/2dbcd98977be027db18570e35dcfe2e5.png`
- ... and `7` more

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF-安卓逆向入门题目_Thunder_J的博客-CSDN博客_ctf 安卓逆向

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/CharlesGodX/article/details/86602958](https://blog.csdn.net/CharlesGodX/article/details/86602958)`

### Step 3: 0x00：介绍

- Route type: `netcat-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `以下题目都是比较简单的安卓逆向题目，主要训练目的是熟悉安卓逆向的一些基础题目，如果是第一次接触安卓逆向，建议先去学一点安卓开发的相关知识，这样做题目就更快一些，当然题目做多了自然也就熟悉了，题目我都上传到Github上了，需要的可以下载。`

### Step 4: 链接：

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://github.com/ThunderJie/CTF-Practice/tree/master/CTF-Andorid%20Reverse/androideasy`

### Step 5: 解题思路：

- Route type: `netcat-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat with the extracted filter/query `分析函数内容，可以看出数组v0即是我们输入的注册码，根据if语句可以确定注册码的长度和s[]数组一样有31位，下面又有一个if语句判断即为我们的关键语句：s[v1] == (v0[v1] ^ 23)` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `分析函数内容，可以看出数组v0即是我们输入的注册码，根据if语句可以确定注册码的长度和s[]数组一样有31位，下面又有一个if语句判断即为我们的关键语句：s[v1] == (v0[v1] ^ 23)`
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat with the extracted filter/query `分析函数内容，可以看出数组v0即是我们输入的注册码，根据if语句可以确定注册码的长度和s[]数组一样有31位，下面又有一个if语句判断即为我们的关键语句：s[v1] == (v0[v1] ^ 23)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `cff67bbe25bdb9b1e9a216312bbbd83d`

### Step 6: 链接：

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://github.com/ThunderJie/CTF-Practice/tree/master/CTF-Andorid%20Reverse/simplecheck`

### Step 7: 解题思路：

- Route type: `netcat-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 with the extracted filter/query `a[m]== b[m] * v4[m]* v4[m] + c[m] * v4[m] + d[m]` and inspect the matching evidence.
- Tools: netcat, radare2
- Filters or commands:
  - `a[m]== b[m] * v4[m]* v4[m] + c[m] * v4[m] + d[m]`
  - `a[m+ 1] == b[m] * v4[m+ 1] * v4[m+ 1] + c[m] * v4[m+ 1] + d[m]`
  - `(a[m] == b[m] * i * i + c[m] * f + d[m])||(a[m] == b[m-1] * i * i + c[m-1] * i + d[m-1])`
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 with the extracted filter/query `a[m]== b[m] * v4[m]* v4[m] + c[m] * v4[m] + d[m]` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `f77ce2e884305ff0b2daf177b8b68ca4`

### Step 8: 链接：

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://github.com/ThunderJie/CTF-Practice/tree/master/CTF-Andorid%20Reverse/DD%20-%20Android%20Easy`

### Step 9: 解题思路：

- Route type: `netcat-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `fd2d0b349eb8d0516472d2b7ed685e27`

### Step 10: 链接：

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://github.com/ThunderJie/CTF-Practice/tree/master/CTF-Andorid%20Reverse/smali`

### Step 11: 解题思路：

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use radare2 with the extracted filter/query `cipher = "sSNnx1UKbYrA1+MOrdtDTA=="` and inspect the matching evidence.
- Tools: radare2
- Filters or commands:
  - `cipher = "sSNnx1UKbYrA1+MOrdtDTA=="`
  - `key = "cGhyYWNrICBjdGYgMjAxNg=="`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use radare2 with the extracted filter/query `cipher = "sSNnx1UKbYrA1+MOrdtDTA=="` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2dbcd98977be027db18570e35dcfe2e5`

### Step 12: 链接：

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://github.com/ThunderJie/CTF-Practice/tree/master/CTF-Andorid%20Reverse/CFF2016-%E7%88%AC%E6%A5%BC%E6%A2%AF`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
