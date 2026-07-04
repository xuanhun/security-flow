# 〖教程〗K8飞刀-网络安全CTF解题Web篇10例_k8gege的博客-CSDN博客_k8飞刀

## Case Metadata

- Category: `Web`
- Platform: `〖教程〗K8飞刀`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/〖教程〗K8飞刀-网络安全CTF解题Web篇10例_k8gege的博客-CSDN博客_k8飞刀.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%96%E6%95%99%E7%A8%8B%E3%80%97K8%E9%A3%9E%E5%88%80-%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8CTF%E8%A7%A3%E9%A2%98Web%E7%AF%8710%E4%BE%8B_k8gege%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_k8%E9%A3%9E%E5%88%80.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/〖教程〗K8飞刀-网络安全CTF解题Web篇10例_k8gege的博客-CSDN博客_k8飞刀.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app, web-service challenges.

## Input Signals

- Artifacts: ciphertext, web-app, web-service
- Tools: burp
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, http-analysis, php-tricks, sql-injection, web-exploitation, xss

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `10`
- `docs/img/e826325abf6e3bde01a475af2da2be05.png`
- `docs/img/105a2a1c03b22ab75ab6bc88af8a5cfc.png`
- `docs/img/5899e019fa8b4248cf7e073571ee1b70.png`
- `docs/img/6b9423dbfc48e6a43be8378d7a28166e.png`
- `docs/img/0f36340fc1ab5b3b998b3faf6f3e9d6e.png`
- `docs/img/63632258b0654032a63f3e75f0fb3f47.png`
- `docs/img/d62e354b77b92db47b707686c1edf8da.png`
- `docs/img/ebfe7628176eb73e85b0731062ba2660.png`
- `docs/img/e4bef13971df6a427b3f28d375198050.png`
- `docs/img/177ed0a27acc6ffe4b42cd2d0416b92b.png`

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp to collect the smallest evidence slice that answers the goal.
- Tools: burp
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 〖教程〗K8飞刀-网络安全CTF解题Web篇10例_k8gege的博客-CSDN博客_k8飞刀

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use burp to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: burp
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use burp to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `前段时间有人和我说什么时候有空出些CTF用的工具，实际上CTF考查的内容，实战中用到的很多工具都可以使用，关键在于你懂不懂用。也看到有人搜索如何使用K8飞刀，在此以CTF题为例，教大家使用K8飞刀…`

### Step 3: 考查知识点

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: burp
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `10.Cookie欺骗`

### Step 4: 题目1 HTML查看

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:8002`

### Step 5: 题目2 HTML实体

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use burp to verify the sink, context, and trigger condition before choosing the smallest executable payload.
- Tools: burp
- Reasoning chain:
  - Recognize the section as xss route.
  - Use burp to verify the sink, context, and trigger condition before choosing the smallest executable payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:8002`

### Step 6: 题目3 GET提交

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp with the extracted filter/query `echo w h a t ; < b r > i f ( what;<br> if( what;<br>if(what==‘flag’)` and inspect the matching evidence.
- Tools: burp
- Filters or commands:
  - `echo w h a t ; < b r > i f ( what;<br> if( what;<br>if(what==‘flag’)`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp with the extracted filter/query `echo w h a t ; < b r > i f ( what;<br> if( what;<br>if(what==‘flag’)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:8002`

### Step 7: 题目4 POST提交

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp with the extracted filter/query `echo w h a t ; < b r > i f ( what;<br> if( what;<br>if(what==‘flag’)` and inspect the matching evidence.
- Tools: burp
- Filters or commands:
  - `echo w h a t ; < b r > i f ( what;<br> if( what;<br>if(what==‘flag’)`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp with the extracted filter/query `echo w h a t ; < b r > i f ( what;<br> if( what;<br>if(what==‘flag’)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:8002`

### Step 8: 题目5 伪造IP

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: burp
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.31.85:1003`

### Step 9: 题目6 PUT漏洞

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `CVE-2017-12615`

### Step 10: 题目7 URL编码

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: burp
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:8002`

### Step 11: 题目8 cookie欺骗

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `123.206.87.240:8002`

### Step 12: 题目9 Referer来源

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `123.206.87.240:9009`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
