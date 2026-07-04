# Web / stego-media

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| web-exploitation | 19 | http evidence extraction, sql injection exploitation, cipher decoding, deserialization chain, ssti exploitation |
| http-analysis | 18 | http evidence extraction, cipher decoding, deserialization chain, sql injection exploitation, ssti exploitation |
| command-injection | 16 | http evidence extraction, ssti exploitation, cipher decoding, command execution path, deserialization chain |
| classical-crypto | 14 | http evidence extraction, cipher decoding, deserialization chain, ssti exploitation, detect-it-easy-driven evidence lookup |
| crypto-analysis | 14 | http evidence extraction, ssti exploitation, cipher decoding, sql injection exploitation, deserialization chain |
| waf-bypass | 14 | http evidence extraction, cipher decoding, command execution path, deserialization chain, detect-it-easy-driven evidence lookup |
| encoding-analysis | 13 | http evidence extraction, ssti exploitation, cipher decoding, deserialization chain, detect-it-easy-driven evidence lookup |
| misc-analysis | 13 | http evidence extraction, cipher decoding, command execution path, sql injection exploitation, ssti exploitation |
| sql-injection | 13 | http evidence extraction, sql injection exploitation, ssti exploitation, cipher decoding, command execution path |
| file-inclusion | 12 | http evidence extraction, ssti exploitation, cipher decoding, deserialization chain, detect-it-easy-driven evidence lookup |
| file-upload | 11 | http evidence extraction, ssti exploitation, cipher decoding, command execution path, deserialization chain |
| php-tricks | 11 | http evidence extraction, deserialization chain, cipher decoding, detect-it-easy-driven evidence lookup, ssti exploitation |
| deserialization | 9 | http evidence extraction, deserialization chain, cipher decoding, ssti exploitation, command execution path |
| image-analysis | 9 | http evidence extraction, cipher decoding, sql injection exploitation, ssti exploitation, stego extraction |
| binary-exploitation | 8 | http evidence extraction, cipher decoding, command execution path, deserialization chain, reverse engineering |
| dns-analysis | 7 | http evidence extraction, burp-driven evidence lookup, cipher decoding, command execution path, deserialization chain |
| ssti | 7 | ssti exploitation, http evidence extraction, cipher decoding, deserialization chain, detect-it-easy-driven evidence lookup |
| traffic-analysis | 7 | http evidence extraction, cipher decoding, ssti exploitation, waf bypass, command execution path |
| qr-analysis | 5 | cipher decoding, http evidence extraction, deserialization chain, reverse engineering, ssti exploitation |
| ret2libc | 5 | http evidence extraction, ssti exploitation, cipher decoding, command execution path, deserialization chain |
| network-forensics | 4 | http evidence extraction, waf bypass, cipher decoding, command execution path, deserialization chain |
| reverse-engineering | 4 | cipher decoding, http evidence extraction, reverse engineering, command execution path, ssti exploitation |
| xss | 4 | cipher decoding, http evidence extraction, burp-driven evidence lookup, deserialization chain, reverse engineering |
| stego-extraction | 3 | command execution path, http evidence extraction, ssti exploitation, waf bypass, cipher decoding |
| service-enumeration | 2 | burp-driven evidence lookup, cipher decoding, http evidence extraction, netcat-driven evidence lookup, ssti exploitation |
| stack-overflow | 2 | burp-driven evidence lookup, cipher decoding, deserialization chain, http evidence extraction, ssti exploitation |
| symbolic-execution | 2 | ssti exploitation, cipher decoding, command execution path, http evidence extraction, reverse engineering |
| jwt-analysis | 1 | ssti exploitation |
| memory-forensics | 1 | burp-driven evidence lookup, cipher decoding, deserialization chain, http evidence extraction |
| mobile-forensics | 1 | ssti exploitation |
| osint | 1 | cipher decoding, command execution path, http evidence extraction, reverse engineering, ssti exploitation |
| stream-cipher | 1 | cipher decoding, http evidence extraction, reverse engineering, sql injection exploitation, stego extraction |

## Route Types

