# 2019 D3CTF ezupload题解_slug01sh的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `2019 D3CTF ezupload题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/2019-D3CTF-ezupload题解_slug01sh的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/2019-D3CTF-ezupload%E9%A2%98%E8%A7%A3_slug01sh%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/2019-D3CTF-ezupload题解_slug01sh的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: not detected
- Techniques: classical-crypto, command-injection, deserialization, encoding-analysis, file-upload, http-analysis, php-tricks, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `1`
- `docs/img/ef84a03982d1d65e177d63abbb7a245d.png`

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

### Step 2: 2019 D3CTF ezupload题解_slug01sh的博客-CSDN博客

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use the artifact-specific tool to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use the artifact-specific tool to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_43085611/article/details/119717608](https://blog.csdn.net/qq_43085611/article/details/119717608)`

### Step 3: 0 前言

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use the artifact-specific tool to confirm object injection and map the gadget or magic-method path before building the final payload.
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use the artifact-specific tool to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `一个 PHP 反序列化的题目。虽然序列化的的利用链简单，但是还是踩了很多坑。`

### Step 4: 1 题解

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use the artifact-specific tool to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use the artifact-specific tool to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ef84a03982d1d65e177d63abbb7a245d`

### Step 5: 1 .htaccess

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use the artifact-specific tool to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use the artifact-specific tool to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `当然很多绕过方法，都是类似的思想，根据一个具体的目标寻找代替物。`

### Step 6: 2 反序列化的工作路径

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use the artifact-specific tool to confirm object injection and map the gadget or magic-method path before building the final payload.
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use the artifact-specific tool to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `但在后面需要利用 destruct 的 file_put_content 来写入文件，反序列化时程序的工作路径在根目录，所以无法直接使用相对路径来写入文件。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
