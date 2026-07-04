# hxp 36C3 CTF Web题 WriteupBin Writeup (Selenium模拟点击+Content Security Policy+Nonce+Parsley.js触发错误提示)_KevinLuo2000的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `hxp 36C3 CTF Web`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/hxp-36C3-CTF-Web题-WriteupBin-Writeup-(Selenium模拟点击+Content-Security-Policy+Nonce+Parsley.js触发错误提示)_KevinLuo2000的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/hxp-36C3-CTF-Web%E9%A2%98-WriteupBin-Writeup-%28Selenium%E6%A8%A1%E6%8B%9F%E7%82%B9%E5%87%BB%2BContent-Security-Policy%2BNonce%2BParsley.js%E8%A7%A6%E5%8F%91%E9%94%99%E8%AF%AF%E6%8F%90%E7%A4%BA%29_KevinLuo2000%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/hxp-36C3-CTF-Web题-WriteupBin-Writeup-(Selenium模拟点击+Content-Security-Policy+Nonce+Parsley.js触发错误提示)_KevinLuo2000的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app, web-service
- Tools: burp, detect-it-easy, ida, netcat
- Techniques: binary-exploitation, browser-forensics, classical-crypto, command-injection, dns-analysis, encoding-analysis, file-inclusion, http-analysis, misc-analysis, reverse-engineering, sql-injection, waf-bypass, web-exploitation, xss

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `5`
- `docs/img/3797e4f5f7c1099378a2734aa263e819.png`
- `docs/img/d7aaa6949ae81b6a1480dc4ac141d0f9.png`
- `docs/img/6cc976d9a765b2c02751249bb1deb424.png`
- `docs/img/f95590824ad017404221cee34b9dc25a.png`
- `docs/img/a3c923f7598bfe1b89bd791a38bb7bc4.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use burp, detect-it-easy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: burp, detect-it-easy, ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use burp, detect-it-easy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: hxp 36C3 CTF Web题 WriteupBin Writeup (Selenium模拟点击+Content Security Policy+Nonce+Parsley.js触发错误提示)_KevinLuo2000的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, ida, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/keyball123/article/details/104508815/](https://blog.csdn.net/keyball123/article/details/104508815/)`

### Step 3: WriteupBin

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, ida, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://ctftime.org/event/825`

### Step 4: 本地搭建：

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `echo 'hxp{FLAG}' > flag.txt && < /dev/urandom tr -dc a-f0-9 | head -c 16 > writeup-id.txt && docker build -t writeupbin . && docker run --cap-add=SYS_ADMIN --security-opt apparmor=unconfined -ti -p 8001:80 writeupbin` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `echo 'hxp{FLAG}' > flag.txt && < /dev/urandom tr -dc a-f0-9 | head -c 16 > writeup-id.txt && docker build -t writeupbin . && docker run --cap-add=SYS_ADMIN --security-opt apparmor=unconfined -ti -p 8001:80 writeupbin`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `echo 'hxp{FLAG}' > flag.txt && < /dev/urandom tr -dc a-f0-9 | head -c 16 > writeup-id.txt && docker build -t writeupbin . && docker run --cap-add=SYS_ADMIN --security-opt apparmor=unconfined -ti -p 8001:80 writeupbin` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1:8001`

### Step 5: 题目分析

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use burp, detect-it-easy, ida, netcat with the extracted filter/query `replace '__DB_PASSWORD__' "$(< /dev/urandom tr -dc A-Za-z0-9 | head -c32)" -- /root/db.sql /var/www/general.php && \` and inspect the matching evidence.
- Tools: burp, detect-it-easy, ida, netcat
- Filters or commands:
  - `replace '__DB_PASSWORD__' "$(< /dev/urandom tr -dc A-Za-z0-9 | head -c32)" -- /root/db.sql /var/www/general.php && \`
  - `< /dev/urandom tr -dc A-Za-z0-9 | head -c32 > /root/admin-token.txt && \`
  - `| id | user_id | content |`
  - `| :-: | :-: | :-: |`
  - `| __WRITEUP_ID__的值 | admin | __FLAG__的值 |`
  - `| writeup的id | $_SESSION[‘id’] | writeup的内容 |`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use burp, detect-it-easy, ida, netcat with the extracted filter/query `replace '__DB_PASSWORD__' "$(< /dev/urandom tr -dc A-Za-z0-9 | head -c32)" -- /root/db.sql /var/www/general.php && \` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1:1024`

### Step 6: 参考文献

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, ida, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://ctftime.org/writeup/17891`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
