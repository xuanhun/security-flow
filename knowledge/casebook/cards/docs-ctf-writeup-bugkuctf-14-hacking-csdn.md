# CTF平台题库writeup（四）--BugKuCTF-代码审计（14题详解）_Hacking黑白红的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `CTF平台题库writeup（四）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF平台题库writeup（四）--BugKuCTF-代码审计（14题详解）_Hacking黑白红的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%E5%B9%B3%E5%8F%B0%E9%A2%98%E5%BA%93writeup%EF%BC%88%E5%9B%9B%EF%BC%89--BugKuCTF-%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1%EF%BC%8814%E9%A2%98%E8%AF%A6%E8%A7%A3%EF%BC%89_Hacking%E9%BB%91%E7%99%BD%E7%BA%A2%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF平台题库writeup（四）--BugKuCTF-代码审计（14题详解）_Hacking黑白红的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: detect-it-easy, netcat, radare2
- Techniques: classical-crypto, encoding-analysis, file-inclusion, http-analysis, php-tricks, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `2`
- `docs/img/5d7535a1168b5ba0d76c67437d5a68b6.png`
- `docs/img/c454d25fe7dea45f85be51bd4a5901f0.png`

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF平台题库writeup（四）--BugKuCTF-代码审计（14题详解）_Hacking黑白红的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/zsw15841822890/article/details/107121670/](https://blog.csdn.net/zsw15841822890/article/details/107121670/)`

### Step 3: extract变量覆盖

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat, radare2 with the extracted filter/query `if($shiyan==$content)` and inspect the matching evidence.
- Tools: detect-it-easy, netcat, radare2
- Filters or commands:
  - `if($shiyan==$content)`
  - `1\. if(isset($shiyan)) == 》 TRUE`
  - `2. if(shiyan==shiyan==content) == 》 TRUE`
  - `//利用file_get_content()函数返回字符串+php弱类型（null == "string" ==》 true`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat, radare2 with the extracted filter/query `if($shiyan==$content)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:9009`

### Step 4: strcmp比较字符串

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, radare2 with the extracted filter/query `if (strcmp($_GET['a'], $flag) == 0) //如果 str1 小于 str2 返回 < 0； 如果 str1大于 str2返回 > 0；如果两者相等，返回 0。` and inspect the matching evidence.
- Tools: detect-it-easy, radare2
- Filters or commands:
  - `if (strcmp($_GET['a'], $flag) == 0) //如果 str1 小于 str2 返回 < 0； 如果 str1大于 str2返回 > 0；如果两者相等，返回 0。`
  - `strcmp(str1, str2)比较两个字符串大小，若是非字符串（例如数组）比较，则会出错。在5.3之前的php中，显示了报错的警告信息后，将return 0。0==0执行`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, radare2 with the extracted filter/query `if (strcmp($_GET['a'], $flag) == 0) //如果 str1 小于 str2 返回 < 0； 如果 str1大于 str2返回 > 0；如果两者相等，返回 0。` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:9009`

### Step 5: urldecode二次编码绕过

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat with the extracted filter/query `if($_GET[id] == "hackerDJ")` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if($_GET[id] == "hackerDJ")`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat with the extracted filter/query `if($_GET[id] == "hackerDJ")` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:9009`

### Step 6: md5()函数

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use detect-it-easy with the extracted filter/query `if ($_GET['username'] == $_GET['password'])` and inspect the matching evidence.
- Tools: detect-it-easy
- Filters or commands:
  - `if ($_GET['username'] == $_GET['password'])`
  - `else if (md5($_GET['username']) === md5($_GET['password']))`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use detect-it-easy with the extracted filter/query `if ($_GET['username'] == $_GET['password'])` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:9009`

### Step 7: 数组返回NULL绕过

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use detect-it-easy with the extracted filter/query `if (ereg ("^[a-zA-Z0-9]+$", $_GET['password']) === FALSE)` and inspect the matching evidence.
- Tools: detect-it-easy
- Filters or commands:
  - `if (ereg ("^[a-zA-Z0-9]+$", $_GET['password']) === FALSE)`
  - `else if (strpos ($_GET['password'], '--') !== FALSE)`
  - `ereg()只能处理字符，而password是数组，所以返回的是null，三个等号的时候不会进行类型转换。所以null!==false。`
  - `strpos()的参数同样不能够是数组，所以返回的依旧是null，null!==false也是正确。`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use detect-it-easy with the extracted filter/query `if (ereg ("^[a-zA-Z0-9]+$", $_GET['password']) === FALSE)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:9009`

### Step 8: 弱类型整数大小比较绕过

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use detect-it-easy to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: detect-it-easy
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use detect-it-easy to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:9009`

### Step 9: sha()函数比较绕过

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use detect-it-easy with the extracted filter/query `if ($_GET['name'] == $_GET['password'])` and inspect the matching evidence.
- Tools: detect-it-easy
- Filters or commands:
  - `if ($_GET['name'] == $_GET['password'])`
  - `else if (sha1($_GET['name']) === sha1($_GET['password']))`
  - `if ($a != 'QNKCDZO' && $md51 == $md52) {`
  - `PHP在处理哈希字符串时，会利用”!=”或”==”来对哈希值进行比较，它把每一个以“0E”开头的哈希值都解释为0，`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use detect-it-easy with the extracted filter/query `if ($_GET['name'] == $_GET['password'])` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:9009`

### Step 10: 十六进制与数字比较

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use netcat with the extracted filter/query `if($number == $temp)` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if($number == $temp)`
  - `题目中会要求输入的password中不能有0~9数字，并且还需要判断$number==$_GET[password]。所以将$number=3735929054转换为16进制“deadc0de”，再在前面加上0x表示16进制。`
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use netcat with the extracted filter/query `if($number == $temp)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:9009`

### Step 11: 变量覆盖（地址访问不了）

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `120.24.86.145:9009`

### Step 12: ereg正则%00截断

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use detect-it-easy with the extracted filter/query `if (ereg ("^[a-zA-Z0-9]+$", $_GET['password']) === FALSE)` and inspect the matching evidence.
- Tools: detect-it-easy
- Filters or commands:
  - `if (ereg ("^[a-zA-Z0-9]+$", $_GET['password']) === FALSE)`
  - `if (strpos ($_GET['password'], '-') !== FALSE) //strpos — 查找字符串首次出现的位置`
  - `解法一，利用数组绕过strpos()函数。strpos()数组 null!=false, strlen（）数组长度为0`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use detect-it-easy with the extracted filter/query `if (ereg ("^[a-zA-Z0-9]+$", $_GET['password']) === FALSE)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:9009`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
