# Web / binary

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| web-exploitation | 70 | http evidence extraction, netcat-driven evidence lookup, sql injection exploitation, file inclusion exploitation, command execution path |
| http-analysis | 62 | http evidence extraction, file inclusion exploitation, command execution path, netcat-driven evidence lookup, cipher decoding |
| command-injection | 50 | http evidence extraction, command execution path, file inclusion exploitation, netcat-driven evidence lookup, sql injection exploitation |
| crypto-analysis | 49 | http evidence extraction, cipher decoding, sql injection exploitation, deserialization chain, netcat-driven evidence lookup |
| waf-bypass | 48 | http evidence extraction, file inclusion exploitation, waf bypass, sql injection exploitation, command execution path |
| classical-crypto | 47 | http evidence extraction, cipher decoding, file inclusion exploitation, sql injection exploitation, deserialization chain |
| encoding-analysis | 46 | http evidence extraction, sql injection exploitation, file inclusion exploitation, netcat-driven evidence lookup, cipher decoding |
| file-inclusion | 36 | http evidence extraction, file inclusion exploitation, command execution path, sql injection exploitation, burp-driven evidence lookup |
| php-tricks | 35 | http evidence extraction, deserialization chain, netcat-driven evidence lookup, sql injection exploitation, cipher decoding |
| sql-injection | 32 | http evidence extraction, sql injection exploitation, netcat-driven evidence lookup, burp-driven evidence lookup, file inclusion exploitation |
| deserialization | 25 | http evidence extraction, deserialization chain, netcat-driven evidence lookup, ssti exploitation, burp-driven evidence lookup |
| binary-exploitation | 24 | http evidence extraction, sql injection exploitation, command execution path, file inclusion exploitation, netcat-driven evidence lookup |
| file-upload | 24 | http evidence extraction, ssti exploitation, burp-driven evidence lookup, deserialization chain, netcat-driven evidence lookup |
| ssti | 24 | http evidence extraction, ssti exploitation, file inclusion exploitation, netcat-driven evidence lookup, deserialization chain |
| ret2libc | 20 | http evidence extraction, file inclusion exploitation, command execution path, burp-driven evidence lookup, ssti exploitation |
| dns-analysis | 18 | http evidence extraction, file inclusion exploitation, cipher decoding, reverse engineering, sql injection exploitation |
| misc-analysis | 16 | http evidence extraction, cipher decoding, sql injection exploitation, burp-driven evidence lookup, command execution path |
| reverse-engineering | 16 | reverse engineering, http evidence extraction, cipher decoding, command execution path, file inclusion exploitation |
| qr-analysis | 14 | http evidence extraction, cipher decoding, sql injection exploitation, deserialization chain, detect-it-easy-driven evidence lookup |
| xss | 14 | http evidence extraction, sql injection exploitation, cipher decoding, command execution path, burp-driven evidence lookup |
| service-enumeration | 11 | http evidence extraction, command execution path, file inclusion exploitation, sql injection exploitation, burp-driven evidence lookup |
| image-analysis | 9 | cipher decoding, http evidence extraction, reverse engineering, ssti exploitation, stego extraction |
| symbolic-execution | 9 | http evidence extraction, cipher decoding, file inclusion exploitation, reverse engineering, command execution path |
| jwt-analysis | 8 | http evidence extraction, deserialization chain, netcat-driven evidence lookup, command execution path, sql injection exploitation |
| browser-forensics | 7 | http evidence extraction, file inclusion exploitation, burp-driven evidence lookup, cipher decoding, sql injection exploitation |
| timeline-analysis | 7 | http evidence extraction, netcat-driven evidence lookup, command execution path, deserialization chain, file inclusion exploitation |
| traffic-analysis | 5 | cipher decoding, http evidence extraction, reverse engineering, sql injection exploitation, ssti exploitation |
| stack-overflow | 4 | burp-driven evidence lookup, cipher decoding, deserialization chain, file upload bypass, http evidence extraction |
| stego-extraction | 4 | http evidence extraction, reverse engineering, ssti exploitation, cipher decoding, command execution path |
| malware-static | 3 | http evidence extraction, capa-driven evidence lookup, credential discovery, netcat-driven evidence lookup, reverse engineering |
| mobile-forensics | 3 | command execution path, detect-it-easy-driven evidence lookup, file inclusion exploitation, http evidence extraction, netcat-driven evidence lookup |
| network-forensics | 3 | cipher decoding, http evidence extraction, burp-driven evidence lookup, command execution path, deserialization chain |
| privilege-escalation | 3 | http evidence extraction, command execution path, file inclusion exploitation, credential discovery, detect-it-easy-driven evidence lookup |
| web-enumeration | 3 | deserialization chain, http evidence extraction, ssti exploitation, burp-driven evidence lookup, detect-it-easy-driven evidence lookup |
| integer-overflow | 2 | command execution path, http evidence extraction, credential discovery, deserialization chain, file inclusion exploitation |
| osint | 2 | cipher decoding, http evidence extraction, waf bypass, burp-driven evidence lookup, command execution path |
| password-cracking | 2 | http evidence extraction, cipher decoding, dirb-driven evidence lookup, foremost-driven evidence lookup, sql injection exploitation |
| ret2text | 2 | file upload bypass, http evidence extraction, netcat-driven evidence lookup, reverse engineering, waf bypass |
| email-header-analysis | 1 | burp-driven evidence lookup, http evidence extraction |
| memory-forensics | 1 | burp-driven evidence lookup, cipher decoding, deserialization chain, http evidence extraction |
| siem-query | 1 | cipher decoding, elk-driven evidence lookup, indicator enrichment, xss route |
| stream-cipher | 1 | cipher decoding, http evidence extraction, reverse engineering, sql injection exploitation, stego extraction |

