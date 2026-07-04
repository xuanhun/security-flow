# 【CTF reverse】逆向入门题解集合+逆向相关软件安装_hans774882968的博客-CSDN博客

## Case Metadata

- Category: `Reverse`
- Platform: `【CTF reverse】逆向入门题解集合+逆向相关软件安装`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【CTF-reverse】逆向入门题解集合+逆向相关软件安装_hans774882968的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90CTF-reverse%E3%80%91%E9%80%86%E5%90%91%E5%85%A5%E9%97%A8%E9%A2%98%E8%A7%A3%E9%9B%86%E5%90%88%2B%E9%80%86%E5%90%91%E7%9B%B8%E5%85%B3%E8%BD%AF%E4%BB%B6%E5%AE%89%E8%A3%85_hans774882968%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【CTF-reverse】逆向入门题解集合+逆向相关软件安装_hans774882968的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Reverse reference for apk-mobile, binary, ciphertext challenges.

## Input Signals

- Artifacts: apk-mobile, binary, ciphertext, web-app
- Tools: ida, netcat, radare2, strings
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, http-analysis, integer-overflow, malware-static, mobile-forensics, reverse-engineering, stego-extraction, waf-bypass, web-exploitation

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, radare2, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, radare2, strings
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, radare2, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 【CTF reverse】逆向入门题解集合+逆向相关软件安装_hans774882968的博客-CSDN博客

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `UPX.exe`

### Step 3: buu-easyre

- Route type: `integer-overflow bypass`
- Why: Numeric edge cases matter when they alter a length, signedness, allocation, or control-flow boundary.
- Probe: Use ida with the extracted filter/query `if ( a == b )` and inspect the matching evidence.
- Tools: ida
- Filters or commands:
  - `if ( a == b )`
- Reasoning chain:
  - Recognize the section as integer-overflow bypass.
  - Use ida with the extracted filter/query `if ( a == b )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `easyre.exe`

### Step 4: buu-reverse1

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, radare2 with the extracted filter/query `if ( Str2[(signed __int64)*(&v6 + 1)] == 111 )` and inspect the matching evidence.
- Tools: ida, netcat, radare2
- Filters or commands:
  - `if ( Str2[(signed __int64)*(&v6 + 1)] == 111 )`
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, radare2 with the extracted filter/query `if ( Str2[(signed __int64)*(&v6 + 1)] == 111 )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `reverse_1.exe`

### Step 5: buu-reverse2

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, strings with the extracted filter/query `if ( *(&flag + i) == 'i' || *(&flag + i) == 'r' )` and inspect the matching evidence.
- Tools: ida, strings
- Filters or commands:
  - `if ( *(&flag + i) == 'i' || *(&flag + i) == 'r' )`
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, strings with the extracted filter/query `if ( *(&flag + i) == 'i' || *(&flag + i) == 'r' )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: ``flag`的ascii是`{`，注意到aHacking_for_fu这个变量虽然没用到（所以strings window查不到），但它和flag的地址是相邻的，所以**&flag就是字符串`{hacking_for_fun}`**。然后那个循环逻辑很简单，不赘述。答案`flag{hack1ng_fo1_fun}``

### Step 6: buu-内涵的软件

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida with the extracted filter/query `if ( v2 == 'Y' )` and inspect the matching evidence.
- Tools: ida
- Filters or commands:
  - `if ( v2 == 'Y' )`
  - `else if ( v2 == 'N' )`
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida with the extracted filter/query `if ( v2 == 'Y' )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `49d3c93df25caad81232130f3d2ebfad`

### Step 7: buu-新年快乐

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use netcat with the extracted filter/query `代码逻辑就是，期望输入串v5 == “HappyNewYear”。所以这就是flag。` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `代码逻辑就是，期望输入串v5 == “HappyNewYear”。所以这就是flag。`
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use netcat with the extracted filter/query `代码逻辑就是，期望输入串v5 == “HappyNewYear”。所以这就是flag。` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `upx.exe`

### Step 8: buu-xor

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat with the extracted filter/query `xor: Mach-O 64-bit x86_64 executable, flags:<NOUNDEFS|DYLDLINK|TWOLEVEL|PIE>` and inspect the matching evidence.
- Tools: ida, netcat
- Filters or commands:
  - `xor: Mach-O 64-bit x86_64 executable, flags:<NOUNDEFS|DYLDLINK|TWOLEVEL|PIE>`
  - `if ( strlen(v7) != 33 )`
  - `if ( *(_QWORD *)__stack_chk_guard_ptr[0] == v8 )`
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat with the extracted filter/query `xor: Mach-O 64-bit x86_64 executable, flags:<NOUNDEFS|DYLDLINK|TWOLEVEL|PIE>` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `console.log(ans)`

### Step 9: buu-helloword-安卓逆向helloworld

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `return arg3.getItemId() == 0x7F05003C ? true : super.onOptionsItemSelected(arg3);` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `return arg3.getItemId() == 0x7F05003C ? true : super.onOptionsItemSelected(arg3);`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `return arg3.getItemId() == 0x7F05003C ? true : super.onOptionsItemSelected(arg3);` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7631a988259a00816deda84afb29430a`

### Step 10: buu-Java逆向解密

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `得：`This_is_the_flag_!`，记得包上`flag{}`。`

### Step 11: buu-findit-安卓逆向

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use ida, netcat, radare2, strings with the extracted filter/query `if (flagHome[i] < 73 && flagHome[i] >= 65 || flagHome[i] < 105 && flagHome[i] >= 97) {` and inspect the matching evidence.
- Tools: ida, netcat, radare2, strings
- Filters or commands:
  - `if (flagHome[i] < 73 && flagHome[i] >= 65 || flagHome[i] < 105 && flagHome[i] >= 97) {`
  - `} else if (flagHome[i] >= 65 && flagHome[i] <= 90 || flagHome[i] >= 97 && flagHome[i] <= 0x7A) {`
  - `if (ansStr[v0_1] >= 65 && ansStr[v0_1] <= 90 || ansStr[v0_1] >= 97 && ansStr[v0_1] <= 0x7A) {`
  - `if (y[v0_1] > 90 && y[v0_1] < 97 || y[v0_1] >= 0x7A) {`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use ida, netcat, radare2, strings with the extracted filter/query `if (flagHome[i] < 73 && flagHome[i] >= 65 || flagHome[i] < 105 && flagHome[i] >= 97) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `另外，根据https://blog.csdn.net/Waffle666/article/details/109901358，这题跟凯撒密码有关。`

### Step 12: 南邮CTF-py交易-python逆向helloworld

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `main()`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
