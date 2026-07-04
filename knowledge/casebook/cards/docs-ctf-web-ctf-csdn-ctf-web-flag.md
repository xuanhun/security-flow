# 记一次院赛CTF的WEB题（入门级别）_CTF小白的博客-CSDN博客_ctf web解题 找flag

## Case Metadata

- Category: `Web`
- Platform: `记一次院赛CTF的WEB题（入门级别）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/记一次院赛CTF的WEB题（入门级别）_CTF小白的博客-CSDN博客_ctf-web解题-找flag.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E8%AE%B0%E4%B8%80%E6%AC%A1%E9%99%A2%E8%B5%9BCTF%E7%9A%84WEB%E9%A2%98%EF%BC%88%E5%85%A5%E9%97%A8%E7%BA%A7%E5%88%AB%EF%BC%89_CTF%E5%B0%8F%E7%99%BD%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctf-web%E8%A7%A3%E9%A2%98-%E6%89%BEflag.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/记一次院赛CTF的WEB题（入门级别）_CTF小白的博客-CSDN博客_ctf-web解题-找flag.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: netcat, sqlmap
- Techniques: classical-crypto, command-injection, crypto-analysis, encoding-analysis, http-analysis, php-tricks, ssti, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `36`
- `docs/img/65c8306b419751acbf4f563728433bec.png`
- `docs/img/cc7655deee398491d56fa9911b1ecc2c.png`
- `docs/img/3630707999b6ff7ce164f171f6a4ed08.png`
- `docs/img/e0204eada5b5c08af48c685e61d472df.png`
- `docs/img/4e03a421460f6d7a2e9be8a17b107cdd.png`
- `docs/img/a6ca10b927d9c625cc83bf12b5cba399.png`
- `docs/img/6c36ad78ed614eba516080cd330652f5.png`
- `docs/img/7f039d3a56dc9dade07d32bea1cdd21c.png`
- `docs/img/d63ab39a841054d0884a6ae568c6d69a.png`
- `docs/img/e43ce82ecf82e20c1554d917595da59d.png`
- `docs/img/1670c6abf8a6398c5db0f61691e8ad41.png`
- `docs/img/462beaf732e2f8f37b10f35ceb1bd39f.png`
- ... and `24` more

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 记一次院赛CTF的WEB题（入门级别）_CTF小白的博客-CSDN博客_ctf web解题 找flag

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这次院赛的题目比较基础，适合给刚入门CTF的小白提供一个大致CTF解题思路。（主要因为本人小白，表示能学到不少东西。）`

### Step 3: 签到一

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `题目中直接给了flag，提交就可以了。`

### Step 4: 签到二

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `65c8306b419751acbf4f563728433bec`

### Step 5: 口算小天才

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, sqlmap to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, sqlmap to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `3630707999b6ff7ce164f171f6a4ed08`

### Step 6: easy php

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, sqlmap with the extracted filter/query `这边代码审计一下，首先页面get到a、b、c三个参数，然后把a和b经过的md5后的保存下来，这题输出flag的条件分别是，1、a和b存在 2、a！=b，且a的md5和b的md5要相等 3、c<9999999||(String)$c>0这个结果要是false。` and inspect the matching evidence.
- Tools: netcat, sqlmap
- Filters or commands:
  - `这边代码审计一下，首先页面get到a、b、c三个参数，然后把a和b经过的md5后的保存下来，这题输出flag的条件分别是，1、a和b存在 2、a！=b，且a的md5和b的md5要相等 3、c<9999999||(String)$c>0这个结果要是false。`
  - `md5（）这个函数可以去百度一下，如果我们传入的a和b是数组的话，他们md5（）后的返回值会是false，利用false==false可以满足条件2`
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, sqlmap with the extracted filter/query `这边代码审计一下，首先页面get到a、b、c三个参数，然后把a和b经过的md5后的保存下来，这题输出flag的条件分别是，1、a和b存在 2、a！=b，且a的md5和b的md5要相等 3、c<9999999||(String)$c>0这个结果要是false。` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4e03a421460f6d7a2e9be8a17b107cdd`

### Step 7: 录取查询

- Route type: `sqlmap-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: sqlmap
- Reasoning chain:
  - Recognize the section as sqlmap-driven evidence lookup.
  - Use sqlmap to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `e43ce82ecf82e20c1554d917595da59d`

### Step 8: 我爱python

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `d74cc07595c321338908fd94c9c73bf3`

### Step 9: Spring

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `87e2db426359f0df5a24557d190b2f3d`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