## Route Types

| Route type | Cases |
| --- | --- |
| http evidence extraction | 51 |
| netcat-driven evidence lookup | 22 |
| command execution path | 21 |
| file inclusion exploitation | 21 |
| sql injection exploitation | 21 |
| ssti exploitation | 18 |
| cipher decoding | 17 |
| deserialization chain | 15 |
| reverse engineering | 15 |
| waf bypass | 15 |
| burp-driven evidence lookup | 12 |
| detect-it-easy-driven evidence lookup | 9 |
| credential discovery | 6 |
| file upload bypass | 5 |
| xss route | 4 |
| evidence lookup | 3 |
| gdb-driven evidence lookup | 3 |
| stego extraction | 3 |
| incident timeline reconstruction | 2 |
| jwt trust-boundary abuse | 2 |
| Yakit-driven evidence lookup | 2 |
| capa-driven evidence lookup | 1 |
| constraint solving | 1 |
| conversation statistics | 1 |
| dirb-driven evidence lookup | 1 |
| dns pivot | 1 |
| elk-driven evidence lookup | 1 |
| foremost-driven evidence lookup | 1 |
| indicator enrichment | 1 |
| memory artifact analysis | 1 |
| python2 环境-driven evidence lookup | 1 |
| strings-driven evidence lookup | 1 |
| z3-driven evidence lookup | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [+ 未分类](../../../cards/summary.md) | SUMMARY.md |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [17 题解](../../../cards/web-cuc-training-20250117.md) | cuc |  | http-analysis, malware-static, sql-injection, ssti |
| [2019SCUCTF部分题解_东坡何罪发文章总是审核不通过，去博客园了的博客-CSDN博客](../../../cards/docs-2019scuctf-csdn.md) | 2019SCUCTF部分题解 |  | binary-exploitation, classical-crypto, crypto-analysis, deserialization |
| [2020年DDCTF-web签到题题解_slug01sh的博客-CSDN博客](../../../cards/docs-2020-ddctf-web-slug01sh-csdn.md) | 2020年DDCTF |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [2020易博霖CTFWeb2--SSRF题解_flying_bird2019的博客-CSDN博客](../../../cards/docs-2020-ctfweb2-ssrf-flying-bird2019-csdn.md) | 2020易博霖CTFWeb2 |  | classical-crypto, crypto-analysis, dns-analysis, encoding-analysis |
| [2021强网杯Write-Up真题解析之WEB部分（暴力干货，建议收藏）_代码熬夜敲的博客-CSDN博客_强网杯题目](../../../cards/docs-2021-write-up-web-csdn.md) | 2021强网杯Write |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [31C3 CTF web关writeup_weixin_34019929的博客-CSDN博客](../../../cards/docs-31c3-ctf-web-writeup-weixin-34019929-csdn.md) | 31C3 CTF web关writeup |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [[AFCTF 2021]BABY_CSP](../../../cards/web-afctf-2021baby-csp.md) | AFCTF 2021 | 简单 | http-analysis, waf-bypass, web-exploitation, xss |
| [[CISCN 2019华东南]Web4](../../../cards/web-ciscn2019-web4.md) | CISCN 2019华东南 |  | crypto-analysis, encoding-analysis, http-analysis, ssti |
| [[GHCTF 2024 新生赛]理想国](../../../cards/web-ghctf2024.md) | GHCTF 2024 新生赛 |  | command-injection, crypto-analysis, http-analysis, jwt-analysis |
| [[HDCTF 2023]LoginMaster](../../../cards/web-hdctf2023-loginmaster.md) | HDCTF 2023 |  | http-analysis, sql-injection, waf-bypass, web-exploitation |
| [[第五空间 2021]yet_another_mysql_injection](../../../cards/web-2021-yet-another-mysql-injection.md) | 第五空间 2021 |  | command-injection, dns-analysis, file-inclusion, http-analysis |
| [AntCTF X D^3CTF shellgen2 题解_god_speed丶的博客-CSDN博客](../../../cards/docs-antctf-x-d-3ctf-shellgen2-god-speed-csdn.md) | AntCTF X D^3CTF shellgen2 题解 |  | crypto-analysis, misc-analysis, qr-analysis, waf-bypass |
| [BJDCTF 2020-Cookie is so subtle!](../../../cards/web-bjdctf-2020-cookie-is-so-subtle.md) | BJDCTF 2020 |  | file-inclusion, http-analysis, ssti, web-exploitation |
| [bugkuCTF web进阶+web最后两题_goddemon的博客-CSDN博客](../../../cards/docs-bugkuctf-web-web-goddemon-csdn.md) | bugkuCTF web进阶+web最后两题 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [BugkuCTF 部分题解(一)_z.volcano的博客-CSDN博客_bugkuctf](../../../cards/docs-bugkuctf-z-volcano-csdn-bugkuctf.md) | BugkuCTF 部分题解(一) |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [BugkuCTF-WEB部分题解（四）_flying_bird2019的博客-CSDN博客](../../../cards/docs-bugkuctf-web-flying-bird2019-csdn.md) | BugkuCTF |  | classical-crypto, crypto-analysis, encoding-analysis, php-tricks |
| [BugKu题解备注（1）_s11show_163的博客-CSDN博客](../../../cards/docs-bugku-1-s11show-163-csdn.md) | BugKu题解备注（1） |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [buuctf web小结_绿冰壶的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | buuctf web小结 |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [BUUCTF__web题解合集（一）_风过江南乱的博客-CSDN博客_buuctf web](../../../cards/docs-buuctf-web-csdn-buuctf-web.md) | BUUCTF |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [BUUCTF__web题解合集（九）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [BUUCTF__web题解合集（五）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [BUUCTF__web题解合集（八）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [BUUCTF__web题解合集（十二）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | binary-exploitation, classical-crypto, command-injection, encoding-analysis |
| [BUUCTF__web题解合集（四）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [BUUCTF寒假刷题-Web_深海神奇舰舰长的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF寒假刷题 |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [BUUCTF解题十一道(04)_Sprint#51264的博客-CSDN博客](../../../cards/docs-buuctf-04-sprint-51264-csdn.md) | BUUCTF解题十一道(04) |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [Buuctf部分题解_君陌上的博客-CSDN博客_buuctf](../../../cards/docs-buuctf-csdn-buuctf.md) | Buuctf部分题解 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [ctf show-web入门 php特性篇部分题解_z.volcano的博客-CSDN博客_ctfshow的php特性](../../../cards/docs-ctf-show-web-php-z-volcano-csdn-ctfshow-php.md) | ctf show |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [ctf web个人总结_recover517的博客-CSDN博客](../../../cards/docs-ctf-web-recover517-csdn.md) | ctf web个人总结 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF 题型了解_秦罗敷写代码的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | CTF 题型了解 |  | binary-exploitation, crypto-analysis, http-analysis, misc-analysis |
| [CTF-2021中国能源网络WEB题目全解_wulanlin的博客-CSDN博客](../../../cards/docs-ctf-2021-web-wulanlin-csdn.md) | CTF |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF-rootme 题解之Hash - SHA-2_weixin_30237719的博客-CSDN博客](../../../cards/docs-ctf-rootme-hash-sha-2-weixin-30237719-csdn.md) | CTF |  | command-injection, crypto-analysis, http-analysis, php-tricks |
| [CTF-rootme 题解之PHP filters_weixin_30384031的博客-CSDN博客](../../../cards/docs-ctf-rootme-php-filters-weixin-30384031-csdn.md) | CTF |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [CTF-rootme 题解之PHP register globals_weixin_30881367的博客-CSDN博客](../../../cards/docs-ctf-rootme-php-register-globals-weixin-30881367-csdn.md) | CTF |  | command-injection, file-inclusion, http-analysis, reverse-engineering |
| [CTF-rootme 题解之Python - input()_weixin_30612769的博客-CSDN博客](../../../cards/docs-ctf-rootme-python-input-weixin-30612769-csdn.md) | CTF |  | command-injection, ret2libc, reverse-engineering |
| [CTF-rootme 题解之Python - pickle_weixin_30652879的博客-CSDN博客](../../../cards/docs-ctf-rootme-python-pickle-weixin-30652879-csdn.md) | CTF |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF-web 第十一部分 实用脚本_iamsongyu的博客-CSDN博客](../../../cards/docs-ctf-web-iamsongyu-csdn.md) | CTF |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [CTF-入门一__starstarli的博客-CSDN博客](../../../cards/docs-ctf-starstarli-csdn.md) | CTF |  | binary-exploitation, command-injection, crypto-analysis, dns-analysis |
| [CTFHUB Web题解记录（信息泄露、弱口令部分）_valecalida的博客-CSDN博客_ctfhub弱口令](../../../cards/docs-ctfhub-web-valecalida-csdn-ctfhub.md) | CTFHUB Web题解记录（信息泄露、弱口令部分） |  | http-analysis, malware-static, reverse-engineering, stego-extraction |
| [ctfhub技能书+历年真题学习笔记（详解）_Yn8rt的博客-CSDN博客](../../../cards/docs-ctfhub-yn8rt-csdn.md) | ctfhub技能书+历年真题学习笔记（详解） |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF专题一2021网络WEB题目解析_普通网友的博客-CSDN博客_ctf web分析](../../../cards/docs-ctf-2021-web-csdn-ctf-web.md) | CTF专题一2021网络WEB题目解析 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [ctf中文转unicode_CTF实战题解笔记 - Web篇_weixin_39707597的博客-CSDN博客](../../../cards/docs-ctf-unicode-ctf-web-weixin-39707597-csdn.md) | ctf中文转unicode |  | binary-exploitation, encoding-analysis, file-upload, http-analysis |
| [CTF入门第一课(附一道小题)_anquanniu牛油果的博客-CSDN博客](../../../cards/docs-ctf-anquanniu-csdn.md) | CTF入门第一课(附一道小题) |  | binary-exploitation, crypto-analysis, image-analysis, misc-analysis |
| [CTF学习-web解题思路_菜鸟-传奇的博客-CSDN博客](../../../cards/docs-ctf-web-csdn.md) | CTF学习 |  | browser-forensics, classical-crypto, crypto-analysis, dns-analysis |
| [CTF解题-Bugku_Web_WriteUp (下）_Tr0e的博客-CSDN博客](../../../cards/docs-ctf-bugku-web-writeup-tr0e-csdn.md) | CTF解题 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [ctf训练 web安全暴力破解_爱吃香菜的哈哈的博客-CSDN博客](../../../cards/docs-ctf-web-csdn.md) | ctf训练 web安全暴力破解 |  | crypto-analysis, http-analysis, password-cracking, privilege-escalation |
| [ctf赛题secret.php,记一场纯JS赛——DiceCTF2021 Web题解_自强自在的博客-CSDN博客](../../../cards/docs-ctf-secret-php-js-dicectf2021-web-csdn.md) | ctf |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [ctf逆向解题——Bomb二进制炸弹_FunkyPants的博客-CSDN博客](../../../cards/docs-ctf-bomb-funkypants-csdn.md) | ctf逆向解题——Bomb二进制炸弹 |  | malware-static, stego-extraction |
| [D^3CTF(Crypto-D3bug详解 LFSR题目）_Mango|Feng的博客-CSDN博客](../../../cards/docs-d-3ctf-crypto-d3bug-lfsr-mango-feng-csdn.md) | D^3CTF(Crypto |  | crypto-analysis, http-analysis, symbolic-execution, web-exploitation |
| [hgame ctf week2--shinyshot题解_weixin_30753873的博客-CSDN博客](../../../cards/docs-hgame-ctf-week2-shinyshot-weixin-30753873-csdn.md) | hgame ctf week2 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [hxp 36C3 CTF Web题 WriteupBin Writeup (Selenium模拟点击+Content Security Policy+Nonce+Parsley.js触发错误提示)_KevinLuo2000的博客-CSDN博客](../../../cards/docs-hxp-36c3-ctf-web-writeupbin-writeup-selenium-content-security-policy-nonce-parsley-js-kevinluo2000-csdn.md) | hxp 36C3 CTF Web |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [i春秋 百度杯”CTF比赛（二月场） Misc&&web题解 By Assassin_Assassin__is__me的博客-CSDN博客](../../../cards/docs-i-ctf-misc-web-by-assassin-assassin-is-me-csdn.md) | i春秋 |  | binary-exploitation, classical-crypto, command-injection, encoding-analysis |
| [NSSCTF 2nd-MyHurricane](../../../cards/web-nssctf-2nd-myhurricane.md) | NSSCTF 2nd |  | command-injection, http-analysis, ssti, waf-bypass |
| [php伪随机数 ctf,从一道ctf题目理解rand()随机函数_Ma Daniel的博客-CSDN博客](../../../cards/docs-php-ctf-ctf-rand-ma-daniel-csdn.md) | php伪随机数 ctf,从一道ctf题目理解rand()随机函数 |  | classical-crypto, crypto-analysis, http-analysis, reverse-engineering |
| [PWN cmd1 [pwnable.kr]CTF writeup题解系列11_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-cmd1-pwnable-kr-ctf-writeup-11-3ric5r-csdn.md) | PWN cmd1 [pwnable.kr]CTF writeup题解系列11 |  | binary-exploitation, command-injection, service-enumeration |
| [PWN cmd2 [pwnable.kr]CTF writeup题解系列12_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-cmd2-pwnable-kr-ctf-writeup-12-3ric5r-csdn.md) | PWN cmd2 [pwnable.kr]CTF writeup题解系列12 |  | binary-exploitation, command-injection, file-inclusion, ret2libc |
| [PWN lotto [pwnable.kr]CTF writeup题解系列10_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-lotto-pwnable-kr-ctf-writeup-10-3ric5r-csdn.md) | PWN lotto [pwnable.kr]CTF writeup题解系列10 |  | binary-exploitation, browser-forensics, command-injection, file-inclusion |
| [python 重定向 ctf_CTF-rootme 题解之Python - pickle_深夜利行的博客-CSDN博客](../../../cards/docs-python-ctf-ctf-rootme-python-pickle-csdn.md) | python 重定向 ctf |  | classical-crypto, crypto-analysis, deserialization, encoding-analysis |
| [SWPUCTF web 部分题解_HyyMbb的博客-CSDN博客](../../../cards/docs-swpuctf-web-hyymbb-csdn.md) | SWPUCTF web 部分题解 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [UNCTF2020web方向部分题解_bmth666的博客-CSDN博客](../../../cards/docs-unctf2020web-bmth666-csdn.md) | UNCTF2020web方向部分题解 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [web python template injection_CTF引出对Python模板注入的思考_weixin_39630466的博客-CSDN博客](../../../cards/docs-web-python-template-injection-ctf-python-weixin-39630466-csdn.md) | web python template injection |  | command-injection, dns-analysis, http-analysis, image-analysis |
| [【BUUCTF刷题】Web解题方法总结（一)_Y1seco的博客-CSDN博客_buuctfweb](../../../cards/docs-buuctf-web-y1seco-csdn-buuctfweb.md) | 【BUUCTF刷题】Web解题方法总结（一) |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [【CTF】基础常识_你们这样一点都不可耐的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | 【CTF】基础常识 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [一道CTF题看JWT和python反序列化_weixin_44377940的博客-CSDN博客_jwt反序列化](../../../cards/docs-ctf-jwt-python-weixin-44377940-csdn-jwt.md) | 一道CTF题看JWT和python反序列化 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [南邮ctf平台部分题解_这是游戏吗的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | 南邮ctf平台部分题解 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [好家伙！学习Laravel框架之CTF真题暴力解析_代码熬夜敲的博客-CSDN博客](../../../cards/docs-laravel-ctf-csdn.md) | 好家伙！学习Laravel框架之CTF真题暴力解析 |  | binary-exploitation, classical-crypto, command-injection, deserialization |
| [如何在ctf解题实战中绕过disable_function_YnG_t0的博客-CSDN博客_disablefunctions 绕过](../../../cards/docs-ctf-disable-function-yng-t0-csdn-disablefunctions.md) | 如何在ctf解题实战中绕过disable |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [实战：2019 0ctf final Web Writeup（一）_systemino的博客-CSDN博客](../../../cards/docs-2019-0ctf-final-web-writeup-systemino-csdn.md) | 实战：2019 0ctf final Web Writeup（一） |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [技能五子棋](../../../cards/web-gccctf-2025.md) | GCCCTF 2025 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [攻防世界-web-shrine-从0到1的解题历程writeup_CTF小白的博客-CSDN博客](../../../cards/docs-web-shrine-0-1-writeup-ctf-csdn.md) | 攻防世界 |  | ssti, waf-bypass, web-exploitation |
| [某校赛的题解...再膜鸡哥_Assassin__is__me的博客-CSDN博客](../../../cards/docs-assassin-is-me-csdn.md) | 某校赛的题解...再膜鸡哥 |  | dns-analysis, file-upload, http-analysis, ret2text |
| [第三届上海市大学生网络安全大赛 i春秋CTF Web解题思路_曹振国cc的博客-CSDN博客](../../../cards/docs-i-ctf-web-cc-csdn.md) | 第三届上海市大学生网络安全大赛 i春秋CTF Web解题思路 |  | sql-injection, web-exploitation |
| [第四届“”世安杯“”线上赛题解（Web+Stego+Misc+Crypto）_Assassin__is__me的博客-CSDN博客](../../../cards/docs-web-stego-misc-crypto-assassin-is-me-csdn.md) | 第四届“”世安杯“”线上赛题解（Web+Stego+Misc+Crypto） |  | classical-crypto, command-injection, crypto-analysis, deserialization |
