# 信息安全web入门——南邮ctf解题_sevenlob的博客-CSDN博客_南邮ctf

## Case Metadata

- Category: `Web`
- Platform: `信息安全web入门——南邮ctf解题`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/信息安全web入门——南邮ctf解题_sevenlob的博客-CSDN博客_南邮ctf.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E4%BF%A1%E6%81%AF%E5%AE%89%E5%85%A8web%E5%85%A5%E9%97%A8%E2%80%94%E2%80%94%E5%8D%97%E9%82%AEctf%E8%A7%A3%E9%A2%98_sevenlob%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_%E5%8D%97%E9%82%AEctf.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/信息安全web入门——南邮ctf解题_sevenlob的博客-CSDN博客_南邮ctf.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app, web-service challenges.

## Input Signals

- Artifacts: ciphertext, web-app, web-service
- Tools: burp, netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, dns-analysis, encoding-analysis, file-inclusion, http-analysis, php-tricks, sql-injection, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `15`
- `docs/img/6b7b8344f7d45e1a65d2865a644049c8.png`
- `docs/img/9427f71d6ca6919ac4f25a2cc9af05a5.png`
- `docs/img/e65c16ee43ad5ccde701670b828f498f.png`
- `docs/img/154925ed034772bda705e5808f8ccf7f.png`
- `docs/img/307eb82d9150cdb0e191fd0244ebd48e.png`
- `docs/img/39b2133512ab3faca72aadc7923ec188.png`
- `docs/img/985cfe45bcefa0872679d6dac46afd84.png`
- `docs/img/49cf43b87a777af5cbfa5e90765101fa.png`
- `docs/img/a58388c1eccee80b2d92d3ae433c1ff5.png`
- `docs/img/c4d9e742c08f72987b2be603cad1daab.png`
- `docs/img/e2bf7d5c3dd20dac70d50ca2edabe89e.png`
- `docs/img/cf4697bcb2b7838de168bce8e52fd3cb.png`
- ... and `3` more

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

### Step 2: 信息安全web入门——南邮ctf解题_sevenlob的博客-CSDN博客_南邮ctf

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/sevenlob/article/details/103987096](https://blog.csdn.net/sevenlob/article/details/103987096)`

### Step 3: 签到题

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `鼠标右键查看源码或ctrl+u`

### Step 4: md5 collision

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat with the extracted filter/query `if ($a != 'QNKCDZO' && $md51 == $md52) {` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if ($a != 'QNKCDZO' && $md51 == $md52) {`
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat with the extracted filter/query `if ($a != 'QNKCDZO' && $md51 == $md52) {` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `?>`

### Step 5: 弱类型

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat with the extracted filter/query `等于号 == 在进行比较的时候，会先将**字符串类型转化成相同**，再比较。` and inspect the matching evidence.
- Tools: burp, netcat
- Filters or commands:
  - `等于号 == 在进行比较的时候，会先将**字符串类型转化成相同**，再比较。`
  - `等于号 === 在进行比较的时候，会**先判断两种字符串的类型是否相等**，再比较。`
  - `在比较$a==$b`
  - `0=='abcdef'`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat with the extracted filter/query `等于号 == 在进行比较的时候，会先将**字符串类型转化成相同**，再比较。` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `[php弱类型总结](https://www.cnblogs.com/Mrsm1th/p/6745532.html)`

### Step 6: @错误控制操作符

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `在PHP中，@被称为错误控制操作符(error control operator)，前置@符号的表达式产生的任何错误都将被忽略。`

### Step 7: isset()

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `isset — 检测变量是否已设置并且非 NULL,返回true或false`

### Step 8: MD5——哈希算法

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat with the extracted filter/query `| 参数 | 描述 |` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `| 参数 | 描述 |`
  - `| --- | --- |`
  - `| string | 必需。规定要计算的字符串。 |`
  - `| raw | 可选。规定十六进制或二进制输出格式： |`
  - `| string(strlen($var)) $var | string(strlen(md5($ var))) md5($var) |`
  - `| s878926199a | 0e545993274517709034328855841020 |`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat with the extracted filter/query `| 参数 | 描述 |` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0e545993274517709034328855841020`

### Step 9: 题目分析

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat with the extracted filter/query `if ($a != 'QNKCDZO' && $md51 == $md52) {` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if ($a != 'QNKCDZO' && $md51 == $md52) {`
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat with the extracted filter/query `if ($a != 'QNKCDZO' && $md51 == $md52) {` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `else{echo "please input a";}`

### Step 10: 签到提2

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use burp, netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use burp, netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6b7b8344f7d45e1a65d2865a644049c8`

### Step 11: 这题不是WEB

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `看来还真的不是web题。。。`

### Step 12: 层层递进

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `e65c16ee43ad5ccde701670b828f498f`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
