# 平时练习 ctf 解题报告 web类_白山茶i的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `平时练习 ctf 解题报告 web类`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/平时练习-ctf-解题报告-web类_白山茶i的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E5%B9%B3%E6%97%B6%E7%BB%83%E4%B9%A0-ctf-%E8%A7%A3%E9%A2%98%E6%8A%A5%E5%91%8A-web%E7%B1%BB_%E7%99%BD%E5%B1%B1%E8%8C%B6i%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/平时练习-ctf-解题报告-web类_白山茶i的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, encoding-analysis, http-analysis, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `33`
- `docs/img/33625031c76a10392c75d5f7b4627f96.png`
- `docs/img/84fc0a0f63518a08b9394c710d9de2f6.png`
- `docs/img/e60c7b1f93e996a13caa05d26e793a06.png`
- `docs/img/20450c3cadd062cec43b4d1f7eb5c368.png`
- `docs/img/b5fd3536e63233ff4e1eabbfee43cf58.png`
- `docs/img/5930ce0852b375a7c376ceab6578c83e.png`
- `docs/img/d6e9be9e3381b3cd97dd9620606c0d98.png`
- `docs/img/ef40f9a4192dbdd3c417eb7bfa39f268.png`
- `docs/img/7ce8b2803ef6d7162beabdb4a1c21254.png`
- `docs/img/e79a64a8e306bf2bdaa2568b06de5f78.png`
- `docs/img/50f11dfd0bd473cdb6817363dd5b4a2b.png`
- `docs/img/23ae141c2a8bf02bb7b35980b12c395d.png`
- ... and `21` more

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

### Step 2: 平时练习 ctf 解题报告 web类_白山茶i的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_30435981/article/details/81219313](https://blog.csdn.net/qq_30435981/article/details/81219313)`

### Step 3: **1.读文件**

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `length==16^be0f23233ace98aa$c7be9)` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `length==16^be0f23233ace98aa$c7be9)`
  - `/)!=null=[" write(s[o%4]button`
  - `if(e.length==16)if(e.match(/^be0f23/)!=null)`
  - `if(e.match(/233ac/)!=null)`
  - `if(e.match(/e98aa$/)!=null)`
  - `if(e.match(/c7be9/)!=null)`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `length==16^be0f23233ace98aa$c7be9)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `33625031c76a10392c75d5f7b4627f96`

### Step 4: urldecode

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `42a0ffa74921d2d6af3a0dabbd21357e`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
