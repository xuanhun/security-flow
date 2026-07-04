# CTF学习笔记——[极客大挑战 2019]PHP_Obs_cure的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `CTF学习笔记——[极客大挑战 2019]PHP`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF学习笔记——[极客大挑战-2019]PHP_Obs_cure的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0%E2%80%94%E2%80%94%5B%E6%9E%81%E5%AE%A2%E5%A4%A7%E6%8C%91%E6%88%98-2019%5DPHP_Obs_cure%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF学习笔记——[极客大挑战-2019]PHP_Obs_cure的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: detect-it-easy, netcat
- Techniques: deserialization, file-inclusion, php-tricks, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `9`
- `docs/img/d2a42c05c6bbe70c415ace0bfe40b153.png`
- `docs/img/cc355a69ead393975546fb814a8ddca7.png`
- `docs/img/bf8f17c0e24e6eb0349f7bd800b54927.png`
- `docs/img/3f4b74ca0311c42a754e9cac0f25ecc3.png`
- `docs/img/8d5e15853ecf6d76df76e4a514d9e654.png`
- `docs/img/cf9915d3332d94358e2b93f252add361.png`
- `docs/img/7181a79d986e84bc5c5bd90611d21222.png`
- `docs/img/ed4b77a37205fb18ddfd751f74fa8205.png`
- `docs/img/d9f33fa8a2166d04f90b6e1b18ea2a2c.png`

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

### Step 2: CTF学习笔记——[极客大挑战 2019]PHP_Obs_cure的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/obs_cure/article/details/109404404](https://blog.csdn.net/obs_cure/article/details/109404404)`

### Step 3: 题目

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `d2a42c05c6bbe70c415ace0bfe40b153`

### Step 4: 解题步骤

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
- Result: `cc355a69ead393975546fb814a8ddca7`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
