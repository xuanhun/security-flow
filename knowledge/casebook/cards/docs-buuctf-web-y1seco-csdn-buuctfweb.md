# 【BUUCTF刷题】Web解题方法总结（一)_Y1seco的博客-CSDN博客_buuctfweb

## Case Metadata

- Category: `Web`
- Platform: `【BUUCTF刷题】Web解题方法总结（一)`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【BUUCTF刷题】Web解题方法总结（一)_Y1seco的博客-CSDN博客_buuctfweb.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90BUUCTF%E5%88%B7%E9%A2%98%E3%80%91Web%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%E6%80%BB%E7%BB%93%EF%BC%88%E4%B8%80%29_Y1seco%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_buuctfweb.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【BUUCTF刷题】Web解题方法总结（一)_Y1seco的博客-CSDN博客_buuctfweb.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app, web-service
- Tools: burp, detect-it-easy, netcat, radare2
- Techniques: binary-exploitation, classical-crypto, command-injection, crypto-analysis, deserialization, encoding-analysis, file-inclusion, file-upload, http-analysis, php-tricks, service-enumeration, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `20`
- `docs/img/c2232b493c7a5e02cd1bbef37c9ac09b.png`
- `docs/img/9d4e1d80198b080da2d531b502d33e62.png`
- `docs/img/3d80818c674c31609708fe147331d505.png`
- `docs/img/d379405d024b34e7cbef9945284562eb.png`
- `docs/img/2af33795ed4cfedaf9198b10cc9ae26a.png`
- `docs/img/810199eb769d484a81b5d988d65295ba.png`
- `docs/img/c56e659405097efffd55e93b6f47c623.png`
- `docs/img/799e0b0ba589ade80f9cf9cdd10ca6d3.png`
- `docs/img/76eeec49f3096a11ff452befd9121546.png`
- `docs/img/97a1b4163614c40631ae0dd6c5d79a48.png`
- `docs/img/5bda924b5188393224b1204fb0ba1124.png`
- `docs/img/16a7b734ef4935b2171dd5830af9a6fb.png`
- ... and `8` more

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

### Step 2: 前言

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `边刷题边总结些知识点，还在更新，冲！`

### Step 3: 信息搜集

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-e 指定网站语言`

### Step 4: SQL缺省

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat with the extracted filter/query `查询语句：select *,1||flag from Flag` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `查询语句：select *,1||flag from Flag`
  - `在oracle 缺省支持 通过 ‘ || ’ 来实现字符串拼接。`
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat with the extracted filter/query `查询语句：select *,1||flag from Flag` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `模式：pipes_as_concat 来实现oracle 的一些功能。`

### Step 5: 代码审计

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `if (! isset($page) || !is_string($page)) {` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if (! isset($page) || !is_string($page)) {`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `if (! isset($page) || !is_string($page)) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c2232b493c7a5e02cd1bbef37c9ac09b`

### Step 6: 常规流程

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat, radare2 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat, radare2 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `即按需求打印内容`

### Step 7: BUUCTF HardSQL

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat, z3 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat, z3 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `9d4e1d80198b080da2d531b502d33e62`

### Step 8: 堆叠注入

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat with the extracted filter/query `(DEALLOCATE || DROP) PREPARE sqla; 删除预定义SQL语句` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `(DEALLOCATE || DROP) PREPARE sqla; 删除预定义SQL语句`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat with the extracted filter/query `(DEALLOCATE || DROP) PREPARE sqla; 删除预定义SQL语句` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `准备好的SQL语句通过EXECUTE命令执行，通过DEALLOCATE PREPARE命令释放掉。`

### Step 9: 使用MD5函数实现sql注入

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use burp, detect-it-easy, netcat, radare2 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use burp, detect-it-easy, netcat, radare2 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c56e659405097efffd55e93b6f47c623`

### Step 10: BUUCTF WEB [CISCN2019 华北赛区 Day2 Web1]Hack World(SQL盲注，PHP）

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use burp, netcat with the extracted filter/query `|` and inspect the matching evidence.
- Tools: burp, netcat
- Filters or commands:
  - `|`
  - `||`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use burp, netcat with the extracted filter/query `|` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5bda924b5188393224b1204fb0ba1124`

### Step 11: [GYCTF2020]Blacklist [堆叠注入]

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use burp, detect-it-easy, netcat, radare2 to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use burp, detect-it-easy, netcat, radare2 to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `16a7b734ef4935b2171dd5830af9a6fb`

### Step 12: Ping命令

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use burp, detect-it-easy, netcat, radare2 with the extracted filter/query `| （按位或）表示管道，上一条命令的输出，作为下一条命令参数，直接执行|后面的语句，如 echo ‘yes’ | wc -l` and inspect the matching evidence.
- Tools: burp, detect-it-easy, netcat, radare2
- Filters or commands:
  - `| （按位或）表示管道，上一条命令的输出，作为下一条命令参数，直接执行|后面的语句，如 echo ‘yes’ | wc -l`
  - `|| （逻辑或）表示上一条命令执行失败后，才执行下一条命令，否则只执行前面的语句，如 cat nofile || echo “fail”`
  - `echo “cat flag.php” | base64`
  - `echo Y2F0IGZsYWcucGhwCg== | base64 -d | sh`
  - `?ip=127.0.0.1;echo$IFS$9Y2F0IGZsYWcucGhwCg==$IFS$9|$IFS$9base64$IFS$9-d$IFS$9|$IFS$9sh`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use burp, detect-it-easy, netcat, radare2 with the extracted filter/query `| （按位或）表示管道，上一条命令的输出，作为下一条命令参数，直接执行|后面的语句，如 echo ‘yes’ | wc -l` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
