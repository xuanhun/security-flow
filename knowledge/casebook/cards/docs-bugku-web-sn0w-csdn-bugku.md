# Bugku—web题解_Sn0w/的博客-CSDN博客_bugku题解

## Case Metadata

- Category: `Web`
- Platform: `Bugku—web题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/Bugku—web题解_Sn0w／的博客-CSDN博客_bugku题解.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/Bugku%E2%80%94web%E9%A2%98%E8%A7%A3_Sn0w%EF%BC%8F%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_bugku%E9%A2%98%E8%A7%A3.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/Bugku—web题解_Sn0w／的博客-CSDN博客_bugku题解.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app, web-service challenges.

## Input Signals

- Artifacts: ciphertext, web-app, web-service
- Tools: burp, detect-it-easy, netcat, radare2
- Techniques: classical-crypto, command-injection, crypto-analysis, dns-analysis, encoding-analysis, file-inclusion, http-analysis, php-tricks, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `69`
- `docs/img/415954c5696d39dde78f25edede263c4.png`
- `docs/img/9e8566f111457273a4235afcd7bb19ce.png`
- `docs/img/55de137cafe8e207876960758614fbeb.png`
- `docs/img/4168dafba4f0a540d274a9b4309f87de.png`
- `docs/img/eb8dac3773a97e6971ca5496f65f1d26.png`
- `docs/img/6cab5c646cb3650e3f271390a4078661.png`
- `docs/img/700f37e3e4fb3a28a7a2adf7815690af.png`
- `docs/img/42141fe5db8f41145567ba9bdbc31db6.png`
- `docs/img/24fb47e61e185c91fa0da0deaf6628ba.png`
- `docs/img/d264bb310fdfa181a983238f804d9785.png`
- `docs/img/debf8f6db586ad82ff4890989b543033.png`
- `docs/img/0e84a421e2551d06f7d8443e2189d979.png`
- ... and `57` more

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: Bugku—web题解_Sn0w/的博客-CSDN博客_bugku题解

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `前言：最近做了一些Bugku入门的web题目，感觉web题挺有趣的，并非是得出flag，而是可以通过一个题目学习到很多知识。`

### Step 3: **域名解析**

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use burp, detect-it-easy, netcat, radare2 to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as dns pivot.
  - Use burp, detect-it-easy, netcat, radare2 to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `415954c5696d39dde78f25edede263c4`

### Step 4: **你必须让他停下**

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use burp to align timestamps and identify the event that satisfies the question.
- Tools: burp
- Reasoning chain:
  - Recognize the section as timeline reconstruction.
  - Use burp to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `55de137cafe8e207876960758614fbeb`

### Step 5: **变量1**

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use detect-it-easy, netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use detect-it-easy, netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:8004`

### Step 6: **头等舱**

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `这个没啥好做的，抓一下包就可得出flag`

### Step 7: **本地包含**

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `eb8dac3773a97e6971ca5496f65f1d26`

### Step 8: **web5**

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `debf8f6db586ad82ff4890989b543033`

### Step 9: **网站被黑**

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `93b7722925abca39f029de6e10ad5d2a`

### Step 10: **输入密码查看flag**

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp to collect the smallest evidence slice that answers the goal.
- Tools: burp
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8da33dc43511b75700a93107e83d17e0`

### Step 11: **点击一百万次**

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ec542e3a9c0c62693cf5fae293c470e6`

### Step 12: **备份是个好习惯**

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use burp, detect-it-easy, netcat, radare2 with the extracted filter/query `if(md5($key1) == md5($key2) && $key1 !== $key2){` and inspect the matching evidence.
- Tools: burp, detect-it-easy, netcat, radare2
- Filters or commands:
  - `if(md5($key1) == md5($key2) && $key1 !== $key2){`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use burp, detect-it-easy, netcat, radare2 with the extracted filter/query `if(md5($key1) == md5($key2) && $key1 !== $key2){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:8002`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
