# ctf刷题日记_AndrewMe8211的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `ctf刷题日记`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/ctf刷题日记_AndrewMe8211的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/ctf%E5%88%B7%E9%A2%98%E6%97%A5%E8%AE%B0_AndrewMe8211%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/ctf刷题日记_AndrewMe8211的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: netcat, stegsolve
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, http-analysis, misc-analysis, php-tricks, qr-analysis, service-enumeration, web-exploitation

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, stegsolve to collect the smallest evidence slice that answers the goal.
- Tools: netcat, stegsolve
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, stegsolve to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: ctf刷题日记_AndrewMe8211的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, stegsolve to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, stegsolve
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, stegsolve to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_43907802/article/details/120589441](https://blog.csdn.net/weixin_43907802/article/details/120589441)`

### Step 3: BUUCTF MD5

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, stegsolve to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, stegsolve
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, stegsolve to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `这里的这个网站就是一个使用暴力破解来解码的网站`

### Step 4: BUUCTF 丢失的MD5 1

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406`

### Step 5: BUUCTF 一眼就解密

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, stegsolve to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, stegsolve
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, stegsolve to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://www.cnblogs.com/luguo3000/p/3940197.html`

### Step 6: BUUCTF Url编码 1

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, stegsolve to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, stegsolve
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, stegsolve to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `url是什么：https://blog.csdn.net/houqicun/article/details/78296886`

### Step 7: BUUCTF 看我回旋踢

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, stegsolve to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, stegsolve
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, stegsolve to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `一看就很像凯撒密码，试了一下果然是`

### Step 8: BUUCTF 摩丝 1

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, stegsolve to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, stegsolve
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, stegsolve to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `文件下载下来看发现是摩尔斯电码，解密后套上flag{}得到答案`

### Step 9: BUUCTF password

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use netcat, stegsolve to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: netcat, stegsolve
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use netcat, stegsolve to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `离谱，居然还有这种题。。。姓名首字母+生日=flag`

### Step 10: BUUCTF 变异凯撒

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, stegsolve to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, stegsolve
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, stegsolve to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `这题正确的思路应该是先去找标识符，也就是先假设密码里面的前四个字母对应的是flag，这样的话就可以去找规律。从ascii的角度出发，那么不难知道，这个密码每一位的位移都不一样，第一位在ascii里面移动了5，第二位是6，第三位是7，以此类推，就得到flag`

### Step 11: BUUCTF Quoted-printable

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, stegsolve to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, stegsolve
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, stegsolve to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `quoted-printable是什么:http://blog.chacuo.net/494.html`

### Step 12: BUUCTF rabbit

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `至于rabbit是个啥。。。不是很懂`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
