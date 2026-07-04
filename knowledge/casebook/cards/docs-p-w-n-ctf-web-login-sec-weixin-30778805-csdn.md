# P.W.N. CTF - Web - Login Sec_weixin_30778805的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `P.W.N. CTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/P.W.N.-CTF---Web---Login-Sec_weixin_30778805的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/P.W.N.-CTF---Web---Login-Sec_weixin_30778805%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/P.W.N.-CTF---Web---Login-Sec_weixin_30778805的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: netcat
- Techniques: crypto-analysis, dns-analysis, file-inclusion, http-analysis, php-tricks, ssti, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `5`
- `docs/img/28a2b7d6b4ddc372ea17884e481fd590.png`
- `docs/img/026a6b6ca4493d8f96502d03f9f7503d.png`
- `docs/img/71105a82752f488f12d68c0695c380e5.png`
- `docs/img/74ac4ab741a86d7116a009e86c203c47.png`
- `docs/img/128ad56e01a7b59b3c654903b2c31b64.png`

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

### Step 2: P.W.N. CTF - Web - Login Sec_weixin_30778805的博客-CSDN博客

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_30778805/article/details/95144764](https://blog.csdn.net/weixin_30778805/article/details/95144764)`

### Step 3: 题目

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `28a2b7d6b4ddc372ea17884e481fd590`

### Step 4: Login 1

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use netcat with the extracted filter/query `http.createServer(function (req, res) {` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `http.createServer(function (req, res) {`
  - `if (passwd == url_content.query.passwd) {`
- Reasoning chain:
  - Recognize the section as dns pivot.
  - Use netcat with the extracted filter/query `http.createServer(function (req, res) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `026a6b6ca4493d8f96502d03f9f7503d`

### Step 5: Login 2

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `if (hash("md5", $_GET['passwd']) == '0e514198428367523082236389979035') {` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if (hash("md5", $_GET['passwd']) == '0e514198428367523082236389979035') {`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `if (hash("md5", $_GET['passwd']) == '0e514198428367523082236389979035') {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0e514198428367523082236389979035`

### Step 6: Login 3

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use netcat with the extracted filter/query `assert(len(passwd) == 3)` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `assert(len(passwd) == 3)`
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use netcat with the extracted filter/query `assert(len(passwd) == 3)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `128ad56e01a7b59b3c654903b2c31b64`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
