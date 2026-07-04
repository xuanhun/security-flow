# Buuctf部分题解_君陌上的博客-CSDN博客_buuctf

## Case Metadata

- Category: `Web`
- Platform: `Buuctf部分题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/Buuctf部分题解_君陌上的博客-CSDN博客_buuctf.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/Buuctf%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3_%E5%90%9B%E9%99%8C%E4%B8%8A%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_buuctf.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/Buuctf部分题解_君陌上的博客-CSDN博客_buuctf.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app, web-service
- Tools: burp, detect-it-easy, netcat, radare2
- Techniques: classical-crypto, command-injection, crypto-analysis, deserialization, encoding-analysis, file-inclusion, file-upload, http-analysis, jwt-analysis, php-tricks, qr-analysis, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `61`
- `docs/img/f002c2b0143a81f76217e53b92ac9488.png`
- `docs/img/99fe67cfd71dd74cc2599a90e7f59c6f.png`
- `docs/img/e21f61407ce33f65dbbd09aea059a10e.png`
- `docs/img/57be9c7c9ce16ccbd10cb78ce45e4b19.png`
- `docs/img/26ec3c30406e5a385aee15dd65ecccc4.png`
- `docs/img/b27b270c8976b77f4b772f6d6d59a410.png`
- `docs/img/033516fde237fd2ff23791a35a7b4532.png`
- `docs/img/30124033e3a7c916f0f5aef2b989b41b.png`
- `docs/img/2624d0372166a3f397a5b256ad2bc303.png`
- `docs/img/ffd8d8f6f1a24442d569d3e24a49e97d.png`
- `docs/img/9c087c818608487b20ae786fccb223b3.png`
- `docs/img/11d278d1012149aa38440f49291db884.png`
- ... and `49` more

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

### Step 2: Buuctf部分题解_君陌上的博客-CSDN博客_buuctf

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_53549425/article/details/120314290](https://blog.csdn.net/weixin_53549425/article/details/120314290)`

### Step 3: [极客大挑战 2019]Http1

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1`

### Step 4: [极客大挑战 2019]Knife1

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `033516fde237fd2ff23791a35a7b4532`

### Step 5: [极客大挑战 2019]Upload1

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use burp to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: burp
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use burp to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2624d0372166a3f397a5b256ad2bc303`

### Step 6: [极客大挑战 2019]PHP1

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `if ($this->password != 100) {` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `if ($this->password != 100) {`
  - `if ($this->username === 'admin') {`
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use detect-it-easy, netcat with the extracted filter/query `if ($this->password != 100) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `16787de10de501dd63fe207901d622b5`

### Step 7: Buuctf__[SUCTF 2019]CheckIn 1

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `if (preg_match("/ph|htacess/i", $extension)) {` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `if (preg_match("/ph|htacess/i", $extension)) {`
  - `if (mb_strpos(file_get_contents($tmp_name), "<?") !== FALSE) {`
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use detect-it-easy, netcat with the extracted filter/query `if (preg_match("/ph|htacess/i", $extension)) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `79468e145cd599c3ead6c652ee9b2c2b`

### Step 8: [ACTF2020 新生赛]Exec1

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat with the extracted filter/query `然后浏览目录，输入`127.0.0.1 | ls`，发现只有一个index.php，查看它的上级目录，`127.0.0.1 | ls/`` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `然后浏览目录，输入`127.0.0.1 | ls`，发现只有一个index.php，查看它的上级目录，`127.0.0.1 | ls/``
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat with the extracted filter/query `然后浏览目录，输入`127.0.0.1 | ls`，发现只有一个index.php，查看它的上级目录，`127.0.0.1 | ls/`` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1`

### Step 9: [GXYCTF2019]Ping Ping Ping1

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use burp, detect-it-easy, netcat, radare2 to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use burp, detect-it-easy, netcat, radare2 to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1`

### Step 10: [BJDCTF2020]Easy MD5 1

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `if($a != $b && md5($a) == md5($b)){` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if($a != $b && md5($a) == md5($b)){`
  - `if($_POST['param1']!==$_POST['param2']&&md5($_POST['param1'])===md5($_POST['param2'])){`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `if($a != $b && md5($a) == md5($b)){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0450c102b8f36ab184f49fcec93ab093`

### Step 11: [ACTF2020 新生赛]BackupFile1

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat, radare2 with the extracted filter/query `if($key == $str) {` and inspect the matching evidence.
- Tools: netcat, radare2
- Filters or commands:
  - `if($key == $str) {`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat, radare2 with the extracted filter/query `if($key == $str) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `57623e653e3704ed6803d9458aea3ed2`

### Step 12: [GXYCTF2019]BabySQli

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use burp, detect-it-easy, netcat, radare2 with the extracted filter/query `c2VsZWN0ICogZnJvbSB1c2VyIHdoZXJlIHVzZXJuYW1lID0gJyRuYW1lJw==` and inspect the matching evidence.
- Tools: burp, detect-it-easy, netcat, radare2
- Filters or commands:
  - `c2VsZWN0ICogZnJvbSB1c2VyIHdoZXJlIHVzZXJuYW1lID0gJyRuYW1lJw==`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use burp, detect-it-easy, netcat, radare2 with the extracted filter/query `c2VsZWN0ICogZnJvbSB1c2VyIHdoZXJlIHVzZXJuYW1lID0gJyRuYW1lJw==` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `86953dc62bbcb6b8e4a6d5be7652d78b`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
