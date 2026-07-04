# 2020易博霖CTFWeb2--SSRF题解_flying_bird2019的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `2020易博霖CTFWeb2`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/2020易博霖CTFWeb2--SSRF题解_flying_bird2019的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/2020%E6%98%93%E5%8D%9A%E9%9C%96CTFWeb2--SSRF%E9%A2%98%E8%A7%A3_flying_bird2019%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/2020易博霖CTFWeb2--SSRF题解_flying_bird2019的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: ida, radare2, z3
- Techniques: classical-crypto, crypto-analysis, dns-analysis, encoding-analysis, http-analysis, reverse-engineering, symbolic-execution, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `3`
- `docs/img/21088892bf876da578f11102acd206e9.png`
- `docs/img/7042abaabc0c07a0e4606cb251e2d86d.png`
- `docs/img/652c7aa9e7341a53b16daa28a7613775.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, radare2, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, radare2, z3
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, radare2, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 2020易博霖CTFWeb2--SSRF题解_flying_bird2019的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, radare2, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, radare2, z3
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, radare2, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/flying_bird2019/article/details/105249075](https://blog.csdn.net/flying_bird2019/article/details/105249075)`

### Step 3: SSRF

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use ida, radare2, z3 with the extracted filter/query `index.php?file=WTNSbWFXMWhaMlV1YW5Cbg==**` and inspect the matching evidence.
- Tools: ida, radare2, z3
- Filters or commands:
  - `index.php?file=WTNSbWFXMWhaMlV1YW5Cbg==**`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use ida, radare2, z3 with the extracted filter/query `index.php?file=WTNSbWFXMWhaMlV1YW5Cbg==**` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `21088892bf876da578f11102acd206e9`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
