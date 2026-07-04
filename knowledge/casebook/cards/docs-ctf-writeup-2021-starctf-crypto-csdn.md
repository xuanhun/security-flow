# 【CTF WriteUp】2021 starCTF部分Crypto题解_零食商人的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `【CTF WriteUp】2021 starCTF部分Crypto题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【CTF-WriteUp】2021-starCTF部分Crypto题解_零食商人的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90CTF-WriteUp%E3%80%912021-starCTF%E9%83%A8%E5%88%86Crypto%E9%A2%98%E8%A7%A3_%E9%9B%B6%E9%A3%9F%E5%95%86%E4%BA%BA%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【CTF-WriteUp】2021-starCTF部分Crypto题解_零食商人的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: netcat, pwntools
- Techniques: binary-exploitation, crypto-analysis, encoding-analysis, http-analysis, web-exploitation

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `2`
- `docs/img/ecde9c826f6fe7c9df57d52a021be930.png`
- `docs/img/4c5c4b639aa28c49ecce66a2f3429d5c.png`

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 【CTF WriteUp】2021 starCTF部分Crypto题解_零食商人的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `（打比赛感想：大佬真TM多。。。）`

### Step 3: 题目

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `print flag`

### Step 4: 解答

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `题目出错了，给出key让猜key，输入mask=0保持key不变就可以了。`

### Step 5: 题目

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `print flag`

### Step 6: 解答

- Route type: `pwntools-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use pwntools to collect the smallest evidence slice that answers the goal.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as pwntools-driven evidence lookup.
  - Use pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `52.163.228.53`

### Step 7: 题目

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, pwntools with the extracted filter/query `assert (special > (ord("*")*100) and gcd(special,(p-1)*(q-1))!=1 )` and inspect the matching evidence.
- Tools: netcat, pwntools
- Filters or commands:
  - `assert (special > (ord("*")*100) and gcd(special,(p-1)*(q-1))!=1 )`
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, pwntools with the extracted filter/query `assert (special > (ord("*")*100) and gcd(special,(p-1)*(q-1))!=1 )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `out.sage`

### Step 8: 解答

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `assert(pow(mp2, e, p) == cp)` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `assert(pow(mp2, e, p) == cp)`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `assert(pow(mp2, e, p) == cp)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `print "Start time: 0.0"`

### Step 9: find all roots for pow(x, e, p)=1 and pow(x, e, q)=1

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use netcat, pwntools to align timestamps and identify the event that satisfies the question.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as timeline reconstruction.
  - Use netcat, pwntools to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `q_proot = findAllPRoot(q, e)`

### Step 10: find all roots for pow(x, e, p)=cp and pow(x, e, q)=cq

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use netcat, pwntools to align timestamps and identify the event that satisfies the question.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as timeline reconstruction.
  - Use netcat, pwntools to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `return False`

### Step 11: check 4919*4919 possibles for answer

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use netcat, pwntools to align timestamps and identify the event that satisfies the question.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as timeline reconstruction.
  - Use netcat, pwntools to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ecde9c826f6fe7c9df57d52a021be930`

### Step 12: 题目

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use netcat with the extracted filter/query `assert len(flag)==15` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `assert len(flag)==15`
- Reasoning chain:
  - Recognize the section as timeline reconstruction.
  - Use netcat with the extracted filter/query `assert len(flag)==15` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `print "done:",ct`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
