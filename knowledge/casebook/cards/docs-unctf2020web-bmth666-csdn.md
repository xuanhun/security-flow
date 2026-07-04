# UNCTF2020web方向部分题解_bmth666的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `UNCTF2020web方向部分题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/UNCTF2020web方向部分题解_bmth666的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/UNCTF2020web%E6%96%B9%E5%90%91%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3_bmth666%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/UNCTF2020web方向部分题解_bmth666的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, disk-image challenges.

## Input Signals

- Artifacts: binary, ciphertext, disk-image, web-app
- Tools: netcat, sqlmap
- Techniques: classical-crypto, command-injection, crypto-analysis, deserialization, encoding-analysis, file-upload, http-analysis, misc-analysis, php-tricks, ssti, timeline-analysis, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `23`
- `docs/img/e3e10f1858a6ba85a1fdf94e404fcde1.png`
- `docs/img/e15f2b894b694caacdb69eff37b509c3.png`
- `docs/img/f81fa061fc0e10f314cfd9c6d57ce010.png`
- `docs/img/fcb281e08604304b642e9ae53b2df145.png`
- `docs/img/c8ba78b5ddca4b8c653ee5f1d9a174af.png`
- `docs/img/5c495c464842f7bc74dc6fc363a8beeb.png`
- `docs/img/71e853cf191a452f10d3aac6f376ebb5.png`
- `docs/img/5db4343cb1905f27ac7fce1deb89ed38.png`
- `docs/img/6b877123020352cc9ef2e7eff82b0530.png`
- `docs/img/7474ca08c97994dbd233f1e917055741.png`
- `docs/img/c610f23e5d5e1e3d1b8d3badf6241f3f.png`
- `docs/img/47df6700dd08520dedb075a678e69aff.png`
- ... and `11` more

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: UNCTF2020web方向部分题解_bmth666的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/bmth666/article/details/109765055](https://blog.csdn.net/bmth666/article/details/109765055)`

### Step 3: easy_ssrf

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `e3e10f1858a6ba85a1fdf94e404fcde1`

### Step 4: easyflask

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use netcat, sqlmap with the extracted filter/query `?guess={{%20({}|attr(request.args.x1)|attr(request.args.x2)|%20attr(request.args.x3)())}}&x1=__class__&x2=__base__&x3=__subclasses__` and inspect the matching evidence.
- Tools: netcat, sqlmap
- Filters or commands:
  - `?guess={{%20({}|attr(request.args.x1)|attr(request.args.x2)|%20attr(request.args.x3)())}}&x1=__class__&x2=__base__&x3=__subclasses__`
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use netcat, sqlmap with the extracted filter/query `?guess={{%20({}|attr(request.args.x1)|attr(request.args.x2)|%20attr(request.args.x3)())}}&x1=__class__&x2=__base__&x3=__subclasses__` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `e15f2b894b694caacdb69eff37b509c3`

### Step 5: 俄罗斯方块人大战奥特曼

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `fcb281e08604304b642e9ae53b2df145`

### Step 6: easyunserialize

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use netcat, sqlmap to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use netcat, sqlmap to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `71e853cf191a452f10d3aac6f376ebb5`

### Step 7: babyeval

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, sqlmap with the extracted filter/query `?a=echo `ls|base64`;` and inspect the matching evidence.
- Tools: netcat, sqlmap
- Filters or commands:
  - `?a=echo `ls|base64`;`
  - `?a=echo `cat flag.php|base64`;`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, sqlmap with the extracted filter/query `?a=echo `ls|base64`;` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5db4343cb1905f27ac7fce1deb89ed38`

### Step 8: ezphp

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use netcat, sqlmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use netcat, sqlmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `47df6700dd08520dedb075a678e69aff`

### Step 9: easy_upload

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use netcat, sqlmap to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use netcat, sqlmap to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0efc2f2edf446dc948bd3c3aafbbde44`

### Step 10: UN’s_online_tools

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use sqlmap to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: sqlmap
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use sqlmap to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `fafda7a66f68af0bd312cbb8c78275bd`

### Step 11: ezfind

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, sqlmap with the extracted filter/query `给出了提示才做出来的：**if(!(is_file($name)===false)){flag}else{no flag}**` and inspect the matching evidence.
- Tools: netcat, sqlmap
- Filters or commands:
  - `给出了提示才做出来的：**if(!(is_file($name)===false)){flag}else{no flag}**`
  - `发现是NULL，然后===false是false，再来一个!结果就是true`
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, sqlmap with the extracted filter/query `给出了提示才做出来的：**if(!(is_file($name)===false)){flag}else{no flag}**` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `dfd1e9ae3389b790029a5baccc73e3a5`

### Step 12: checkin-sql：

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `但。。。。找不到flag，写文件的话不知道是姿势错了还是写不进去，tcl`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
