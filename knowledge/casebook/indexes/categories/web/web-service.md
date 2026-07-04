# Web / web-service

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| web-exploitation | 74 | burp-driven evidence lookup, http evidence extraction, sql injection exploitation, file upload bypass, waf bypass |
| http-analysis | 64 | http evidence extraction, burp-driven evidence lookup, sql injection exploitation, file inclusion exploitation, file upload bypass |
| command-injection | 49 | http evidence extraction, burp-driven evidence lookup, sql injection exploitation, command execution path, file inclusion exploitation |
| encoding-analysis | 47 | burp-driven evidence lookup, http evidence extraction, sql injection exploitation, file inclusion exploitation, file upload bypass |
| crypto-analysis | 44 | burp-driven evidence lookup, http evidence extraction, sql injection exploitation, file inclusion exploitation, file upload bypass |
| php-tricks | 44 | burp-driven evidence lookup, http evidence extraction, sql injection exploitation, file inclusion exploitation, deserialization chain |
| waf-bypass | 44 | http evidence extraction, burp-driven evidence lookup, sql injection exploitation, waf bypass, file inclusion exploitation |
| sql-injection | 43 | http evidence extraction, burp-driven evidence lookup, sql injection exploitation, file inclusion exploitation, waf bypass |
| classical-crypto | 41 | burp-driven evidence lookup, http evidence extraction, sql injection exploitation, file inclusion exploitation, deserialization chain |
| file-inclusion | 33 | http evidence extraction, burp-driven evidence lookup, file inclusion exploitation, sql injection exploitation, file upload bypass |
| file-upload | 28 | http evidence extraction, burp-driven evidence lookup, file upload bypass, sql injection exploitation, file inclusion exploitation |
| deserialization | 20 | http evidence extraction, burp-driven evidence lookup, sql injection exploitation, deserialization chain, file inclusion exploitation |
| dns-analysis | 17 | http evidence extraction, burp-driven evidence lookup, file inclusion exploitation, dns pivot, sql injection exploitation |
| ret2libc | 17 | http evidence extraction, burp-driven evidence lookup, sql injection exploitation, file inclusion exploitation, command execution path |
| service-enumeration | 16 | http evidence extraction, burp-driven evidence lookup, sql injection exploitation, command execution path, file upload bypass |
| xss | 16 | burp-driven evidence lookup, http evidence extraction, sql injection exploitation, xss route, cipher decoding |
| ssti | 13 | http evidence extraction, ssti exploitation, burp-driven evidence lookup, file inclusion exploitation, sql injection exploitation |
| browser-forensics | 12 | burp-driven evidence lookup, http evidence extraction, sql injection exploitation, file inclusion exploitation, waf bypass |
| binary-exploitation | 11 | burp-driven evidence lookup, http evidence extraction, file inclusion exploitation, sql injection exploitation, command execution path |
| misc-analysis | 11 | burp-driven evidence lookup, http evidence extraction, file upload bypass, sql injection exploitation, ssti exploitation |
| qr-analysis | 7 | http evidence extraction, burp-driven evidence lookup, deserialization chain, sql injection exploitation, cipher decoding |
| jwt-analysis | 6 | burp-driven evidence lookup, file upload bypass, http evidence extraction, sql injection exploitation, deserialization chain |
| web-enumeration | 6 | http evidence extraction, burp-driven evidence lookup, deserialization chain, sql injection exploitation, ssti exploitation |
| traffic-analysis | 5 | burp-driven evidence lookup, deserialization chain, ssti exploitation, cipher decoding, file upload bypass |
| image-analysis | 4 | burp-driven evidence lookup, http evidence extraction, ssti exploitation, cipher decoding, command execution path |
| symbolic-execution | 4 | http evidence extraction, burp-driven evidence lookup, file inclusion exploitation, sql injection exploitation, deserialization chain |
| osint | 3 | burp-driven evidence lookup, http evidence extraction, cipher decoding, waf bypass, xss route |
| password-cracking | 3 | burp-driven evidence lookup, dirb-driven evidence lookup, http evidence extraction, sql injection exploitation, ssti exploitation |
| email-header-analysis | 2 | burp-driven evidence lookup, http evidence extraction, waf bypass |
| reverse-engineering | 2 | file inclusion exploitation, http evidence extraction, reverse engineering, sql injection exploitation, ssti exploitation |
| stack-overflow | 2 | burp-driven evidence lookup, cipher decoding, deserialization chain, http evidence extraction, ssti exploitation |
| stego-extraction | 2 | burp-driven evidence lookup, deserialization chain, ssti exploitation |
| format-string | 1 | burp-driven evidence lookup, command execution path, http evidence extraction, sql injection exploitation, waf bypass |
| malware-static | 1 | burp-driven evidence lookup, deserialization chain |
| memory-forensics | 1 | burp-driven evidence lookup, cipher decoding, deserialization chain, http evidence extraction |
| mobile-forensics | 1 | ssti exploitation |
| network-forensics | 1 | burp-driven evidence lookup, cipher decoding, deserialization chain, http evidence extraction |
| privilege-escalation | 1 | dirb-driven evidence lookup, http evidence extraction, ssti exploitation |
| ret2text | 1 | burp-driven evidence lookup, http evidence extraction |
| timeline-analysis | 1 | detect-it-easy-driven evidence lookup, dns pivot, file inclusion exploitation, http evidence extraction, sql injection exploitation |

