# [NUSTCTF 2022 新生赛]Translate

## Case Metadata

- Category: `Web`
- Platform: `NUSTCTF 2022 新生赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/NUSTCTF2022新生赛_Translate.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/NUSTCTF2022%E6%96%B0%E7%94%9F%E8%B5%9B_Translate.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/NUSTCTF2022新生赛_Translate.md`
- Challenge URL: `https://www.nssctf.cn/problem/3151`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: Yakit, sqlmap, mysql, adminer, netcat
- Techniques: classical-crypto, command-injection, encoding-analysis, file-inclusion, http-analysis, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `3`
- `web/images/2022-NUSTCTF-Translate-yakit-fuzz-php-filter.png`
- `web/images/2022-NUSTCTF-Translate-yakit-pattern-match-config.png`
- `web/images/2022-NUSTCTF-Translate-yakit-pattern-match.png`

## Solve Thinking

### Step 1: 第一轮

- Route type: `Yakit-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use Yakit, sqlmap, mysql, adminer to collect the smallest evidence slice that answers the goal.
- Tools: Yakit, sqlmap, mysql, adminer, netcat
- Reasoning chain:
  - Recognize the section as Yakit-driven evidence lookup.
  - Use Yakit, sqlmap, mysql, adminer to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `**题目关键信息列表**：`

### Step 2: 想到什么解题思路

- Route type: `Yakit-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use Yakit, sqlmap, mysql, adminer to collect the smallest evidence slice that answers the goal.
- Tools: Yakit, sqlmap, mysql, adminer, netcat
- Reasoning chain:
  - Recognize the section as Yakit-driven evidence lookup.
  - Use Yakit, sqlmap, mysql, adminer to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 3: 尝试过程和结果记录

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat, yakit to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat, yakit
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat, yakit to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `test.php`

### Step 4: 怀疑过滤了 base64-encode 关键词，直接尝试

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `base64-encode`

### Step 5: 输出：让我康康是谁!

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use Yakit, sqlmap, mysql, adminer to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: Yakit, sqlmap, mysql, adminer, netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use Yakit, sqlmap, mysql, adminer to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag.php`

### Step 6: 输出：让我康康是谁!

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use yakit with the extracted filter/query `if ($row['password'] === $password) { // 熟悉的 quine 注入又来了` and inspect the matching evidence.
- Tools: yakit
- Filters or commands:
  - `if ($row['password'] === $password) { // 熟悉的 quine 注入又来了`
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use yakit with the extracted filter/query `if ($row['password'] === $password) { // 熟悉的 quine 注入又来了` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag.php`

### Step 7: 本地工具环境配置

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat, yakit to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat, yakit
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat, yakit to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag.php`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
