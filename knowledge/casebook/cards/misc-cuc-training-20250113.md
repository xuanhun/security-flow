# 13 题解

## Case Metadata

- Category: `Misc`
- Platform: `cuc`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `misc/cuc_training_20250113.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/misc/cuc_training_20250113.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/misc/cuc_training_20250113.md`

## Why This Case Matters

Use this case as a Misc reference for ciphertext, stego-media, web-app challenges.

## Input Signals

- Artifacts: ciphertext, stego-media, web-app
- Tools: cyberchef, netcat, strings
- Techniques: binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis, http-analysis, image-analysis, malware-static, misc-analysis, stego-extraction, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Solve Thinking

### Step 1: [LitCTF 2023]404notfound (初级)

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use strings with the extracted filter/query `strings 1.png | grep -i ctf` and inspect the matching evidence.
- Tools: strings
- Filters or commands:
  - `strings 1.png | grep -i ctf`
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use strings with the extracted filter/query `strings 1.png | grep -i ctf` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ````bash`

### Step 2: <rdf:li xml:lang='x-default'>LitCTF_Logo - 8</rdf:li>

- Route type: `cyberchef-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, netcat, strings to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, netcat, strings
- Reasoning chain:
  - Recognize the section as cyberchef-driven evidence lookup.
  - Use cyberchef, netcat, strings to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 3: [LitCTF 2023]What_1s_BASE (初级)

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use cyberchef, netcat, strings with the extracted filter/query `Linux shell: |, base64` and inspect the matching evidence.
- Tools: cyberchef, netcat, strings
- Filters or commands:
  - `Linux shell: |, base64`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use cyberchef, netcat, strings with the extracted filter/query `Linux shell: |, base64` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ````bash`

### Step 4: 建议将 pypi 类工具统一使用 conda 管理起来

- Route type: `cyberchef-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, netcat, strings with the extracted filter/query `ciphey -t "TGl0Q1RGe0tGQ19DcjR6eV9UaHVyM2RheV9WX21lXzUwfQ=="` and inspect the matching evidence.
- Tools: cyberchef, netcat, strings
- Filters or commands:
  - `ciphey -t "TGl0Q1RGe0tGQ19DcjR6eV9UaHVyM2RheV9WX21lXzUwfQ=="`
- Reasoning chain:
  - Recognize the section as cyberchef-driven evidence lookup.
  - Use cyberchef, netcat, strings with the extracted filter/query `ciphey -t "TGl0Q1RGe0tGQ19DcjR6eV9UaHVyM2RheV9WX21lXzUwfQ=="` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ciphey -t "TGl0Q1RGe0tGQ19DcjR6eV9UaHVyM2RheV9WX21lXzUwfQ=="`

### Step 5: Possible plaintext: 'LitCTF{KFC_Cr4zy_Thur3day_V_me_50}'

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use cyberchef, netcat, strings with the extracted filter/query `echo -n 'TGl0Q1RGe0tGQ19DcjR6eV9UaHVyM2RheV9WX21lXzUwfQ==' | base64 -d` and inspect the matching evidence.
- Tools: cyberchef, netcat, strings
- Filters or commands:
  - `echo -n 'TGl0Q1RGe0tGQ19DcjR6eV9UaHVyM2RheV9WX21lXzUwfQ==' | base64 -d`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use cyberchef, netcat, strings with the extracted filter/query `echo -n 'TGl0Q1RGe0tGQ19DcjR6eV9UaHVyM2RheV9WX21lXzUwfQ==' | base64 -d` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `echo -n 'TGl0Q1RGe0tGQ19DcjR6eV9UaHVyM2RheV9WX21lXzUwfQ==' | base64 -d`

### Step 6: LitCTF{KFC_Cr4zy_Thur3day_V_me_50}

- Route type: `cyberchef-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, netcat, strings to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, netcat, strings
- Reasoning chain:
  - Recognize the section as cyberchef-driven evidence lookup.
  - Use cyberchef, netcat, strings to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 7: [HDCTF 2023]hardMisc

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use strings with the extracted filter/query `unzip 0.zip && strings emoji.png | tail -n 1 | base64 -d` and inspect the matching evidence.
- Tools: strings
- Filters or commands:
  - `unzip 0.zip && strings emoji.png | tail -n 1 | base64 -d`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use strings with the extracted filter/query `unzip 0.zip && strings emoji.png | tail -n 1 | base64 -d` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ````bash`

### Step 8: HDCTF{wE1c0w3_10_HDctf_M15c}

- Route type: `cyberchef-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, netcat, strings to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, netcat, strings
- Reasoning chain:
  - Recognize the section as cyberchef-driven evidence lookup.
  - Use cyberchef, netcat, strings to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 9: [LitCTF 2023]Hex？Hex！(初级)

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use cyberchef to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ````bash`

### Step 10: 工具-1 ciphey

- Route type: `cyberchef-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, netcat, strings to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, netcat, strings
- Reasoning chain:
  - Recognize the section as cyberchef-driven evidence lookup.
  - Use cyberchef, netcat, strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `4c69744354467b746169313131636f6f6c6c616161217d`

### Step 11: 工具-3 python

- Route type: `cyberchef-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, netcat, strings to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, netcat, strings
- Reasoning chain:
  - Recognize the section as cyberchef-driven evidence lookup.
  - Use cyberchef, netcat, strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `4c69744354467b746169313131636f6f6c6c616161217d`

### Step 12: [LitCTF 2023]Is this only base?  https://www.nssctf.cn/problem/3968

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use cyberchef, netcat with the extracted filter/query `Caesar Cipher == ROT3` and inspect the matching evidence.
- Tools: cyberchef, netcat
- Filters or commands:
  - `Caesar Cipher == ROT3`
  - `观察密文中有等号，猜测可能是 base64 编码，但是位置不对，继续猜测可能是栅栏密码，尝试使用 CyberChef 解密。在 CyberChef 中逐个 key 遍历可以发现 output 不断变化，直到 key 为 23 时，发现输出像是 base64 编码结果了：SWZxWlFDe0liUV9ScF9FNFMzX2NSMCEhISEhfQ==`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use cyberchef, netcat with the extracted filter/query `Caesar Cipher == ROT3` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: ````bash`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
