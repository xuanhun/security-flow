# [FSCTF 2023]巴巴托斯！

## Case Metadata

- Category: `Web`
- Platform: `FSCTF 2023`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/random.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/random.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/random.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: yakit
- Techniques: browser-forensics, file-inclusion, http-analysis, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `2`
- `web/images/FSCTF2023巴巴托斯-1.png`
- `web/images/FSCTF2023巴巴托斯-2.png`

## Solve Thinking

### Step 1: [FSCTF 2023]巴巴托斯！

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use yakit to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: yakit
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use yakit to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `show_image.php`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
