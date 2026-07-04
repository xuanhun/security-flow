# BugkuCTF-WEB部分题解（一）_flying_bird2019的博客-CSDN博客_bugkuctfweb题解

## Case Metadata

- Category: `Web`
- Platform: `BugkuCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BugkuCTF-WEB部分题解（一）_flying_bird2019的博客-CSDN博客_bugkuctfweb题解.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BugkuCTF-WEB%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3%EF%BC%88%E4%B8%80%EF%BC%89_flying_bird2019%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_bugkuctfweb%E9%A2%98%E8%A7%A3.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BugkuCTF-WEB部分题解（一）_flying_bird2019的博客-CSDN博客_bugkuctfweb题解.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app, web-service challenges.

## Input Signals

- Artifacts: ciphertext, web-app, web-service
- Tools: burp, netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, dns-analysis, encoding-analysis, file-inclusion, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `3`
- `docs/img/c413b908a8e7070f05d37746261516c8.png`
- `docs/img/8074646a2bb7630202ce0699c15049cd.png`
- `docs/img/8fbd5a4be0ebd43e032d9e4db7242efd.png`

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BugkuCTF-WEB部分题解（一）_flying_bird2019的博客-CSDN博客_bugkuctfweb题解

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/flying_bird2019/article/details/104595139](https://blog.csdn.net/flying_bird2019/article/details/104595139)`

### Step 3: 域名解析

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use burp, netcat to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as dns pivot.
  - Use burp, netcat to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240`

### Step 4: 修改hosts文件：

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `120.24.86.145`

### Step 5: 修改头信息：

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `**得到flag**`

### Step 6: 变量1

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c413b908a8e7070f05d37746261516c8`

### Step 7: Web5

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `将一长串代码复制到浏览器控制台运行，得到Flag后字母转化为大写`

### Step 8: 网站被黑

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp to collect the smallest evidence slice that answers the goal.
- Tools: burp
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `shell.php`

### Step 9: 管理员系统

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1`

### Step 10: web4

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8fbd5a4be0ebd43e032d9e4db7242efd`

### Step 11: flag在index里

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `index.php`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
