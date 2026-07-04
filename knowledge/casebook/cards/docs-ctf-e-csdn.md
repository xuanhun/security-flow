# 南邮一道ctf题目关于e的解释_软柿子捏捏的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `南邮一道ctf题目关于e的解释`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/南邮一道ctf题目关于e的解释_软柿子捏捏的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E5%8D%97%E9%82%AE%E4%B8%80%E9%81%93ctf%E9%A2%98%E7%9B%AE%E5%85%B3%E4%BA%8Ee%E7%9A%84%E8%A7%A3%E9%87%8A_%E8%BD%AF%E6%9F%BF%E5%AD%90%E6%8D%8F%E6%8D%8F%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/南邮一道ctf题目关于e的解释_软柿子捏捏的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: netcat
- Techniques: http-analysis, php-tricks, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

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

### Step 2: 南邮一道ctf题目关于e的解释_软柿子捏捏的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat with the extracted filter/query `if ($a != 'QNKCDZO' && $md51 == $md52) {` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if ($a != 'QNKCDZO' && $md51 == $md52) {`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat with the extracted filter/query `if ($a != 'QNKCDZO' && $md51 == $md52) {` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `?>`

### Step 3: md5 collision

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat with the extracted filter/query `md5('s878926199a')==md5('s155964671a') //就是True` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `md5('s878926199a')==md5('s155964671a') //就是True`
  - `php关于==号是这样处理的，如果一边是整型，另一边也需要是整型。`
  - `1e1 == 1e2 这个结果是对是错？`
  - `所以1e1 == 1e2这是false，但是`
  - `100 == 1e2 这是true，为什么1e2先转为整型，是100`
  - `var_dump(0 == "a"); // 0 == 0 -> true var_dump("1" == "01"); // 1 == 1 -> true var_dump("10" == "1e1"); // 10 == 10 -> true var_dump(100 == "1e2"); // 100 == 100 -> true switch ("a") {`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat with the extracted filter/query `md5('s878926199a')==md5('s155964671a') //就是True` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0e545993274517709034328855841020`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
