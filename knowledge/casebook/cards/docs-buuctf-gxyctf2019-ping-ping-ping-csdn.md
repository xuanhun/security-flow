# BUUCTF__[GXYCTF2019]Ping Ping Ping_题解_风过江南乱的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `BUUCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF__[GXYCTF2019]Ping-Ping-Ping_题解_风过江南乱的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF__%5BGXYCTF2019%5DPing-Ping-Ping_%E9%A2%98%E8%A7%A3_%E9%A3%8E%E8%BF%87%E6%B1%9F%E5%8D%97%E4%B9%B1%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF__[GXYCTF2019]Ping-Ping-Ping_题解_风过江南乱的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: detect-it-easy
- Techniques: classical-crypto, command-injection, crypto-analysis, encoding-analysis, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `8`
- `docs/img/77c8cee233eebaa596334c78c82ae150.png`
- `docs/img/9d9fa3d12d9e5b81e7fed111c1355f0b.png`
- `docs/img/383e3a1ba71b6169ab19af30fc440fca.png`
- `docs/img/8622f81cddb4539c128152c0bfd7e81e.png`
- `docs/img/2abd7c85c9e6a6d53c36dcaa329a193d.png`
- `docs/img/63d5eaef7be9c9d60bf0f8936ed7bd7e.png`
- `docs/img/f4fec3121d2165e4df315f9f189daef0.png`
- `docs/img/2b222d7e768f6dd9ed517a1fdfff91f7.png`

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BUUCTF__[GXYCTF2019]Ping Ping Ping_题解_风过江南乱的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/TM_1024/article/details/106890338](https://blog.csdn.net/TM_1024/article/details/106890338)`

### Step 3: 前言

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* 这题有点东西，不算太水。只是对我来说。`

### Step 4: 读题

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use detect-it-easy with the extracted filter/query `> | 表示管道，上一条命令的输出，作为下一条命令参数，如 echo ‘yes’ | wc -l` and inspect the matching evidence.
- Tools: detect-it-easy
- Filters or commands:
  - `> | 表示管道，上一条命令的输出，作为下一条命令参数，如 echo ‘yes’ | wc -l`
  - `> || 表示上一条命令执行失败后，才执行下一条命令，如 cat nofile || echo “fail”`
  - `然后尝试用`|` 回显得知 index.php 和 flag.php`
  - `|\'|\"|\\|\(|\)|\[|\]|\{|\}/", $ip, $match)){`
  - `echo preg_match("/\&|\/|\?|\*|\<|[\x{00}-\x{20}]|\>|\'|\"|\\|\(|\)|\[|\]|\{|\}/", $ip, $match);`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use detect-it-easy with the extracted filter/query `> | 表示管道，上一条命令的输出，作为下一条命令参数，如 echo ‘yes’ | wc -l` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1`

### Step 5: 方法一、变量拼接字符串

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `f4fec3121d2165e4df315f9f189daef0`

### Step 6: 方法二、sh命令来执行

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use detect-it-easy with the extracted filter/query `> echo “cat flag.php” | base64` and inspect the matching evidence.
- Tools: detect-it-easy
- Filters or commands:
  - `> echo “cat flag.php” | base64`
  - `> echo Y2F0IGZsYWcucGhwCg== | base64 -d | sh`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use detect-it-easy with the extracted filter/query `> echo “cat flag.php” | base64` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag.php`

### Step 7: 方法三、内联执行

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1`

### Step 8: 最后

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use detect-it-easy to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: detect-it-easy
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use detect-it-easy to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* 最后欢迎来访[个人博客](http://ctf-web.zm996.cloud/)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
