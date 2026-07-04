# BUUCTF-Web题解（一）_flying_bird2019的博客-CSDN博客_buuctfweb第一题

## Case Metadata

- Category: `Web`
- Platform: `BUUCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF-Web题解（一）_flying_bird2019的博客-CSDN博客_buuctfweb第一题.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF-Web%E9%A2%98%E8%A7%A3%EF%BC%88%E4%B8%80%EF%BC%89_flying_bird2019%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_buuctfweb%E7%AC%AC%E4%B8%80%E9%A2%98.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF-Web题解（一）_flying_bird2019的博客-CSDN博客_buuctfweb第一题.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: detect-it-easy, netcat
- Techniques: classical-crypto, command-injection, deserialization, encoding-analysis, file-inclusion, file-upload, php-tricks, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `12`
- `docs/img/f8f49c05f8d35f5927f26cb989243fe3.png`
- `docs/img/02ec0a0fbd1fb4dbf3e2a946d93485b5.png`
- `docs/img/aa9f65119e2c37d10e443990789b5aa3.png`
- `docs/img/35cb70d33d33afec74315fdb59fbb97b.png`
- `docs/img/5c7543c6c907c09bef99c756d5307b27.png`
- `docs/img/3a1cfb3d8f6ab688f1952ad94aad0bee.png`
- `docs/img/9e3265f0ee8cd9b2b7f0458e3e9236b6.png`
- `docs/img/5d82c3ef0fd396fb8c27c417581ea30c.png`
- `docs/img/d11761819386c43552432076c4baf70d.png`
- `docs/img/5e6bbac31deea3680bbc2f193d39b9f1.png`
- `docs/img/e509c135e270778ce1fe858339285220.png`
- `docs/img/a77ba06776a0f8a0ad8e590b38760f88.png`

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BUUCTF-Web题解（一）_flying_bird2019的博客-CSDN博客_buuctfweb第一题

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/flying_bird2019/article/details/111249695](https://blog.csdn.net/flying_bird2019/article/details/111249695)`

### Step 3: ping ping ping

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use detect-it-easy with the extracted filter/query `|\'|\"|\\|\(|\)|\[|\]|\{|\}/", $ip, $match)){` and inspect the matching evidence.
- Tools: detect-it-easy
- Filters or commands:
  - `|\'|\"|\\|\(|\)|\[|\]|\{|\}/", $ip, $match)){`
  - `echo preg_match("/\&|\/|\?|\*|\<|[\x{00}-\x{20}]|\>|\'|\"|\\|\(|\)|\[|\]|\{|\}/", $ip, $match);`
  - `?ip=127.0.0.1;echo$IFS$1Y2F0IGZsYWcucGhw|base64$IFS$1-d|sh`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use detect-it-easy with the extracted filter/query `|\'|\"|\\|\(|\)|\[|\]|\{|\}/", $ip, $match)){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1`

### Step 4: Easy Calc

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use detect-it-easy, netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use detect-it-easy, netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `f8f49c05f8d35f5927f26cb989243fe3`

### Step 5: PHP

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `35cb70d33d33afec74315fdb59fbb97b`

### Step 6: upload

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use detect-it-easy, netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use detect-it-easy, netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `5c7543c6c907c09bef99c756d5307b27`

### Step 7: BabySQL（报错注入）

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use detect-it-easy, netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use detect-it-easy, netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `9e3265f0ee8cd9b2b7f0458e3e9236b6`

### Step 8: CheckIn

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use detect-it-easy with the extracted filter/query `if (preg_match("/ph|htacess/i", $extension)) {` and inspect the matching evidence.
- Tools: detect-it-easy
- Filters or commands:
  - `if (preg_match("/ph|htacess/i", $extension)) {`
  - `if (mb_strpos(file_get_contents($tmp_name), "<?") !== FALSE) {`
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use detect-it-easy with the extracted filter/query `if (preg_match("/ph|htacess/i", $extension)) {` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `5d82c3ef0fd396fb8c27c417581ea30c`

### Step 9: EasyMD5

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use detect-it-easy, netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use detect-it-easy, netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `5e6bbac31deea3680bbc2f193d39b9f1`

### Step 10: NiZhuanSiWei

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use netcat with the extracted filter/query `if(isset($text)&&(file_get_contents($text,'r')==="welcome to the zjctf")){` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if(isset($text)&&(file_get_contents($text,'r')==="welcome to the zjctf")){`
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use netcat with the extracted filter/query `if(isset($text)&&(file_get_contents($text,'r')==="welcome to the zjctf")){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a77ba06776a0f8a0ad8e590b38760f88`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
