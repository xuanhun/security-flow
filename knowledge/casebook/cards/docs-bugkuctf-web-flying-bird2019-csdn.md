# BugkuCTF-WEB部分题解（四）_flying_bird2019的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `BugkuCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BugkuCTF-WEB部分题解（四）_flying_bird2019的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BugkuCTF-WEB%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3%EF%BC%88%E5%9B%9B%EF%BC%89_flying_bird2019%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BugkuCTF-WEB部分题解（四）_flying_bird2019的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: detect-it-easy, netcat
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, php-tricks, qr-analysis, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `1`
- `docs/img/455ba6049d81fb16d6825e1fd8be0fa3.png`

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

### Step 2: BugkuCTF-WEB部分题解（四）_flying_bird2019的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/flying_bird2019/article/details/109983418](https://blog.csdn.net/flying_bird2019/article/details/109983418)`

### Step 3: 字符？正则？

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2.php`

### Step 4: login1(skctf)

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use detect-it-easy, netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use detect-it-easy, netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `因此我们可以构造一个用户名’xxxxx+(多个空格)+1(不唯一)‘这样在注册时sql查询表中有无该用户名时能继续下一步，如果构造的用户名超过限制，则会取前x个字符插入，此时插入的用户名实际为’xxxxx+(多个空格)’`

### Step 5: 多次

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat with the extracted filter/query `id=1’^(length(‘union’))!=0–+` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `id=1’^(length(‘union’))!=0–+`
  - `当union被过滤的时候length(’’)!=0为假，真与假异或为真，页面显示正确`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat with the extracted filter/query `id=1’^(length(‘union’))!=0–+` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `455ba6049d81fb16d6825e1fd8be0fa3`

### Step 6: PHP_encrypt_1(ISCCCTF)

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `if ($x == $klen)` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `if ($x == $klen)`
  - `if(((ord($payload[$k]) + ord($char[$i])) % 128)-ord($str1[$i])===0){`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use detect-it-easy, netcat with the extracted filter/query `if ($x == $klen)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `{asdqwdfasfdawfefqwdqwdadwqadawd}`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
