# Web / ids

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| http-analysis | 16 | http evidence extraction, burp-driven evidence lookup, sql injection exploitation, command execution path, detect-it-easy-driven evidence lookup |
| web-exploitation | 16 | http evidence extraction, burp-driven evidence lookup, sql injection exploitation, command execution path, detect-it-easy-driven evidence lookup |
| waf-bypass | 13 | http evidence extraction, burp-driven evidence lookup, sql injection exploitation, waf bypass, command execution path |
| command-injection | 11 | http evidence extraction, command execution path, detect-it-easy-driven evidence lookup, file inclusion exploitation, burp-driven evidence lookup |
| classical-crypto | 10 | http evidence extraction, sql injection exploitation, burp-driven evidence lookup, file inclusion exploitation, command execution path |
| crypto-analysis | 10 | http evidence extraction, burp-driven evidence lookup, sql injection exploitation, command execution path, file inclusion exploitation |
| encoding-analysis | 10 | http evidence extraction, sql injection exploitation, burp-driven evidence lookup, file inclusion exploitation, command execution path |
| php-tricks | 10 | http evidence extraction, burp-driven evidence lookup, sql injection exploitation, detect-it-easy-driven evidence lookup, deserialization chain |
| sql-injection | 10 | http evidence extraction, sql injection exploitation, burp-driven evidence lookup, file inclusion exploitation, command execution path |
| file-inclusion | 8 | http evidence extraction, file inclusion exploitation, sql injection exploitation, burp-driven evidence lookup, command execution path |
| deserialization | 7 | http evidence extraction, burp-driven evidence lookup, deserialization chain, detect-it-easy-driven evidence lookup, sql injection exploitation |
| dns-analysis | 7 | http evidence extraction, burp-driven evidence lookup, sql injection exploitation, command execution path, detect-it-easy-driven evidence lookup |
| binary-exploitation | 6 | http evidence extraction, command execution path, file inclusion exploitation, detect-it-easy-driven evidence lookup, burp-driven evidence lookup |
| file-upload | 6 | http evidence extraction, file inclusion exploitation, file upload bypass, burp-driven evidence lookup, command execution path |
| ret2libc | 6 | http evidence extraction, command execution path, detect-it-easy-driven evidence lookup, file inclusion exploitation, burp-driven evidence lookup |
| ssti | 6 | http evidence extraction, waf bypass, burp-driven evidence lookup, file inclusion exploitation, cipher decoding |
| browser-forensics | 4 | http evidence extraction, burp-driven evidence lookup, sql injection exploitation, file inclusion exploitation, deserialization chain |
| misc-analysis | 4 | http evidence extraction, command execution path, burp-driven evidence lookup, file inclusion exploitation, antsword-driven evidence lookup |
| xss | 4 | http evidence extraction, burp-driven evidence lookup, command execution path, detect-it-easy-driven evidence lookup, file inclusion exploitation |
| jwt-analysis | 3 | http evidence extraction, command execution path, detect-it-easy-driven evidence lookup, dns pivot, file inclusion exploitation |
| service-enumeration | 3 | http evidence extraction, detect-it-easy-driven evidence lookup, file inclusion exploitation, sql injection exploitation, burp-driven evidence lookup |
| symbolic-execution | 3 | http evidence extraction, burp-driven evidence lookup, file inclusion exploitation, sql injection exploitation, deserialization chain |
| qr-analysis | 2 | detect-it-easy-driven evidence lookup, file inclusion exploitation, http evidence extraction, command execution path, dns pivot |
| format-string | 1 | deserialization chain, detect-it-easy-driven evidence lookup |
| image-analysis | 1 | burp-driven evidence lookup, command execution path, http evidence extraction, stego extraction, waf bypass |
| mobile-forensics | 1 | command execution path, detect-it-easy-driven evidence lookup, file inclusion exploitation, http evidence extraction |
| network-forensics | 1 | command execution path, deserialization chain, detect-it-easy-driven evidence lookup, file upload bypass, http evidence extraction |
| password-cracking | 1 | command execution path, http evidence extraction, python环境-driven evidence lookup, timeline reconstruction |
| stego-extraction | 1 | command execution path, deserialization chain, detect-it-easy-driven evidence lookup, file upload bypass, http evidence extraction |
| timeline-analysis | 1 | detect-it-easy-driven evidence lookup, dns pivot, file inclusion exploitation, http evidence extraction, sql injection exploitation |
| traffic-analysis | 1 | command execution path, deserialization chain, detect-it-easy-driven evidence lookup, file upload bypass, http evidence extraction |
| web-enumeration | 1 | burp-driven evidence lookup, deserialization chain, http evidence extraction, sql injection exploitation |

## Route Types

