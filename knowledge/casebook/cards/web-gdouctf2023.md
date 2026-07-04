# [GDOUCTF 2023]受不了一点

## Case Metadata

- Category: `Web`
- Platform: `GDOUCTF 2023`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/GDOUCTF2023-受不了一点.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/GDOUCTF2023-%E5%8F%97%E4%B8%8D%E4%BA%86%E4%B8%80%E7%82%B9.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/GDOUCTF2023-受不了一点.md`
- Challenge URL: `https://www.nssctf.cn/problem/3727`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: PHP环境, hackbar, yakit
- Techniques: http-analysis, php-tricks, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `1`
- `web/images/[GDOUCTF 2023]受不了一点-payloads.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `PHP环境-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use PHP环境, hackbar, yakit to collect the smallest evidence slice that answers the goal.
- Tools: PHP环境, hackbar, yakit
- Reasoning chain:
  - Recognize the section as PHP环境-driven evidence lookup.
  - Use PHP环境, hackbar, yakit to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `**题目关键信息列表**：`

### Step 2: 想到什么解题思路

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use PHP环境, hackbar, yakit to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: PHP环境, hackbar, yakit
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use PHP环境, hackbar, yakit to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- 题目意思很明确，按照条件判断的指示，构造一层层的参数进行绕过，最终进入到`echo $flag; `。`

### Step 3: 尝试过程和结果记录

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use yakit with the extracted filter/query ``if($_POST['gdou']!=$_POST['ctf'] && md5($a)===md5($b))`这是md5的强比较，可以通过数组进行绕过。数组的md5值都是`Null`,满足强比较。` and inspect the matching evidence.
- Tools: yakit
- Filters or commands:
  - ``if($_POST['gdou']!=$_POST['ctf'] && md5($a)===md5($b))`这是md5的强比较，可以通过数组进行绕过。数组的md5值都是`Null`,满足强比较。`
  - ``if ($_COOKIE['cookie']=='j0k3r')`设置`cookie`值为相应值即可。`
  - ``if($aaa==114514 && $bbb==114514 && $aaa!=$bbb)`这也属于php的弱比较，当字符串与数字进行比较时，字符串会转换为对应类型的数字进行比较。`
  - ``if(isset($_GET['flag']) && isset($_POST['flag']))`和`if($_POST['flag'] === 'flag' || $_GET['flag'] === 'flag')``
  - `if( ($a != $b) && (md5($a) === md5($b)) && (sha1($a)=== sha1($b)) && md5($a) == null && sha1($a) == null){`
  - `if($aaa==114514 && $bbb==114514 && $aaa!=$bbb){`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use yakit with the extracted filter/query ``if($_POST['gdou']!=$_POST['ctf'] && md5($a)===md5($b))`这是md5的强比较，可以通过数组进行绕过。数组的md5值都是`Null`,满足强比较。` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `![payloads](images/[GDOUCTF%202023]受不了一点-payloads.png)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