## Route Types

| Route type | Cases |
| --- | --- |
| burp-driven evidence lookup | 58 |
| http evidence extraction | 58 |
| sql injection exploitation | 28 |
| file upload bypass | 14 |
| waf bypass | 14 |
| command execution path | 13 |
| file inclusion exploitation | 13 |
| deserialization chain | 8 |
| netcat-driven evidence lookup | 8 |
| ssti exploitation | 8 |
| cipher decoding | 7 |
| xss route | 6 |
| detect-it-easy-driven evidence lookup | 4 |
| dns pivot | 4 |
| nmap-driven evidence lookup | 3 |
| credential discovery | 2 |
| antsword-driven evidence lookup | 1 |
| conversation statistics | 1 |
| dirb-driven evidence lookup | 1 |
| jwt trust-boundary abuse | 1 |
| reverse engineering | 1 |
| stego extraction | 1 |
| timeline reconstruction | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [+ 未分类](../../../cards/summary.md) | SUMMARY.md |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [2019SCUCTF部分题解_东坡何罪发文章总是审核不通过，去博客园了的博客-CSDN博客](../../../cards/docs-2019scuctf-csdn.md) | 2019SCUCTF部分题解 |  | binary-exploitation, classical-crypto, crypto-analysis, deserialization |
| [[BUUCTF 2018]Online Tool 题解_偷一个月亮的博客-CSDN博客](../../../cards/docs-buuctf-2018-online-tool-csdn.md) | BUUCTF 2018 |  | command-injection, http-analysis, php-tricks, ret2libc |
| [[BUUCTF 2018]Online Tool_Sk1y的博客-CSDN博客](../../../cards/docs-buuctf-2018-online-tool-sk1y-csdn.md) | BUUCTF 2018 |  | command-injection, http-analysis, php-tricks, ret2libc |
| [[FSCTF 2023]加速加速](../../../cards/web-fsctf-2023.md) | FSCTF 2023 |  | command-injection, file-inclusion, file-upload, http-analysis |
| [[HNCTF 2022 WEEK2]easy_sql](../../../cards/web-hnctf-2022-week2-easy-sql.md) | HNCTF 2022 WEEK2 |  | http-analysis, sql-injection, waf-bypass, web-exploitation |
| [[NSSRound#30 Duo]hack_the_world!](../../../cards/web-nssround-30-duo-hack-the-world.md) | NSSRound#30 Duo |  | dns-analysis, http-analysis, jwt-analysis, ssti |
| [[WP/BUU/Unicode编码]BUUCTF Unicorn shop题解_車鈊的博客-CSDN博客](../../../cards/docs-wp-buu-unicode-buuctf-unicorn-shop-csdn.md) | WP/BUU/Unicode编码 |  | encoding-analysis, http-analysis, web-exploitation |
| [[网鼎杯 2018]Fakebook](../../../cards/web-2018-fakebook.md) | 网鼎杯 2018 |  | binary-exploitation, deserialization, http-analysis, php-tricks |
| [Bugku CTF 题目解析 (1-10题)_半夜好饿的博客-CSDN博客_ctf题库及详解](../../../cards/docs-bugku-ctf-1-10-csdn-ctf.md) | Bugku CTF 题目解析 (1 |  | command-injection, crypto-analysis, http-analysis, php-tricks |
| [BugkuCTF WEB前五题题解 莽就完事了_废物竹子的博客-CSDN博客](../../../cards/docs-bugkuctf-web-csdn.md) | BugkuCTF WEB前五题题解 莽就完事了 |  | http-analysis, php-tricks, web-exploitation |
| [BugkuCTF-WEB部分题解（一）_flying_bird2019的博客-CSDN博客_bugkuctfweb题解](../../../cards/docs-bugkuctf-web-flying-bird2019-csdn-bugkuctfweb.md) | BugkuCTF |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [BugkuCTF-WEB部分题解（二）_flying_bird2019的博客-CSDN博客](../../../cards/docs-bugkuctf-web-flying-bird2019-csdn.md) | BugkuCTF |  | classical-crypto, crypto-analysis, encoding-analysis, php-tricks |
| [BugkuCTF: web3 ； 域名解析_s0i1的博客-CSDN博客](../../../cards/docs-bugkuctf-web3-s0i1-csdn.md) | BugkuCTF: web3 ； 域名解析 |  | crypto-analysis, dns-analysis, file-upload, http-analysis |
| [BugKuCTF_WEB题解报告_whatacutepanda的博客-CSDN博客_bugku web题解](../../../cards/docs-bugkuctf-web-whatacutepanda-csdn-bugku-web.md) | BugKuCTF |  | browser-forensics, file-upload, http-analysis, web-exploitation |
| [BugkuCTF平台-Web题目笔记_手可摘星辰丶的博客-CSDN博客](../../../cards/docs-bugkuctf-web-csdn.md) | BugkuCTF平台 |  | command-injection, crypto-analysis, encoding-analysis, file-inclusion |
| [Bugku—web题解_Sn0w/的博客-CSDN博客_bugku题解](../../../cards/docs-bugku-web-sn0w-csdn-bugku.md) | Bugku—web题解 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [BugKu题解备注（1）_s11show_163的博客-CSDN博客](../../../cards/docs-bugku-1-s11show-163-csdn.md) | BugKu题解备注（1） |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [buuctf web小结_绿冰壶的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | buuctf web小结 |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [BUUCTF__[BUUCTF 2018]Online Tool_题解_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-buuctf-2018-online-tool-csdn.md) | BUUCTF |  | command-injection, http-analysis, php-tricks, ret2libc |
| [BUUCTF__web题解合集（七）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | classical-crypto, command-injection, deserialization, encoding-analysis |
| [BUUCTF__web题解合集（十一）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | browser-forensics, classical-crypto, command-injection, encoding-analysis |
| [BUUCTF__web题解合集（四）_风过江南乱的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [BUUCTF_web部分题解_ro4lsc的博客-CSDN博客](../../../cards/docs-buuctf-web-ro4lsc-csdn.md) | BUUCTF |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [BUUCTF寒假刷题-Web_深海神奇舰舰长的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF寒假刷题 |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [BUUCTF解题web十一道(03)_Sprint#51264的博客-CSDN博客](../../../cards/docs-buuctf-web-03-sprint-51264-csdn.md) | BUUCTF解题web十一道(03) |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [BUUCTF解题十一道(04)_Sprint#51264的博客-CSDN博客](../../../cards/docs-buuctf-04-sprint-51264-csdn.md) | BUUCTF解题十一道(04) |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [Buuctf部分题解_君陌上的博客-CSDN博客_buuctf](../../../cards/docs-buuctf-csdn-buuctf.md) | Buuctf部分题解 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [ctf php 流量分析题,GKCTF EZWEB的分析题解和思考_一点能源的博客-CSDN博客](../../../cards/docs-ctf-php-gkctf-ezweb-csdn.md) | ctf php 流量分析题,GKCTF EZWEB的分析题解和思考 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [ctf show-web入门 php特性篇部分题解_z.volcano的博客-CSDN博客_ctfshow的php特性](../../../cards/docs-ctf-show-web-php-z-volcano-csdn-ctfshow-php.md) | ctf show |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [ctf show-web入门 SSTI篇部分题解_z.volcano的博客-CSDN博客_ctfshow web入门ssti](../../../cards/docs-ctf-show-web-ssti-z-volcano-csdn-ctfshow-web-ssti.md) | ctf show |  | command-injection, ssti, waf-bypass, web-exploitation |
| [ctf web个人总结_recover517的博客-CSDN博客](../../../cards/docs-ctf-web-recover517-csdn.md) | ctf web个人总结 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF web入门——HTTP头相关的----修改请求头、伪造Cookie类题目——Bugku Web题目详细题解_日熙！的博客-CSDN博客_ctf请求头题目](../../../cards/docs-ctf-web-http-cookie-bugku-web-csdn-ctf.md) | CTF web入门——HTTP头相关的 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [CTF web题型解题技巧_吃素的小动物的博客-CSDN博客](../../../cards/docs-ctf-web-csdn.md) | CTF web题型解题技巧 |  | browser-forensics, crypto-analysis, file-inclusion, file-upload |
| [CTF---Web入门第二题 上传绕过_weixin_30344995的博客-CSDN博客](../../../cards/docs-ctf-web-weixin-30344995-csdn.md) | CTF |  | command-injection, encoding-analysis, file-upload, waf-bypass |
| [CTF-rootme 题解之HTTP - Open redirect_weixin_30952535的博客-CSDN博客](../../../cards/docs-ctf-rootme-http-open-redirect-weixin-30952535-csdn.md) | CTF |  | binary-exploitation, command-injection, http-analysis, php-tricks |
| [CTF-Web小白入门篇超详细——了解CTF-Web基本题型及其解题方法 总结——包含例题的详细题解_日熙！的博客-CSDN博客_ctf](../../../cards/docs-ctf-web-ctf-web-csdn-ctf.md) | CTF |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [CTF-入门一__starstarli的博客-CSDN博客](../../../cards/docs-ctf-starstarli-csdn.md) | CTF |  | binary-exploitation, command-injection, crypto-analysis, dns-analysis |
| [CTF-加密与解密（十一）_红烧兔纸的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | CTF |  | command-injection, crypto-analysis, encoding-analysis, http-analysis |
| [ctfhub技能书+历年真题学习笔记（详解）_Yn8rt的博客-CSDN博客](../../../cards/docs-ctfhub-yn8rt-csdn.md) | ctfhub技能书+历年真题学习笔记（详解） |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF|BugkuCTF-WEB解题思路_「已注销」的博客-CSDN博客_bugkuctfweb题解](../../../cards/docs-ctf-bugkuctf-web-csdn-bugkuctfweb.md) | CTF|BugkuCTF |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [CTF之Sqli-Labs题目解析（1-11题）_z11h的博客-CSDN博客_sqllabs题目](../../../cards/docs-ctf-sqli-labs-1-11-z11h-csdn-sqllabs.md) | CTF之Sqli |  | http-analysis, php-tricks, qr-analysis, sql-injection |
| [CTF之WEB（BUGku Ctf 1-7 题解）_嗅探的博客-CSDN博客](../../../cards/docs-ctf-web-bugku-ctf-1-7-csdn.md) | CTF之WEB（BUGku Ctf 1 |  | binary-exploitation, command-injection, encoding-analysis, web-exploitation |
| [CTF学习-web解题思路_菜鸟-传奇的博客-CSDN博客](../../../cards/docs-ctf-web-csdn.md) | CTF学习 |  | browser-forensics, classical-crypto, crypto-analysis, dns-analysis |
| [CTF解题-Bugku_Web_WriteUp (上）_Tr0e的博客-CSDN博客_bugku web writeup](../../../cards/docs-ctf-bugku-web-writeup-tr0e-csdn-bugku-web-writeup.md) | CTF解题 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF解题-网安实验室(注入关)_Tr0e的博客-CSDN博客](../../../cards/docs-ctf-tr0e-csdn.md) | CTF解题 |  | dns-analysis, file-inclusion, http-analysis, php-tricks |
| [CTF解题思路笔记_山兔1的博客-CSDN博客_ctf解题](../../../cards/docs-ctf-1-csdn-ctf.md) | CTF解题思路笔记 |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [ctf训练 web安全暴力破解_爱吃香菜的哈哈的博客-CSDN博客](../../../cards/docs-ctf-web-csdn.md) | ctf训练 web安全暴力破解 |  | crypto-analysis, http-analysis, password-cracking, privilege-escalation |
| [CTF里面的WEB题的一些解决思路_F10W3RDANC3的博客-CSDN博客_ctfweb思路](../../../cards/docs-ctf-web-f10w3rdanc3-csdn-ctfweb.md) | CTF里面的WEB题的一些解决思路 |  | command-injection, file-upload, http-analysis, sql-injection |
| [ctf镜子里面的世界_攻防世界XCTF-WEB入门12题解题报告_weixin_39877050的博客-CSDN博客](../../../cards/docs-ctf-xctf-web-12-weixin-39877050-csdn.md) | ctf镜子里面的世界 |  | command-injection, crypto-analysis, http-analysis, ret2libc |
| [ctf题解——sql注入（cookie注入）_ckkkkkkkkke的博客-CSDN博客](../../../cards/docs-ctf-sql-cookie-ckkkkkkkkke-csdn.md) | ctf题解——sql注入（cookie注入） |  | http-analysis, sql-injection, web-exploitation |
| [hxp 36C3 CTF Web题 WriteupBin Writeup (Selenium模拟点击+Content Security Policy+Nonce+Parsley.js触发错误提示)_KevinLuo2000的博客-CSDN博客](../../../cards/docs-hxp-36c3-ctf-web-writeupbin-writeup-selenium-content-security-policy-nonce-parsley-js-kevinluo2000-csdn.md) | hxp 36C3 CTF Web |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [JIS-CTF : VulnUpload 题解_weixin_33676492的博客-CSDN博客](../../../cards/docs-jis-ctf-vulnupload-weixin-33676492-csdn.md) | JIS |  | file-upload, http-analysis, service-enumeration, web-exploitation |
| [python 重定向 ctf_CTF web题型解题技巧 第四课 web总结_weixin_39615984的博客-CSDN博客](../../../cards/docs-python-ctf-ctf-web-web-weixin-39615984-csdn.md) | python 重定向 ctf |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [S3cCTF-gyy-Writeup_Err0rCM的博客-CSDN博客](../../../cards/docs-s3cctf-gyy-writeup-err0rcm-csdn.md) | S3cCTF |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [SWPUCTF web 部分题解_HyyMbb的博客-CSDN博客](../../../cards/docs-swpuctf-web-hyymbb-csdn.md) | SWPUCTF web 部分题解 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [There only 10 people use the same phone as you（i春秋CTF题解）_weixin_30618985的博客-CSDN博客](../../../cards/docs-there-only-10-people-use-the-same-phone-as-you-i-ctf-weixin-30618985-csdn.md) | There only 10 people use the same phone |  | sql-injection |
| [welcome to bugkuctf（详解）——Bugku_weixin_33728268的博客-CSDN博客](../../../cards/docs-welcome-to-bugkuctf-bugku-weixin-33728268-csdn.md) | welcome to bugkuctf（详解）——Bugku |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [【BUUCTF刷题】Web解题方法总结（一)_Y1seco的博客-CSDN博客_buuctfweb](../../../cards/docs-buuctf-web-y1seco-csdn-buuctfweb.md) | 【BUUCTF刷题】Web解题方法总结（一) |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [【web】BUUCTF-web刷题记录_weixin_30684743的博客-CSDN博客](../../../cards/docs-web-buuctf-web-weixin-30684743-csdn.md) | 【web】BUUCTF |  | binary-exploitation, encoding-analysis, http-analysis, php-tricks |
| [〖教程〗K8飞刀-网络安全CTF解题Web篇10个例子_k8gege的博客-CSDN博客](../../../cards/docs-k8-ctf-web-10-k8gege-csdn.md) | 〖教程〗K8飞刀 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [〖教程〗K8飞刀-网络安全CTF解题Web篇10例_k8gege的博客-CSDN博客_k8飞刀](../../../cards/docs-k8-ctf-web-10-k8gege-csdn-k8.md) | 〖教程〗K8飞刀 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [一道简单的CTF登录题题解_anquanniu牛油果的博客-CSDN博客_ctf login题目](../../../cards/docs-ctf-anquanniu-csdn-ctf-login.md) | 一道简单的CTF登录题题解 |  | classical-crypto, crypto-analysis, deserialization, encoding-analysis |
| [使用burpsuite解决ctf的web题_我眼中的你的博客-CSDN博客](../../../cards/docs-burpsuite-ctf-web-csdn.md) | 使用burpsuite解决ctf的web题 |  | web-exploitation |
| [信息安全web入门——南邮ctf解题_sevenlob的博客-CSDN博客_南邮ctf](../../../cards/docs-web-ctf-sevenlob-csdn-ctf.md) | 信息安全web入门——南邮ctf解题 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [实验吧CTF练习题---WEB---头有点大解析_dingbai2663的博客-CSDN博客](../../../cards/docs-ctf-web-dingbai2663-csdn.md) | 实验吧CTF练习题 |  | crypto-analysis, http-analysis, web-exploitation |
| [实验吧WEB CTF 头有点大 全网最简单易懂的解题方法_滕青山YYDS的博客-CSDN博客_实验吧维护](../../../cards/docs-web-ctf-yyds-csdn.md) | 实验吧WEB CTF 头有点大 全网最简单易懂的解题方法 |  | command-injection, crypto-analysis, http-analysis, web-exploitation |
| [手把手教你用Burp抓包——Bugku 头等舱 超详细题解——CTF web小白入门基础篇_日熙！的博客-CSDN博客_bugku头等舱](../../../cards/docs-burp-bugku-ctf-web-csdn-bugku.md) | 手把手教你用Burp抓包——Bugku |  | command-injection, web-exploitation |
| [技能五子棋](../../../cards/web-gccctf-2025.md) | GCCCTF 2025 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [攻防世界-web-fakebook-从0到1的解题历程writeup_CTF小白的博客-CSDN博客_攻防世界fakebook](../../../cards/docs-web-fakebook-0-1-writeup-ctf-csdn-fakebook.md) | 攻防世界 |  | deserialization, http-analysis, php-tricks, sql-injection |
| [春秋web题目解题及思路汇总（自用搜集）_香草星冰乐的博客-CSDN博客](../../../cards/docs-web-csdn.md) | 春秋web题目解题及思路汇总（自用搜集） |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [蓝鲸CTF-web-密码泄露_烟雨天青色的博客-CSDN博客](../../../cards/docs-ctf-web-csdn.md) | 蓝鲸CTF |  | classical-crypto, encoding-analysis, web-exploitation, xss |
| [西普学院CTF习题解析——WEB(已完成16/16)_Xyntax的博客-CSDN博客](../../../cards/docs-ctf-web-16-16-xyntax-csdn.md) | 西普学院CTF习题解析——WEB(已完成16/16) |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [解网鼎杯一道web题（fakebook）_诸神之眼的博客-CSDN博客_fakebook](../../../cards/docs-web-fakebook-csdn-fakebook.md) | 解网鼎杯一道web题（fakebook） |  | browser-forensics, classical-crypto, deserialization, encoding-analysis |
| [静默开水的博客_CSDN博客-CTF,web题解题思路,Misc 图片隐写领域博主](../../../cards/docs-csdn-ctf-web-misc.md) | 静默开水的博客 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