| Route type | Cases |
| --- | --- |
| http evidence extraction | 14 |
| sql injection exploitation | 7 |
| cipher decoding | 6 |
| deserialization chain | 6 |
| ssti exploitation | 6 |
| command execution path | 5 |
| detect-it-easy-driven evidence lookup | 5 |
| burp-driven evidence lookup | 4 |
| file inclusion exploitation | 4 |
| file upload bypass | 4 |
| waf bypass | 4 |
| evidence lookup | 3 |
| reverse engineering | 3 |
| stego extraction | 3 |
| netcat-driven evidence lookup | 2 |
| antsword-driven evidence lookup | 1 |
| credential discovery | 1 |
| dns pivot | 1 |
| incident timeline reconstruction | 1 |
| xss route | 1 |
| 无-driven evidence lookup | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [+ 未分类](../../../cards/summary.md) | SUMMARY.md |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [2019SCUCTF部分题解_东坡何罪发文章总是审核不通过，去博客园了的博客-CSDN博客](../../../cards/docs-2019scuctf-csdn.md) | 2019SCUCTF部分题解 |  | binary-exploitation, classical-crypto, crypto-analysis, deserialization |
| [2021强网杯Write-Up真题解析之WEB部分（暴力干货，建议收藏）_代码熬夜敲的博客-CSDN博客_强网杯题目](../../../cards/docs-2021-write-up-web-csdn.md) | 2021强网杯Write |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [[NSSRound#18]门酱想玩什么呢](../../../cards/web-nssround-18.md) | NSSRound#18 | 中等 | dns-analysis, http-analysis, waf-bypass, web-exploitation |
| [BugkuCTF 部分题解(一)_z.volcano的博客-CSDN博客_bugkuctf](../../../cards/docs-bugkuctf-z-volcano-csdn-bugkuctf.md) | BugkuCTF 部分题解(一) |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [CTF-入门一__starstarli的博客-CSDN博客](../../../cards/docs-ctf-starstarli-csdn.md) | CTF |  | binary-exploitation, command-injection, crypto-analysis, dns-analysis |
| [ctfhub技能书+历年真题学习笔记（详解）_Yn8rt的博客-CSDN博客](../../../cards/docs-ctfhub-yn8rt-csdn.md) | ctfhub技能书+历年真题学习笔记（详解） |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF专题一2021网络WEB题目解析_普通网友的博客-CSDN博客_ctf web分析](../../../cards/docs-ctf-2021-web-csdn-ctf-web.md) | CTF专题一2021网络WEB题目解析 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF从入门到提升（四）基于时间盲注例题及解法_anquanniu牛油果的博客-CSDN博客_ctf 时间盲注](../../../cards/docs-ctf-anquanniu-csdn-ctf.md) | CTF从入门到提升（四）基于时间盲注例题及解法 |  | http-analysis, sql-injection, web-exploitation |
| [CTF入门第一课(附一道小题)_anquanniu牛油果的博客-CSDN博客](../../../cards/docs-ctf-anquanniu-csdn.md) | CTF入门第一课(附一道小题) |  | binary-exploitation, crypto-analysis, image-analysis, misc-analysis |
| [CTF解题-2020年强网杯参赛WriteUp_Tr0e的博客-CSDN博客_ctf解题赛](../../../cards/docs-ctf-2020-writeup-tr0e-csdn-ctf.md) | CTF解题 |  | classical-crypto, command-injection, deserialization, encoding-analysis |
| [CTF里面的WEB题的一些解决思路_F10W3RDANC3的博客-CSDN博客_ctfweb思路](../../../cards/docs-ctf-web-f10w3rdanc3-csdn-ctfweb.md) | CTF里面的WEB题的一些解决思路 |  | command-injection, file-upload, http-analysis, sql-injection |
| [HITCTF2018-web全题解_合天网安实验室的博客-CSDN博客](../../../cards/docs-hitctf2018-web-csdn.md) | HITCTF2018 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [ichunqiu CTF 训练 Basic 全解_Daren_f0的博客-CSDN博客](../../../cards/docs-ichunqiu-ctf-basic-daren-f0-csdn.md) | ichunqiu CTF 训练 Basic 全解 |  | command-injection |
| [【CTF】基础常识_你们这样一点都不可耐的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | 【CTF】基础常识 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [南京邮电大学CG-CTF平台Writeup_Gard3nia的博客-CSDN博客_cgctf平台](../../../cards/docs-cg-ctf-writeup-gard3nia-csdn-cgctf.md) | 南京邮电大学CG |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [好家伙！学习Laravel框架之CTF真题暴力解析_代码熬夜敲的博客-CSDN博客](../../../cards/docs-laravel-ctf-csdn.md) | 好家伙！学习Laravel框架之CTF真题暴力解析 |  | binary-exploitation, classical-crypto, command-injection, deserialization |
| [春秋web题目解题及思路汇总（自用搜集）_香草星冰乐的博客-CSDN博客](../../../cards/docs-web-csdn.md) | 春秋web题目解题及思路汇总（自用搜集） |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [第四届“”世安杯“”线上赛题解（Web+Stego+Misc+Crypto）_Assassin__is__me的博客-CSDN博客](../../../cards/docs-web-stego-misc-crypto-assassin-is-me-csdn.md) | 第四届“”世安杯“”线上赛题解（Web+Stego+Misc+Crypto） |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [静默开水的博客_CSDN博客-CTF,web题解题思路,Misc 图片隐写领域博主](../../../cards/docs-csdn-ctf-web-misc.md) | 静默开水的博客 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
