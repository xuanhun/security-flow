# 31C3 CTF web关writeup_weixin_34019929的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `31C3 CTF web关writeup`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/31C3-CTF-web关writeup_weixin_34019929的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/31C3-CTF-web%E5%85%B3writeup_weixin_34019929%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/31C3-CTF-web关writeup_weixin_34019929的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, ids challenges.

## Input Signals

- Artifacts: binary, ciphertext, ids, linux-logs, web-app
- Tools: detect-it-easy, netcat
- Techniques: binary-exploitation, classical-crypto, command-injection, crypto-analysis, dns-analysis, encoding-analysis, file-inclusion, http-analysis, service-enumeration, sql-injection, waf-bypass, web-exploitation, xss

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

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

### Step 2: 31C3 CTF web关writeup_weixin_34019929的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> ∑-TEAM · 2015/01/07 9:47`

### Step 3: 0x00 背景

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `英文的题解可以看这里https://github.com/ctfs/write-ups/tree/master/31c3-ctf-2014/web`

### Step 4: 0x01 pCRAPp

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `这里也利用了相同的原理，array_search 会使用'ctf'和array中的每个值作比较，而且intval('ctf')==0.` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `这里也利用了相同的原理，array_search 会使用'ctf'和array中的每个值作比较，而且intval('ctf')==0.`
  - `if(count($a["a2"])!==5 OR !is_array($a["a2"][0])) die("nope");`
  - `$pos===false?die("nope"):NULL;`
  - `$val==="ctf"?die("nope"):NULL;`
  - `if($var = $b === NULL){`
  - `($var===true)?$v3=1:NULL;`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use detect-it-easy, netcat with the extracted filter/query `这里也利用了相同的原理，array_search 会使用'ctf'和array中的每个值作比较，而且intval('ctf')==0.` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `188.40.18.69`

### Step 5: 0x02 Page Builder

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use detect-it-easy, netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as xss route.
  - Use detect-it-easy, netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `188.40.18.76`

### Step 6: 0x03 HTTP

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat with the extracted filter/query `if (chdir(host) == -1) {` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if (chdir(host) == -1) {`
  - `if (fd == -1) {`
  - `if (fstat(fd, &stat) == -1) {`
  - `if (file == NULL) {`
  - `line_reader.collect do |line|`
  - `end.compact.inject({}) { |h, x| h[x[0]]= x[1]; h }`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat with the extracted filter/query `if (chdir(host) == -1) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `x:1001:1001:31C3_b45fa9e4d5969e3c524bdcde15f84125:/home/flag:`

### Step 7: 0x04 5CHAN

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use detect-it-easy, netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use detect-it-easy, netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `188.40.18.89`

### Step 8: 0x05 Devilish

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use detect-it-easy, netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use detect-it-easy, netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `188.40.18.70`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
