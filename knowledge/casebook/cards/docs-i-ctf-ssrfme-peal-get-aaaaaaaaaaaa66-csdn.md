# i春秋CTF ssrfme (peal函数中get命令漏洞)命令执行 详细题解＋原理 学习过程_AAAAAAAAAAAA66的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `i春秋CTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/i春秋CTF-ssrfme-(peal函数中get命令漏洞)命令执行-详细题解＋原理-学习过程_AAAAAAAAAAAA66的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/i%E6%98%A5%E7%A7%8BCTF-ssrfme-%28peal%E5%87%BD%E6%95%B0%E4%B8%ADget%E5%91%BD%E4%BB%A4%E6%BC%8F%E6%B4%9E%29%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C-%E8%AF%A6%E7%BB%86%E9%A2%98%E8%A7%A3%EF%BC%8B%E5%8E%9F%E7%90%86-%E5%AD%A6%E4%B9%A0%E8%BF%87%E7%A8%8B_AAAAAAAAAAAA66%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/i春秋CTF-ssrfme-(peal函数中get命令漏洞)命令执行-详细题解＋原理-学习过程_AAAAAAAAAAAA66的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: not detected
- Techniques: command-injection, php-tricks, ret2libc

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `11`
- `docs/img/fc496e7bced4cce69bae49298f936828.png`
- `docs/img/865b58b3daa18bab095a70720bea15ca.png`
- `docs/img/a5e696d4fa6a3af1101bfd5d83e0ee56.png`
- `docs/img/f80ada9d137cb38e7ffec2aa2b2928e0.png`
- `docs/img/fb4213478a378a2f4e654e112aa668cc.png`
- `docs/img/d898ebbbefb407e039da26d12065f337.png`
- `docs/img/e1f9e73cf5c0637d9233af7a3419eff9.png`
- `docs/img/6621e7a0cf8cbd8d04cfb65c917696dd.png`
- `docs/img/38c9428fa4309c313b8ff0405514b8ba.png`
- `docs/img/aba06c45fbb51559418091df3bd3b733.png`
- `docs/img/f49c3b7607bcddac58af520822816732.png`

## Solve Thinking

### Step 1: Document

- Route type: `evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: i春秋CTF ssrfme (peal函数中get命令漏洞)命令执行 详细题解＋原理 学习过程_AAAAAAAAAAAA66的博客-CSDN博客

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use the artifact-specific tool to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use the artifact-specific tool to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 3: 题目

- Route type: `evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `fc496e7bced4cce69bae49298f936828`

### Step 4: peal函数中get命令漏洞

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool with the extracted filter/query `perl函数看到要打开的文件名中如果以管道符（键盘上那个竖杠 |）结尾，就会中断原有打开文件操作，并且把这个文件名当作一个命令来执行，并且将命令的执行结果作为这个文件的内容写入。这个命令的执行权限是当前的登录者。如果你执行这个命令，你会看到perl程序运行的结果。**` and inspect the matching evidence.
- Filters or commands:
  - `perl函数看到要打开的文件名中如果以管道符（键盘上那个竖杠 |）结尾，就会中断原有打开文件操作，并且把这个文件名当作一个命令来执行，并且将命令的执行结果作为这个文件的内容写入。这个命令的执行权限是当前的登录者。如果你执行这个命令，你会看到perl程序运行的结果。**`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool with the extracted filter/query `perl函数看到要打开的文件名中如果以管道符（键盘上那个竖杠 |）结尾，就会中断原有打开文件操作，并且把这个文件名当作一个命令来执行，并且将命令的执行结果作为这个文件的内容写入。这个命令的执行权限是当前的登录者。如果你执行这个命令，你会看到perl程序运行的结果。**` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `所以我们可以在 url参数中传入 获取flag文件的命令，被执行后，将flag内容放在我们上传的文件里，我们再打开我们上传的文件就能见到flag了。`

### Step 5: 分析

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `获取用户的ip，并将 MD5后 orangeip的值作为文件夹名（这里ip要点自己的ip）`

### Step 6: 重点

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use the artifact-specific tool to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use the artifact-specific tool to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `最后，把data中的内容（url执行的值）传入到filename中。`

### Step 7: 题解

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use the artifact-specific tool with the extracted filter/query `3.?url=&filename=bash -c /readflag| 创建一个文件夹 文件夹名为命令执行语句 内容为空（随便填，不影响）` and inspect the matching evidence.
- Filters or commands:
  - `3.?url=&filename=bash -c /readflag| 创建一个文件夹 文件夹名为命令执行语句 内容为空（随便填，不影响）`
  - `4.?url=file:bash -c /readflag|&filename=321 通过命令执行，把执行完readflag获得的值存入到321文件`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use the artifact-specific tool with the extracted filter/query `3.?url=&filename=bash -c /readflag| 创建一个文件夹 文件夹名为命令执行语句 内容为空（随便填，不影响）` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4.?url=file:bash -c /readflag|&filename=321 通过命令执行，把执行完readflag获得的值存入到321文件`

### Step 8: 详细过程

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool with the extracted filter/query `?url=&filename=bash -c /readflag|` and inspect the matching evidence.
- Filters or commands:
  - `?url=&filename=bash -c /readflag|`
  - `?url=file:bash -c /readflag|&filename=321`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool with the extracted filter/query `?url=&filename=bash -c /readflag|` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a5e696d4fa6a3af1101bfd5d83e0ee56`

### Step 9: 这道题的思考

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use the artifact-specific tool to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use the artifact-specific tool to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `f49c3b7607bcddac58af520822816732`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
