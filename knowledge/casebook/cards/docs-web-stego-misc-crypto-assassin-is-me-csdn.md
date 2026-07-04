# 第四届“”世安杯“”线上赛题解（Web+Stego+Misc+Crypto）_Assassin__is__me的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `第四届“”世安杯“”线上赛题解（Web+Stego+Misc+Crypto）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/第四届“”世安杯“”线上赛题解（Web+Stego+Misc+Crypto）_Assassin__is__me的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E7%AC%AC%E5%9B%9B%E5%B1%8A%E2%80%9C%E2%80%9D%E4%B8%96%E5%AE%89%E6%9D%AF%E2%80%9C%E2%80%9D%E7%BA%BF%E4%B8%8A%E8%B5%9B%E9%A2%98%E8%A7%A3%EF%BC%88Web%2BStego%2BMisc%2BCrypto%EF%BC%89_Assassin__is__me%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/第四届“”世安杯“”线上赛题解（Web+Stego+Misc+Crypto）_Assassin__is__me的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, stego-media challenges.

## Input Signals

- Artifacts: binary, ciphertext, stego-media, web-app
- Tools: detect-it-easy, netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, deserialization, encoding-analysis, file-inclusion, http-analysis, image-analysis, misc-analysis, php-tricks, qr-analysis, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `12`
- `docs/img/ce064a0a5147aa2bd6537419793c2797.png`
- `docs/img/379e19b65019279f09b5898692ae257d.png`
- `docs/img/72fcb82d842e72e16055f6ce674f332c.png`
- `docs/img/ef1d5a4313ed5afa07a1f4794ddb7698.png`
- `docs/img/25b019e232660e80a836ffb2e58136dd.png`
- `docs/img/44d327377db37524ac728ee9444895d3.png`
- `docs/img/96c34ddae90157f55a178fd87e61feed.png`
- `docs/img/dbebc661fdd5b2d0ad47e3f9e98ec8ef.png`
- `docs/img/488979721f08137cba8bb6bfbb26afed.png`
- `docs/img/ff46eb892fd716efef27e9a4f91d38eb.png`
- `docs/img/ac5f55d6da24cd87210de6e825bb8a7b.png`
- `docs/img/55e3d444f2074a3d6028ececa1087b5d.png`

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

### Step 2: 第四届“”世安杯“”线上赛题解（Web+Stego+Misc+Crypto）_Assassin__is__me的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `题目很多原题，但是还是考验了不少的知识点，就算是原来见过的也当做是复习了一下知识点了。`

### Step 3: **ctf入门级题目**

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ce064a0a5147aa2bd6537419793c2797`

### Step 4: **曲奇饼**

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `if($file=='') header("location:index.php?line=&file=a2V5LnR4dA==");` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `if($file=='') header("location:index.php?line=&file=a2V5LnR4dA==");`
  - `if(isset($_COOKIE['key']) && $_COOKIE['key']=='li_lr_480'){`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use detect-it-easy, netcat with the extracted filter/query `if($file=='') header("location:index.php?line=&file=a2V5LnR4dA==");` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `379e19b65019279f09b5898692ae257d`

### Step 5: **类型**

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `$x1=="1"?die("ha?"):NULL;` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `$x1=="1"?die("ha?"):NULL;`
  - `if(count($x2["x22"])!==2 OR !is_array($x2["x22"][0])) die("ha?");`
  - `$p===false?die("ha?"):NULL;`
  - `$val==="XIPU"?die("ha?"):NULL;`
  - `if ($x3 != '15562') {`
  - `if (substr(md5($x3),8,16) == substr(md5('15562'),8,16)) {`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use detect-it-easy, netcat with the extracted filter/query `$x1=="1"?die("ha?"):NULL;` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `72fcb82d842e72e16055f6ce674f332c`

### Step 6: **登录**

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `index.php`

### Step 7: **admin**

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use netcat with the extracted filter/query `if(isset($user)&&(file_get_contents($user,'r')==="the user is admin")){` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if(isset($user)&&(file_get_contents($user,'r')==="the user is admin")){`
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use netcat with the extracted filter/query `if(isset($user)&&(file_get_contents($user,'r')==="the user is admin")){` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ef1d5a4313ed5afa07a1f4794ddb7698`

### Step 8: **low**

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use detect-it-easy, netcat to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use detect-it-easy, netcat to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `44d327377db37524ac728ee9444895d3`

### Step 9: **斑马斑马**

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `96c34ddae90157f55a178fd87e61feed`

### Step 10: **CreateByWho**

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use detect-it-easy, netcat to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use detect-it-easy, netcat to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `488979721f08137cba8bb6bfbb26afed`

### Step 11: **适合作为桌面图片**

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ff46eb892fd716efef27e9a4f91d38eb`

### Step 12: **reverseMe**

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ac5f55d6da24cd87210de6e825bb8a7b`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
