# 记录一道神仙CTF-wtf.sh-150_asdqwe10203的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `记录一道神仙CTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/记录一道神仙CTF-wtf.sh-150_asdqwe10203的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E8%AE%B0%E5%BD%95%E4%B8%80%E9%81%93%E7%A5%9E%E4%BB%99CTF-wtf.sh-150_asdqwe10203%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/记录一道神仙CTF-wtf.sh-150_asdqwe10203的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: netcat
- Techniques: file-inclusion, http-analysis, privilege-escalation, sql-injection, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `16`
- `docs/img/d551a9c198b35009143539680006413a.png`
- `docs/img/59ac5373a122d4e926a322d58b13fa06.png`
- `docs/img/1ea91fe21b8b08fac63c1e11aaab16b6.png`
- `docs/img/b81b1a02bf8d13262ff5c6fa6d4e7b4c.png`
- `docs/img/2b46b06bdb5a86afa8617495a8a1c65e.png`
- `docs/img/19eaf117ed683e27917e5486fb8ed875.png`
- `docs/img/dacb1dc3635757f6471bc568cacbf3ab.png`
- `docs/img/f83cd7861e3aca0ad138bfe614968fe1.png`
- `docs/img/1a53072f1fff65ab37b45a2c3d7e34be.png`
- `docs/img/ce3211707ebfb719cf3296be5656ba81.png`
- `docs/img/e46bf361eb46569c53c0409616caf24d.png`
- `docs/img/e7517d0dbde6bd1e0a8147fa4d4f48ed.png`
- ... and `4` more

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

### Step 2: 记录一道神仙CTF-wtf.sh-150_asdqwe10203的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `记录一道完全超出我能力的CTF神仙题（不愧是世界级比赛的真题orz)，此题我仅解出了第一部分的flag，第二部分则参考了WP。不得不说这种题目解出来还是很有自豪感的嘛~ 直接看题！`

### Step 3: **0x01 第一部分flag**

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `d551a9c198b35009143539680006413a`

### Step 4: **0x02:第二个flag**

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `12 curr_id=$(for d in posts/${post_id}/*; do basename $d; done | sort -n | tail -n 1); 13` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `12 curr_id=$(for d in posts/${post_id}/*; do basename $d; done | sort -n | tail -n 1); 13`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `12 curr_id=$(for d in posts/${post_id}/*; do basename $d; done | sort -n | tail -n 1); 13` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ce3211707ebfb719cf3296be5656ba81`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
