# bugkuCTF web进阶+web最后两题_goddemon的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `bugkuCTF web进阶+web最后两题`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/bugkuCTF-web进阶+web最后两题_goddemon的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/bugkuCTF-web%E8%BF%9B%E9%98%B6%2Bweb%E6%9C%80%E5%90%8E%E4%B8%A4%E9%A2%98_goddemon%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/bugkuCTF-web进阶+web最后两题_goddemon的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: ida, netcat, radare2
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, http-analysis, reverse-engineering, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `12`
- `docs/img/3d805408431c41a93a02d218b1276148.png`
- `docs/img/e83e1aafa517e2199e67db317965bd0c.png`
- `docs/img/294f22aea625fe50f54e86914803d57b.png`
- `docs/img/78d14d2fb747cfa3fbd13d8addc82c45.png`
- `docs/img/5f3d557ba84ac59e69f00bfd7b186930.png`
- `docs/img/aa8cf4d0bc2adabb6fb35fa4c06d5905.png`
- `docs/img/68da96513cc90676b9a206839e14ec9d.png`
- `docs/img/7f1fdf3b0771f27ba154a7cb993692f8.png`
- `docs/img/d5db4d612234522a808c48a81632e0f7.png`
- `docs/img/76cc84aa2869a95454c05400d985f07a.png`
- `docs/img/5eee00d1dfcf04101325243415b2304c.png`
- `docs/img/3a579d78f94ee65d742053a4368b517a.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, radare2
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: bugkuCTF web进阶+web最后两题_goddemon的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_33942040/article/details/109131637](https://blog.csdn.net/qq_33942040/article/details/109131637)`

### Step 3: 江湖魔头

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat, radare2 with the extracted filter/query `enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);` and inspect the matching evidence.
- Tools: ida, netcat, radare2
- Filters or commands:
  - `enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);`
  - `enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat, radare2 with the extracted filter/query `enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3d805408431c41a93a02d218b1276148`

### Step 4: web进阶

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `120.24.86.145:8008`

### Step 5: bugku导航

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, netcat, radare2 with the extracted filter/query `思路①==` and inspect the matching evidence.
- Tools: ida, netcat, radare2
- Filters or commands:
  - `思路①==`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, netcat, radare2 with the extracted filter/query `思路①==` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7f1fdf3b0771f27ba154a7cb993692f8`

### Step 6: 实战2-注入

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3a579d78f94ee65d742053a4368b517a`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
