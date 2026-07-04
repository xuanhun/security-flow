# SWPUCTF web 部分题解_HyyMbb的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `SWPUCTF web 部分题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/SWPUCTF-web-部分题解_HyyMbb的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/SWPUCTF-web-%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3_HyyMbb%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/SWPUCTF-web-部分题解_HyyMbb的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app, web-service
- Tools: burp, netcat, radare2
- Techniques: classical-crypto, command-injection, crypto-analysis, deserialization, encoding-analysis, file-inclusion, file-upload, http-analysis, misc-analysis, php-tricks, ret2libc, sql-injection, ssti, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `26`
- `docs/img/915f1295e422b827845479bc73aeb107.png`
- `docs/img/882898bb8d3ba8b7c314fe26200451a0.png`
- `docs/img/a2fd5c07039ca827dce02b21670b582a.png`
- `docs/img/457dc3b514e70bd84f2c706165777344.png`
- `docs/img/c91670415f2cc4c1569b86694964a04d.png`
- `docs/img/e3779a75d98cb8cae6508af2fcdd7574.png`
- `docs/img/7875afb85442c668917c9bddd4fd141b.png`
- `docs/img/2f28d9ea55ae13c1f490c5824144bee7.png`
- `docs/img/d3f594977a69e52d1288d2caef79fdcf.png`
- `docs/img/ee976cfb3334527a5d2a47fdfe37036b.png`
- `docs/img/335649c97f03fe0da714376750037967.png`
- `docs/img/f26a598fc617623ac8b17d8edaf85209.png`
- ... and `14` more

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat, radare2
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: SWPUCTF web 部分题解_HyyMbb的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/a3320315/article/details/103760266](https://blog.csdn.net/a3320315/article/details/103760266)`

### Step 3: 0x01 web1 easyweb

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use netcat to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as conversation statistics.
  - Use netcat to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `915f1295e422b827845479bc73aeb107`

### Step 4: 由于这儿我们最多只能知道表名，无法知道列名，可以使用无列名注入，我已知的有两种方法

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `882898bb8d3ba8b7c314fe26200451a0`

### Step 5: 0x02 web3 easy_python

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use netcat with the extracted filter/query `ip = ip.encode(encoding='utf-8')` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `ip = ip.encode(encoding='utf-8')`
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use netcat with the extracted filter/query `ip = ip.encode(encoding='utf-8')` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c91670415f2cc4c1569b86694964a04d`

### Step 6: 解法一

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `$()里面的命令都会执行，不管是否赋值成功~`

### Step 7: 解法二

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use burp, netcat, radare2 with the extracted filter/query `只是过滤了|和;，但是&和#都没有过滤掉，所以可以构造任意命令执行` and inspect the matching evidence.
- Tools: burp, netcat, radare2
- Filters or commands:
  - `只是过滤了|和;，但是&和#都没有过滤掉，所以可以构造任意命令执行`
  - `3、$ cat 1.txt | base64 -d > flag.jpg`
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use burp, netcat, radare2 with the extracted filter/query `只是过滤了|和;，但是&和#都没有过滤掉，所以可以构造任意命令执行` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `然后将文本带出保存在本地，在直接base64 -d转换为图片`

### Step 8: 0x03 web4 demo_mvc

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat with the extracted filter/query ``select updatexml extractvalue or and if ascii sleep substr , || &&`` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - ``select updatexml extractvalue or and if ascii sleep substr , || &&``
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat with the extracted filter/query ``select updatexml extractvalue or and if ascii sleep substr , || &&`` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7875afb85442c668917c9bddd4fd141b`

### Step 9: 0x04 web6 出题人不知道

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use burp, netcat, radare2 with the extracted filter/query `if ($h == $swpuctf)` and inspect the matching evidence.
- Tools: burp, netcat, radare2
- Filters or commands:
  - `if ($h == $swpuctf)`
  - `echo de_crypt("3J6Roahxaw==",$key)`
  - `$headers = array('X-Forwarded-For:127.0.0.1', 'Cookie:user=xZmdm9NxaQ==; PHPSESSID=fuck3' );`
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use burp, netcat, radare2 with the extracted filter/query `if ($h == $swpuctf)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1:8080`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
