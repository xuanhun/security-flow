# bugctf web代码审计 writeup_R_1v3r的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `bugctf web代码审计 writeup`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/bugctf-web代码审计-writeup_R_1v3r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/bugctf-web%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1-writeup_R_1v3r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/bugctf-web代码审计-writeup_R_1v3r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: netcat
- Techniques: http-analysis, php-tricks, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

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

### Step 2: bugctf web代码审计 writeup_R_1v3r的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `把题目做完了，记录一下题解`

### Step 3: extract变量覆盖

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat with the extracted filter/query `if($shiyan==$content)` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if($shiyan==$content)`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat with the extracted filter/query `if($shiyan==$content)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:9009`

### Step 4: strcmp比较字符串

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `6.php`

### Step 5: Urldecode二次编码绕过

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `浏览器回进行一次urldecode所以要对hackerDJ进行两次urlencode`

### Step 6: md5函数

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `index.php`

### Step 7: 弱类型整数大小比较绕过

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat with the extracted filter/query `Sha()处理数组时候，回返回NULL，所以可以绕过===` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `Sha()处理数组时候，回返回NULL，所以可以绕过===`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat with the extracted filter/query `Sha()处理数组时候，回返回NULL，所以可以绕过===` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `22.php`

### Step 8: Md5加密相等绕过

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat with the extracted filter/query `if ($a != 'QNKCDZO' && $md51 == $md52) {` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if ($a != 'QNKCDZO' && $md51 == $md52) {`
  - `md5('s878926199a')==md5('s155964671a') //就是True`
  - `php关于==号是这样处理的，如果一边是整型，另一边也需要是整型。`
  - `1e1 == 1e2 这个结果是对是错？`
  - `所以1e1 == 1e2这是false，但是`
  - `100 == 1e2 这是true，为什么1e2先转为整型，是100`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat with the extracted filter/query `if ($a != 'QNKCDZO' && $md51 == $md52) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0e545993274517709034328855841020`

### Step 9: 十六进制与数字比较

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `构造payload`

### Step 10: ereg正则截断

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use netcat with the extracted filter/query `var_dump(NULL === FALSE);` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `var_dump(NULL === FALSE);`
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use netcat with the extracted filter/query `var_dump(NULL === FALSE);` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5.php`

### Step 11: strpos数组绕过

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `）`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
