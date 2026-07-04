# TWCTF 2016 (Tokyo Westerns CTF ) WEB WriteUp_Bendawang的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `TWCTF 2016`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/TWCTF-2016-(Tokyo-Westerns-CTF-)-WEB-WriteUp_Bendawang的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/TWCTF-2016-%28Tokyo-Westerns-CTF-%29-WEB-WriteUp_Bendawang%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/TWCTF-2016-(Tokyo-Westerns-CTF-)-WEB-WriteUp_Bendawang的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, pcap, web-app challenges.

## Input Signals

- Artifacts: ciphertext, pcap, web-app
- Tools: detect-it-easy, netcat, wireshark
- Techniques: classical-crypto, command-injection, encoding-analysis, file-inclusion, file-upload, http-analysis, network-forensics, service-enumeration, sql-injection, ssti, traffic-analysis, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `16`
- `docs/img/f09630e10481589010c7972eb011f3a2.png`
- `docs/img/91aa2f05408def7d49068b8ee65b61d2.png`
- `docs/img/9de637c13e40f9178a685fded0863469.png`
- `docs/img/2f4e87067667f2aec3a1416a7efa3ae0.png`
- `docs/img/97e54c4d7e91dd58db6debdd845f3e28.png`
- `docs/img/86cd20ccbde26354fc693c9651836334.png`
- `docs/img/279c3acd1bf844227918daee44413cc2.png`
- `docs/img/5f43d2da361ad70deb2ed5fe9d80e717.png`
- `docs/img/8a207a698749df66455b583191622483.png`
- `docs/img/40207cc23495238a09789e4aa76ba6d2.png`
- `docs/img/475f6bc4ce6408d5153c742949541faf.png`
- `docs/img/dde26d4408ebcbe012f6f114133c9983.png`
- ... and `4` more

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat, wireshark
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: TWCTF 2016 (Tokyo Westerns CTF ) WEB WriteUp_Bendawang的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat, wireshark
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `现在貌似还开着的，不知道会开多久。`

### Step 3: web 50 Global Page

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `f09630e10481589010c7972eb011f3a2`

### Step 4: web 100 Get the admin password!

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use detect-it-easy, netcat, wireshark to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: detect-it-easy, netcat, wireshark
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use detect-it-easy, netcat, wireshark to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `91aa2f05408def7d49068b8ee65b61d2`

### Step 5: web 150 rotten uploader

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use detect-it-easy, netcat, wireshark with the extracted filter/query `if(stripos($_GET['f'], 'file_list') !== FALSE) die();` and inspect the matching evidence.
- Tools: detect-it-easy, netcat, wireshark
- Filters or commands:
  - `if(stripos($_GET['f'], 'file_list') !== FALSE) die();`
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use detect-it-easy, netcat, wireshark with the extracted filter/query `if(stripos($_GET['f'], 'file_list') !== FALSE) die();` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `9de637c13e40f9178a685fded0863469`

### Step 6: web 200 ZIP cracker

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `86cd20ccbde26354fc693c9651836334`

### Step 7: web 300 Tsurai Web

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat, wireshark with the extracted filter/query `|-a` and inspect the matching evidence.
- Tools: detect-it-easy, netcat, wireshark
- Filters or commands:
  - `|-a`
  - `|`
  - `|-a.py`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat, wireshark with the extracted filter/query `|-a` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `475f6bc4ce6408d5153c742949541faf`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
