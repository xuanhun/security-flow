# CTF专题一2021网络WEB题目解析_普通网友的博客-CSDN博客_ctf web分析

## Case Metadata

- Category: `Web`
- Platform: `CTF专题一2021网络WEB题目解析`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF专题一2021网络WEB题目解析_普通网友的博客-CSDN博客_ctf-web分析.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%E4%B8%93%E9%A2%98%E4%B8%802021%E7%BD%91%E7%BB%9CWEB%E9%A2%98%E7%9B%AE%E8%A7%A3%E6%9E%90_%E6%99%AE%E9%80%9A%E7%BD%91%E5%8F%8B%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctf-web%E5%88%86%E6%9E%90.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF专题一2021网络WEB题目解析_普通网友的博客-CSDN博客_ctf-web分析.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, linux-logs challenges.

## Input Signals

- Artifacts: binary, ciphertext, linux-logs, stego-media, web-app
- Tools: detect-it-easy, netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, deserialization, encoding-analysis, file-inclusion, file-upload, http-analysis, php-tricks, ssti, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `39`
- `docs/img/fe2f03505eb3027446ceec86088d41a8.png`
- `docs/img/3d21dffacd52b93a2dfe5f6be079d1de.png`
- `docs/img/27b2bc8e370412dd29e8703873682ef2.png`
- `docs/img/7a738bc83b4b04df9f7dfe7c2373706e.png`
- `docs/img/363d55b7e0ecbe80c9ebc7a3553bad02.png`
- `docs/img/5eb8311b71d0147ba0678720acb0fbf8.png`
- `docs/img/291b2a09bdce7b86069e286637e0f03e.png`
- `docs/img/6ecbd5e6b3a6c92c8eae7ebd66d786d4.png`
- `docs/img/e10ea910abd48aa413dbac3097e728cf.png`
- `docs/img/19a4ac8c645a38e64fa029d0765d876e.png`
- `docs/img/88b802d05e4ac097abdbd6c2a721c80a.png`
- `docs/img/fc3355686185af46798c9814ee6ffbf0.png`
- ... and `27` more

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

### Step 2: CTF专题一2021网络WEB题目解析_普通网友的博客-CSDN博客_ctf web分析

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/kali_ma/article/details/120847330](https://blog.csdn.net/kali_ma/article/details/120847330)`

### Step 3: **0x01 前言**

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use detect-it-easy, netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use detect-it-easy, netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `fe2f03505eb3027446ceec86088d41a8`

### Step 4: **0x02 ezphp**

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `27b2bc8e370412dd29e8703873682ef2`

### Step 5: **0x03 phar**

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `6ecbd5e6b3a6c92c8eae7ebd66d786d4`

### Step 6: **0x04 HardCode**

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `6a33165bb8cd252dd7a40c436f37fb9f`

### Step 7: **0x05 CODE**

- Route type: `incident timeline reconstruction`
- Why: Incident-response cases become reusable when every claim is anchored to timestamped artifact correlation.
- Probe: Use detect-it-easy with the extracted filter/query `if(!@isset($username['admin'])||$username['admin'] != @md5($_SESSION['username'])) {` and inspect the matching evidence.
- Tools: detect-it-easy
- Filters or commands:
  - `if(!@isset($username['admin'])||$username['admin'] != @md5($_SESSION['username'])) {`
- Reasoning chain:
  - Recognize the section as incident timeline reconstruction.
  - Use detect-it-easy with the extracted filter/query `if(!@isset($username['admin'])||$username['admin'] != @md5($_SESSION['username'])) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a317df21f993261fd12cfab5393ebdfc`

### Step 8: **0x06 EZpy**

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use netcat with the extracted filter/query `#==判断` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `#==判断`
  - `return type(other) is people and self.name == other.name and self.sex == other.sex and self.age==other.age`
  - `correct = (result == people(b.name, b.sex, b.age))`
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use netcat with the extracted filter/query `#==判断` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0.0.0.0`

### Step 9: **0x07 ezp0p**

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `if($_POST['x']!=$_POST['y'] && md5($_POST['x'])===md5($_POST['y'])){` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `if($_POST['x']!=$_POST['y'] && md5($_POST['x'])===md5($_POST['y'])){`
  - `if(file_get_contents(substr($_POST['x'],0,20))!=null){`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use detect-it-easy, netcat with the extracted filter/query `if($_POST['x']!=$_POST['y'] && md5($_POST['x'])===md5($_POST['y'])){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `849c3965391c841810c3944ebe52dd0f`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
