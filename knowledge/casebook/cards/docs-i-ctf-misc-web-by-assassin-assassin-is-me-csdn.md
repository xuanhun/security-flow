# i春秋 百度杯”CTF比赛（二月场） Misc&&web题解 By Assassin_Assassin__is__me的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `i春秋`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/i春秋-百度杯”CTF比赛（二月场）-Misc&&web题解-By-Assassin_Assassin__is__me的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/i%E6%98%A5%E7%A7%8B-%E7%99%BE%E5%BA%A6%E6%9D%AF%E2%80%9DCTF%E6%AF%94%E8%B5%9B%EF%BC%88%E4%BA%8C%E6%9C%88%E5%9C%BA%EF%BC%89-Misc%26%26web%E9%A2%98%E8%A7%A3-By-Assassin_Assassin__is__me%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/i春秋-百度杯”CTF比赛（二月场）-Misc&&web题解-By-Assassin_Assassin__is__me的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for apk-mobile, binary, ciphertext challenges.

## Input Signals

- Artifacts: apk-mobile, binary, ciphertext, ids, web-app
- Tools: detect-it-easy, netcat, radare2
- Techniques: binary-exploitation, classical-crypto, command-injection, encoding-analysis, file-inclusion, http-analysis, misc-analysis, mobile-forensics, php-tricks, qr-analysis, ret2libc, web-exploitation, xss

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: i春秋 百度杯”CTF比赛（二月场） Misc&&web题解 By Assassin_Assassin__is__me的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `[百度杯”CTF比赛（二月场）训练赛传送门](http://www.ichunqiu.com/racing/57697)`

### Step 3: 爆破-1

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use detect-it-easy, netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use detect-it-easy, netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag.php`

### Step 4: 爆破-2

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag.php`

### Step 5: 爆破-3

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use detect-it-easy, netcat, radare2 with the extracted filter/query `if($_SESSION['whoami']==($value[0].$value[1]) && substr(md5($value),5,4)==0){` and inspect the matching evidence.
- Tools: detect-it-easy, netcat, radare2
- Filters or commands:
  - `if($_SESSION['whoami']==($value[0].$value[1]) && substr(md5($value),5,4)==0){`
  - `jq jqbnewgg`
  - `nc ncvhxdkq`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use detect-it-easy, netcat, radare2 with the extracted filter/query `if($_SESSION['whoami']==($value[0].$value[1]) && substr(md5($value),5,4)==0){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `dc600d84281e40cba349347d92660cd31c3a29f654104b35`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
