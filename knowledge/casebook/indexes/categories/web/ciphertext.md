# Web / ciphertext

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| web-exploitation | 149 | http evidence extraction, netcat-driven evidence lookup, sql injection exploitation, file inclusion exploitation, cipher decoding |
| encoding-analysis | 133 | http evidence extraction, file inclusion exploitation, netcat-driven evidence lookup, sql injection exploitation, cipher decoding |
| classical-crypto | 131 | http evidence extraction, netcat-driven evidence lookup, file inclusion exploitation, cipher decoding, sql injection exploitation |
| http-analysis | 121 | http evidence extraction, file inclusion exploitation, sql injection exploitation, cipher decoding, netcat-driven evidence lookup |
| crypto-analysis | 112 | http evidence extraction, netcat-driven evidence lookup, cipher decoding, sql injection exploitation, burp-driven evidence lookup |
| command-injection | 109 | http evidence extraction, file inclusion exploitation, netcat-driven evidence lookup, sql injection exploitation, command execution path |
| waf-bypass | 91 | http evidence extraction, sql injection exploitation, file inclusion exploitation, detect-it-easy-driven evidence lookup, waf bypass |
| php-tricks | 90 | http evidence extraction, sql injection exploitation, netcat-driven evidence lookup, burp-driven evidence lookup, deserialization chain |
| file-inclusion | 80 | http evidence extraction, file inclusion exploitation, netcat-driven evidence lookup, sql injection exploitation, burp-driven evidence lookup |
| sql-injection | 72 | http evidence extraction, sql injection exploitation, burp-driven evidence lookup, netcat-driven evidence lookup, file inclusion exploitation |
| file-upload | 49 | http evidence extraction, file upload bypass, sql injection exploitation, detect-it-easy-driven evidence lookup, burp-driven evidence lookup |
| deserialization | 44 | http evidence extraction, deserialization chain, sql injection exploitation, netcat-driven evidence lookup, burp-driven evidence lookup |
| dns-analysis | 33 | http evidence extraction, detect-it-easy-driven evidence lookup, file inclusion exploitation, sql injection exploitation, burp-driven evidence lookup |
| ret2libc | 33 | http evidence extraction, detect-it-easy-driven evidence lookup, file inclusion exploitation, command execution path, sql injection exploitation |
| ssti | 28 | http evidence extraction, ssti exploitation, file inclusion exploitation, netcat-driven evidence lookup, command execution path |
| misc-analysis | 25 | http evidence extraction, cipher decoding, sql injection exploitation, detect-it-easy-driven evidence lookup, file upload bypass |
| xss | 24 | http evidence extraction, sql injection exploitation, burp-driven evidence lookup, xss route, cipher decoding |
| browser-forensics | 22 | http evidence extraction, burp-driven evidence lookup, sql injection exploitation, detect-it-easy-driven evidence lookup, file upload bypass |
| binary-exploitation | 21 | http evidence extraction, sql injection exploitation, command execution path, file inclusion exploitation, netcat-driven evidence lookup |
| qr-analysis | 17 | http evidence extraction, cipher decoding, sql injection exploitation, deserialization chain, detect-it-easy-driven evidence lookup |
| service-enumeration | 17 | http evidence extraction, sql injection exploitation, burp-driven evidence lookup, command execution path, detect-it-easy-driven evidence lookup |
| symbolic-execution | 12 | http evidence extraction, sql injection exploitation, cipher decoding, constraint solving, deserialization chain |
| jwt-analysis | 11 | http evidence extraction, sql injection exploitation, deserialization chain, netcat-driven evidence lookup, command execution path |
| traffic-analysis | 11 | http evidence extraction, cipher decoding, sql injection exploitation, burp-driven evidence lookup, command execution path |
| image-analysis | 10 | http evidence extraction, cipher decoding, file inclusion exploitation, sql injection exploitation, ssti exploitation |
| reverse-engineering | 10 | reverse engineering, cipher decoding, http evidence extraction, file inclusion exploitation, sql injection exploitation |
| network-forensics | 6 | http evidence extraction, cipher decoding, command execution path, detect-it-easy-driven evidence lookup, sql injection exploitation |
| password-cracking | 6 | http evidence extraction, sql injection exploitation, burp-driven evidence lookup, command execution path, ssti exploitation |
| timeline-analysis | 6 | http evidence extraction, netcat-driven evidence lookup, command execution path, deserialization chain, file inclusion exploitation |
| osint | 5 | burp-driven evidence lookup, http evidence extraction, cipher decoding, waf bypass, command execution path |
| web-enumeration | 5 | http evidence extraction, burp-driven evidence lookup, deserialization chain, sql injection exploitation, ssti exploitation |
| stego-extraction | 4 | command execution path, deserialization chain, http evidence extraction, ssti exploitation, waf bypass |
| mobile-forensics | 3 | command execution path, detect-it-easy-driven evidence lookup, file inclusion exploitation, http evidence extraction, netcat-driven evidence lookup |
| stack-overflow | 3 | burp-driven evidence lookup, cipher decoding, deserialization chain, http evidence extraction, netcat-driven evidence lookup |
| email-header-analysis | 2 | burp-driven evidence lookup, http evidence extraction, waf bypass |
| privilege-escalation | 2 | http evidence extraction, command execution path, detect-it-easy-driven evidence lookup, dirb-driven evidence lookup, file inclusion exploitation |
| format-string | 1 | burp-driven evidence lookup, command execution path, http evidence extraction, sql injection exploitation, waf bypass |
| integer-overflow | 1 | command execution path, deserialization chain, http evidence extraction, jwt trust-boundary abuse, netcat-driven evidence lookup |
| malware-static | 1 | burp-driven evidence lookup, deserialization chain |
| memory-forensics | 1 | burp-driven evidence lookup, cipher decoding, deserialization chain, http evidence extraction |
| siem-query | 1 | cipher decoding, elk-driven evidence lookup, indicator enrichment, xss route |
| stream-cipher | 1 | cipher decoding, http evidence extraction, reverse engineering, sql injection exploitation, stego extraction |

