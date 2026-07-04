# CTF刷题02_Atkxor的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `CTF刷题02`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF刷题02_Atkxor的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%E5%88%B7%E9%A2%9802_Atkxor%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF刷题02_Atkxor的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, encoding-analysis, misc-analysis, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `20`
- `docs/img/8a5ed6eea70badf9002479d18f3e9f22.png`
- `docs/img/2757ee11135303253178df37912399d5.png`
- `docs/img/74855279dcb975c374ba11aec268be0a.png`
- `docs/img/8a1d274d18e2eefff26f59564da8aad6.png`
- `docs/img/6be73292b2f090eb3fa2dba5099e7874.png`
- `docs/img/fb2a47d7bd0285e19e05cc41ec696233.png`
- `docs/img/231bfbd98816aec73280573c85728746.png`
- `docs/img/2692e349b62d19cc7ca5e2b73f24d3de.png`
- `docs/img/7192dee18c286ed12f95a815bbdc7708.png`
- `docs/img/5f24c91c09eea07c3bb9683d43f3d9a8.png`
- `docs/img/b0aec3c10dd8099638a64db4de318440.png`
- `docs/img/5d0fe3b30266003d9178f6b0913719a8.png`
- ... and `8` more

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

### Step 2: CTF刷题02_Atkxor的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_46150940/article/details/108717330](https://blog.csdn.net/qq_46150940/article/details/108717330)`

### Step 3: [极客大挑战 2019]EasySQL

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8a5ed6eea70badf9002479d18f3e9f22`

### Step 4: [BugKu]Web4

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `var p1 = 'function checkSubmit(){var a=document.getElementById("password");if("undefined"!=typeof a){if("67d709b2b';` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `var p1 = 'function checkSubmit(){var a=document.getElementById("password");if("undefined"!=typeof a){if("67d709b2b';`
  - `var p2 = 'aa648cf6e87a7114f1"==a.value)return!0;alert("Error");a.focus();return!1}}document.getElementById("levelQuest").οnsubmit=checkSubmit;';`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `var p1 = 'function checkSubmit(){var a=document.getElementById("password");if("undefined"!=typeof a){if("67d709b2b';` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `fb2a47d7bd0285e19e05cc41ec696233`

### Step 5: [HCTF 2018]WarmUp

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat with the extracted filter/query `if (! isset($page) || !is_string($page)) {` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if (! isset($page) || !is_string($page)) {`
  - `| 函数 | 描述 |`
  - `| --- | --- |`
  - `| isset | 用于检测变量是否已设置并且非 NULL，若是返回false。 |`
  - `| is_string | 检测变量是否是字符串，若存在返回true。 |`
  - `| in_array() | 函数搜索数组中是否存在指定的值，若存在返回true |`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat with the extracted filter/query `if (! isset($page) || !is_string($page)) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7192dee18c286ed12f95a815bbdc7708`

### Step 6: 掀桌子

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `d908eaf65ff1c57a8875fa16a1302af7`

### Step 7: 基础破解

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `be0f585b7b71a4f559807c84cbd62b89`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
