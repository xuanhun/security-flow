# 西邮ctf2020 web之文件包含解析_落雪wink的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `西邮ctf2020 web之文件包含解析`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/西邮ctf2020-web之文件包含解析_落雪wink的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E8%A5%BF%E9%82%AEctf2020-web%E4%B9%8B%E6%96%87%E4%BB%B6%E5%8C%85%E5%90%AB%E8%A7%A3%E6%9E%90_%E8%90%BD%E9%9B%AAwink%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/西邮ctf2020-web之文件包含解析_落雪wink的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, encoding-analysis, file-inclusion, http-analysis, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `15`
- `docs/img/8200724fd5787d9c83a65ec9a6f93911.png`
- `docs/img/189e57e7064f59606258a3299ccd6b85.png`
- `docs/img/8b4eed8765a6e0c2b5f86aa3022d37ae.png`
- `docs/img/ab2b45f40af5b02cbfd214cf470b51de.png`
- `docs/img/6f482dbc1763c4fa8c15b5f67d31c6a4.png`
- `docs/img/5de52c1b41d4dec9133d70a69e764858.png`
- `docs/img/7f34699f42769ac3671604376ad8b5c8.png`
- `docs/img/92aea7d3c227d5bd6da2a551f3226cc5.png`
- `docs/img/576655f5984d31b391b919f98d37ed16.png`
- `docs/img/89de6324fbf6954c4fedf8423cca59cc.png`
- `docs/img/457d4ad64f75df98e7d0cbab61c67148.png`
- `docs/img/03a925b26add8e043a5e4115de58e35b.png`
- ... and `3` more

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

### Step 2: 西邮ctf2020 web之文件包含解析_落雪wink的博客-CSDN博客

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_44145452/article/details/109498277](https://blog.csdn.net/weixin_44145452/article/details/109498277)`

### Step 3: 比赛地址：`http://39.97.182.97/`

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8200724fd5787d9c83a65ec9a6f93911`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