## Route Types

| Route type | Cases |
| --- | --- |
| http evidence extraction | 108 |
| netcat-driven evidence lookup | 53 |
| sql injection exploitation | 49 |
| file inclusion exploitation | 47 |
| cipher decoding | 46 |
| command execution path | 35 |
| burp-driven evidence lookup | 34 |
| detect-it-easy-driven evidence lookup | 31 |
| waf bypass | 27 |
| deserialization chain | 26 |
| file upload bypass | 24 |
| ssti exploitation | 19 |
| credential discovery | 13 |
| xss route | 10 |
| evidence lookup | 9 |
| reverse engineering | 9 |
| dns pivot | 6 |
| constraint solving | 3 |
| jwt trust-boundary abuse | 3 |
| PHP环境-driven evidence lookup | 3 |
| incident timeline reconstruction | 2 |
| indicator enrichment | 2 |
| stego extraction | 2 |
| Yakit-driven evidence lookup | 2 |
| z3-driven evidence lookup | 2 |
| antsword-driven evidence lookup | 1 |
| conversation statistics | 1 |
| dirb-driven evidence lookup | 1 |
| elk-driven evidence lookup | 1 |
| foremost-driven evidence lookup | 1 |
| hashcat-driven evidence lookup | 1 |
| john-driven evidence lookup | 1 |
| sqlmap-driven evidence lookup | 1 |
| timeline reconstruction | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [+ 未分类](../../../cards/summary.md) | SUMMARY.md |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [2019 D3CTF ezupload题解_slug01sh的博客-CSDN博客](../../../cards/docs-2019-d3ctf-ezupload-slug01sh-csdn.md) | 2019 D3CTF ezupload题解 |  | classical-crypto, command-injection, deserialization, encoding-analysis |
| [2019SCUCTF部分题解_东坡何罪发文章总是审核不通过，去博客园了的博客-CSDN博客](../../../cards/docs-2019scuctf-csdn.md) | 2019SCUCTF部分题解 |  | binary-exploitation, classical-crypto, crypto-analysis, deserialization |
| [2020年DDCTF-web签到题题解_slug01sh的博客-CSDN博客](../../../cards/docs-2020-ddctf-web-slug01sh-csdn.md) | 2020年DDCTF |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [2020易博霖CTFWeb2--SSRF题解_flying_bird2019的博客-CSDN博客](../../../cards/docs-2020-ctfweb2-ssrf-flying-bird2019-csdn.md) | 2020易博霖CTFWeb2 |  | classical-crypto, crypto-analysis, dns-analysis, encoding-analysis |
| [2021强网杯Write-Up真题解析之WEB部分（暴力干货，建议收藏）_代码熬夜敲的博客-CSDN博客_强网杯题目](../../../cards/docs-2021-write-up-web-csdn.md) | 2021强网杯Write |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [31C3 CTF web关writeup_weixin_34019929的博客-CSDN博客](../../../cards/docs-31c3-ctf-web-writeup-weixin-34019929-csdn.md) | 31C3 CTF web关writeup |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [[CISCN 2023 华北]ez_date](../../../cards/web-ciscn2023-ez-date.md) | CISCN 2023 华北 |  | classical-crypto, deserialization, encoding-analysis, http-analysis |
| [[CISCN 2023 华北]pysym](../../../cards/web-ciscn2023-pysym.md) | CISCN 2023 华北 |  | classical-crypto, command-injection, encoding-analysis, http-analysis |
| [[GCCCTF 2025]守法公民](../../../cards/web-gccctf-2025.md) | GCCCTF 2025 |  | classical-crypto, crypto-analysis, encoding-analysis, web-exploitation |
| [[NISACTF 2022]popchains](../../../cards/web-nisactf2022-popchains.md) | NISACTF 2022 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [[NUSTCTF 2022 新生赛]Translate](../../../cards/web-nustctf2022-translate.md) | NUSTCTF 2022 新生赛 |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [[SDCTF 2022]jawt that down!](../../../cards/web-sdctf-2022-jawt-that-down.md) | SDCTF 2022 |  | browser-forensics, crypto-analysis, http-analysis, jwt-analysis |
| [[ZJCTF 2019]NiZhuanSiWei](../../../cards/web-zjctf2019-nizhuansiwei.md) | ZJCTF 2019 |  | classical-crypto, command-injection, deserialization, encoding-analysis |
| [[鹏城杯 2022]简单包含](../../../cards/web-2022.md) | 鹏城杯 2022 |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [ACTF题解_Mr_小白先生的博客-CSDN博客](../../../cards/docs-actf-mr-csdn.md) | ACTF题解 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [asp.net web submit链接页面_De1CTF2020的Web部分题解_weixin_39606137的博客-CSDN博客](../../../cards/docs-asp-net-web-submit-de1ctf2020-web-weixin-39606137-csdn.md) | asp.net web submit链接页面 |  | browser-forensics, command-injection, crypto-analysis, dns-analysis |
| [BUGKU CTF WEB (10-15题)_半夜好饿的博客-CSDN博客_bugkuctfweb题解](../../../cards/docs-bugku-ctf-web-10-15-csdn-bugkuctfweb.md) | BUGKU CTF WEB (10 |  | classical-crypto, crypto-analysis, encoding-analysis, web-exploitation |
| [Bugku CTF Web 解题报告二（16-20）_Vayn3的博客-CSDN博客](../../../cards/docs-bugku-ctf-web-16-20-vayn3-csdn.md) | Bugku CTF Web 解题报告二（16 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [Bugku CTF Web 解题报告（一）_Vayn3的博客-CSDN博客_bugku 金币](../../../cards/docs-bugku-ctf-web-vayn3-csdn-bugku.md) | Bugku CTF Web 解题报告（一） |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [BugkuCTF WEB解题记录 16-20_aap49042的博客-CSDN博客](../../../cards/docs-bugkuctf-web-16-20-aap49042-csdn.md) | BugkuCTF WEB解题记录 16 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [BugkuCTF WEB解题记录 16-20_weixin_30596735的博客-CSDN博客](../../../cards/docs-bugkuctf-web-16-20-weixin-30596735-csdn.md) | BugkuCTF WEB解题记录 16 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [bugkuCTF web进阶+web最后两题_goddemon的博客-CSDN博客](../../../cards/docs-bugkuctf-web-web-goddemon-csdn.md) | bugkuCTF web进阶+web最后两题 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [BugkuCTF 部分题解(一)_z.volcano的博客-CSDN博客_bugkuctf](../../../cards/docs-bugkuctf-z-volcano-csdn-bugkuctf.md) | BugkuCTF 部分题解(一) |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [BugkuCTF-WEB部分题解（一）_flying_bird2019的博客-CSDN博客_bugkuctfweb题解](../../../cards/docs-bugkuctf-web-flying-bird2019-csdn-bugkuctfweb.md) | BugkuCTF |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [BugkuCTF-WEB部分题解（二）_flying_bird2019的博客-CSDN博客](../../../cards/docs-bugkuctf-web-flying-bird2019-csdn.md) | BugkuCTF |  | classical-crypto, crypto-analysis, encoding-analysis, php-tricks |
| [BugkuCTF-WEB部分题解（四）_flying_bird2019的博客-CSDN博客](../../../cards/docs-bugkuctf-web-flying-bird2019-csdn.md) | BugkuCTF |  | classical-crypto, crypto-analysis, encoding-analysis, php-tricks |
| [BugkuCTF解题报告---WEB_jak0018的博客-CSDN博客](../../../cards/docs-bugkuctf-web-jak0018-csdn.md) | BugkuCTF解题报告 |  | browser-forensics, classical-crypto, command-injection, encoding-analysis |
| [Bugku—web题解_Sn0w/的博客-CSDN博客_bugku题解](../../../cards/docs-bugku-web-sn0w-csdn-bugku.md) | Bugku—web题解 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [bugku【welcome to bugkuctf】题解_大方子的博客-CSDN博客](../../../cards/docs-bugku-welcome-to-bugkuctf-csdn.md) | bugku【welcome to bugkuctf】题解 |  | classical-crypto, command-injection, deserialization, encoding-analysis |
| [BugKu题解备注（1）_s11show_163的博客-CSDN博客](../../../cards/docs-bugku-1-s11show-163-csdn.md) | BugKu题解备注（1） |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [BUUCTF [ACTF2020 新生赛]Include_是阿星呀的博客-CSDN博客](../../../cards/docs-buuctf-actf2020-include-csdn.md) | BUUCTF [ACTF2020 新生赛]Include |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [buuctf web小结_绿冰壶的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | buuctf web小结 |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [BUUCTF-[羊城杯]Easyser_moyuyyds的博客-CSDN博客](../../../cards/docs-buuctf-easyser-moyuyyds-csdn.md) | BUUCTF |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [BUUCTF-Crypto-Quoted-printable题解_ASSOINT的博客-CSDN博客](../../../cards/docs-buuctf-crypto-quoted-printable-assoint-csdn.md) | BUUCTF |  | crypto-analysis, http-analysis, web-exploitation |
| [BUUCTF-Web题解（一）_flying_bird2019的博客-CSDN博客_buuctfweb第一题](../../../cards/docs-buuctf-web-flying-bird2019-csdn-buuctfweb.md) | BUUCTF |  | classical-crypto, command-injection, deserialization, encoding-analysis |
| [BUUCTF__[EIS 2019]EzPOP_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-eis-2019-ezpop-csdn.md) | BUUCTF |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [BUUCTF__[GXYCTF2019]Ping Ping Ping_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-gxyctf2019-ping-ping-ping-csdn.md) | BUUCTF |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [BUUCTF__[HCTF 2018]admin_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-hctf-2018-admin-csdn.md) | BUUCTF |  | crypto-analysis, dns-analysis, encoding-analysis, http-analysis |
| [BUUCTF__[ZJCTF 2019]NiZhuanSiWei_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-zjctf-2019-nizhuansiwei-csdn.md) | BUUCTF |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [BUUCTF__web题解合集（一）_风过江南乱的博客-CSDN博客_buuctf web](../../../cards/docs-buuctf-web-csdn-buuctf-web.md) | BUUCTF |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [BUUCTF__web题解合集（七）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | classical-crypto, command-injection, deserialization, encoding-analysis |
| [BUUCTF__web题解合集（三）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | classical-crypto, command-injection, encoding-analysis, file-upload |
| [BUUCTF__web题解合集（九）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [BUUCTF__web题解合集（五）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [BUUCTF__web题解合集（八）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [BUUCTF__web题解合集（十一）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | browser-forensics, classical-crypto, command-injection, encoding-analysis |
| [BUUCTF__web题解合集（十二）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | binary-exploitation, classical-crypto, command-injection, encoding-analysis |
| [BUUCTF__web题解合集（十）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [BUUCTF__web题解合集（四）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [BUUCTF_web部分题解_ro4lsc的博客-CSDN博客](../../../cards/docs-buuctf-web-ro4lsc-csdn.md) | BUUCTF |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [BUUCTF全题解目录（一）_昂首下楼梯的博客-CSDN博客_buuctf答案](../../../cards/docs-buuctf-csdn-buuctf.md) | BUUCTF全题解目录（一） |  | classical-crypto, command-injection, deserialization, encoding-analysis |
| [BUUCTF寒假刷题-Web_深海神奇舰舰长的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF寒假刷题 |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [BUUCTF解题web十一道(03)_Sprint#51264的博客-CSDN博客](../../../cards/docs-buuctf-web-03-sprint-51264-csdn.md) | BUUCTF解题web十一道(03) |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [BUUCTF解题十一道(04)_Sprint#51264的博客-CSDN博客](../../../cards/docs-buuctf-04-sprint-51264-csdn.md) | BUUCTF解题十一道(04) |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [BUUCTF部分web题解（easysql，easy_tornado，Ping Ping Ping）_obsetear的博客-CSDN博客_ctf web题ping](../../../cards/docs-buuctf-web-easysql-easy-tornado-ping-ping-ping-obsetear-csdn-ctf-web-ping.md) | BUUCTF部分web题解（easysql，easy |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [Buuctf部分题解_君陌上的博客-CSDN博客_buuctf](../../../cards/docs-buuctf-csdn-buuctf.md) | Buuctf部分题解 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [buuoj部分web题解_Lionel_kai的博客-CSDN博客](../../../cards/docs-buuoj-web-lionel-kai-csdn.md) | buuoj部分web题解 |  | classical-crypto, command-injection, dns-analysis, encoding-analysis |
| [CG CTF WEB Download~!_Starzkg的博客-CSDN博客](../../../cards/docs-cg-ctf-web-download-starzkg-csdn.md) | CG CTF WEB Download~! |  | classical-crypto, crypto-analysis, encoding-analysis, symbolic-execution |
| [CG-CTF WEB 解题记录 6-10_aap49042的博客-CSDN博客](../../../cards/docs-cg-ctf-web-6-10-aap49042-csdn.md) | CG |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [ctf php 流量分析题,GKCTF EZWEB的分析题解和思考_一点能源的博客-CSDN博客](../../../cards/docs-ctf-php-gkctf-ezweb-csdn.md) | ctf php 流量分析题,GKCTF EZWEB的分析题解和思考 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [ctf show-web入门 php特性篇部分题解_z.volcano的博客-CSDN博客_ctfshow的php特性](../../../cards/docs-ctf-show-web-php-z-volcano-csdn-ctfshow-php.md) | ctf show |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [ctf web个人总结_recover517的博客-CSDN博客](../../../cards/docs-ctf-web-recover517-csdn.md) | ctf web个人总结 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF web入门——HTTP头相关的----修改请求头、伪造Cookie类题目——Bugku Web题目详细题解_日熙！的博客-CSDN博客_ctf请求头题目](../../../cards/docs-ctf-web-http-cookie-bugku-web-csdn-ctf.md) | CTF web入门——HTTP头相关的 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [CTF web题型解题技巧_吃素的小动物的博客-CSDN博客](../../../cards/docs-ctf-web-csdn.md) | CTF web题型解题技巧 |  | browser-forensics, crypto-analysis, file-inclusion, file-upload |
| [CTF 题型了解_秦罗敷写代码的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | CTF 题型了解 |  | binary-exploitation, crypto-analysis, http-analysis, misc-analysis |
| [CTF-2021中国能源网络WEB题目全解_wulanlin的博客-CSDN博客](../../../cards/docs-ctf-2021-web-wulanlin-csdn.md) | CTF |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF-rootme 题解之PHP filters_weixin_30384031的博客-CSDN博客](../../../cards/docs-ctf-rootme-php-filters-weixin-30384031-csdn.md) | CTF |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [CTF-rootme 题解之Python - pickle_weixin_30652879的博客-CSDN博客](../../../cards/docs-ctf-rootme-python-pickle-weixin-30652879-csdn.md) | CTF |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF-web 第十一部分 实用脚本_iamsongyu的博客-CSDN博客](../../../cards/docs-ctf-web-iamsongyu-csdn.md) | CTF |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [CTF-Web小白入门篇超详细——了解CTF-Web基本题型及其解题方法 总结——包含例题的详细题解_日熙！的博客-CSDN博客_ctf](../../../cards/docs-ctf-web-ctf-web-csdn-ctf.md) | CTF |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [CTF-入门九__starstarli的博客-CSDN博客](../../../cards/docs-ctf-starstarli-csdn.md) | CTF |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [CTF-加密与解密（十一）_红烧兔纸的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | CTF |  | command-injection, crypto-analysis, encoding-analysis, http-analysis |
| [CTF-加密与解密（十九）_红烧兔纸的博客-CSDN博客_ctf中txt文件的解密过程](../../../cards/docs-ctf-csdn-ctf-txt.md) | CTF |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [CTF-加密与解密（十六）_红烧兔纸的博客-CSDN博客_文本加密为音乐符号](../../../cards/docs-ctf-csdn.md) | CTF |  | crypto-analysis, http-analysis, web-exploitation |
| [ctf.show crypto题解_��阿兮��的博客-CSDN博客_ctf秀crypto6](../../../cards/docs-ctf-show-crypto-csdn-ctf-crypto6.md) | ctf.show crypto题解 |  | crypto-analysis, http-analysis, php-tricks, web-exploitation |
| [CTF_Web：8位以内可控字符getshell_星辰照耀你我的博客-CSDN博客_ctf getshell](../../../cards/docs-ctf-web-8-getshell-csdn-ctf-getshell.md) | CTF |  | classical-crypto, command-injection, encoding-analysis, web-exploitation |
| [ctfhub技能书+历年真题学习笔记（详解）_Yn8rt的博客-CSDN博客](../../../cards/docs-ctfhub-yn8rt-csdn.md) | ctfhub技能书+历年真题学习笔记（详解） |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF|BugkuCTF-WEB解题思路_「已注销」的博客-CSDN博客_bugkuctfweb题解](../../../cards/docs-ctf-bugkuctf-web-csdn-bugkuctfweb.md) | CTF|BugkuCTF |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [CTF专题一2021网络WEB题目解析_普通网友的博客-CSDN博客_ctf web分析](../../../cards/docs-ctf-2021-web-csdn-ctf-web.md) | CTF专题一2021网络WEB题目解析 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF中Web找Flag题目（1）_「已注销」的博客-CSDN博客_web找flag](../../../cards/docs-ctf-web-flag-1-csdn-web-flag.md) | CTF中Web找Flag题目（1） |  | classical-crypto, crypto-analysis, encoding-analysis, web-exploitation |
| [CTF入门第一课(附一道小题)_anquanniu牛油果的博客-CSDN博客](../../../cards/docs-ctf-anquanniu-csdn.md) | CTF入门第一课(附一道小题) |  | binary-exploitation, crypto-analysis, image-analysis, misc-analysis |
| [CTF刷题02_Atkxor的博客-CSDN博客](../../../cards/docs-ctf-02-atkxor-csdn.md) | CTF刷题02 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [CTF学习-web解题思路_菜鸟-传奇的博客-CSDN博客](../../../cards/docs-ctf-web-csdn.md) | CTF学习 |  | browser-forensics, classical-crypto, crypto-analysis, dns-analysis |
| [CTF实验吧-WEB专题-5_77458的博客-CSDN博客](../../../cards/docs-ctf-web-5-77458-csdn.md) | CTF实验吧 |  | classical-crypto, encoding-analysis, php-tricks, qr-analysis |
| [CTF平台题库writeup（四）--BugKuCTF-代码审计（14题详解）_Hacking黑白红的博客-CSDN博客](../../../cards/docs-ctf-writeup-bugkuctf-14-hacking-csdn.md) | CTF平台题库writeup（四） |  | classical-crypto, encoding-analysis, file-inclusion, http-analysis |
| [ctf每日练习-第10天__wand1的博客-CSDN博客](../../../cards/docs-ctf-10-wand1-csdn.md) | ctf每日练习 |  | classical-crypto, command-injection, encoding-analysis, http-analysis |
| [CTF解题-2020年强网杯参赛WriteUp_Tr0e的博客-CSDN博客_ctf解题赛](../../../cards/docs-ctf-2020-writeup-tr0e-csdn-ctf.md) | CTF解题 |  | classical-crypto, command-injection, deserialization, encoding-analysis |
| [CTF解题-Bugku_Web_WriteUp (上）_Tr0e的博客-CSDN博客_bugku web writeup](../../../cards/docs-ctf-bugku-web-writeup-tr0e-csdn-bugku-web-writeup.md) | CTF解题 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF解题-Bugku_Web_WriteUp (下）_Tr0e的博客-CSDN博客](../../../cards/docs-ctf-bugku-web-writeup-tr0e-csdn.md) | CTF解题 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [CTF解题思路笔记_山兔1的博客-CSDN博客_ctf解题](../../../cards/docs-ctf-1-csdn-ctf.md) | CTF解题思路笔记 |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [CTF解题思路： 数据包相关题目_tiny丶的博客-CSDN博客](../../../cards/docs-ctf-tiny-csdn.md) | CTF解题思路： 数据包相关题目 |  | classical-crypto, encoding-analysis, http-analysis, web-exploitation |
| [ctf训练 web安全暴力破解_爱吃香菜的哈哈的博客-CSDN博客](../../../cards/docs-ctf-web-csdn.md) | ctf训练 web安全暴力破解 |  | crypto-analysis, http-analysis, password-cracking, privilege-escalation |
| [CTF论剑场web解题_梳刘海的杰瑞的博客-CSDN博客](../../../cards/docs-ctf-web-csdn.md) | CTF论剑场web解题 |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [ctf赛题secret.php,记一场纯JS赛——DiceCTF2021 Web题解_自强自在的博客-CSDN博客](../../../cards/docs-ctf-secret-php-js-dicectf2021-web-csdn.md) | ctf |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [ctl文件去空格_CTF从入门到提升（十三）文件包含session及例题详解_weixin_39964869的博客-CSDN博客](../../../cards/docs-ctl-ctf-session-weixin-39964869-csdn.md) | ctl文件去空格 |  | classical-crypto, crypto-analysis, encoding-analysis, file-inclusion |
| [D^3CTF(Crypto-D3bug详解 LFSR题目）_Mango|Feng的博客-CSDN博客](../../../cards/docs-d-3ctf-crypto-d3bug-lfsr-mango-feng-csdn.md) | D^3CTF(Crypto |  | crypto-analysis, http-analysis, symbolic-execution, web-exploitation |
| [De1CTF2020的Web部分题解_合天网安实验室的博客-CSDN博客](../../../cards/docs-de1ctf2020-web-csdn.md) | De1CTF2020的Web部分题解 |  | binary-exploitation, browser-forensics, command-injection, crypto-analysis |
| [hgame ctf week2--shinyshot题解_weixin_30753873的博客-CSDN博客](../../../cards/docs-hgame-ctf-week2-shinyshot-weixin-30753873-csdn.md) | hgame ctf week2 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [HITCTF2018-web全题解_合天网安实验室的博客-CSDN博客](../../../cards/docs-hitctf2018-web-csdn.md) | HITCTF2018 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [hxp 36C3 CTF Web题 WriteupBin Writeup (Selenium模拟点击+Content Security Policy+Nonce+Parsley.js触发错误提示)_KevinLuo2000的博客-CSDN博客](../../../cards/docs-hxp-36c3-ctf-web-writeupbin-writeup-selenium-content-security-policy-nonce-parsley-js-kevinluo2000-csdn.md) | hxp 36C3 CTF Web |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [i春秋 百度杯”CTF比赛（二月场） Misc&&web题解 By Assassin_Assassin__is__me的博客-CSDN博客](../../../cards/docs-i-ctf-misc-web-by-assassin-assassin-is-me-csdn.md) | i春秋 |  | binary-exploitation, classical-crypto, command-injection, encoding-analysis |
| [i春秋CTF-WEB题解(二)_ 晓德的博客-CSDN博客](../../../cards/docs-i-ctf-web-csdn.md) | i春秋CTF |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [I春秋CTF训练营web题解（一）_Super_Yiang的博客-CSDN博客](../../../cards/docs-i-ctf-web-super-yiang-csdn.md) | I春秋CTF训练营web题解（一） |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [i春秋网络内生安全试验场CTF夺旗赛（第四季）12月赛web write up题解_努力的学渣'#的博客-CSDN博客](../../../cards/docs-i-ctf-12-web-write-up-csdn.md) | i春秋网络内生安全试验场CTF夺旗赛（第四季）12月赛web |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [NJCTF2017 线上赛 web 题解 By Assassin_Assassin__is__me的博客-CSDN博客](../../../cards/docs-njctf2017-web-by-assassin-assassin-is-me-csdn.md) | NJCTF2017 线上赛 web 题解 By Assassin |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [P.W.N. CTF - Web - Login Sec_weixin_30778805的博客-CSDN博客](../../../cards/docs-p-w-n-ctf-web-login-sec-weixin-30778805-csdn.md) | P.W.N. CTF |  | crypto-analysis, dns-analysis, file-inclusion, http-analysis |
| [php ctf题解,国际赛-N1CTF 2018-Web题解_无敌小羊历险记的博客-CSDN博客](../../../cards/docs-php-ctf-n1ctf-2018-web-csdn.md) | php ctf题解,国际赛 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [php伪随机数 ctf,从一道ctf题目理解rand()随机函数_Ma Daniel的博客-CSDN博客](../../../cards/docs-php-ctf-ctf-rand-ma-daniel-csdn.md) | php伪随机数 ctf,从一道ctf题目理解rand()随机函数 |  | classical-crypto, crypto-analysis, http-analysis, reverse-engineering |
| [php安全挑战赛,BiliBili1024安全挑战赛题目及解答(关联ctf)_Deep Yao的博客-CSDN博客](../../../cards/docs-php-bilibili1024-ctf-deep-yao-csdn.md) | php安全挑战赛,BiliBili1024安全挑战赛题目及解答(关联ctf) |  | browser-forensics, crypto-analysis, http-analysis, php-tricks |
| [PHP签到](../../../cards/web-gccctf-2025-php.md) | GCCCTF 2025 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [python 重定向 ctf_CTF web题型解题技巧 第四课 web总结_weixin_39615984的博客-CSDN博客](../../../cards/docs-python-ctf-ctf-web-web-weixin-39615984-csdn.md) | python 重定向 ctf |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [python 重定向 ctf_CTF-rootme 题解之Python - pickle_深夜利行的博客-CSDN博客](../../../cards/docs-python-ctf-ctf-rootme-python-pickle-csdn.md) | python 重定向 ctf |  | classical-crypto, crypto-analysis, deserialization, encoding-analysis |
| [RoarCTFweb题解_qq_41575340的博客-CSDN博客](../../../cards/docs-roarctfweb-qq-41575340-csdn.md) | RoarCTFweb题解 |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [S3cCTF-gyy-Writeup_Err0rCM的博客-CSDN博客](../../../cards/docs-s3cctf-gyy-writeup-err0rcm-csdn.md) | S3cCTF |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [SUCTF_2019部分题解复现_FFM-G的博客-CSDN博客](../../../cards/docs-suctf-2019-ffm-g-csdn.md) | SUCTF |  | browser-forensics, classical-crypto, command-injection, encoding-analysis |
| [SWPUCTF web 部分题解_HyyMbb的博客-CSDN博客](../../../cards/docs-swpuctf-web-hyymbb-csdn.md) | SWPUCTF web 部分题解 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [there is nothing（i春秋CTF题解）_weixin_30258027的博客-CSDN博客](../../../cards/docs-there-is-nothing-i-ctf-weixin-30258027-csdn.md) | there is nothing（i春秋CTF题解） |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [TWCTF 2016 (Tokyo Westerns CTF ) WEB WriteUp_Bendawang的博客-CSDN博客](../../../cards/docs-twctf-2016-tokyo-westerns-ctf-web-writeup-bendawang-csdn.md) | TWCTF 2016 |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [UNCTF2020web方向部分题解_bmth666的博客-CSDN博客](../../../cards/docs-unctf2020web-bmth666-csdn.md) | UNCTF2020web方向部分题解 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [web 计算器_De1CTF2020的Web部分题解_weixin_39924307的博客-CSDN博客](../../../cards/docs-web-de1ctf2020-web-weixin-39924307-csdn.md) | web 计算器 |  | browser-forensics, command-injection, crypto-analysis, dns-analysis |
| [welcome to bugkuctf（详解）——Bugku_weixin_33728268的博客-CSDN博客](../../../cards/docs-welcome-to-bugkuctf-bugku-weixin-33728268-csdn.md) | welcome to bugkuctf（详解）——Bugku |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [【BUUCTF刷题】Web解题方法总结（一)_Y1seco的博客-CSDN博客_buuctfweb](../../../cards/docs-buuctf-web-y1seco-csdn-buuctfweb.md) | 【BUUCTF刷题】Web解题方法总结（一) |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [【CTF】关于SQL盲注的细节_publicStr的博客-CSDN博客](../../../cards/docs-ctf-sql-publicstr-csdn.md) | 【CTF】关于SQL盲注的细节 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [【CTF】加解密专题_BJFU_vth的博客-CSDN博客](../../../cards/docs-ctf-bjfu-vth-csdn.md) | 【CTF】加解密专题 |  | classical-crypto, crypto-analysis, encoding-analysis |
| [【CTF】基础常识_你们这样一点都不可耐的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | 【CTF】基础常识 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [【vishwaCTF】web题解wp_Sunlight_316的博客-CSDN博客](../../../cards/docs-vishwactf-web-wp-sunlight-316-csdn.md) | 【vishwaCTF】web题解wp |  | command-injection, crypto-analysis, deserialization, encoding-analysis |
| [〖教程〗K8飞刀-网络安全CTF解题Web篇10个例子_k8gege的博客-CSDN博客](../../../cards/docs-k8-ctf-web-10-k8gege-csdn.md) | 〖教程〗K8飞刀 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [〖教程〗K8飞刀-网络安全CTF解题Web篇10例_k8gege的博客-CSDN博客_k8飞刀](../../../cards/docs-k8-ctf-web-10-k8gege-csdn-k8.md) | 〖教程〗K8飞刀 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [一个ctf题目解析，关于des(unix)解密_qzxdh的博客-CSDN博客_ctf des](../../../cards/docs-ctf-des-unix-qzxdh-csdn-ctf-des.md) | 一个ctf题目解析，关于des(unix)解密 |  | command-injection, crypto-analysis, http-analysis, password-cracking |
| [一道CTF题看JWT和python反序列化_weixin_44377940的博客-CSDN博客_jwt反序列化](../../../cards/docs-ctf-jwt-python-weixin-44377940-csdn-jwt.md) | 一道CTF题看JWT和python反序列化 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [一道简单的CTF登录题题解_anquanniu牛油果的博客-CSDN博客_ctf login题目](../../../cards/docs-ctf-anquanniu-csdn-ctf-login.md) | 一道简单的CTF登录题题解 |  | classical-crypto, crypto-analysis, deserialization, encoding-analysis |
| [信息安全web入门——南邮ctf解题_sevenlob的博客-CSDN博客_南邮ctf](../../../cards/docs-web-ctf-sevenlob-csdn-ctf.md) | 信息安全web入门——南邮ctf解题 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [初遇z3并与starCTF碰面_黑羽re的博客-CSDN博客](../../../cards/docs-z3-starctf-re-csdn.md) | 初遇z3并与starCTF碰面 |  | crypto-analysis, sql-injection, symbolic-execution, web-exploitation |
| [利用文件名进行GetShell---CTF题目的相关知识解析_xuchen16的博客-CSDN博客_后台getshell](../../../cards/docs-getshell-ctf-xuchen16-csdn-getshell.md) | 利用文件名进行GetShell |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [南京邮电大学CG-CTF平台Writeup_Gard3nia的博客-CSDN博客_cgctf平台](../../../cards/docs-cg-ctf-writeup-gard3nia-csdn-cgctf.md) | 南京邮电大学CG |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [南邮CTF-web第一篇_萌萌哒的baola的博客-CSDN博客](../../../cards/docs-ctf-web-baola-csdn.md) | 南邮CTF |  | classical-crypto, command-injection, dns-analysis, encoding-analysis |
| [南邮ctf平台部分题解_这是游戏吗的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | 南邮ctf平台部分题解 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [哔哩哔哩1024安全挑战赛 Bilibili CTF题解(含代码)_一口快乐水的博客-CSDN博客](../../../cards/docs-1024-bilibili-ctf-csdn.md) | 哔哩哔哩1024安全挑战赛 Bilibili CTF题解(含代码) |  | browser-forensics, crypto-analysis, http-analysis, php-tricks |
| [如何在ctf解题实战中绕过disable_function_YnG_t0的博客-CSDN博客_disablefunctions 绕过](../../../cards/docs-ctf-disable-function-yng-t0-csdn-disablefunctions.md) | 如何在ctf解题实战中绕过disable |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [平时练习 ctf 解题报告 web类_白山茶i的博客-CSDN博客](../../../cards/docs-ctf-web-i-csdn.md) | 平时练习 ctf 解题报告 web类 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [当堂XSS-labs 挑战](../../../cards/web-xss-labs.md) | 当堂XSS |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [技能五子棋](../../../cards/web-gccctf-2025.md) | GCCCTF 2025 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [春秋web题目解题及思路汇总（自用搜集）_香草星冰乐的博客-CSDN博客](../../../cards/docs-web-csdn.md) | 春秋web题目解题及思路汇总（自用搜集） |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [第四届“”世安杯“”线上赛题解（Web+Stego+Misc+Crypto）_Assassin__is__me的博客-CSDN博客](../../../cards/docs-web-stego-misc-crypto-assassin-is-me-csdn.md) | 第四届“”世安杯“”线上赛题解（Web+Stego+Misc+Crypto） |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [蓝鲸CTF-web-密码泄露_烟雨天青色的博客-CSDN博客](../../../cards/docs-ctf-web-csdn.md) | 蓝鲸CTF |  | classical-crypto, encoding-analysis, web-exploitation, xss |
| [西普学院CTF习题解析——WEB(已完成16/16)_Xyntax的博客-CSDN博客](../../../cards/docs-ctf-web-16-16-xyntax-csdn.md) | 西普学院CTF习题解析——WEB(已完成16/16) |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [西邮ctf2020 web之文件包含解析_落雪wink的博客-CSDN博客](../../../cards/docs-ctf2020-web-wink-csdn.md) | 西邮ctf2020 web之文件包含解析 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [解网鼎杯一道web题（fakebook）_诸神之眼的博客-CSDN博客_fakebook](../../../cards/docs-web-fakebook-csdn-fakebook.md) | 解网鼎杯一道web题（fakebook） |  | browser-forensics, classical-crypto, deserialization, encoding-analysis |
| [记一次院赛CTF的WEB题（入门级别）_CTF小白的博客-CSDN博客_ctf web解题 找flag](../../../cards/docs-ctf-web-ctf-csdn-ctf-web-flag.md) | 记一次院赛CTF的WEB题（入门级别） |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [静默开水的博客_CSDN博客-CTF,web题解题思路,Misc 图片隐写领域博主](../../../cards/docs-csdn-ctf-web-misc.md) | 静默开水的博客 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
