# CTF AWD靶场搭建和第一题题解_星星明亮的博客-CSDN博客_awd靶场

## Case Metadata

- Category: `Web`
- Platform: `CTF AWD靶场搭建和第一题题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF-AWD靶场搭建和第一题题解_星星明亮的博客-CSDN博客_awd靶场.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF-AWD%E9%9D%B6%E5%9C%BA%E6%90%AD%E5%BB%BA%E5%92%8C%E7%AC%AC%E4%B8%80%E9%A2%98%E9%A2%98%E8%A7%A3_%E6%98%9F%E6%98%9F%E6%98%8E%E4%BA%AE%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_awd%E9%9D%B6%E5%9C%BA.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF-AWD靶场搭建和第一题题解_星星明亮的博客-CSDN博客_awd靶场.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: netcat
- Techniques: command-injection, crypto-analysis, file-inclusion, http-analysis, service-enumeration, sql-injection, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `13`
- `docs/img/df7fa50e7d6f708c264d3604c105b476.png`
- `docs/img/92e3de18b0696dc5c4eced97d0c495d8.png`
- `docs/img/e828baddaa0859b04c212f7a8502ef6c.png`
- `docs/img/fcd38b41821dd7139ee135a81030f075.png`
- `docs/img/c12a30ff15956ebc0bd1c2925a4be5e8.png`
- `docs/img/4a798c4a8101fc01868f7fc09f46a5a6.png`
- `docs/img/c3859c7cd4cd6f29b76d8de8d5ba0723.png`
- `docs/img/2fdac68104383d3ed06bee3258d5a6e3.png`
- `docs/img/525fcaff8347a2dcf2a5b790253ad562.png`
- `docs/img/38b0b7b3c3fb898be41d05a9ae7f1713.png`
- `docs/img/948df300a2455b4aff4dc682e304183c.png`
- `docs/img/a2ce4ce4ad3582b753ec467fe33af013.png`
- ... and `1` more

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

### Step 2: CTF AWD靶场搭建和第一题题解_星星明亮的博客-CSDN博客_awd靶场

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat with the extracted filter/query `curl -fsSL https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/debian/gpg | sudo apt-key add -` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `curl -fsSL https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/debian/gpg | sudo apt-key add -`
  - `echo 'deb https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/debian/ buster stable' | sudo tee /etc/apt/sources.list.d/docker.list`
  - `python batch.py web_dir team_number`
  - `python start.py ./ team_number`
  - `python check.py`
  - `python batch.py web_yunnan_simple 2`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat with the extracted filter/query `curl -fsSL https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/debian/gpg | sudo apt-key add -` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `172.17.0.6:80`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
