# BUUCTF_web部分题解_ro4lsc的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `BUUCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF_web部分题解_ro4lsc的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF_web%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3_ro4lsc%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF_web部分题解_ro4lsc的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app, web-service challenges.

## Input Signals

- Artifacts: ciphertext, web-app, web-service
- Tools: burp, detect-it-easy, netcat, radare2
- Techniques: classical-crypto, command-injection, crypto-analysis, encoding-analysis, file-inclusion, file-upload, http-analysis, jwt-analysis, php-tricks, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `51`
- `docs/img/7ba451ba72b2d1d36816b0c8991a9d75.png`
- `docs/img/2a823773a7e58e47ec6257aebab1cb90.png`
- `docs/img/a207d9c3528b9ae839c4b70ddf47ef0b.png`
- `docs/img/2c21bedd3c71911bd6d66e34d1b9a4f1.png`
- `docs/img/152e82d4c5985d64feb19804d13c5573.png`
- `docs/img/355e38c5fe1ce47e5609ee0ea717c026.png`
- `docs/img/d8e58d6f3982e8fdfdd98e1a7cc3d9e4.png`
- `docs/img/90db963bda37e14be3f36af2f92cf130.png`
- `docs/img/1ec1102262104f6295fcd4507498e43e.png`
- `docs/img/9c5cade01b9286f578e7f55944cfa380.png`
- `docs/img/179d0b0d75b895721603874af14c7114.png`
- `docs/img/d3d4979ddb59823388c825b5a3db2a7a.png`
- ... and `39` more

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

### Step 2: BUUCTF_web部分题解_ro4lsc的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/gd_9988/article/details/105481036](https://blog.csdn.net/gd_9988/article/details/105481036)`

### Step 3: 前言

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `[[ACTF2020 新生赛]BackupFile](#15)`

### Step 4: [极客大挑战 2019]Havefun

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, radare2 with the extracted filter/query `if($cat == 'dog'){` and inspect the matching evidence.
- Tools: burp, detect-it-easy, netcat, radare2
- Filters or commands:
  - `if($cat == 'dog'){`
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, radare2 with the extracted filter/query `if($cat == 'dog'){` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `7ba451ba72b2d1d36816b0c8991a9d75`

### Step 5: [CISCN2019 华北赛区 Day2 Web1]Hack World

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use burp, detect-it-easy, netcat, radare2 with the extracted filter/query `$blackList = array(' ','||','#','-',';','&','+','or','and','`','"','insert','group','limit','update','delete','*','into','union','load_file','outfile','./');` and inspect the matching evidence.
- Tools: burp, detect-it-easy, netcat, radare2
- Filters or commands:
  - `$blackList = array(' ','||','#','-',';','&','+','or','and','`','"','insert','group','limit','update','delete','*','into','union','load_file','outfile','./');`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use burp, detect-it-easy, netcat, radare2 with the extracted filter/query `$blackList = array(' ','||','#','-',';','&','+','or','and','`','"','insert','group','limit','update','delete','*','into','union','load_file','outfile','./');` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2c21bedd3c71911bd6d66e34d1b9a4f1`

### Step 6: [极客大挑战 2019]Secret File

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use burp, netcat with the extracted filter/query `if(strstr($file,"../")||stristr($file, "tp")||stristr($file,"input")||stristr($file,"data")){` and inspect the matching evidence.
- Tools: burp, netcat
- Filters or commands:
  - `if(strstr($file,"../")||stristr($file, "tp")||stristr($file,"input")||stristr($file,"data")){`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use burp, netcat with the extracted filter/query `if(strstr($file,"../")||stristr($file, "tp")||stristr($file,"input")||stristr($file,"data")){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `152e82d4c5985d64feb19804d13c5573`

### Step 7: [极客大挑战 2019]Knife

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `bc803c9b0885f37cb07937867578c7af`

### Step 8: [极客大挑战 2019]LoveSQL

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `check.php`

### Step 9: [极客大挑战 2019]Http

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `04e986367683aa4b38b408e0375bfada`

### Step 10: [GXYCTF2019]Ping Ping Ping

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use detect-it-easy with the extracted filter/query `if(preg_match("/\&|\/|\?|\*|\<|[\x{00}-\x{1f}]|\>|\'|\"|\\|\(|\)|\[|\]|\{|\}/", $ip, $match)){` and inspect the matching evidence.
- Tools: detect-it-easy
- Filters or commands:
  - `if(preg_match("/\&|\/|\?|\*|\<|[\x{00}-\x{1f}]|\>|\'|\"|\\|\(|\)|\[|\]|\{|\}/", $ip, $match)){`
  - `echo preg_match("/\&|\/|\?|\*|\<|[\x{00}-\x{20}]|\>|\'|\"|\\|\(|\)|\[|\]|\{|\}/", $ip, $match);`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use detect-it-easy with the extracted filter/query `if(preg_match("/\&|\/|\?|\*|\<|[\x{00}-\x{1f}]|\>|\'|\"|\\|\(|\)|\[|\]|\{|\}/", $ip, $match)){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1`

### Step 11: [极客大挑战 2019]BabySQL

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `bc0251170ad2851bda65225a56aeac50`

### Step 12: [极客大挑战 2019]BuyFlag

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use burp to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: burp
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use burp to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3ba6674758075e2ae3f5671ef5180a68`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
