# BUUCTF__[ACTF2020 新生赛]BackupFile_题解_风过江南乱的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `BUUCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF__[ACTF2020-新生赛]BackupFile_题解_风过江南乱的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF__%5BACTF2020-%E6%96%B0%E7%94%9F%E8%B5%9B%5DBackupFile_%E9%A2%98%E8%A7%A3_%E9%A3%8E%E8%BF%87%E6%B1%9F%E5%8D%97%E4%B9%B1%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF__[ACTF2020-新生赛]BackupFile_题解_风过江南乱的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: netcat, radare2
- Techniques: command-injection, crypto-analysis, file-inclusion, jwt-analysis, php-tricks

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BUUCTF__[ACTF2020 新生赛]BackupFile_题解_风过江南乱的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/TM_1024/article/details/107160915](https://blog.csdn.net/TM_1024/article/details/107160915)`

### Step 3: 读题

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat, radare2 with the extracted filter/query `if($key == $str) {` and inspect the matching evidence.
- Tools: netcat, radare2
- Filters or commands:
  - `if($key == $str) {`
  - `就很简单了，get传入key，与一串开头为123的字符串比较。`==` 为弱比较，直接令`key=123`就可以。直接出flag。`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat, radare2 with the extracted filter/query `if($key == $str) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag.php`

### Step 4: 最后

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 with the extracted filter/query `还是PHP的弱类型。`==`和`===` 的差别。` and inspect the matching evidence.
- Tools: netcat, radare2
- Filters or commands:
  - `还是PHP的弱类型。`==`和`===` 的差别。`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 with the extracted filter/query `还是PHP的弱类型。`==`和`===` 的差别。` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* 最后欢迎来踩[个人博客](http://ctf-web.zm996.cloud/)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