| Route type | Cases |
| --- | --- |
| http evidence extraction | 12 |
| burp-driven evidence lookup | 7 |
| sql injection exploitation | 7 |
| command execution path | 6 |
| detect-it-easy-driven evidence lookup | 5 |
| file inclusion exploitation | 5 |
| waf bypass | 5 |
| deserialization chain | 3 |
| file upload bypass | 3 |
| cipher decoding | 2 |
| xss route | 2 |
| antsword-driven evidence lookup | 1 |
| dns pivot | 1 |
| evidence lookup | 1 |
| python环境-driven evidence lookup | 1 |
| ssti exploitation | 1 |
| stego extraction | 1 |
| timeline reconstruction | 1 |
| Yakit-driven evidence lookup | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [31C3 CTF web关writeup_weixin_34019929的博客-CSDN博客](../../../cards/docs-31c3-ctf-web-writeup-weixin-34019929-csdn.md) | 31C3 CTF web关writeup |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [[NSSRound#30 Duo]hack_the_world!](../../../cards/web-nssround-30-duo-hack-the-world.md) | NSSRound#30 Duo |  | dns-analysis, http-analysis, jwt-analysis, ssti |
| [[NSSRound#30 Duo]你也是迷宫高手吗](../../../cards/web-nssround-30-duo.md) | NSSRound#30 Duo |  | binary-exploitation, command-injection, crypto-analysis, http-analysis |
| [buuctf web小结_绿冰壶的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | buuctf web小结 |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [BUUCTF寒假刷题-Web_深海神奇舰舰长的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF寒假刷题 |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [CTF-入门一__starstarli的博客-CSDN博客](../../../cards/docs-ctf-starstarli-csdn.md) | CTF |  | binary-exploitation, command-injection, crypto-analysis, dns-analysis |
| [ctfhub技能书+历年真题学习笔记（详解）_Yn8rt的博客-CSDN博客](../../../cards/docs-ctfhub-yn8rt-csdn.md) | ctfhub技能书+历年真题学习笔记（详解） |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF从入门到提升（十四）session phpinfo包含及例题详解_anquanniu牛油果的博客-CSDN博客](../../../cards/docs-ctf-session-phpinfo-anquanniu-csdn.md) | CTF从入门到提升（十四）session phpinfo包含及例题详解 |  | file-inclusion, file-upload |
| [CTF解题-2020年强网杯参赛WriteUp_Tr0e的博客-CSDN博客_ctf解题赛](../../../cards/docs-ctf-2020-writeup-tr0e-csdn-ctf.md) | CTF解题 |  | classical-crypto, command-injection, deserialization, encoding-analysis |
| [CTF解题-网安实验室(注入关)_Tr0e的博客-CSDN博客](../../../cards/docs-ctf-tr0e-csdn.md) | CTF解题 |  | dns-analysis, file-inclusion, http-analysis, php-tricks |
| [DASCTF-两道web题复现_cr4ke3的博客-CSDN博客](../../../cards/docs-dasctf-web-cr4ke3-csdn.md) | DASCTF |  | command-injection, crypto-analysis, deserialization, format-string |
| [GWCTF 2019-你的名字](../../../cards/web-gwctf-2019.md) | GWCTF 2019 |  | http-analysis, ssti, waf-bypass, web-exploitation |
| [i春秋 百度杯”CTF比赛（二月场） Misc&&web题解 By Assassin_Assassin__is__me的博客-CSDN博客](../../../cards/docs-i-ctf-misc-web-by-assassin-assassin-is-me-csdn.md) | i春秋 |  | binary-exploitation, classical-crypto, command-injection, encoding-analysis |
| [一道简单的CTF登录题题解_anquanniu牛油果的博客-CSDN博客_ctf login题目](../../../cards/docs-ctf-anquanniu-csdn-ctf-login.md) | 一道简单的CTF登录题题解 |  | classical-crypto, crypto-analysis, deserialization, encoding-analysis |
| [春秋web题目解题及思路汇总（自用搜集）_香草星冰乐的博客-CSDN博客](../../../cards/docs-web-csdn.md) | 春秋web题目解题及思路汇总（自用搜集） |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [西普学院CTF习题解析——WEB(已完成16/16)_Xyntax的博客-CSDN博客](../../../cards/docs-ctf-web-16-16-xyntax-csdn.md) | 西普学院CTF习题解析——WEB(已完成16/16) |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [解网鼎杯一道web题（fakebook）_诸神之眼的博客-CSDN博客_fakebook](../../../cards/docs-web-fakebook-csdn-fakebook.md) | 解网鼎杯一道web题（fakebook） |  | browser-forensics, classical-crypto, deserialization, encoding-analysis |
