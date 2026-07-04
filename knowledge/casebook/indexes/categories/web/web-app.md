# Web / web-app

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| web-exploitation | 320 | http evidence extraction, netcat-driven evidence lookup, sql injection exploitation, file inclusion exploitation, command execution path |
| http-analysis | 253 | http evidence extraction, netcat-driven evidence lookup, sql injection exploitation, file inclusion exploitation, command execution path |
| command-injection | 181 | http evidence extraction, file inclusion exploitation, command execution path, netcat-driven evidence lookup, sql injection exploitation |
| waf-bypass | 156 | http evidence extraction, sql injection exploitation, waf bypass, netcat-driven evidence lookup, file inclusion exploitation |
| encoding-analysis | 152 | http evidence extraction, file inclusion exploitation, netcat-driven evidence lookup, sql injection exploitation, cipher decoding |
| crypto-analysis | 148 | http evidence extraction, netcat-driven evidence lookup, sql injection exploitation, burp-driven evidence lookup, cipher decoding |
| classical-crypto | 135 | http evidence extraction, netcat-driven evidence lookup, file inclusion exploitation, cipher decoding, sql injection exploitation |
| php-tricks | 132 | http evidence extraction, sql injection exploitation, netcat-driven evidence lookup, burp-driven evidence lookup, deserialization chain |
| sql-injection | 126 | http evidence extraction, sql injection exploitation, netcat-driven evidence lookup, burp-driven evidence lookup, file inclusion exploitation |
| file-inclusion | 117 | http evidence extraction, file inclusion exploitation, netcat-driven evidence lookup, sql injection exploitation, detect-it-easy-driven evidence lookup |
| file-upload | 82 | http evidence extraction, file upload bypass, sql injection exploitation, netcat-driven evidence lookup, burp-driven evidence lookup |
| dns-analysis | 62 | http evidence extraction, sql injection exploitation, detect-it-easy-driven evidence lookup, netcat-driven evidence lookup, file inclusion exploitation |
| deserialization | 57 | http evidence extraction, deserialization chain, sql injection exploitation, netcat-driven evidence lookup, burp-driven evidence lookup |
| ret2libc | 54 | http evidence extraction, command execution path, file inclusion exploitation, detect-it-easy-driven evidence lookup, netcat-driven evidence lookup |
| ssti | 51 | http evidence extraction, ssti exploitation, netcat-driven evidence lookup, file inclusion exploitation, sql injection exploitation |
| binary-exploitation | 38 | http evidence extraction, sql injection exploitation, command execution path, netcat-driven evidence lookup, file inclusion exploitation |
| xss | 35 | http evidence extraction, sql injection exploitation, xss route, burp-driven evidence lookup, netcat-driven evidence lookup |
| browser-forensics | 33 | http evidence extraction, burp-driven evidence lookup, detect-it-easy-driven evidence lookup, sql injection exploitation, file upload bypass |
| misc-analysis | 33 | http evidence extraction, cipher decoding, command execution path, sql injection exploitation, detect-it-easy-driven evidence lookup |
| service-enumeration | 29 | http evidence extraction, sql injection exploitation, command execution path, file inclusion exploitation, netcat-driven evidence lookup |
| qr-analysis | 21 | http evidence extraction, cipher decoding, sql injection exploitation, deserialization chain, detect-it-easy-driven evidence lookup |
| jwt-analysis | 18 | http evidence extraction, netcat-driven evidence lookup, sql injection exploitation, command execution path, deserialization chain |
| reverse-engineering | 15 | reverse engineering, http evidence extraction, cipher decoding, file inclusion exploitation, command execution path |
| symbolic-execution | 13 | http evidence extraction, sql injection exploitation, cipher decoding, constraint solving, deserialization chain |
| image-analysis | 12 | http evidence extraction, cipher decoding, ssti exploitation, waf bypass, command execution path |
| traffic-analysis | 11 | http evidence extraction, cipher decoding, sql injection exploitation, burp-driven evidence lookup, command execution path |
| osint | 8 | http evidence extraction, burp-driven evidence lookup, waf bypass, cipher decoding, evidence lookup |
| password-cracking | 8 | http evidence extraction, command execution path, sql injection exploitation, burp-driven evidence lookup, file inclusion exploitation |
| timeline-analysis | 7 | http evidence extraction, netcat-driven evidence lookup, command execution path, deserialization chain, file inclusion exploitation |
| network-forensics | 6 | http evidence extraction, cipher decoding, command execution path, detect-it-easy-driven evidence lookup, sql injection exploitation |
| stego-extraction | 6 | http evidence extraction, deserialization chain, command execution path, reverse engineering, ssti exploitation |
| web-enumeration | 6 | http evidence extraction, burp-driven evidence lookup, deserialization chain, sql injection exploitation, ssti exploitation |
| privilege-escalation | 5 | file inclusion exploitation, http evidence extraction, command execution path, netcat-driven evidence lookup, credential discovery |
| mobile-forensics | 4 | command execution path, detect-it-easy-driven evidence lookup, evidence lookup, file inclusion exploitation, http evidence extraction |
| stack-overflow | 4 | burp-driven evidence lookup, cipher decoding, deserialization chain, file upload bypass, http evidence extraction |
| format-string | 3 | burp-driven evidence lookup, command execution path, deserialization chain, detect-it-easy-driven evidence lookup, http evidence extraction |
| malware-static | 3 | http evidence extraction, burp-driven evidence lookup, capa-driven evidence lookup, credential discovery, deserialization chain |
| ret2text | 3 | file upload bypass, http evidence extraction, burp-driven evidence lookup, netcat-driven evidence lookup, reverse engineering |
| email-header-analysis | 2 | burp-driven evidence lookup, http evidence extraction, waf bypass |
| integer-overflow | 2 | command execution path, http evidence extraction, credential discovery, deserialization chain, file inclusion exploitation |
| maldoc-analysis | 1 | command execution path, http evidence extraction, maldoc analysis, netcat-driven evidence lookup, sql injection exploitation |
| memory-forensics | 1 | burp-driven evidence lookup, cipher decoding, deserialization chain, http evidence extraction |
| siem-query | 1 | cipher decoding, elk-driven evidence lookup, indicator enrichment, xss route |
| stream-cipher | 1 | cipher decoding, http evidence extraction, reverse engineering, sql injection exploitation, stego extraction |

## Route Types

