# BUUCTF__[极客大挑战 2019]PHP_题解_风过江南乱的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `BUUCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF__[极客大挑战-2019]PHP_题解_风过江南乱的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF__%5B%E6%9E%81%E5%AE%A2%E5%A4%A7%E6%8C%91%E6%88%98-2019%5DPHP_%E9%A2%98%E8%A7%A3_%E9%A3%8E%E8%BF%87%E6%B1%9F%E5%8D%97%E4%B9%B1%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF__[极客大挑战-2019]PHP_题解_风过江南乱的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: detect-it-easy, netcat
- Techniques: classical-crypto, deserialization, file-inclusion, php-tricks, waf-bypass

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `7`
- `docs/img/27a735884ed0f8c0df6413f958e3b6c1.png`
- `docs/img/93ded62907058d4cac490a2f19a5be81.png`
- `docs/img/a6ad55ef50c9eae4cf7bfa1d5cb4e314.png`
- `docs/img/74edbdfb77034d5f562ae2dc9b6d6b1b.png`
- `docs/img/33f3acfb3b5ada089287ea2c83fb4aab.png`
- `docs/img/3031e84da11563dc7362c8bb5846d945.png`
- `docs/img/3417bbcae46c1b241637cf1f47b3cab5.png`

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

### Step 2: BUUCTF__[极客大挑战 2019]PHP_题解_风过江南乱的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/TM_1024/article/details/106627210](https://blog.csdn.net/TM_1024/article/details/106627210)`

### Step 3: 前言

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* 期末考试真的烦，得冷静冷静。`

### Step 4: 源码泄露

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
- Result: `27a735884ed0f8c0df6413f958e3b6c1`

### Step 5: 魔术方法 __wakeup()

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `首先看如何得flag，一看就很明显了，需要反序列化后满足 `password = 100` 和`username === 'admin'`` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `首先看如何得flag，一看就很明显了，需要反序列化后满足 `password = 100` 和`username === 'admin'``
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use detect-it-easy, netcat with the extracted filter/query `首先看如何得flag，一看就很明显了，需要反序列化后满足 `password = 100` 和`username === 'admin'`` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `33f3acfb3b5ada089287ea2c83fb4aab`

### Step 6: public 、public、protected

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use detect-it-easy, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use detect-it-easy, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `* 到这里就明白了`

### Step 7: 解题

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3031e84da11563dc7362c8bb5846d945`

### Step 8: 最后

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use detect-it-easy, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use detect-it-easy, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* 最后欢迎来访[个人博客](http://ctf-web.zm996.cloud/)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
