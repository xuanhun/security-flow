# CTF-web 第十一部分 实用脚本_iamsongyu的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `CTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF-web-第十一部分-实用脚本_iamsongyu的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF-web-%E7%AC%AC%E5%8D%81%E4%B8%80%E9%83%A8%E5%88%86-%E5%AE%9E%E7%94%A8%E8%84%9A%E6%9C%AC_iamsongyu%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF-web-第十一部分-实用脚本_iamsongyu的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, siem challenges.

## Input Signals

- Artifacts: binary, ciphertext, siem, web-app
- Tools: elk, netcat, radare2, z3
- Techniques: browser-forensics, classical-crypto, command-injection, crypto-analysis, encoding-analysis, http-analysis, image-analysis, php-tricks, qr-analysis, siem-query, symbolic-execution, waf-bypass, web-exploitation, xss

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Solve Thinking

### Step 1: Document

- Route type: `elk-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk, netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
- Tools: elk, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as elk-driven evidence lookup.
  - Use elk, netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF-web 第十一部分 实用脚本_iamsongyu的博客-CSDN博客

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use elk, netcat, radare2, z3 to verify the sink, context, and trigger condition before choosing the smallest executable payload.
- Tools: elk, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as xss route.
  - Use elk, netcat, radare2, z3 to verify the sink, context, and trigger condition before choosing the smallest executable payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `import requests`

### Step 3: 再次post提交 {"ichunqiu": 解码数据}

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use elk, netcat, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: elk, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use elk, netcat, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `607d622601d049a3a3e7ef03f58670e445529dac09dd4a96`

### Step 4: flag_is_here: NjY0MzY0 需要使用：进行分组

- Route type: `elk-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk, netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
- Tools: elk, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as elk-driven evidence lookup.
  - Use elk, netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `key = splitstr[1].replace('\'', '')`

### Step 5: 对后面的再次解码

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use elk, netcat, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: elk, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use elk, netcat, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `print(f.text)`

### Step 6: import base64,requests

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use elk, netcat, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: elk, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use elk, netcat, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `#`

### Step 7: print(f.text)

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: elk, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `from multiprocessing.dummy import Pool as ThreadPool`

### Step 8: 例子 substr(md5(captcha), 0, 6)=60b7ef

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `for i in range(start, end):`

### Step 9: print(md5(i)[md5start:md5length])

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Use elk, netcat, radare2, z3 with the extracted filter/query `if md5(i)[0:6] == keymd5: # 拿到加密字符串` and inspect the matching evidence.
- Tools: elk, netcat, radare2, z3
- Filters or commands:
  - `if md5(i)[0:6] == keymd5: # 拿到加密字符串`
- Reasoning chain:
  - Recognize the section as indicator enrichment.
  - Use elk, netcat, radare2, z3 with the extracted filter/query `if md5(i)[0:6] == keymd5: # 拿到加密字符串` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `import requests`

### Step 10: 本题 限制120s 爆破10次以上 变量固定前两个字符，MD5截断为固定值

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `return hashlib.md5(str(s).encode('utf-8')).hexdigest()`

### Step 11: substr(md5($value),5,4)==0)

- Route type: `elk-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use elk, netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
- Tools: elk, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as elk-driven evidence lookup.
  - Use elk, netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `return str`

### Step 12: 访问并截取新的关键字

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk, netcat, radare2, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use elk, netcat, radare2, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `return respon[0:2], len(respon), respon`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
