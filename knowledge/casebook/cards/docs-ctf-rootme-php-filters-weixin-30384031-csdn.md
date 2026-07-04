# CTF-rootme 题解之PHP filters_weixin_30384031的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `CTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF-rootme-题解之PHP-filters_weixin_30384031的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF-rootme-%E9%A2%98%E8%A7%A3%E4%B9%8BPHP-filters_weixin_30384031%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF-rootme-题解之PHP-filters_weixin_30384031的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, disk-image challenges.

## Input Signals

- Artifacts: binary, ciphertext, disk-image, web-app
- Tools: ida, netcat
- Techniques: classical-crypto, command-injection, encoding-analysis, file-inclusion, http-analysis, reverse-engineering, timeline-analysis, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF-rootme 题解之PHP filters_weixin_30384031的博客-CSDN博客

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use ida, netcat with the extracted filter/query `if ($f == "index.php" || $f == "ch12.php"){` and inspect the matching evidence.
- Tools: ida, netcat
- Filters or commands:
  - `if ($f == "index.php" || $f == "ch12.php"){`
  - `PD9waHAKCiR1c2VybmFtZT0iYWRtaW4iOwokcGFzc3dvcmQ9IkRBUHQ5RDJta3kwQVBBRiI7Cgo/Pg==`
  - `[ BlackArch Downloads ]# echo -n 'PD9waHAKCiR1c2VybmFtZT0iYWRtaW4iOwokcGFzc3dvcmQ9IkRBUHQ5RDJta3kwQVBBRiI7Cgo/Pg==' |base64 -d`
  - `| 名称 | 描述 | 备注 |`
  - `| --- | :-- | :-- |`
  - `| resource=<要过滤的数据流> | 指定了你要筛选过滤的数据流。 | 必选 |`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use ida, netcat with the extracted filter/query `if ($f == "index.php" || $f == "ch12.php"){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `test.php`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
