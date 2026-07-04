# 南京邮电大学CG-CTF平台Writeup_Gard3nia的博客-CSDN博客_cgctf平台

## Case Metadata

- Category: `Web`
- Platform: `南京邮电大学CG`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/南京邮电大学CG-CTF平台Writeup_Gard3nia的博客-CSDN博客_cgctf平台.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E5%8D%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6CG-CTF%E5%B9%B3%E5%8F%B0Writeup_Gard3nia%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_cgctf%E5%B9%B3%E5%8F%B0.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/南京邮电大学CG-CTF平台Writeup_Gard3nia的博客-CSDN博客_cgctf平台.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, pcap, stego-media challenges.

## Input Signals

- Artifacts: ciphertext, pcap, stego-media, web-app
- Tools: detect-it-easy, netcat, radare2, wireshark
- Techniques: classical-crypto, command-injection, crypto-analysis, dns-analysis, encoding-analysis, file-inclusion, http-analysis, image-analysis, misc-analysis, network-forensics, php-tricks, sql-injection, traffic-analysis, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `40`
- `docs/img/28fba2b3c7a013143c9b1cdaec26a883.png`
- `docs/img/230222c8b7ce02051cd0ad1ee8f108bd.png`
- `docs/img/1b3e50b954cd7d0ecda7624578224d87.png`
- `docs/img/33b4903251b3f67a31c3169559d403bc.png`
- `docs/img/5d1cbaca19ae5052f5f0f51ae39895a7.png`
- `docs/img/57837c76e6aa92b03b2994397fe99c54.png`
- `docs/img/4f8ab83e458ca6a8c2c27a7e76c70685.png`
- `docs/img/28743b130702b5c8e70900dc6c6eeb4e.png`
- `docs/img/7407df5c2cb1c0cf20a1fab1b272de7a.png`
- `docs/img/73294e080a7b6fb64d4be433b8810848.png`
- `docs/img/be8920ba38a9f9d8dd7c505e5e57b3bc.png`
- `docs/img/c89ae29eb393b17a0783056df0dca861.png`
- ... and `28` more

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat, radare2, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat, radare2, wireshark
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat, radare2, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 南京邮电大学CG-CTF平台Writeup_Gard3nia的博客-CSDN博客_cgctf平台

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat, radare2, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat, radare2, wireshark
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat, radare2, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/Gar_denia/article/details/86760587](https://blog.csdn.net/Gar_denia/article/details/86760587)`

### Step 3: 前言

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat, radare2, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat, radare2, wireshark
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat, radare2, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `萌新刷题，寒假又补充更新了Crypto部分；`

### Step 4: 文件包含

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `if(strstr($file,"../")||stristr($file, "tp")||stristr($file,"input")||stristr($file,"data")){` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if(strstr($file,"../")||stristr($file, "tp")||stristr($file,"input")||stristr($file,"data")){`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `if(strstr($file,"../")||stristr($file, "tp")||stristr($file,"input")||stristr($file,"data")){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `28fba2b3c7a013143c9b1cdaec26a883`

### Step 5: bypass again

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use detect-it-easy with the extracted filter/query `php中有两种比较的符号 == 与 ===` and inspect the matching evidence.
- Tools: detect-it-easy
- Filters or commands:
  - `php中有两种比较的符号 == 与 ===`
  - `=== 在进行比较的时候，会先判断两种字符串的类型是否相等，再比较`
  - `== 在进行比较的时候，会先将字符串类型转化成相同，再比较`
  - `if ($_GET['a'] != $_GET['b'])`
  - `if (md5($_GET['a']) == md5($_GET['b']))`
  - `所以当判断中为"=="的时候会将两边先转换为一样的数据类型;0e在比较的时候会将其视作为科学计数法，所以无论0e后面是什么，0的多少次方还是0，md5(‘240610708’) == md5(‘QNKCDZO’)成功绕过!`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use detect-it-easy with the extracted filter/query `php中有两种比较的符号 == 与 ===` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `33b4903251b3f67a31c3169559d403bc`

### Step 6: /x00

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `if (@ereg ("^[1-9]+$", $_GET['nctf']) === FALSE)` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `if (@ereg ("^[1-9]+$", $_GET['nctf']) === FALSE)`
  - `else if (strpos ($_GET['nctf'], '#biubiubiu') !== FALSE)`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use detect-it-easy, netcat with the extracted filter/query `if (@ereg ("^[1-9]+$", $_GET['nctf']) === FALSE)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `f5a14f5e6e3453b78cd73899bad98d53`

### Step 7: SQL1

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use detect-it-easy, netcat, radare2, wireshark with the extracted filter/query `if($query[user]=="admin") {` and inspect the matching evidence.
- Tools: detect-it-easy, netcat, radare2, wireshark
- Filters or commands:
  - `if($query[user]=="admin") {`
  - `if($query[user] != "admin") {`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use detect-it-easy, netcat, radare2, wireshark with the extracted filter/query `if($query[user]=="admin") {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4f8ab83e458ca6a8c2c27a7e76c70685`

### Step 8: MYSQL

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use detect-it-easy, netcat, radare2, wireshark with the extracted filter/query `if ($_GET[id]==1024) {` and inspect the matching evidence.
- Tools: detect-it-easy, netcat, radare2, wireshark
- Filters or commands:
  - `if ($_GET[id]==1024) {`
- Reasoning chain:
  - Recognize the section as dns pivot.
  - Use detect-it-easy, netcat, radare2, wireshark with the extracted filter/query `if ($_GET[id]==1024) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `28743b130702b5c8e70900dc6c6eeb4e`

### Step 9: passcheck

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat with the extracted filter/query `以上代码用于测试此函数的作用结果显而易见，len(string1)==len(string2)返回0，否则返回string1比string2长多少或者短多少。` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `以上代码用于测试此函数的作用结果显而易见，len(string1)==len(string2)返回0，否则返回string1比string2长多少或者短多少。`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat with the extracted filter/query `以上代码用于测试此函数的作用结果显而易见，len(string1)==len(string2)返回0，否则返回string1比string2长多少或者短多少。` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `be8920ba38a9f9d8dd7c505e5e57b3bc`

### Step 10: 变量覆盖

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use detect-it-easy, netcat, radare2, wireshark with the extracted filter/query `$pass==$thepassword_123` and inspect the matching evidence.
- Tools: detect-it-easy, netcat, radare2, wireshark
- Filters or commands:
  - `$pass==$thepassword_123`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use detect-it-easy, netcat, radare2, wireshark with the extracted filter/query `$pass==$thepassword_123` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c89ae29eb393b17a0783056df0dca861`

### Step 11: 起名字真难

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat with the extracted filter/query `return $number == '54975581388';` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `return $number == '54975581388';`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat with the extracted filter/query `return $number == '54975581388';` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `884fed0d3a423f04fc238ea718206450`

### Step 12: 密码重置

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use detect-it-easy, netcat, radare2, wireshark to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: detect-it-easy, netcat, radare2, wireshark
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use detect-it-easy, netcat, radare2, wireshark to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ea767c6ae8720c27d37d32821d0ea4a9`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
