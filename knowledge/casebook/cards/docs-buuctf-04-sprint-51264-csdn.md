# BUUCTF解题十一道(04)_Sprint#51264的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `BUUCTF解题十一道(04)`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF解题十一道(04)_Sprint#51264的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF%E8%A7%A3%E9%A2%98%E5%8D%81%E4%B8%80%E9%81%93%2804%29_Sprint%2351264%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF解题十一道(04)_Sprint#51264的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, email challenges.

## Input Signals

- Artifacts: binary, ciphertext, email, web-app, web-service
- Tools: detect-it-easy, dirb, netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, deserialization, dns-analysis, encoding-analysis, file-inclusion, file-upload, http-analysis, php-tricks, ret2libc, sql-injection, ssti, waf-bypass, web-enumeration, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `59`
- `docs/img/08e5d1d097838e0911c868453eb4591a.png`
- `docs/img/c45be9c8d7cf6540ed75d3834b87c8ff.png`
- `docs/img/5499e7930c67e43f04e872fcce44f443.png`
- `docs/img/85a60e2fac6509aa1672af244b4b84c8.png`
- `docs/img/272f713befdb5e413f164b1d4a0f5e1b.png`
- `docs/img/20eeed7fe2cfe4498f3e619d25d2b208.png`
- `docs/img/9ad20eac412139a4e411c52cdddd482c.png`
- `docs/img/62a7faa312b81cc760030b674c5e9c04.png`
- `docs/img/2933ba2301113bb8345dbc0a73a7dc4b.png`
- `docs/img/54d033da3ac176c745de6e8ed829f36f.png`
- `docs/img/f431315e0615b90dd63785bbaccc2fb5.png`
- `docs/img/09eee89556606a1d189f2592e0ad6ebf.png`
- ... and `47` more

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, dirb, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, dirb, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, dirb, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BUUCTF解题十一道(04)_Sprint#51264的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, dirb, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, dirb, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, dirb, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_45837896/article/details/117751870](https://blog.csdn.net/qq_45837896/article/details/117751870)`

### Step 3: [GWCTF 2019]我有一个数据库

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use dirb to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: dirb
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use dirb to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `CVE-2018-12613`

### Step 4: [BJDCTF2020]ZJCTF，不过如此

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5499e7930c67e43f04e872fcce44f443`

### Step 5: [BJDCTF2020]The mystery of ip

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use detect-it-easy, dirb, netcat to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
- Tools: detect-it-easy, dirb, netcat
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use detect-it-easy, dirb, netcat to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `9ad20eac412139a4e411c52cdddd482c`

### Step 6: [BJDCTF2020]Mark loves cat

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use netcat with the extracted filter/query `if($_GET['flag'] === $x && $x !== 'flag'){` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if($_GET['flag'] === $x && $x !== 'flag'){`
  - `if($_POST['flag'] === 'flag' || $_GET['flag'] === 'flag'){`
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use netcat with the extracted filter/query `if($_GET['flag'] === $x && $x !== 'flag'){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `f431315e0615b90dd63785bbaccc2fb5`

### Step 7: [安洵杯 2019]easy_web

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `error_reporting(E_ALL || ~ E_NOTICE);` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `error_reporting(E_ALL || ~ E_NOTICE);`
  - `if (!isset($_GET['img']) || !isset($_GET['cmd']))`
  - `if ((string)$_POST['a'] !== (string)$_POST['b'] && md5($_POST['a']) === md5($_POST['b'])) {`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use detect-it-easy, netcat with the extracted filter/query `error_reporting(E_ALL || ~ E_NOTICE);` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `84b022f7cb6080884a56d48ac5d3c345`

### Step 8: [网鼎杯 2020 朱雀组]phpweb

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `if ($a == "string") {` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `if ($a == "string") {`
  - `if ($this->func != "") {`
  - `if ($func != null) {`
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use detect-it-easy, netcat with the extracted filter/query `if ($a == "string") {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `cbe5f331151b9b1a5d539ad7e7581bcc`

### Step 9: [ASIS 2019]Unicorn shop

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, dirb, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, dirb, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, dirb, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `d98eb9569b157c5390101d002903dfb6`

### Step 10: [BJDCTF2020]Cookie is so stable

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use detect-it-easy, dirb, netcat to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
- Tools: detect-it-easy, dirb, netcat
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use detect-it-easy, dirb, netcat to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8363ea0bb3d8537d3f9368535251b423`

### Step 11: [BSidesCF 2020]Had a bad day

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `if( strpos( $file, "woofers" ) !== false || strpos( $file, "meowers" ) !== false || strpos( $file, "index")){` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if( strpos( $file, "woofers" ) !== false || strpos( $file, "meowers" ) !== false || strpos( $file, "index")){`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `if( strpos( $file, "woofers" ) !== false || strpos( $file, "meowers" ) !== false || strpos( $file, "index")){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a3cc41c59226d1404079ea03ba565183`

### Step 12: [WUSTCTF2020]朴实无华

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use detect-it-easy with the extracted filter/query `if ($md5==md5($md5))` and inspect the matching evidence.
- Tools: detect-it-easy
- Filters or commands:
  - `if ($md5==md5($md5))`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use detect-it-easy with the extracted filter/query `if ($md5==md5($md5))` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a1a8d1828ec9dac9a36c206a472143ec`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