| Route type | Cases |
| --- | --- |
| http evidence extraction | 230 |
| netcat-driven evidence lookup | 98 |
| sql injection exploitation | 92 |
| file inclusion exploitation | 70 |
| evidence lookup | 68 |
| command execution path | 64 |
| burp-driven evidence lookup | 58 |
| waf bypass | 52 |
| file upload bypass | 50 |
| cipher decoding | 48 |
| detect-it-easy-driven evidence lookup | 46 |
| deserialization chain | 36 |
| ssti exploitation | 36 |
| credential discovery | 24 |
| xss route | 16 |
| reverse engineering | 14 |
| dns pivot | 10 |
| PHP环境-driven evidence lookup | 6 |
| Yakit-driven evidence lookup | 6 |
| jwt trust-boundary abuse | 4 |
| sqlmap-driven evidence lookup | 4 |
| constraint solving | 3 |
| indicator enrichment | 3 |
| nmap-driven evidence lookup | 3 |
| stego extraction | 3 |
| 无-driven evidence lookup | 3 |
| gdb-driven evidence lookup | 2 |
| incident timeline reconstruction | 2 |
| timeline reconstruction | 2 |
| z3-driven evidence lookup | 2 |
| antsword-driven evidence lookup | 1 |
| binwalk-driven evidence lookup | 1 |
| capa-driven evidence lookup | 1 |
| conversation statistics | 1 |
| dirb-driven evidence lookup | 1 |
| elk-driven evidence lookup | 1 |
| foremost-driven evidence lookup | 1 |
| hashcat-driven evidence lookup | 1 |
| john-driven evidence lookup | 1 |
| maldoc analysis | 1 |
| memory artifact analysis | 1 |
| python2 环境-driven evidence lookup | 1 |
| python环境-driven evidence lookup | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [+ 未分类](../../../cards/summary.md) | SUMMARY.md |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [12 题解](../../../cards/web-cuc-training-20250212.md) | cuc |  | deserialization, http-analysis, web-exploitation |
| [17 题解](../../../cards/web-cuc-training-20250117.md) | cuc |  | http-analysis, malware-static, sql-injection, ssti |
| [19 题解](../../../cards/web-cuc-training-20250319.md) | cuc |  | http-analysis, web-exploitation |
| [2018 SCUCTF web题：cat？非常规题解_东坡何罪发文章总是审核不通过，去博客园了的博客-CSDN博客](../../../cards/docs-2018-scuctf-web-cat-csdn.md) | 2018 SCUCTF web题：cat？非常规题解 |  | http-analysis, web-exploitation |
| [2019 0CTF/TCTF wallbreaker easy 题目理解_youGuess28的博客-CSDN博客](../../../cards/docs-2019-0ctf-tctf-wallbreaker-easy-youguess28-csdn.md) | 2019 0CTF/TCTF wallbreaker easy 题目理解 |  | dns-analysis, http-analysis, php-tricks, waf-bypass |
| [2019 D3CTF ezupload题解_slug01sh的博客-CSDN博客](../../../cards/docs-2019-d3ctf-ezupload-slug01sh-csdn.md) | 2019 D3CTF ezupload题解 |  | classical-crypto, command-injection, deserialization, encoding-analysis |
| [2019 D^3CTF_wp：fakeonlinephp解法（类实网渗透）_Smity(Liu)的博客-CSDN博客](../../../cards/docs-2019-d-3ctf-wp-fakeonlinephp-smity-liu-csdn.md) | 2019 D^3CTF |  | command-injection, dns-analysis, file-inclusion, http-analysis |
| [2019SCUCTF部分题解_东坡何罪发文章总是审核不通过，去博客园了的博客-CSDN博客](../../../cards/docs-2019scuctf-csdn.md) | 2019SCUCTF部分题解 |  | binary-exploitation, classical-crypto, crypto-analysis, deserialization |
| [2020年1月-*CTF比赛Web部分题解_slug01sh的博客-CSDN博客](../../../cards/docs-2020-1-ctf-web-slug01sh-csdn.md) | 2020年1月 |  | command-injection, crypto-analysis, dns-analysis, file-upload |
| [2020年DDCTF-web签到题题解_slug01sh的博客-CSDN博客](../../../cards/docs-2020-ddctf-web-slug01sh-csdn.md) | 2020年DDCTF |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [2020易博霖CTFWeb2--SSRF题解_flying_bird2019的博客-CSDN博客](../../../cards/docs-2020-ctfweb2-ssrf-flying-bird2019-csdn.md) | 2020易博霖CTFWeb2 |  | classical-crypto, crypto-analysis, dns-analysis, encoding-analysis |
| [2021强网杯Write-Up真题解析之WEB部分（暴力干货，建议收藏）_代码熬夜敲的博客-CSDN博客_强网杯题目](../../../cards/docs-2021-write-up-web-csdn.md) | 2021强网杯Write |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [2021虎符初赛Web部分题解_bfengj的博客-CSDN博客](../../../cards/docs-2021-web-bfengj-csdn.md) | 2021虎符初赛Web部分题解 |  | command-injection, crypto-analysis, http-analysis, maldoc-analysis |
| [22 题解](../../../cards/web-cuc-training-20250122.md) | cuc |  | file-inclusion, file-upload, http-analysis, web-exploitation |
| [24 题解](../../../cards/web-cuc-training-20250124.md) | cuc |  | http-analysis, web-exploitation |
| [31C3 CTF web关writeup_weixin_34019929的博客-CSDN博客](../../../cards/docs-31c3-ctf-web-writeup-weixin-34019929-csdn.md) | 31C3 CTF web关writeup |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [6um1n的博客_CSDN博客-Python,CTF题解,WEB安全领域博主](../../../cards/docs-6um1n-csdn-python-ctf-web.md) | 6um1n的博客 |  | web-exploitation |
| [[0CTF 2016] piapiapia 题解_lonmar~的博客-CSDN博客](../../../cards/docs-0ctf-2016-piapiapia-lonmar-csdn.md) | 0CTF 2016 |  | deserialization, file-upload, http-analysis, php-tricks |
| [[AFCTF 2021]BABY_CSP](../../../cards/web-afctf-2021baby-csp.md) | AFCTF 2021 | 简单 | http-analysis, waf-bypass, web-exploitation, xss |
| [[BUUCTF 2018]Online Tool 题解_偷一个月亮的博客-CSDN博客](../../../cards/docs-buuctf-2018-online-tool-csdn.md) | BUUCTF 2018 |  | command-injection, http-analysis, php-tricks, ret2libc |
| [[BUUCTF 2018]Online Tool_Sk1y的博客-CSDN博客](../../../cards/docs-buuctf-2018-online-tool-sk1y-csdn.md) | BUUCTF 2018 |  | command-injection, http-analysis, php-tricks, ret2libc |
| [[CISCN 2019华东南]Web4](../../../cards/web-ciscn2019-web4.md) | CISCN 2019华东南 |  | crypto-analysis, encoding-analysis, http-analysis, ssti |
| [[CISCN 2023 华北]ez_date](../../../cards/web-ciscn2023-ez-date.md) | CISCN 2023 华北 |  | classical-crypto, deserialization, encoding-analysis, http-analysis |
| [[CISCN 2023 华北]pysym](../../../cards/web-ciscn2023-pysym.md) | CISCN 2023 华北 |  | classical-crypto, command-injection, encoding-analysis, http-analysis |
| [[FSCTF 2023]加速加速](../../../cards/web-fsctf-2023.md) | FSCTF 2023 |  | command-injection, file-inclusion, file-upload, http-analysis |
| [[FSCTF 2023]巴巴托斯！](../../../cards/web-random.md) | FSCTF 2023 |  | browser-forensics, file-inclusion, http-analysis, web-exploitation |
| [[FSCTF 2023]是兄弟，就来传你の🐎！](../../../cards/web-fsctf-2023.md) | FSCTF 2023 |  | command-injection, file-upload, http-analysis, waf-bypass |
| [[GDOUCTF 2023]受不了一点](../../../cards/web-gdouctf2023.md) | GDOUCTF 2023 |  | http-analysis, php-tricks, waf-bypass, web-exploitation |
| [[GHCTF 2024 新生赛]理想国](../../../cards/web-ghctf2024.md) | GHCTF 2024 新生赛 |  | command-injection, crypto-analysis, http-analysis, jwt-analysis |
| [[GKCTF 2020]老八小超市儿](../../../cards/web-gkctf-2020.md) | GKCTF 2020 |  | command-injection, http-analysis, misc-analysis, ret2libc |
| [[GXYCTF2019]BabyUpload 题解_偷一个月亮的博客-CSDN博客](../../../cards/docs-gxyctf2019-babyupload-csdn.md) | GXYCTF2019 |  | file-upload, http-analysis, web-exploitation |
| [[HCTF 2018]WarmUp 题解_偷一个月亮的博客-CSDN博客_hctf warmup](../../../cards/docs-hctf-2018-warmup-csdn-hctf-warmup.md) | HCTF 2018 |  | command-injection, file-inclusion, http-analysis, web-exploitation |
| [[HDCTF 2023]LoginMaster](../../../cards/web-hdctf2023-loginmaster.md) | HDCTF 2023 |  | http-analysis, sql-injection, waf-bypass, web-exploitation |
| [[HNCTF 2022 WEEK2]easy_include](../../../cards/web-hnctf2022week2-easy-include.md) | HNCTF 2022 WEEK2 |  | command-injection, file-inclusion, http-analysis, web-exploitation |
| [[HNCTF 2022 WEEK2]easy_sql](../../../cards/web-hnctf-2022-week2-easy-sql.md) | HNCTF 2022 WEEK2 |  | http-analysis, sql-injection, waf-bypass, web-exploitation |
| [[MoeCTF 2021]地狱通讯-改](../../../cards/web-moectf-2021.md) | MoeCTF 2021 |  | crypto-analysis, format-string, http-analysis, jwt-analysis |
| [[NISACTF 2022]popchains](../../../cards/web-nisactf2022-popchains.md) | NISACTF 2022 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [[NSSCTF 2022]ezgame](../../../cards/web-nssctf2022ezgame.md) | NSSCTF 2022 | 轻松 | http-analysis, web-exploitation |
| [[NSSRound#13]TimeTrcer](../../../cards/web-nssround-13timetrcer.md) | NSSRound#13 | 困难 | command-injection, crypto-analysis, http-analysis, web-exploitation |
| [[NSSRound#18]门酱想玩什么呢](../../../cards/web-nssround-18.md) | NSSRound#18 | 中等 | dns-analysis, http-analysis, waf-bypass, web-exploitation |
| [[NSSRound#30 Duo]hack_the_world!](../../../cards/web-nssround-30-duo-hack-the-world.md) | NSSRound#30 Duo |  | dns-analysis, http-analysis, jwt-analysis, ssti |
| [[NSSRound#30 Duo]你也是迷宫高手吗](../../../cards/web-nssround-30-duo.md) | NSSRound#30 Duo |  | binary-exploitation, command-injection, crypto-analysis, http-analysis |
| [[NSSRound_16 Basic]了解过PHP特性吗](../../../cards/web-nssround-16-basic-php.md) | NSSRound_16 Basic |  | command-injection, file-inclusion, http-analysis, php-tricks |
| [[NUSTCTF 2022 新生赛]Translate](../../../cards/web-nustctf2022-translate.md) | NUSTCTF 2022 新生赛 |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [[SDCTF 2022]jawt that down!](../../../cards/web-sdctf-2022-jawt-that-down.md) | SDCTF 2022 |  | browser-forensics, crypto-analysis, http-analysis, jwt-analysis |
| [[SWPUCTF 2021 新生赛]babyunser](../../../cards/web-swpuctf-2021-babyunser.md) | SWPUCTF 2021 新生赛 |  | command-injection, crypto-analysis, deserialization, file-upload |
| [[SWPUCTF 2021 新生赛]easyupload1.0](../../../cards/web-swpuctf2021-easyupload1-0.md) | SWPUCTF 2021 新生赛 |  | command-injection, file-upload, http-analysis, waf-bypass |
| [[SWPUCTF 2021 新生赛]sql](../../../cards/web-swpuctf-2021-sql.md) | SWPUCTF 2021 新生赛 |  | dns-analysis, http-analysis, sql-injection, waf-bypass |
| [[SWPUCTF 2022 新生赛]ez_ez_unserialize](../../../cards/web-swpuctf2022-ez-ez-unserialize.md) | SWPUCTF 2022 新生赛 |  | deserialization, http-analysis, php-tricks, waf-bypass |
| [[WEB攻防] i春秋- “百度杯”CTF比赛 十二月场-YeserCMS cmseasy CmsEasy_5.6_20151009 无限制报错注入 复现过程_AAAAAAAAAAAA66的博客-CSDN博客](../../../cards/docs-web-i-ctf-yesercms-cmseasy-cmseasy-5-6-20151009-aaaaaaaaaaaa66-csdn.md) | WEB攻防 |  | dns-analysis, file-upload, http-analysis, php-tricks |
| [[WP/BUU/Unicode编码]BUUCTF Unicorn shop题解_車鈊的博客-CSDN博客](../../../cards/docs-wp-buu-unicode-buuctf-unicorn-shop-csdn.md) | WP/BUU/Unicode编码 |  | encoding-analysis, http-analysis, web-exploitation |
| [[ZJCTF 2019]NiZhuanSiWei](../../../cards/web-zjctf2019-nizhuansiwei.md) | ZJCTF 2019 |  | classical-crypto, command-injection, deserialization, encoding-analysis |
| [[第五空间 2021]yet_another_mysql_injection](../../../cards/web-2021-yet-another-mysql-injection.md) | 第五空间 2021 |  | command-injection, dns-analysis, file-inclusion, http-analysis |
| [[网鼎杯 2018]Fakebook](../../../cards/web-2018-fakebook.md) | 网鼎杯 2018 |  | binary-exploitation, deserialization, http-analysis, php-tricks |
| [[鹏城杯 2022]简单包含](../../../cards/web-2022.md) | 鹏城杯 2022 |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [ACTF题解_Mr_小白先生的博客-CSDN博客](../../../cards/docs-actf-mr-csdn.md) | ACTF题解 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [AntCTF X D^3CTF shellgen2 题解_god_speed丶的博客-CSDN博客](../../../cards/docs-antctf-x-d-3ctf-shellgen2-god-speed-csdn.md) | AntCTF X D^3CTF shellgen2 题解 |  | crypto-analysis, misc-analysis, qr-analysis, waf-bypass |
| [ApacheCN CTF 知识库](../../../cards/readme.md) | ApacheCN CTF |  | http-analysis, web-exploitation |
| [asp.net web submit链接页面_De1CTF2020的Web部分题解_weixin_39606137的博客-CSDN博客](../../../cards/docs-asp-net-web-submit-de1ctf2020-web-weixin-39606137-csdn.md) | asp.net web submit链接页面 |  | browser-forensics, command-injection, crypto-analysis, dns-analysis |
| [BJDCTF 2020-Cookie is so subtle!](../../../cards/web-bjdctf-2020-cookie-is-so-subtle.md) | BJDCTF 2020 |  | file-inclusion, http-analysis, ssti, web-exploitation |
| [BMZCTF SSRFME 详解_black guest丶的博客-CSDN博客_bmzctf](../../../cards/docs-bmzctf-ssrfme-black-guest-csdn-bmzctf.md) | BMZCTF SSRFME 详解 |  | command-injection, crypto-analysis, encoding-analysis, file-inclusion |
| [bugctf web代码审计 writeup_R_1v3r的博客-CSDN博客](../../../cards/docs-bugctf-web-writeup-r-1v3r-csdn.md) | bugctf web代码审计 writeup |  | http-analysis, php-tricks, waf-bypass, web-exploitation |
| [BUGKU CTF WEB (10-15题)_半夜好饿的博客-CSDN博客_bugkuctfweb题解](../../../cards/docs-bugku-ctf-web-10-15-csdn-bugkuctfweb.md) | BUGKU CTF WEB (10 |  | classical-crypto, crypto-analysis, encoding-analysis, web-exploitation |
| [Bugku CTF Web 解题报告二（16-20）_Vayn3的博客-CSDN博客](../../../cards/docs-bugku-ctf-web-16-20-vayn3-csdn.md) | Bugku CTF Web 解题报告二（16 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [Bugku CTF Web 解题报告（一）_Vayn3的博客-CSDN博客_bugku 金币](../../../cards/docs-bugku-ctf-web-vayn3-csdn-bugku.md) | Bugku CTF Web 解题报告（一） |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [BugKu CTF web25解题思路笔记_曹振国cc的博客-CSDN博客](../../../cards/docs-bugku-ctf-web25-cc-csdn.md) | BugKu CTF web25解题思路笔记 |  | web-exploitation |
| [Bugku CTF 题目解析 (1-10题)_半夜好饿的博客-CSDN博客_ctf题库及详解](../../../cards/docs-bugku-ctf-1-10-csdn-ctf.md) | Bugku CTF 题目解析 (1 |  | command-injection, crypto-analysis, http-analysis, php-tricks |
| [BugkuCTF SQL注入1_weixin_34397291的博客-CSDN博客](../../../cards/docs-bugkuctf-sql-1-weixin-34397291-csdn.md) | BugkuCTF SQL注入1 |  | binary-exploitation, crypto-analysis, dns-analysis, http-analysis |
| [BugkuCTF web3_weixin_30262255的博客-CSDN博客](../../../cards/docs-bugkuctf-web3-weixin-30262255-csdn.md) | BugkuCTF web3 |  | browser-forensics, command-injection, crypto-analysis, encoding-analysis |
| [BugkuCTF web3_weixin_34161032的博客-CSDN博客](../../../cards/docs-bugkuctf-web3-weixin-34161032-csdn.md) | BugkuCTF web3 |  | browser-forensics, command-injection, crypto-analysis, encoding-analysis |
| [BugkuCTF WEB前五题题解 莽就完事了_废物竹子的博客-CSDN博客](../../../cards/docs-bugkuctf-web-csdn.md) | BugkuCTF WEB前五题题解 莽就完事了 |  | http-analysis, php-tricks, web-exploitation |
| [BugkuCTF web基础$_GET_普通网友的博客-CSDN博客](../../../cards/docs-bugkuctf-web-get-csdn.md) | BugkuCTF web基础$ |  | web-exploitation |
| [BugkuCTF web基础$_POST_weixin_34194359的博客-CSDN博客](../../../cards/docs-bugkuctf-web-post-weixin-34194359-csdn.md) | BugkuCTF web基础$ |  | browser-forensics, http-analysis, web-exploitation |
| [BugkuCTF web基础$_POST_weixin_34306446的博客-CSDN博客](../../../cards/docs-bugkuctf-web-post-weixin-34306446-csdn.md) | BugkuCTF web基础$ |  | browser-forensics, http-analysis, web-exploitation |
| [BugkuCTF WEB解题记录 1-5_aap49042的博客-CSDN博客](../../../cards/docs-bugkuctf-web-1-5-aap49042-csdn.md) | BugkuCTF WEB解题记录 1 |  | command-injection, crypto-analysis, file-upload, http-analysis |
| [BugkuCTF WEB解题记录 1-5_weixin_30556959的博客-CSDN博客](../../../cards/docs-bugkuctf-web-1-5-weixin-30556959-csdn.md) | BugkuCTF WEB解题记录 1 |  | command-injection, crypto-analysis, file-upload, http-analysis |
| [BugkuCTF WEB解题记录 11-15_weixin_30699463的博客-CSDN博客](../../../cards/docs-bugkuctf-web-11-15-weixin-30699463-csdn.md) | BugkuCTF WEB解题记录 11 |  | command-injection, file-inclusion, http-analysis, web-exploitation |
| [BugkuCTF WEB解题记录 16-20_aap49042的博客-CSDN博客](../../../cards/docs-bugkuctf-web-16-20-aap49042-csdn.md) | BugkuCTF WEB解题记录 16 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [BugkuCTF WEB解题记录 16-20_weixin_30596735的博客-CSDN博客](../../../cards/docs-bugkuctf-web-16-20-weixin-30596735-csdn.md) | BugkuCTF WEB解题记录 16 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [BugkuCTF WEB解题记录 6-10_aap49042的博客-CSDN博客](../../../cards/docs-bugkuctf-web-6-10-aap49042-csdn.md) | BugkuCTF WEB解题记录 6 |  | binary-exploitation, crypto-analysis, dns-analysis, http-analysis |
| [bugkuCTF web进阶+web最后两题_goddemon的博客-CSDN博客](../../../cards/docs-bugkuctf-web-web-goddemon-csdn.md) | bugkuCTF web进阶+web最后两题 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [bugkuctf web部分（前8题）解题报告_KEN781215的博客-CSDN博客](../../../cards/docs-bugkuctf-web-8-ken781215-csdn.md) | bugkuctf web部分（前8题）解题报告 |  | web-exploitation |
| [BugkuCTF web题解析_qq_37078651的博客-CSDN博客_bugkuctfweb题解](../../../cards/docs-bugkuctf-web-qq-37078651-csdn-bugkuctfweb.md) | BugkuCTF web题解析 |  | encoding-analysis, web-exploitation |
| [BugkuCTF 部分题解(一)_z.volcano的博客-CSDN博客_bugkuctf](../../../cards/docs-bugkuctf-z-volcano-csdn-bugkuctf.md) | BugkuCTF 部分题解(一) |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [BugkuCTF-WEB部分题解（一）_flying_bird2019的博客-CSDN博客_bugkuctfweb题解](../../../cards/docs-bugkuctf-web-flying-bird2019-csdn-bugkuctfweb.md) | BugkuCTF |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [BugkuCTF-WEB部分题解（二）_flying_bird2019的博客-CSDN博客](../../../cards/docs-bugkuctf-web-flying-bird2019-csdn.md) | BugkuCTF |  | classical-crypto, crypto-analysis, encoding-analysis, php-tricks |
| [BugkuCTF-WEB部分题解（四）_flying_bird2019的博客-CSDN博客](../../../cards/docs-bugkuctf-web-flying-bird2019-csdn.md) | BugkuCTF |  | classical-crypto, crypto-analysis, encoding-analysis, php-tricks |
| [BugkuCTF: web3 ； 域名解析_s0i1的博客-CSDN博客](../../../cards/docs-bugkuctf-web3-s0i1-csdn.md) | BugkuCTF: web3 ； 域名解析 |  | crypto-analysis, dns-analysis, file-upload, http-analysis |
| [Bugkuctf_web3题解wp_东方黑手的博客-CSDN博客](../../../cards/docs-bugkuctf-web3-wp-csdn.md) | Bugkuctf |  | web-exploitation |
| [Bugkuctf_web6题解wp_东方黑手的博客-CSDN博客](../../../cards/docs-bugkuctf-web6-wp-csdn.md) | Bugkuctf |  | web-exploitation |
| [BugKuCTF_WEB题解报告_whatacutepanda的博客-CSDN博客_bugku web题解](../../../cards/docs-bugkuctf-web-whatacutepanda-csdn-bugku-web.md) | BugKuCTF |  | browser-forensics, file-upload, http-analysis, web-exploitation |
| [BugkuCTF平台-Web题目笔记_手可摘星辰丶的博客-CSDN博客](../../../cards/docs-bugkuctf-web-csdn.md) | BugkuCTF平台 |  | command-injection, crypto-analysis, encoding-analysis, file-inclusion |
| [BugkuCTF解题报告---WEB_jak0018的博客-CSDN博客](../../../cards/docs-bugkuctf-web-jak0018-csdn.md) | BugkuCTF解题报告 |  | browser-forensics, classical-crypto, command-injection, encoding-analysis |
| [BugkuCTF题解——web2_cggwz的博客-CSDN博客](../../../cards/docs-bugkuctf-web2-cggwz-csdn.md) | BugkuCTF题解——web2 |  | web-exploitation |
| [Bugku—web题解_Sn0w/的博客-CSDN博客_bugku题解](../../../cards/docs-bugku-web-sn0w-csdn-bugku.md) | Bugku—web题解 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [bugku【welcome to bugkuctf】题解_大方子的博客-CSDN博客](../../../cards/docs-bugku-welcome-to-bugkuctf-csdn.md) | bugku【welcome to bugkuctf】题解 |  | classical-crypto, command-injection, deserialization, encoding-analysis |
| [BugKu题解备注（1）_s11show_163的博客-CSDN博客](../../../cards/docs-bugku-1-s11show-163-csdn.md) | BugKu题解备注（1） |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [BUUCTF [ACTF2020 新生赛]Include_是阿星呀的博客-CSDN博客](../../../cards/docs-buuctf-actf2020-include-csdn.md) | BUUCTF [ACTF2020 新生赛]Include |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [buuctf web小结_绿冰壶的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | buuctf web小结 |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [buuctf XCTF October 2019 Twice SQL Injection 二次注入原理+题解_AAAAAAAAAAAA66的博客-CSDN博客](../../../cards/docs-buuctf-xctf-october-2019-twice-sql-injection-aaaaaaaaaaaa66-csdn.md) | buuctf XCTF October 2019 Twice SQL Injec |  | sql-injection |
| [BUUCTF-[羊城杯]Easyser_moyuyyds的博客-CSDN博客](../../../cards/docs-buuctf-easyser-moyuyyds-csdn.md) | BUUCTF |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [BUUCTF-basic——Linux labs题解wp_东方黑手的博客-CSDN博客](../../../cards/docs-buuctf-basic-linux-labs-wp-csdn.md) | BUUCTF |  | http-analysis, service-enumeration, web-exploitation |
| [BUUCTF-Crypto-Quoted-printable题解_ASSOINT的博客-CSDN博客](../../../cards/docs-buuctf-crypto-quoted-printable-assoint-csdn.md) | BUUCTF |  | crypto-analysis, http-analysis, web-exploitation |
| [BUUCTF-Web题解（一）_flying_bird2019的博客-CSDN博客_buuctfweb第一题](../../../cards/docs-buuctf-web-flying-bird2019-csdn-buuctfweb.md) | BUUCTF |  | classical-crypto, command-injection, deserialization, encoding-analysis |
| [BUUCTF-Web题解（二）_flying_bird2019的博客-CSDN博客](../../../cards/docs-buuctf-web-flying-bird2019-csdn.md) | BUUCTF |  | sql-injection, web-exploitation |
| [BUUCTF__[ACTF2020 新生赛]BackupFile_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-actf2020-backupfile-csdn.md) | BUUCTF |  | command-injection, crypto-analysis, file-inclusion, jwt-analysis |
| [BUUCTF__[ACTF2020 新生赛]Upload_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-actf2020-upload-csdn.md) | BUUCTF |  | file-upload |
| [BUUCTF__[BJDCTF2020]Easy MD5_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-bjdctf2020-easy-md5-csdn.md) | BUUCTF |  | php-tricks, sql-injection, web-exploitation |
| [BUUCTF__[BJDCTF2020]Easy MD5_题解_鼹鼠yanshu的博客-CSDN博客](../../../cards/docs-buuctf-bjdctf2020-easy-md5-yanshu-csdn.md) | BUUCTF |  | http-analysis, php-tricks, sql-injection, web-exploitation |
| [BUUCTF__[BUUCTF 2018]Online Tool_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-buuctf-2018-online-tool-csdn.md) | BUUCTF |  | command-injection, http-analysis, php-tricks, ret2libc |
| [BUUCTF__[CISCN2019 华北赛区 Day2 Web1]Hack World_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-ciscn2019-day2-web1-hack-world-csdn.md) | BUUCTF |  | dns-analysis, http-analysis, sql-injection, waf-bypass |
| [BUUCTF__[EIS 2019]EzPOP_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-eis-2019-ezpop-csdn.md) | BUUCTF |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [BUUCTF__[GWCTF 2019]mypassword_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-gwctf-2019-mypassword-csdn.md) | BUUCTF |  | crypto-analysis, http-analysis, waf-bypass, web-exploitation |
| [BUUCTF__[GXYCTF2019]Ping Ping Ping_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-gxyctf2019-ping-ping-ping-csdn.md) | BUUCTF |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [BUUCTF__[HCTF 2018]admin_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-hctf-2018-admin-csdn.md) | BUUCTF |  | crypto-analysis, dns-analysis, encoding-analysis, http-analysis |
| [BUUCTF__[HCTF 2018]WarmUp_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-hctf-2018-warmup-csdn.md) | BUUCTF |  | command-injection, encoding-analysis, file-inclusion, http-analysis |
| [BUUCTF__[RoarCTF 2019]Easy Calc_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-roarctf-2019-easy-calc-csdn.md) | BUUCTF |  | command-injection, http-analysis, ssti, waf-bypass |
| [BUUCTF__[SUCTF 2019]EasySQL_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-suctf-2019-easysql-csdn.md) | BUUCTF |  | binary-exploitation, dns-analysis, encoding-analysis, file-inclusion |
| [BUUCTF__[ZJCTF 2019]NiZhuanSiWei_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-zjctf-2019-nizhuansiwei-csdn.md) | BUUCTF |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [BUUCTF__[强网杯 2019]高明的黑客_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-2019-csdn.md) | BUUCTF |  | http-analysis, misc-analysis, web-exploitation |
| [BUUCTF__[极客大挑战 2019]BabySQL_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-2019-babysql-csdn.md) | BUUCTF |  | web-exploitation |
| [BUUCTF__[极客大挑战 2019]EasySQL_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-2019-easysql-csdn.md) | BUUCTF |  | web-exploitation |
| [BUUCTF__[极客大挑战 2019]Http_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-2019-http-csdn.md) | BUUCTF |  | http-analysis, web-exploitation |
| [BUUCTF__[极客大挑战 2019]LoveSQL_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-2019-lovesql-csdn.md) | BUUCTF |  | web-exploitation |
| [BUUCTF__[极客大挑战 2019]PHP_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-2019-php-csdn.md) | BUUCTF |  | classical-crypto, deserialization, file-inclusion, php-tricks |
| [BUUCTF__[极客大挑战 2019]Upload_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-2019-upload-csdn.md) | BUUCTF |  | file-upload |
| [BUUCTF__[网鼎杯 2018]Fakebook_题解_风过江南乱的博客-CSDN博客_fakebook网鼎杯](../../../cards/docs-buuctf-2018-fakebook-csdn-fakebook.md) | BUUCTF |  | deserialization, http-analysis, osint, php-tricks |
| [BUUCTF__web题解合集（一）_风过江南乱的博客-CSDN博客_buuctf web](../../../cards/docs-buuctf-web-csdn-buuctf-web.md) | BUUCTF |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [BUUCTF__web题解合集（七）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | classical-crypto, command-injection, deserialization, encoding-analysis |
| [BUUCTF__web题解合集（三）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | classical-crypto, command-injection, encoding-analysis, file-upload |
| [BUUCTF__web题解合集（九）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [BUUCTF__web题解合集（二）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | binary-exploitation, encoding-analysis, file-inclusion, http-analysis |
| [BUUCTF__web题解合集（五）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [BUUCTF__web题解合集（八）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [BUUCTF__web题解合集（六）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | command-injection, http-analysis, misc-analysis, ret2libc |
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
| [CG-CTF WEB 解题记录 11-15_aap49042的博客-CSDN博客](../../../cards/docs-cg-ctf-web-11-15-aap49042-csdn.md) | CG |  | dns-analysis, http-analysis, sql-injection, web-exploitation |
| [CG-CTF WEB 解题记录 6-10_aap49042的博客-CSDN博客](../../../cards/docs-cg-ctf-web-6-10-aap49042-csdn.md) | CG |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [Codegate CTF和HackTM CTF的两个web题解_合天网安实验室的博客-CSDN博客](../../../cards/docs-codegate-ctf-hacktm-ctf-web-csdn.md) | Codegate CTF和HackTM CTF的两个web题解 |  | browser-forensics, command-injection, encoding-analysis, file-inclusion |
| [CTF AWD靶场搭建和第一题题解_星星明亮的博客-CSDN博客_awd靶场](../../../cards/docs-ctf-awd-csdn-awd.md) | CTF AWD靶场搭建和第一题题解 |  | command-injection, crypto-analysis, file-inclusion, http-analysis |
| [ctf php 流量分析题,GKCTF EZWEB的分析题解和思考_一点能源的博客-CSDN博客](../../../cards/docs-ctf-php-gkctf-ezweb-csdn.md) | ctf php 流量分析题,GKCTF EZWEB的分析题解和思考 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [ctf show-web入门 php特性篇部分题解_z.volcano的博客-CSDN博客_ctfshow的php特性](../../../cards/docs-ctf-show-web-php-z-volcano-csdn-ctfshow-php.md) | ctf show |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [ctf show-web入门 SSTI篇部分题解_z.volcano的博客-CSDN博客_ctfshow web入门ssti](../../../cards/docs-ctf-show-web-ssti-z-volcano-csdn-ctfshow-web-ssti.md) | ctf show |  | command-injection, ssti, waf-bypass, web-exploitation |
| [CTF web 攻防世界 disabled_button_weixin_30457065的博客-CSDN博客](../../../cards/docs-ctf-web-disabled-button-weixin-30457065-csdn.md) | CTF web 攻防世界 disabled |  | web-exploitation |
| [ctf web个人总结_recover517的博客-CSDN博客](../../../cards/docs-ctf-web-recover517-csdn.md) | ctf web个人总结 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF web入门——HTTP头相关的----修改请求头、伪造Cookie类题目——Bugku Web题目详细题解_日熙！的博客-CSDN博客_ctf请求头题目](../../../cards/docs-ctf-web-http-cookie-bugku-web-csdn-ctf.md) | CTF web入门——HTTP头相关的 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [CTF Web入门题目——Bugku Web 题目题解——发送HTTP请求篇（3道基础题目)_日熙！的博客-CSDN博客](../../../cards/docs-ctf-web-bugku-web-http-3-csdn.md) | CTF Web |  | http-analysis, web-exploitation |
| [CTF web题型解题技巧_吃素的小动物的博客-CSDN博客](../../../cards/docs-ctf-web-csdn.md) | CTF web题型解题技巧 |  | browser-forensics, crypto-analysis, file-inclusion, file-upload |
| [CTF —— web方向思路_吃肉唐僧的博客-CSDN博客_ctf web方向](../../../cards/docs-ctf-web-csdn-ctf-web.md) | CTF —— web方向思路 |  | file-upload, sql-injection, web-exploitation |
| [CTF 题型了解_秦罗敷写代码的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | CTF 题型了解 |  | binary-exploitation, crypto-analysis, http-analysis, misc-analysis |
| [CTF---Web入门第二题 上传绕过_weixin_30344995的博客-CSDN博客](../../../cards/docs-ctf-web-weixin-30344995-csdn.md) | CTF |  | command-injection, encoding-analysis, file-upload, waf-bypass |
| [CTF-2021中国能源网络WEB题目全解_wulanlin的博客-CSDN博客](../../../cards/docs-ctf-2021-web-wulanlin-csdn.md) | CTF |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF-rootme 题解之Bash - System 2_weixin_30508309的博客-CSDN博客](../../../cards/docs-ctf-rootme-bash-system-2-weixin-30508309-csdn.md) | CTF |  | command-injection, file-inclusion, privilege-escalation, ret2libc |
| [CTF-rootme 题解之Hash - SHA-2_weixin_30237719的博客-CSDN博客](../../../cards/docs-ctf-rootme-hash-sha-2-weixin-30237719-csdn.md) | CTF |  | command-injection, crypto-analysis, http-analysis, php-tricks |
| [CTF-rootme 题解之HTTP - Open redirect_weixin_30952535的博客-CSDN博客](../../../cards/docs-ctf-rootme-http-open-redirect-weixin-30952535-csdn.md) | CTF |  | binary-exploitation, command-injection, http-analysis, php-tricks |
| [CTF-rootme 题解之PHP filters_weixin_30384031的博客-CSDN博客](../../../cards/docs-ctf-rootme-php-filters-weixin-30384031-csdn.md) | CTF |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [CTF-rootme 题解之PHP register globals_weixin_30881367的博客-CSDN博客](../../../cards/docs-ctf-rootme-php-register-globals-weixin-30881367-csdn.md) | CTF |  | command-injection, file-inclusion, http-analysis, reverse-engineering |
| [CTF-rootme 题解之Python - pickle_weixin_30652879的博客-CSDN博客](../../../cards/docs-ctf-rootme-python-pickle-weixin-30652879-csdn.md) | CTF |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF-web 第十一部分 实用脚本_iamsongyu的博客-CSDN博客](../../../cards/docs-ctf-web-iamsongyu-csdn.md) | CTF |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [ctf-web刷题-ctfshow-爆破-web22_None安全团队的博客-CSDN博客](../../../cards/docs-ctf-web-ctfshow-web22-none-csdn.md) | ctf |  | web-exploitation |
| [CTF-Web小白入门篇超详细——了解CTF-Web基本题型及其解题方法 总结——包含例题的详细题解_日熙！的博客-CSDN博客_ctf](../../../cards/docs-ctf-web-ctf-web-csdn-ctf.md) | CTF |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [CTF-入门一__starstarli的博客-CSDN博客](../../../cards/docs-ctf-starstarli-csdn.md) | CTF |  | binary-exploitation, command-injection, crypto-analysis, dns-analysis |
| [CTF-入门九__starstarli的博客-CSDN博客](../../../cards/docs-ctf-starstarli-csdn.md) | CTF |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [CTF-加密与解密（十一）_红烧兔纸的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | CTF |  | command-injection, crypto-analysis, encoding-analysis, http-analysis |
| [CTF-加密与解密（十九）_红烧兔纸的博客-CSDN博客_ctf中txt文件的解密过程](../../../cards/docs-ctf-csdn-ctf-txt.md) | CTF |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [CTF-加密与解密（十六）_红烧兔纸的博客-CSDN博客_文本加密为音乐符号](../../../cards/docs-ctf-csdn.md) | CTF |  | crypto-analysis, http-analysis, web-exploitation |
| [ctf.show crypto题解_��阿兮��的博客-CSDN博客_ctf秀crypto6](../../../cards/docs-ctf-show-crypto-csdn-ctf-crypto6.md) | ctf.show crypto题解 |  | crypto-analysis, http-analysis, php-tricks, web-exploitation |
| [CTF/合天网安实验室-web100题解【eval与alert的利用】_Sp4rkW的博客-CSDN博客](../../../cards/docs-ctf-web100-eval-alert-sp4rkw-csdn.md) | CTF/合天网安实验室 |  | command-injection, http-analysis, web-exploitation |
| [CTF:web题目中的md5弱类型解析_神林丶的博客-CSDN博客_md5弱比较](../../../cards/docs-ctf-web-md5-csdn-md5.md) | CTF:web题目中的md5弱类型解析 |  | http-analysis, php-tricks, web-exploitation, xss |
| [CTF_Web：8位以内可控字符getshell_星辰照耀你我的博客-CSDN博客_ctf getshell](../../../cards/docs-ctf-web-8-getshell-csdn-ctf-getshell.md) | CTF |  | classical-crypto, command-injection, encoding-analysis, web-exploitation |
| [CTF_Web：长安杯-2021 Old But A Little New & asuka题解_星辰照耀你我的博客-CSDN博客](../../../cards/docs-ctf-web-2021-old-but-a-little-new-asuka-csdn.md) | CTF |  | command-injection, http-analysis, web-exploitation |
| [CTFHUB Web题解记录（信息泄露、弱口令部分）_valecalida的博客-CSDN博客_ctfhub弱口令](../../../cards/docs-ctfhub-web-valecalida-csdn-ctfhub.md) | CTFHUB Web题解记录（信息泄露、弱口令部分） |  | http-analysis, malware-static, reverse-engineering, stego-extraction |
| [ctfhub技能书+历年真题学习笔记（详解）_Yn8rt的博客-CSDN博客](../../../cards/docs-ctfhub-yn8rt-csdn.md) | ctfhub技能书+历年真题学习笔记（详解） |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTFHub题解-技能树-Web（SQL注入-过滤空格）_唤变的博客-CSDN博客_sqlmap 空格过滤](../../../cards/docs-ctfhub-web-sql-csdn-sqlmap.md) | CTFHub题解 |  | binary-exploitation, http-analysis, sql-injection, waf-bypass |
| [ctfshow 萌新22 （类似级客巅峰web4）_Firebasky的博客-CSDN博客_ctf p神](../../../cards/docs-ctfshow-22-web4-firebasky-csdn-ctf-p.md) | ctfshow 萌新22 （类似级客巅峰web4） |  | command-injection, file-inclusion, http-analysis, ret2libc |
| [ctfshow 萌新web题解_Mr_小白先生的博客-CSDN博客](../../../cards/docs-ctfshow-web-mr-csdn.md) | ctfshow 萌新web题解 |  | command-injection, ret2libc, sql-injection, web-exploitation |
| [CTFWeb——Bugku秋名山老司机 详细题解_日熙！的博客-CSDN博客_ctf秋名山](../../../cards/docs-ctfweb-bugku-csdn-ctf.md) | CTFWeb——Bugku秋名山老司机 详细题解 |  | command-injection, http-analysis, web-exploitation |
| [CTFweb题目中的md5弱类型题解_神林丶的博客-CSDN博客_ctf md5题目](../../../cards/docs-ctfweb-md5-csdn-ctf-md5.md) | CTFweb题目中的md5弱类型题解 |  | php-tricks, web-exploitation, xss |
| [CTF|BugkuCTF-WEB解题思路_「已注销」的博客-CSDN博客_bugkuctfweb题解](../../../cards/docs-ctf-bugkuctf-web-csdn-bugkuctfweb.md) | CTF|BugkuCTF |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [ctf不允许上传该类型php,d3ctf easyweb题解_司梦化虚的博客-CSDN博客](../../../cards/docs-ctf-php-d3ctf-easyweb-csdn.md) | ctf不允许上传该类型php,d3ctf easyweb题解 |  | command-injection, deserialization, dns-analysis, file-inclusion |
| [CTF专题一2021网络WEB题目解析_普通网友的博客-CSDN博客_ctf web分析](../../../cards/docs-ctf-2021-web-csdn-ctf-web.md) | CTF专题一2021网络WEB题目解析 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF中Web找Flag题目（1）_「已注销」的博客-CSDN博客_web找flag](../../../cards/docs-ctf-web-flag-1-csdn-web-flag.md) | CTF中Web找Flag题目（1） |  | classical-crypto, crypto-analysis, encoding-analysis, web-exploitation |
| [CTF中文件上传题目整理总结_xiaosec的博客-CSDN博客_文件上传ctf题目](../../../cards/docs-ctf-xiaosec-csdn-ctf.md) | CTF中文件上传题目整理总结 |  | dns-analysis, encoding-analysis, file-inclusion, file-upload |
| [ctf中文转unicode_CTF实战题解笔记 - Web篇_weixin_39707597的博客-CSDN博客](../../../cards/docs-ctf-unicode-ctf-web-weixin-39707597-csdn.md) | ctf中文转unicode |  | binary-exploitation, encoding-analysis, file-upload, http-analysis |
| [CTF之Sqli-Labs题目解析（1-11题）_z11h的博客-CSDN博客_sqllabs题目](../../../cards/docs-ctf-sqli-labs-1-11-z11h-csdn-sqllabs.md) | CTF之Sqli |  | http-analysis, php-tricks, qr-analysis, sql-injection |
| [CTF之WEB（BUGku Ctf 1-7 题解）_嗅探的博客-CSDN博客](../../../cards/docs-ctf-web-bugku-ctf-1-7-csdn.md) | CTF之WEB（BUGku Ctf 1 |  | binary-exploitation, command-injection, encoding-analysis, web-exploitation |
| [CTF从入门到提升（十四）session phpinfo包含及例题详解_anquanniu牛油果的博客-CSDN博客](../../../cards/docs-ctf-session-phpinfo-anquanniu-csdn.md) | CTF从入门到提升（十四）session phpinfo包含及例题详解 |  | file-inclusion, file-upload |
| [CTF从入门到提升（四）基于时间盲注例题及解法_anquanniu牛油果的博客-CSDN博客_ctf 时间盲注](../../../cards/docs-ctf-anquanniu-csdn-ctf.md) | CTF从入门到提升（四）基于时间盲注例题及解法 |  | http-analysis, sql-injection, web-exploitation |
| [CTF入门第一课(附一道小题)_anquanniu牛油果的博客-CSDN博客](../../../cards/docs-ctf-anquanniu-csdn.md) | CTF入门第一课(附一道小题) |  | binary-exploitation, crypto-analysis, image-analysis, misc-analysis |
| [CTF刷题02_Atkxor的博客-CSDN博客](../../../cards/docs-ctf-02-atkxor-csdn.md) | CTF刷题02 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [CTF学习-web解题思路_菜鸟-传奇的博客-CSDN博客](../../../cards/docs-ctf-web-csdn.md) | CTF学习 |  | browser-forensics, classical-crypto, crypto-analysis, dns-analysis |
| [CTF学习笔记——[极客大挑战 2019]PHP_Obs_cure的博客-CSDN博客](../../../cards/docs-ctf-2019-php-obs-cure-csdn.md) | CTF学习笔记——[极客大挑战 2019]PHP |  | deserialization, file-inclusion, php-tricks, waf-bypass |
| [CTF实验吧-WEB专题-1_77458的博客-CSDN博客](../../../cards/docs-ctf-web-1-77458-csdn.md) | CTF实验吧 |  | command-injection, crypto-analysis, encoding-analysis, http-analysis |
| [CTF实验吧-WEB专题-5_77458的博客-CSDN博客](../../../cards/docs-ctf-web-5-77458-csdn.md) | CTF实验吧 |  | classical-crypto, encoding-analysis, php-tricks, qr-analysis |
| [CTF平台题库writeup（四）--BugKuCTF-代码审计（14题详解）_Hacking黑白红的博客-CSDN博客](../../../cards/docs-ctf-writeup-bugkuctf-14-hacking-csdn.md) | CTF平台题库writeup（四） |  | classical-crypto, encoding-analysis, file-inclusion, http-analysis |
| [CTF攻防世界web-新手区解题过程及使用工具_Peppa _Peppa的博客-CSDN博客_ctf web 工具](../../../cards/docs-ctf-web-peppa-peppa-csdn-ctf-web.md) | CTF攻防世界web |  | browser-forensics, http-analysis, osint, web-exploitation |
| [CTF攻防世界web题思路解析2robot_想喝书亦的博客-CSDN博客](../../../cards/docs-ctf-web-2robot-csdn.md) | CTF攻防世界web题思路解析2robot |  | http-analysis, osint, web-exploitation |
| [ctf每日练习-第10天__wand1的博客-CSDN博客](../../../cards/docs-ctf-10-wand1-csdn.md) | ctf每日练习 |  | classical-crypto, command-injection, encoding-analysis, http-analysis |
| [ctf解题--PHP大法（web）_妤儿兮兮的博客-CSDN博客_ctf php题](../../../cards/docs-ctf-php-web-csdn-ctf-php.md) | ctf解题 |  | web-exploitation |
| [CTF解题-2020年强网杯参赛WriteUp_Tr0e的博客-CSDN博客_ctf解题赛](../../../cards/docs-ctf-2020-writeup-tr0e-csdn-ctf.md) | CTF解题 |  | classical-crypto, command-injection, deserialization, encoding-analysis |
| [CTF解题-Bugku_Web_WriteUp (上）_Tr0e的博客-CSDN博客_bugku web writeup](../../../cards/docs-ctf-bugku-web-writeup-tr0e-csdn-bugku-web-writeup.md) | CTF解题 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF解题-Bugku_Web_WriteUp (下）_Tr0e的博客-CSDN博客](../../../cards/docs-ctf-bugku-web-writeup-tr0e-csdn.md) | CTF解题 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [CTF解题-网安实验室(注入关)_Tr0e的博客-CSDN博客](../../../cards/docs-ctf-tr0e-csdn.md) | CTF解题 |  | dns-analysis, file-inclusion, http-analysis, php-tricks |
| [ctf解题姿势#目录_vircorns的博客-CSDN博客](../../../cards/docs-ctf-vircorns-csdn.md) | ctf解题姿势#目录 |  | web-exploitation |
| [CTF解题思路笔记_山兔1的博客-CSDN博客_ctf解题](../../../cards/docs-ctf-1-csdn-ctf.md) | CTF解题思路笔记 |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [CTF解题思路： 数据包相关题目_tiny丶的博客-CSDN博客](../../../cards/docs-ctf-tiny-csdn.md) | CTF解题思路： 数据包相关题目 |  | classical-crypto, encoding-analysis, http-analysis, web-exploitation |
| [CTF解题笔记（1）_TravisZeng的博客-CSDN博客](../../../cards/docs-ctf-1-traviszeng-csdn.md) | CTF解题笔记（1） |  | command-injection, crypto-analysis, dns-analysis, http-analysis |
| [CTF解题笔记（2）_TravisZeng的博客-CSDN博客_ctf题解](../../../cards/docs-ctf-2-traviszeng-csdn-ctf.md) | CTF解题笔记（2） |  | http-analysis, sql-injection, waf-bypass, web-exploitation |
| [ctf训练 web安全暴力破解_爱吃香菜的哈哈的博客-CSDN博客](../../../cards/docs-ctf-web-csdn.md) | ctf训练 web安全暴力破解 |  | crypto-analysis, http-analysis, password-cracking, privilege-escalation |
| [CTF论剑场web解题_梳刘海的杰瑞的博客-CSDN博客](../../../cards/docs-ctf-web-csdn.md) | CTF论剑场web解题 |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [ctf赛题secret.php,CTF赛题全解之CTF成长之路（三）_weixin_39594312的博客-CSDN博客](../../../cards/docs-ctf-secret-php-ctf-ctf-weixin-39594312-csdn.md) | ctf赛题secret.php,CTF赛题全解之CTF成长之路（三） |  | command-injection, crypto-analysis, file-inclusion, file-upload |
| [ctf赛题secret.php,记一场纯JS赛——DiceCTF2021 Web题解_自强自在的博客-CSDN博客](../../../cards/docs-ctf-secret-php-js-dicectf2021-web-csdn.md) | ctf |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [CTF里面的WEB题的一些解决思路_F10W3RDANC3的博客-CSDN博客_ctfweb思路](../../../cards/docs-ctf-web-f10w3rdanc3-csdn-ctfweb.md) | CTF里面的WEB题的一些解决思路 |  | command-injection, file-upload, http-analysis, sql-injection |
| [ctf镜子里面的世界_攻防世界XCTF-WEB入门12题解题报告_weixin_39877050的博客-CSDN博客](../../../cards/docs-ctf-xctf-web-12-weixin-39877050-csdn.md) | ctf镜子里面的世界 |  | command-injection, crypto-analysis, http-analysis, ret2libc |
| [CTF题解_greedy-hat的博客-CSDN博客_ctf题解](../../../cards/docs-ctf-greedy-hat-csdn-ctf.md) | CTF题解 |  | php-tricks, sql-injection, waf-bypass, web-exploitation |
| [ctf题解——sql注入（cookie注入）_ckkkkkkkkke的博客-CSDN博客](../../../cards/docs-ctf-sql-cookie-ckkkkkkkkke-csdn.md) | ctf题解——sql注入（cookie注入） |  | http-analysis, sql-injection, web-exploitation |
| [ctl文件去空格_CTF从入门到提升（十三）文件包含session及例题详解_weixin_39964869的博客-CSDN博客](../../../cards/docs-ctl-ctf-session-weixin-39964869-csdn.md) | ctl文件去空格 |  | classical-crypto, crypto-analysis, encoding-analysis, file-inclusion |
| [D3CTF 8-bit解题详解_N0Tai1学习又咕了的博客-CSDN博客](../../../cards/docs-d3ctf-8-bit-n0tai1-csdn.md) | D3CTF 8 |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [D^3CTF(Crypto-D3bug详解 LFSR题目）_Mango|Feng的博客-CSDN博客](../../../cards/docs-d-3ctf-crypto-d3bug-lfsr-mango-feng-csdn.md) | D^3CTF(Crypto |  | crypto-analysis, http-analysis, symbolic-execution, web-exploitation |
| [DASCTF-两道web题复现_cr4ke3的博客-CSDN博客](../../../cards/docs-dasctf-web-cr4ke3-csdn.md) | DASCTF |  | command-injection, crypto-analysis, deserialization, format-string |
| [De1CTF2020的Web部分题解_合天网安实验室的博客-CSDN博客](../../../cards/docs-de1ctf2020-web-csdn.md) | De1CTF2020的Web部分题解 |  | binary-exploitation, browser-forensics, command-injection, crypto-analysis |
| [GHCTF 2025-upload SSTI!](../../../cards/web-ghctf-2025-upload-ssti.md) | GHCTF 2025 |  | file-upload, http-analysis, ssti, waf-bypass |
| [GWCTF 2019-你的名字](../../../cards/web-gwctf-2019.md) | GWCTF 2019 |  | http-analysis, ssti, waf-bypass, web-exploitation |
| [hgame ctf week2--shinyshot题解_weixin_30753873的博客-CSDN博客](../../../cards/docs-hgame-ctf-week2-shinyshot-weixin-30753873-csdn.md) | hgame ctf week2 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [HITCTF2018-web全题解_合天网安实验室的博客-CSDN博客](../../../cards/docs-hitctf2018-web-csdn.md) | HITCTF2018 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [hxp 36C3 CTF Web题 WriteupBin Writeup (Selenium模拟点击+Content Security Policy+Nonce+Parsley.js触发错误提示)_KevinLuo2000的博客-CSDN博客](../../../cards/docs-hxp-36c3-ctf-web-writeupbin-writeup-selenium-content-security-policy-nonce-parsley-js-kevinluo2000-csdn.md) | hxp 36C3 CTF Web |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [ISCTF新生赛 Web easy_sql题解（sqlmap的基操）_Jeff_54088的博客-CSDN博客](../../../cards/docs-isctf-web-easy-sql-sqlmap-jeff-54088-csdn.md) | ISCTF新生赛 Web easy |  | http-analysis, sql-injection, web-exploitation |
| [i春秋 百度杯”CTF比赛（二月场） Misc&&web题解 By Assassin_Assassin__is__me的博客-CSDN博客](../../../cards/docs-i-ctf-misc-web-by-assassin-assassin-is-me-csdn.md) | i春秋 |  | binary-exploitation, classical-crypto, command-injection, encoding-analysis |
| [i春秋CTF ssrfme (peal函数中get命令漏洞)命令执行 详细题解＋原理 学习过程_AAAAAAAAAAAA66的博客-CSDN博客](../../../cards/docs-i-ctf-ssrfme-peal-get-aaaaaaaaaaaa66-csdn.md) | i春秋CTF |  | command-injection, php-tricks, ret2libc |
| [i春秋CTF-WEB题解(一)_ 晓德的博客-CSDN博客_ctf题解](../../../cards/docs-i-ctf-web-csdn-ctf.md) | i春秋CTF |  | command-injection, crypto-analysis, file-inclusion, file-upload |
| [i春秋CTF-WEB题解(二)_ 晓德的博客-CSDN博客](../../../cards/docs-i-ctf-web-csdn.md) | i春秋CTF |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [I春秋CTF训练营web题解（一）_Super_Yiang的博客-CSDN博客](../../../cards/docs-i-ctf-web-super-yiang-csdn.md) | I春秋CTF训练营web题解（一） |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [i春秋网络内生安全试验场CTF夺旗赛（第四季）12月赛web write up题解_努力的学渣'#的博客-CSDN博客](../../../cards/docs-i-ctf-12-web-write-up-csdn.md) | i春秋网络内生安全试验场CTF夺旗赛（第四季）12月赛web |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [JIS-CTF : VulnUpload 题解_weixin_33676492的博客-CSDN博客](../../../cards/docs-jis-ctf-vulnupload-weixin-33676492-csdn.md) | JIS |  | file-upload, http-analysis, service-enumeration, web-exploitation |
| [mysql_char ctf_buuctf_sql注入_随便注1_折柳为信的博客-CSDN博客](../../../cards/docs-mysql-char-ctf-buuctf-sql-1-csdn.md) | mysql |  | sql-injection, waf-bypass, web-exploitation |
| [NJCTF2017 线上赛 web 题解 By Assassin_Assassin__is__me的博客-CSDN博客](../../../cards/docs-njctf2017-web-by-assassin-assassin-is-me-csdn.md) | NJCTF2017 线上赛 web 题解 By Assassin |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [NSSCTF 2nd-MyHurricane](../../../cards/web-nssctf-2nd-myhurricane.md) | NSSCTF 2nd |  | command-injection, http-analysis, ssti, waf-bypass |
| [P.W.N. CTF - Web - Login Sec_weixin_30778805的博客-CSDN博客](../../../cards/docs-p-w-n-ctf-web-login-sec-weixin-30778805-csdn.md) | P.W.N. CTF |  | crypto-analysis, dns-analysis, file-inclusion, http-analysis |
| [php ctf题解,国际赛-N1CTF 2018-Web题解_无敌小羊历险记的博客-CSDN博客](../../../cards/docs-php-ctf-n1ctf-2018-web-csdn.md) | php ctf题解,国际赛 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [php string ctf,PHP字符解析特性绕WAF【buuctf题 easy calc】_weixin_39939601的博客-CSDN博客](../../../cards/docs-php-string-ctf-php-waf-buuctf-easy-calc-weixin-39939601-csdn.md) | php string ctf |  | encoding-analysis, http-analysis, waf-bypass, web-exploitation |
| [php伪随机数 ctf,从一道ctf题目理解rand()随机函数_Ma Daniel的博客-CSDN博客](../../../cards/docs-php-ctf-ctf-rand-ma-daniel-csdn.md) | php伪随机数 ctf,从一道ctf题目理解rand()随机函数 |  | classical-crypto, crypto-analysis, http-analysis, reverse-engineering |
| [php安全挑战赛,BiliBili1024安全挑战赛题目及解答(关联ctf)_Deep Yao的博客-CSDN博客](../../../cards/docs-php-bilibili1024-ctf-deep-yao-csdn.md) | php安全挑战赛,BiliBili1024安全挑战赛题目及解答(关联ctf) |  | browser-forensics, crypto-analysis, http-analysis, php-tricks |
| [PHP签到](../../../cards/web-gccctf-2025-php.md) | GCCCTF 2025 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [PWN cmd2 [pwnable.kr]CTF writeup题解系列12_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-cmd2-pwnable-kr-ctf-writeup-12-3ric5r-csdn.md) | PWN cmd2 [pwnable.kr]CTF writeup题解系列12 |  | binary-exploitation, command-injection, file-inclusion, ret2libc |
| [PWN lotto [pwnable.kr]CTF writeup题解系列10_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-lotto-pwnable-kr-ctf-writeup-10-3ric5r-csdn.md) | PWN lotto [pwnable.kr]CTF writeup题解系列10 |  | binary-exploitation, browser-forensics, command-injection, file-inclusion |
| [python 重定向 ctf_CTF web题型解题技巧 第四课 web总结_weixin_39615984的博客-CSDN博客](../../../cards/docs-python-ctf-ctf-web-web-weixin-39615984-csdn.md) | python 重定向 ctf |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [python 重定向 ctf_CTF-rootme 题解之Python - pickle_深夜利行的博客-CSDN博客](../../../cards/docs-python-ctf-ctf-rootme-python-pickle-csdn.md) | python 重定向 ctf |  | classical-crypto, crypto-analysis, deserialization, encoding-analysis |
| [RITSEC CTF2021 Forensics1597题解记录_k_i_k_i的博客-CSDN博客](../../../cards/docs-ritsec-ctf2021-forensics1597-k-i-k-i-csdn.md) | RITSEC CTF2021 Forensics1597题解记录 |  | http-analysis, web-exploitation |
| [RoarCTFweb题解_qq_41575340的博客-CSDN博客](../../../cards/docs-roarctfweb-qq-41575340-csdn.md) | RoarCTFweb题解 |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [S3cCTF-gyy-Writeup_Err0rCM的博客-CSDN博客](../../../cards/docs-s3cctf-gyy-writeup-err0rcm-csdn.md) | S3cCTF |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [sql注入的初步了解以及CTF的一些题的wp_Tang_y1的博客-CSDN博客](../../../cards/docs-sql-ctf-wp-tang-y1-csdn.md) | sql注入的初步了解以及CTF的一些题的wp |  | binary-exploitation, dns-analysis, sql-injection, waf-bypass |
| [SUCTF_2019部分题解复现_FFM-G的博客-CSDN博客](../../../cards/docs-suctf-2019-ffm-g-csdn.md) | SUCTF |  | browser-forensics, classical-crypto, command-injection, encoding-analysis |
| [SWPU 2024 新生引导-ez_SSTI](../../../cards/web-swpu-2024-ez-ssti.md) | SWPU 2024 新生引导 |  | http-analysis, ssti, web-exploitation |
| [SWPUCTF web 部分题解_HyyMbb的博客-CSDN博客](../../../cards/docs-swpuctf-web-hyymbb-csdn.md) | SWPUCTF web 部分题解 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [there is nothing（i春秋CTF题解）_weixin_30258027的博客-CSDN博客](../../../cards/docs-there-is-nothing-i-ctf-weixin-30258027-csdn.md) | there is nothing（i春秋CTF题解） |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [There only 10 people use the same phone as you（i春秋CTF题解）_weixin_30618985的博客-CSDN博客](../../../cards/docs-there-only-10-people-use-the-same-phone-as-you-i-ctf-weixin-30618985-csdn.md) | There only 10 people use the same phone |  | sql-injection |
| [TWCTF 2016 (Tokyo Westerns CTF ) WEB WriteUp_Bendawang的博客-CSDN博客](../../../cards/docs-twctf-2016-tokyo-westerns-ctf-web-writeup-bendawang-csdn.md) | TWCTF 2016 |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [UNCTF2020web方向部分题解_bmth666的博客-CSDN博客](../../../cards/docs-unctf2020web-bmth666-csdn.md) | UNCTF2020web方向部分题解 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [WEB CTF入门题解析_Slient-猿的博客-CSDN博客_ctf入门题](../../../cards/docs-web-ctf-slient-csdn-ctf.md) | WEB CTF入门题解析 |  | command-injection, file-inclusion, http-analysis, php-tricks |
| [web ctf解题记录 bugku的ctf_论剑场_昂首下楼梯的博客-CSDN博客](../../../cards/docs-web-ctf-bugku-ctf-csdn.md) | web ctf解题记录 bugku的ctf |  | http-analysis, sql-injection, web-exploitation |
| [web python template injection_CTF引出对Python模板注入的思考_weixin_39630466的博客-CSDN博客](../../../cards/docs-web-python-template-injection-ctf-python-weixin-39630466-csdn.md) | web python template injection |  | command-injection, dns-analysis, http-analysis, image-analysis |
| [web 计算器_De1CTF2020的Web部分题解_weixin_39924307的博客-CSDN博客](../../../cards/docs-web-de1ctf2020-web-weixin-39924307-csdn.md) | web 计算器 |  | browser-forensics, command-injection, crypto-analysis, dns-analysis |
| [webCTF简单题解_ONE_huster0828的博客-CSDN博客](../../../cards/docs-webctf-one-huster0828-csdn.md) | webCTF简单题解 |  | command-injection, http-analysis, web-exploitation |
| [welcome to bugkuctf（详解）——Bugku_weixin_33728268的博客-CSDN博客](../../../cards/docs-welcome-to-bugkuctf-bugku-weixin-33728268-csdn.md) | welcome to bugkuctf（详解）——Bugku |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [Writeup_BugkuCTF_Web_秦小乙的工作台的博客-CSDN博客](../../../cards/docs-writeup-bugkuctf-web-csdn.md) | Writeup |  | dns-analysis, encoding-analysis, web-exploitation |
| [“百度杯”CTF比赛 九月场 YeserCMS 详细解析_「已注销」的博客-CSDN博客_yesercms漏洞](../../../cards/docs-ctf-yesercms-csdn-yesercms.md) | “百度杯”CTF比赛 九月场 YeserCMS 详细解析 |  | dns-analysis, file-upload, http-analysis, php-tricks |
| [【BUUCTF刷题】Web解题方法总结（一)_Y1seco的博客-CSDN博客_buuctfweb](../../../cards/docs-buuctf-web-y1seco-csdn-buuctfweb.md) | 【BUUCTF刷题】Web解题方法总结（一) |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [【CTF】关于SQL盲注的细节_publicStr的博客-CSDN博客](../../../cards/docs-ctf-sql-publicstr-csdn.md) | 【CTF】关于SQL盲注的细节 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [【CTF】加解密专题_BJFU_vth的博客-CSDN博客](../../../cards/docs-ctf-bjfu-vth-csdn.md) | 【CTF】加解密专题 |  | classical-crypto, crypto-analysis, encoding-analysis |
| [【CTF】基础常识_你们这样一点都不可耐的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | 【CTF】基础常识 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [【CTF大赛】2021 DASCTF July cybercms 一探再探_IT老涵的博客-CSDN博客](../../../cards/docs-ctf-2021-dasctf-july-cybercms-it-csdn.md) | 【CTF大赛】2021 DASCTF July cybercms 一探再探 |  | browser-forensics, command-injection, file-upload, http-analysis |
| [【CTF日记】BUUOJ篇_ch3uhx9的博客-CSDN博客](../../../cards/docs-ctf-buuoj-ch3uhx9-csdn.md) | 【CTF日记】BUUOJ篇 |  | binary-exploitation, command-injection, file-inclusion, http-analysis |
| [【vishwaCTF】web题解wp_Sunlight_316的博客-CSDN博客](../../../cards/docs-vishwactf-web-wp-sunlight-316-csdn.md) | 【vishwaCTF】web题解wp |  | command-injection, crypto-analysis, deserialization, encoding-analysis |
| [【web】BUUCTF-web刷题记录_weixin_30684743的博客-CSDN博客](../../../cards/docs-web-buuctf-web-weixin-30684743-csdn.md) | 【web】BUUCTF |  | binary-exploitation, encoding-analysis, http-analysis, php-tricks |
| [〖教程〗K8飞刀-网络安全CTF解题Web篇10个例子_k8gege的博客-CSDN博客](../../../cards/docs-k8-ctf-web-10-k8gege-csdn.md) | 〖教程〗K8飞刀 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [〖教程〗K8飞刀-网络安全CTF解题Web篇10例_k8gege的博客-CSDN博客_k8飞刀](../../../cards/docs-k8-ctf-web-10-k8gege-csdn-k8.md) | 〖教程〗K8飞刀 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [一个ctf题目解析，关于des(unix)解密_qzxdh的博客-CSDN博客_ctf des](../../../cards/docs-ctf-des-unix-qzxdh-csdn-ctf-des.md) | 一个ctf题目解析，关于des(unix)解密 |  | command-injection, crypto-analysis, http-analysis, password-cracking |
| [一道CTF题看JWT和python反序列化_weixin_44377940的博客-CSDN博客_jwt反序列化](../../../cards/docs-ctf-jwt-python-weixin-44377940-csdn-jwt.md) | 一道CTF题看JWT和python反序列化 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [一道关于 XML 实体注入的 CTF题_YT--98的博客-CSDN博客_ctf xml注入](../../../cards/docs-xml-ctf-yt-98-csdn-ctf-xml.md) | 一道关于 XML 实体注入的 CTF题 |  | web-exploitation |
| [一道审计型注入CTF题解（injection_cut）_bylfsj的博客-CSDN博客](../../../cards/docs-ctf-injection-cut-bylfsj-csdn.md) | 一道审计型注入CTF题解（injection |  | crypto-analysis, dns-analysis, php-tricks, sql-injection |
| [一道简单的CTF登录题题解_anquanniu牛油果的博客-CSDN博客_ctf login题目](../../../cards/docs-ctf-anquanniu-csdn-ctf-login.md) | 一道简单的CTF登录题题解 |  | classical-crypto, crypto-analysis, deserialization, encoding-analysis |
| [从一道CTF的非预期解看PHP反斜杠匹配问题_Je3Z的博客-CSDN博客](../../../cards/docs-ctf-php-je3z-csdn.md) | 从一道CTF的非预期解看PHP反斜杠匹配问题 |  | command-injection, file-inclusion, web-exploitation |
| [使用burpsuite解决ctf的web题_我眼中的你的博客-CSDN博客](../../../cards/docs-burpsuite-ctf-web-csdn.md) | 使用burpsuite解决ctf的web题 |  | web-exploitation |
| [信息安全web入门——南邮ctf解题_sevenlob的博客-CSDN博客_南邮ctf](../../../cards/docs-web-ctf-sevenlob-csdn-ctf.md) | 信息安全web入门——南邮ctf解题 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [初遇z3并与starCTF碰面_黑羽re的博客-CSDN博客](../../../cards/docs-z3-starctf-re-csdn.md) | 初遇z3并与starCTF碰面 |  | crypto-analysis, sql-injection, symbolic-execution, web-exploitation |
| [利用文件名进行GetShell---CTF题目的相关知识解析_xuchen16的博客-CSDN博客_后台getshell](../../../cards/docs-getshell-ctf-xuchen16-csdn-getshell.md) | 利用文件名进行GetShell |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [南京邮电大学CG-CTF平台Writeup_Gard3nia的博客-CSDN博客_cgctf平台](../../../cards/docs-cg-ctf-writeup-gard3nia-csdn-cgctf.md) | 南京邮电大学CG |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [南邮CTF-web第一篇_萌萌哒的baola的博客-CSDN博客](../../../cards/docs-ctf-web-baola-csdn.md) | 南邮CTF |  | classical-crypto, command-injection, dns-analysis, encoding-analysis |
| [南邮ctf平台部分题解_这是游戏吗的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | 南邮ctf平台部分题解 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [南邮一道ctf题目关于e的解释_软柿子捏捏的博客-CSDN博客](../../../cards/docs-ctf-e-csdn.md) | 南邮一道ctf题目关于e的解释 |  | http-analysis, php-tricks, web-exploitation |
| [哔哩哔哩1024安全挑战赛 Bilibili CTF题解(含代码)_一口快乐水的博客-CSDN博客](../../../cards/docs-1024-bilibili-ctf-csdn.md) | 哔哩哔哩1024安全挑战赛 Bilibili CTF题解(含代码) |  | browser-forensics, crypto-analysis, http-analysis, php-tricks |
| [四叶草云演-CTF03# ereg_weixin_43973521的博客-CSDN博客](../../../cards/docs-ctf03-ereg-weixin-43973521-csdn.md) | 四叶草云演 |  | waf-bypass |
| [好家伙！学习Laravel框架之CTF真题暴力解析_代码熬夜敲的博客-CSDN博客](../../../cards/docs-laravel-ctf-csdn.md) | 好家伙！学习Laravel框架之CTF真题暴力解析 |  | binary-exploitation, classical-crypto, command-injection, deserialization |
| [如何在ctf解题实战中绕过disable_function_YnG_t0的博客-CSDN博客_disablefunctions 绕过](../../../cards/docs-ctf-disable-function-yng-t0-csdn-disablefunctions.md) | 如何在ctf解题实战中绕过disable |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [安恒四月月赛 DASCTF 部分题解_ruokeqx的博客-CSDN博客_安恒ctf题库](../../../cards/docs-dasctf-ruokeqx-csdn-ctf.md) | 安恒四月月赛 DASCTF 部分题解 |  | command-injection, deserialization, http-analysis, php-tricks |
| [实战：2019 0ctf final Web Writeup（一）_systemino的博客-CSDN博客](../../../cards/docs-2019-0ctf-final-web-writeup-systemino-csdn.md) | 实战：2019 0ctf final Web Writeup（一） |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [实验吧CTF练习题---WEB---头有点大解析_dingbai2663的博客-CSDN博客](../../../cards/docs-ctf-web-dingbai2663-csdn.md) | 实验吧CTF练习题 |  | crypto-analysis, http-analysis, web-exploitation |
| [实验吧WEB CTF 头有点大 全网最简单易懂的解题方法_滕青山YYDS的博客-CSDN博客_实验吧维护](../../../cards/docs-web-ctf-yyds-csdn.md) | 实验吧WEB CTF 头有点大 全网最简单易懂的解题方法 |  | command-injection, crypto-analysis, http-analysis, web-exploitation |
| [平时练习 ctf 解题报告 web类_白山茶i的博客-CSDN博客](../../../cards/docs-ctf-web-i-csdn.md) | 平时练习 ctf 解题报告 web类 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [当堂XSS-labs 挑战](../../../cards/web-xss-labs.md) | 当堂XSS |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [手把手教你用Burp抓包——Bugku 头等舱 超详细题解——CTF web小白入门基础篇_日熙！的博客-CSDN博客_bugku头等舱](../../../cards/docs-burp-bugku-ctf-web-csdn-bugku.md) | 手把手教你用Burp抓包——Bugku |  | command-injection, web-exploitation |
| [技能五子棋](../../../cards/web-gccctf-2025.md) | GCCCTF 2025 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [护网杯 2018-easy_tornado](../../../cards/web-2018-easy-tornado.md) | 护网杯 2018 |  | http-analysis, php-tricks, ssti, web-exploitation |
| [攻防世界-web-bug-从0到1的解题历程writeup_CTF小白的博客-CSDN博客](../../../cards/docs-web-bug-0-1-writeup-ctf-csdn.md) | 攻防世界 |  | file-upload, web-exploitation |
| [攻防世界-web-fakebook-从0到1的解题历程writeup_CTF小白的博客-CSDN博客_攻防世界fakebook](../../../cards/docs-web-fakebook-0-1-writeup-ctf-csdn-fakebook.md) | 攻防世界 |  | deserialization, http-analysis, php-tricks, sql-injection |
| [攻防世界-web-FlatScience-从0到1的解题历程writeup_CTF小白的博客-CSDN博客](../../../cards/docs-web-flatscience-0-1-writeup-ctf-csdn.md) | 攻防世界 |  | command-injection, crypto-analysis, dns-analysis, encoding-analysis |
| [攻防世界-web-shrine-从0到1的解题历程writeup_CTF小白的博客-CSDN博客](../../../cards/docs-web-shrine-0-1-writeup-ctf-csdn.md) | 攻防世界 |  | ssti, waf-bypass, web-exploitation |
| [攻防世界-web-unfinish-从0到1的解题历程writeup_CTF小白的博客-CSDN博客](../../../cards/docs-web-unfinish-0-1-writeup-ctf-csdn.md) | 攻防世界 |  | http-analysis, sql-injection, web-exploitation |
| [春秋web题目解题及思路汇总（自用搜集）_香草星冰乐的博客-CSDN博客](../../../cards/docs-web-csdn.md) | 春秋web题目解题及思路汇总（自用搜集） |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [某校赛的题解...再膜鸡哥_Assassin__is__me的博客-CSDN博客](../../../cards/docs-assassin-is-me-csdn.md) | 某校赛的题解...再膜鸡哥 |  | dns-analysis, file-upload, http-analysis, ret2text |
| [第三届上海市大学生网络安全大赛 i春秋CTF Web解题思路_曹振国cc的博客-CSDN博客](../../../cards/docs-i-ctf-web-cc-csdn.md) | 第三届上海市大学生网络安全大赛 i春秋CTF Web解题思路 |  | sql-injection, web-exploitation |
| [第四届“”世安杯“”线上赛题解（Web+Stego+Misc+Crypto）_Assassin__is__me的博客-CSDN博客](../../../cards/docs-web-stego-misc-crypto-assassin-is-me-csdn.md) | 第四届“”世安杯“”线上赛题解（Web+Stego+Misc+Crypto） |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [纵横杯CTF部分WEB题解_ChenZIDu的博客-CSDN博客](../../../cards/docs-ctf-web-chenzidu-csdn.md) | 纵横杯CTF部分WEB题解 |  | command-injection, http-analysis, sql-injection, web-exploitation |
| [结合order by 解CTF某题_aiquan9342的博客-CSDN博客](../../../cards/docs-order-by-ctf-aiquan9342-csdn.md) | 结合order by 解CTF某题 |  | command-injection, crypto-analysis, dns-analysis, http-analysis |
| [网络安全实验室CTF—选择题解析 writeup_Senimo_的博客-CSDN博客_暗门攻击指的什么](../../../cards/docs-ctf-writeup-senimo-csdn.md) | 网络安全实验室CTF—选择题解析 writeup |  | classical-crypto, http-analysis, service-enumeration, web-exploitation |
| [腾讯犀牛鸟CTF文件上传题目解析_無名之涟的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | 腾讯犀牛鸟CTF文件上传题目解析 |  | file-upload, waf-bypass |
| [蓝鲸CTF-web-密码泄露_烟雨天青色的博客-CSDN博客](../../../cards/docs-ctf-web-csdn.md) | 蓝鲸CTF |  | classical-crypto, encoding-analysis, web-exploitation, xss |
| [西普学院CTF习题解析——WEB(已完成16/16)_Xyntax的博客-CSDN博客](../../../cards/docs-ctf-web-16-16-xyntax-csdn.md) | 西普学院CTF习题解析——WEB(已完成16/16) |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [西邮ctf2020 web之文件包含解析_落雪wink的博客-CSDN博客](../../../cards/docs-ctf2020-web-wink-csdn.md) | 西邮ctf2020 web之文件包含解析 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [解网鼎杯一道web题（fakebook）_诸神之眼的博客-CSDN博客_fakebook](../../../cards/docs-web-fakebook-csdn-fakebook.md) | 解网鼎杯一道web题（fakebook） |  | browser-forensics, classical-crypto, deserialization, encoding-analysis |
| [记一次院赛CTF的WEB题（入门级别）_CTF小白的博客-CSDN博客_ctf web解题 找flag](../../../cards/docs-ctf-web-ctf-csdn-ctf-web-flag.md) | 记一次院赛CTF的WEB题（入门级别） |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [记录一道神仙CTF-wtf.sh-150_asdqwe10203的博客-CSDN博客](../../../cards/docs-ctf-wtf-sh-150-asdqwe10203-csdn.md) | 记录一道神仙CTF |  | file-inclusion, http-analysis, privilege-escalation, sql-injection |
| [静默开水的博客_CSDN博客-CTF,web题解题思路,Misc 图片隐写领域博主](../../../cards/docs-csdn-ctf-web-misc.md) | 静默开水的博客 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
