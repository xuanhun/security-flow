# ctf逆向解题——Bomb二进制炸弹_FunkyPants的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `ctf逆向解题——Bomb二进制炸弹`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/ctf逆向解题——Bomb二进制炸弹_FunkyPants的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/ctf%E9%80%86%E5%90%91%E8%A7%A3%E9%A2%98%E2%80%94%E2%80%94Bomb%E4%BA%8C%E8%BF%9B%E5%88%B6%E7%82%B8%E5%BC%B9_FunkyPants%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/ctf逆向解题——Bomb二进制炸弹_FunkyPants的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: netcat, strings
- Techniques: malware-static, stego-extraction

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `18`
- `docs/img/f585743c38ed3a43b2e50278a07445d8.png`
- `docs/img/319aa840e3bcf4ef7d78e766d72ec9aa.png`
- `docs/img/c859156e8161f289f68a9eb9a75b352b.png`
- `docs/img/8083c11839670499b21ea67f126e0d98.png`
- `docs/img/887ad9273a7504bd2fe87b266adb4ec7.png`
- `docs/img/daccea24fffa4911bee7ceb215e7cb2e.png`
- `docs/img/8b5c8503430c4044f024bf1e8b8f1d19.png`
- `docs/img/cde47dd08db35a0d2e1c413a9d10b9e3.png`
- `docs/img/86ec6d9d815328dfe5ff542df78a1fdf.png`
- `docs/img/49b93035d3099bbcb26f5a7290d7d73d.png`
- `docs/img/6725bac7a3146233a524ca841755311b.png`
- `docs/img/4f1555361af5e2557ea1db0663b921f6.png`
- ... and `6` more

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, strings to collect the smallest evidence slice that answers the goal.
- Tools: netcat, strings
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: ctf逆向解题——Bomb二进制炸弹_FunkyPants的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, strings
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/FunkyPants/article/details/96846945](https://blog.csdn.net/FunkyPants/article/details/96846945)`

### Step 3: Phase1

- Route type: `strings-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use strings to collect the smallest evidence slice that answers the goal.
- Tools: strings
- Reasoning chain:
  - Recognize the section as strings-driven evidence lookup.
  - Use strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `f585743c38ed3a43b2e50278a07445d8`

### Step 4: Phase2

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, strings to collect the smallest evidence slice that answers the goal.
- Tools: netcat, strings
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `c859156e8161f289f68a9eb9a75b352b`

### Step 5: Phase3

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, strings to collect the smallest evidence slice that answers the goal.
- Tools: netcat, strings
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `887ad9273a7504bd2fe87b266adb4ec7`

### Step 6: Phase4

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat with the extracted filter/query `如果要使得返回值t为0，需要满足k==x，通过带入x、y、z计算可以得到k=x=7，即第一个数为7，第二个数为0.` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `如果要使得返回值t为0，需要满足k==x，通过带入x、y、z计算可以得到k=x=7，即第一个数为7，第二个数为0.`
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat with the extracted filter/query `如果要使得返回值t为0，需要满足k==x，通过带入x、y、z计算可以得到k=x=7，即第一个数为7，第二个数为0.` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `cde47dd08db35a0d2e1c413a9d10b9e3`

### Step 7: Phase5

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, strings to collect the smallest evidence slice that answers the goal.
- Tools: netcat, strings
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, strings to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6725bac7a3146233a524ca841755311b`

### Step 8: Phase 6

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, strings to collect the smallest evidence slice that answers the goal.
- Tools: netcat, strings
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Phases接收6个数字输入，使用的函数同样是read_six-numbers。`

### Step 9: Part 1

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, strings to collect the smallest evidence slice that answers the goal.
- Tools: netcat, strings
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `c11ca1a224068afedd1c5f15f42a64f8`

### Step 10: Part 2

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, strings to collect the smallest evidence slice that answers the goal.
- Tools: netcat, strings
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2a41098958500950d2f5171761640e6d`

### Step 11: Part3

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, strings to collect the smallest evidence slice that answers the goal.
- Tools: netcat, strings
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `e909029df0cd5752ae59dcd4eebfa0d7`

### Step 12: Part4

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, strings to collect the smallest evidence slice that answers the goal.
- Tools: netcat, strings
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `cc57de617066eed4fe472c0d685710da`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
