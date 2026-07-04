# 【vishwaCTF】web题解wp_Sunlight_316的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `【vishwaCTF】web题解wp`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【vishwaCTF】web题解wp_Sunlight_316的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90vishwaCTF%E3%80%91web%E9%A2%98%E8%A7%A3wp_Sunlight_316%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【vishwaCTF】web题解wp_Sunlight_316的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: hashcat, netcat, radare2
- Techniques: command-injection, crypto-analysis, deserialization, encoding-analysis, file-inclusion, http-analysis, jwt-analysis, password-cracking, php-tricks, sql-injection, ssti, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `6`
- `docs/img/ec8a68025fa78bbc68fc15cb0724931e.png`
- `docs/img/e546b9986d7d166b36277b75c9a9bc8e.png`
- `docs/img/b3d28164249653572ce0b953e073d834.png`
- `docs/img/09ad0ee34d838118d884c10b9bef3af5.png`
- `docs/img/347be886112b247b4430810fe86a55a6.png`
- `docs/img/83a1a55307dc4992ff7a3654fa8d8f05.png`

## Solve Thinking

### Step 1: Document

- Route type: `hashcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use hashcat, netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: hashcat, netcat, radare2
- Reasoning chain:
  - Recognize the section as hashcat-driven evidence lookup.
  - Use hashcat, netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 【vishwaCTF】web题解wp_Sunlight_316的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use hashcat, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: hashcat, netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use hashcat, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_51614272/article/details/124128472](https://blog.csdn.net/weixin_51614272/article/details/124128472)`

### Step 3: Keep Your Secrets（jwt典例）

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use hashcat, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: hashcat, netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use hashcat, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ec8a68025fa78bbc68fc15cb0724931e`

### Step 4: Todo list（php反序列化）

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use netcat with the extracted filter/query `if(sha1($m) === $h){` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if(sha1($m) === $h){`
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use netcat with the extracted filter/query `if(sha1($m) === $h){` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `echo urlencode(serialize($todos));`

### Step 5: Hey Buddy!（SSTI）

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use hashcat, netcat, radare2 to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
- Tools: hashcat, netcat, radare2
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use hashcat, netcat, radare2 to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `使用subclasses的第99个库，这个库里有os操作，就可以获取flag`

### Step 6: My Useless Website（SQL注入）

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use hashcat, netcat, radare2 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: hashcat, netcat, radare2
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use hashcat, netcat, radare2 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ``-+` 或者 `·--`就是注释符`

### Step 7: Stock Bot（信息检索）

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `83a1a55307dc4992ff7a3654fa8d8f05`

### Step 8: Request Me FLAG（数据包请求方式）

- Route type: `hashcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use hashcat, netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: hashcat, netcat, radare2
- Reasoning chain:
  - Recognize the section as hashcat-driven evidence lookup.
  - Use hashcat, netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `以FLAG请求方式请求数据包，得到flag`

### Step 9: Strong Encryption（php代码审计）

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, radare2 with the extracted filter/query `if($j==strlen($Key)){` and inspect the matching evidence.
- Tools: netcat, radare2
- Filters or commands:
  - `if($j==strlen($Key)){`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, radare2 with the extracted filter/query `if($j==strlen($Key)){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `576e78697e65445c4a7c8033766770357c3960377460357360703a6f6982`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
