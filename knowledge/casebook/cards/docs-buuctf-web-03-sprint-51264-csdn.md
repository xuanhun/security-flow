# BUUCTF解题web十一道(03)_Sprint#51264的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `BUUCTF解题web十一道(03)`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF解题web十一道(03)_Sprint#51264的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF%E8%A7%A3%E9%A2%98web%E5%8D%81%E4%B8%80%E9%81%93%2803%29_Sprint%2351264%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF解题web十一道(03)_Sprint#51264的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app, web-service challenges.

## Input Signals

- Artifacts: ciphertext, web-app, web-service
- Tools: detect-it-easy, netcat, nmap
- Techniques: classical-crypto, command-injection, crypto-analysis, deserialization, encoding-analysis, file-inclusion, file-upload, http-analysis, php-tricks, ret2libc, service-enumeration, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `44`
- `docs/img/4e9b77d60a26686421d94e733c9dd342.png`
- `docs/img/fcf684270dc1c97e4fbed67309e55f53.png`
- `docs/img/c5ab9f420f9a3389202bd4aa1b2a2574.png`
- `docs/img/bbcdc1dc6b9bbfe2e72b449a3dfa7b0d.png`
- `docs/img/51a561456c08e0978fdb3409fe695749.png`
- `docs/img/a6eb1670c0a59ceba6260474d33a8e30.png`
- `docs/img/95078cabf6327d1b1c33702bb6de7e2e.png`
- `docs/img/63ec3a67cccb6cc5d05a3fa712120090.png`
- `docs/img/46308d3fcb59e73b24edd7e0a509b943.png`
- `docs/img/502bac9b64b1ac92870b040eb32df010.png`
- `docs/img/346f0e2a749348e026f85225a6eb4ad5.png`
- `docs/img/ea6bec1d091187d324bed64725922737.png`
- ... and `32` more

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat, nmap to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat, nmap
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat, nmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BUUCTF解题web十一道(03)_Sprint#51264的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat, nmap
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_45837896/article/details/117462101](https://blog.csdn.net/qq_45837896/article/details/117462101)`

### Step 3: [极客大挑战 2019]HardSQL

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4e9b77d60a26686421d94e733c9dd342`

### Step 4: [CISCN2019 华北赛区 Day2 Web1]Hack World

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use detect-it-easy, netcat, nmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: detect-it-easy, netcat, nmap
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use detect-it-easy, netcat, nmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `502bac9b64b1ac92870b040eb32df010`

### Step 5: [网鼎杯 2020 青龙组]AreUSerialz

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `if($this->op == "1") {` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `if($this->op == "1") {`
  - `} else if($this->op == "2") {`
  - `if($this->op === "2")`
  - `如果`op==1`，执行写入，如果字符串内容不大于`100`，就向指定`filename`写入内容`
  - `如果`op==2`，调用`read()`函数，该函数将`filename`文件中内容读取为字符串然后打印出来`
  - `文件包含`flag.php`，这里就要传参数`op==2`然后读取其中的内容，要用到反序列化的知识`
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use detect-it-easy, netcat with the extracted filter/query `if($this->op == "1") {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a71207387b260a8dccda51132e0bb17a`

### Step 6: [GXYCTF2019]BabySQli

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use detect-it-easy, netcat, nmap to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: detect-it-easy, netcat, nmap
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use detect-it-easy, netcat, nmap to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `fe1d5f7288bbe9ef519d2151e372d19d`

### Step 7: [MRCTF2020]你传你🐎呢

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use detect-it-easy, netcat, nmap to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: detect-it-easy, netcat, nmap
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use detect-it-easy, netcat, nmap to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `SetHandler application/x-httpd-php`

### Step 8: [MRCTF2020]Ez_bypass

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `if (md5($id) === md5($gg) && $id !== $gg) {` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `if (md5($id) === md5($gg) && $id !== $gg) {`
  - `if($passwd==1234567)`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use detect-it-easy, netcat with the extracted filter/query `if (md5($id) === md5($gg) && $id !== $gg) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ee4651988d03018f6c25f1fdc9f2b907`

### Step 9: [GYCTF2020]Blacklist

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use detect-it-easy, netcat, nmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: detect-it-easy, netcat, nmap
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use detect-it-easy, netcat, nmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `13a84b92620cb1b266bfc9815b7954b2`

### Step 10: [BUUCTF 2018]Online Tool

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use nmap to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: nmap
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use nmap to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8add7eb5ed1a52e8a4bc4517a355e808`

### Step 11: [GXYCTF2019]BabyUpload

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use detect-it-easy, netcat, nmap to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: detect-it-easy, netcat, nmap
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use detect-it-easy, netcat, nmap to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `57eda9f1c54ca72b8d8f3008632b3401`

### Step 12: [RoarCTF 2019]Easy Java

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use detect-it-easy, netcat, nmap to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: detect-it-easy, netcat, nmap
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use detect-it-easy, netcat, nmap to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ece6acfbcaa257bdd530d9a454b9994a`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
