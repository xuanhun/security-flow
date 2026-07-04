# I春秋CTF训练营web题解（一）_Super_Yiang的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `I春秋CTF训练营web题解（一）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/I春秋CTF训练营web题解（一）_Super_Yiang的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/I%E6%98%A5%E7%A7%8BCTF%E8%AE%AD%E7%BB%83%E8%90%A5web%E9%A2%98%E8%A7%A3%EF%BC%88%E4%B8%80%EF%BC%89_Super_Yiang%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/I春秋CTF训练营web题解（一）_Super_Yiang的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: netcat
- Techniques: classical-crypto, command-injection, encoding-analysis, file-inclusion, file-upload, http-analysis, sql-injection, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `28`
- `docs/img/d370df425435c7105a965926543f51ef.png`
- `docs/img/e8ae261d2280158b218b2d409c1feb8f.png`
- `docs/img/8314ccb4ce5660927af209e9b07c56a4.png`
- `docs/img/8507eee28ed63dfd8563c51ba0ec0367.png`
- `docs/img/615670d1518ee1f0fd484427d8ad1373.png`
- `docs/img/fa648ffe4cf7698740babc80a22e6e6e.png`
- `docs/img/c5d84bc69b83dd149e43c774be0f38c8.png`
- `docs/img/ba67db4882503b90053548306dfae965.png`
- `docs/img/249dfccbc2bf7cc2919ba4f74f66fd40.png`
- `docs/img/d4f175829339f1e31d04fb24eb0b0be5.png`
- `docs/img/d93b6cbc384c6413d5a2288b16fa14d9.png`
- `docs/img/efc9f06276ad211082fb414d36e66ccc.png`
- ... and `16` more

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

### Step 2: I春秋CTF训练营web题解（一）_Super_Yiang的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/Super_Yiang/article/details/82391768](https://blog.csdn.net/Super_Yiang/article/details/82391768)`

### Step 3: （1）include

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `==hint：没错！就是文件包含漏洞.==` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `==hint：没错！就是文件包含漏洞.==`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `==hint：没错！就是文件包含漏洞.==` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `d370df425435c7105a965926543f51ef`

### Step 4: （2）SQL

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat with the extracted filter/query `==hint：出题人就告诉你这个是个注入，有种别走！==` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `==hint：出题人就告诉你这个是个注入，有种别走！==`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat with the extracted filter/query `==hint：出题人就告诉你这个是个注入，有种别走！==` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c5d84bc69b83dd149e43c774be0f38c8`

### Step 5: （3）Do you know upload

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use netcat with the extracted filter/query `==hint：加油吧，少年。==` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `==hint：加油吧，少年。==`
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use netcat with the extracted filter/query `==hint：加油吧，少年。==` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `efc9f06276ad211082fb414d36e66ccc`

### Step 6: （4）broken

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat with the extracted filter/query `==hint：you got a file,but…==` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `==hint：you got a file,but…==`
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat with the extracted filter/query `==hint：you got a file,but…==` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6dea1e4286a200905d7af32c464904b6`

### Step 7: （5）who are you?

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `==hint：我是谁，我在哪，我要做什么？==` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `==hint：我是谁，我在哪，我要做什么？==`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `==hint：我是谁，我在哪，我要做什么？==` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `197be04b6e3c481210917d13ac74a6c4`

### Step 8: （6）Login

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat with the extracted filter/query `==hint：加油，我看好你==` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `==hint：加油，我看好你==`
  - `if($login['user'] === 'ichunqiu')`
  - `}else if($row['pass'] !== $login['pass']){`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat with the extracted filter/query `==hint：加油，我看好你==` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `603bcc5de71132eaac3c8754ab6b7d1e`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
