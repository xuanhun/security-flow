# CTF解题笔记（1）_TravisZeng的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `CTF解题笔记（1）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF解题笔记（1）_TravisZeng的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%E8%A7%A3%E9%A2%98%E7%AC%94%E8%AE%B0%EF%BC%881%EF%BC%89_TravisZeng%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF解题笔记（1）_TravisZeng的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: detect-it-easy, netcat
- Techniques: command-injection, crypto-analysis, dns-analysis, http-analysis, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `7`
- `docs/img/1a3bc95b5578498c4c2dbc0109405e3a.png`
- `docs/img/e0e19d4414b7f983d3b2c8ecb7f1ee64.png`
- `docs/img/b1f94754c09d4b1971e515cff99c064b.png`
- `docs/img/78891682e29b6f0db971d4011b3fd63b.png`
- `docs/img/6bed23b063019d93d09cbdf7a97fb401.png`
- `docs/img/17c8292a1431ad5b56e764f3996d4c8e.png`
- `docs/img/0e54631b61474787b38367aef880b07f.png`

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

### Step 2: CTF解题笔记（1）_TravisZeng的博客-CSDN博客

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `if (!isset($_POST['uname']) || !isset($_POST['pwd'])) {` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `if (!isset($_POST['uname']) || !isset($_POST['pwd'])) {`
  - `if (preg_match("/".$ArrReq."/is",$StrValue)==1){`
  - `$filter = "and|select|from|where|union|join|sleep|benchmark|,|\(|\)";`
  - `if (mysql_num_rows($query) == 1) {`
  - `if($key['pwd'] == $_POST['pwd']) {`
  - `mysql_num_rows($query) == 1`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use detect-it-easy, netcat with the extracted filter/query `if (!isset($_POST['uname']) || !isset($_POST['pwd'])) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1a3bc95b5578498c4c2dbc0109405e3a`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
