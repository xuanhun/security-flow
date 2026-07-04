# Bugku CTF Web 解题报告（一）_Vayn3的博客-CSDN博客_bugku 金币

## Case Metadata

- Category: `Web`
- Platform: `Bugku CTF Web 解题报告（一）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/Bugku-CTF-Web-解题报告（一）_Vayn3的博客-CSDN博客_bugku-金币.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/Bugku-CTF-Web-%E8%A7%A3%E9%A2%98%E6%8A%A5%E5%91%8A%EF%BC%88%E4%B8%80%EF%BC%89_Vayn3%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_bugku-%E9%87%91%E5%B8%81.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/Bugku-CTF-Web-解题报告（一）_Vayn3的博客-CSDN博客_bugku-金币.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, encoding-analysis, file-inclusion, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `19`
- `docs/img/e0c6a2b794505e2df2fe7f78438c7bdc.png`
- `docs/img/e1ae3479a6e30a9ed948d1a79f18a47a.png`
- `docs/img/ac1fdeb9f3e32657a44511d98fa8adf2.png`
- `docs/img/c4affd0071198053fbee8fd035c76efb.png`
- `docs/img/cf829a3d9cb2e0223bb8a6cb379798b9.png`
- `docs/img/69f623532ec9794f0ac2faad643834dd.png`
- `docs/img/d5a0d353de379291490713309af44c24.png`
- `docs/img/cd61eed3bb06ccfeebb34be79c7ce18f.png`
- `docs/img/ebdf1ea0fa06ffb134a1bbce6727bae3.png`
- `docs/img/aafdbe942fd443e0a56c29d2bf8d9619.png`
- `docs/img/61db2747e2982d7cd8a0e993f453292f.png`
- `docs/img/188d0ff77d58af4bed65ba1cef043a3c.png`
- ... and `7` more

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: Bugku CTF Web 解题报告（一）_Vayn3的博客-CSDN博客_bugku 金币

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_51090016/article/details/112976196](https://blog.csdn.net/qq_51090016/article/details/112976196)`

### Step 3: Bugku Web 一 （11-15）

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `e0c6a2b794505e2df2fe7f78438c7bdc`

### Step 4: Web 12 本地管理员

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `cd61eed3bb06ccfeebb34be79c7ce18f`

### Step 5: Web 13 看看源代码？

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use netcat with the extracted filter/query `var p1 = ‘function checkSubmit(){var a=document.getElementById(“password”);if(“undefined”!=typeof a){if("**67d709b2b**’;` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `var p1 = ‘function checkSubmit(){var a=document.getElementById(“password”);if(“undefined”!=typeof a){if("**67d709b2b**’;`
  - `var p2 = ‘**aa648cf6e87a7114f1**"==a.value)return!0;alert(“Error”);a.focus();return!1}}document.getElementById(“levelQuest”).οnsubmit=checkSubmit;’;`
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use netcat with the extracted filter/query `var p1 = ‘function checkSubmit(){var a=document.getElementById(“password”);if(“undefined”!=typeof a){if("**67d709b2b**’;` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `b769713fed375b01904a365381c58244`

### Step 6: Web 14

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `d9085aa73cd93f1f972af1b0cacb5e52`

### Step 7: Web 15 这好像需要密码

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1e855367fb65727a64284054bef3814b`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
