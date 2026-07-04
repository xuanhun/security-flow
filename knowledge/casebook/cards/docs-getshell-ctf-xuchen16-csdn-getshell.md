# 利用文件名进行GetShell---CTF题目的相关知识解析_xuchen16的博客-CSDN博客_后台getshell

## Case Metadata

- Category: `Web`
- Platform: `利用文件名进行GetShell`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/利用文件名进行GetShell---CTF题目的相关知识解析_xuchen16的博客-CSDN博客_后台getshell.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E5%88%A9%E7%94%A8%E6%96%87%E4%BB%B6%E5%90%8D%E8%BF%9B%E8%A1%8CGetShell---CTF%E9%A2%98%E7%9B%AE%E7%9A%84%E7%9B%B8%E5%85%B3%E7%9F%A5%E8%AF%86%E8%A7%A3%E6%9E%90_xuchen16%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_%E5%90%8E%E5%8F%B0getshell.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/利用文件名进行GetShell---CTF题目的相关知识解析_xuchen16的博客-CSDN博客_后台getshell.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: detect-it-easy, netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, dns-analysis, encoding-analysis, file-inclusion, file-upload, http-analysis, php-tricks, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `3`
- `docs/img/91a615648a59d3de27ac16e7278125aa.png`
- `docs/img/1944f931df5ac3974b99d8eaa2f64ff8.png`
- `docs/img/ce3c3f5b964cf6562b0a87c320672b57.png`

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 利用文件名进行GetShell---CTF题目的相关知识解析_xuchen16的博客-CSDN博客_后台getshell

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `32. `if($row[0] === $password){`` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `32. `if($row[0] === $password){``
  - `d_addslashes 函数相当于全局过滤，不存在注入漏洞、且数据库与web都是UTF-8编码，也不存在宽字节注入。根据提示，在$row[0] === $password处存在逻辑漏洞。`
  - `页面对ip格式进行了正则匹配，最小长度输入为1.1.1.1。后面加入分隔符；& |等，无法正常执行命令,经过测试会发现，程序对& ; | ) ( ` $进行了过滤。但是没有对%0a进行过滤。尝试进行命令注入如下1.1.1.1%0awhoami`
  - `24. `if response.status_code == 200:``
  - `29. `if __name__ == "__main__":``
  - `wget 12\`
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use detect-it-easy, netcat with the extracted filter/query `32. `if($row[0] === $password){`` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.1.101:8084`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
