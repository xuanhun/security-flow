# BugkuCTF WEB解题记录 1-5_weixin_30556959的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `BugkuCTF WEB解题记录 1`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BugkuCTF-WEB解题记录-1-5_weixin_30556959的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BugkuCTF-WEB%E8%A7%A3%E9%A2%98%E8%AE%B0%E5%BD%95-1-5_weixin_30556959%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BugkuCTF-WEB解题记录-1-5_weixin_30556959的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: not detected
- Techniques: command-injection, crypto-analysis, file-upload, http-analysis, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `16`
- `docs/img/d3aaa641b083b896e6f5bd9498bc5200.png`
- `docs/img/1acc829d7b007880971a4662d0fce7b9.png`
- `docs/img/a26f23b94bfe7d4647135dd29ee44626.png`
- `docs/img/74951dd90a554d1c71ac0b012906619e.png`
- `docs/img/a8e32b1c36e069de617a4ba7cda790f6.png`
- `docs/img/8f88c6485d0ecadaa4343b0aea94d997.png`
- `docs/img/01cd67da34fa5bf87f60d3b15727c5a5.png`
- `docs/img/dea1b44390b87f248fd6d8b1123bead9.png`
- `docs/img/ac89ce406d5b6ae5951e32bc28759fb5.png`
- `docs/img/7e0e428af400acf50dbd040db09ca58b.png`
- `docs/img/70e964a98a691cfe0a1fbf494b895039.png`
- `docs/img/0779a8f36dcfff69e95b605615263e5e.png`
- ... and `4` more

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

### Step 2: BugkuCTF WEB解题记录 1-5_weixin_30556959的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_30556959/article/details/96107465](https://blog.csdn.net/weixin_30556959/article/details/96107465)`

### Step 3: web2

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `120.24.86.145:8002`

### Step 4: 文件上传测试

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use the artifact-specific tool to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use the artifact-specific tool to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `42e97d465f962c53df9549377b513c7e`

### Step 5: 计算器

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `120.24.86.145:8002`

### Step 6: web基础$_GET

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool with the extracted filter/query `$what=$_GET['what']; echo $what; if($what=='flag') echo 'flag{****}';` and inspect the matching evidence.
- Filters or commands:
  - `$what=$_GET['what']; echo $what; if($what=='flag') echo 'flag{****}';`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool with the extracted filter/query `$what=$_GET['what']; echo $what; if($what=='flag') echo 'flag{****}';` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `120.24.86.145:8002`

### Step 7: web基础$_POST

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool with the extracted filter/query `$what=$_POST['what']; echo $what; if($what=='flag') echo 'flag{****}';` and inspect the matching evidence.
- Filters or commands:
  - `$what=$_POST['what']; echo $what; if($what=='flag') echo 'flag{****}';`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool with the extracted filter/query `$what=$_POST['what']; echo $what; if($what=='flag') echo 'flag{****}';` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `120.24.86.145:8002`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
