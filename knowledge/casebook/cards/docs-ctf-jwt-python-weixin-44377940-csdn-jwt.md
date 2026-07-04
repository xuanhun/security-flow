# 一道CTF题看JWT和python反序列化_weixin_44377940的博客-CSDN博客_jwt反序列化

## Case Metadata

- Category: `Web`
- Platform: `一道CTF题看JWT和python反序列化`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/一道CTF题看JWT和python反序列化_weixin_44377940的博客-CSDN博客_jwt反序列化.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E4%B8%80%E9%81%93CTF%E9%A2%98%E7%9C%8BJWT%E5%92%8Cpython%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96_weixin_44377940%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_jwt%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/一道CTF题看JWT和python反序列化_weixin_44377940的博客-CSDN博客_jwt反序列化.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, disk-image challenges.

## Input Signals

- Artifacts: binary, ciphertext, disk-image, web-app
- Tools: netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, deserialization, encoding-analysis, http-analysis, integer-overflow, jwt-analysis, php-tricks, ret2libc, timeline-analysis, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `12`
- `docs/img/befb4f0aa503bb516ab85ac90ce37c2e.png`
- `docs/img/afd86ea931d718a3fa4d8cfdce2eb6cc.png`
- `docs/img/c858a739cb18aec7902e9a421ab1c8d1.png`
- `docs/img/3bcadaf8a54ac1096b92ffe31272c373.png`
- `docs/img/5b94918d4a42c41daa63854917255dd9.png`
- `docs/img/894573862a3ae54119e15897c8e7c9dd.png`
- `docs/img/84f3f0123437f0b33c93903a8c161703.png`
- `docs/img/4d20119bb619fe2264542350aa570519.png`
- `docs/img/e07eb88e71d3cb6a4dbd0672fffdfac0.png`
- `docs/img/79b2235488f034b07aaa69387a2a4dca.png`
- `docs/img/7da80ce3bbc225693e4e9b0026319e8b.png`
- `docs/img/d221ca2d36c6beaeecd838257c620119.png`

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 一道CTF题看JWT和python反序列化_weixin_44377940的博客-CSDN博客_jwt反序列化

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_44377940/article/details/106863514](https://blog.csdn.net/weixin_44377940/article/details/106863514)`

### Step 3: 题目

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `题为[CISCN2019 华北赛区 Day1 Web2]ikun`

### Step 4: 题解

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `befb4f0aa503bb516ab85ac90ce37c2e`

### Step 5: JWT

- Route type: `jwt trust-boundary abuse`
- Why: JWT cases hinge on understanding what the server actually trusts: signature, claim, header, or backend lookup.
- Probe: Use netcat to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as jwt trust-boundary abuse.
  - Use netcat to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `7da80ce3bbc225693e4e9b0026319e8b`

### Step 6: Python 序列化与反序列化

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `pickle可以手撸，也可以用`__reduce__`方法构造`

### Step 7: 手撸pickle

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `也就是说这个指令等同于`__import__('os').system(*('ls',))``

### Step 8: __reduce__构造

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `这里的`protocol=0`又涉及到另一个小知识了：pickling 的协议`

### Step 9: pickling 的协议

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `想更加了解python的魔术方法可以看这个：[python魔术方法指南](https://pyzh.readthedocs.io/en/latest/python-magic-methods-guide.html)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
