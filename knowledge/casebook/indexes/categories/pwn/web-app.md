# Pwn / web-app

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| binary-exploitation | 51 | stack control exploitation, http evidence extraction, gdb-driven evidence lookup, reverse engineering, file inclusion exploitation |
| web-exploitation | 47 | stack control exploitation, http evidence extraction, gdb-driven evidence lookup, reverse engineering, memory artifact analysis |
| http-analysis | 38 | stack control exploitation, gdb-driven evidence lookup, http evidence extraction, pwntools-driven evidence lookup, reverse engineering |
| ret2libc | 33 | stack control exploitation, http evidence extraction, gdb-driven evidence lookup, file inclusion exploitation, memory artifact analysis |
| stack-overflow | 30 | stack control exploitation, gdb-driven evidence lookup, pwntools-driven evidence lookup, memory artifact analysis, file inclusion exploitation |
| reverse-engineering | 25 | reverse engineering, http evidence extraction, stack control exploitation, command execution path, file inclusion exploitation |
| command-injection | 19 | http evidence extraction, command execution path, file inclusion exploitation, memory artifact analysis, gdb-driven evidence lookup |
| encoding-analysis | 17 | http evidence extraction, reverse engineering, netcat-driven evidence lookup, stack control exploitation, memory artifact analysis |
| ret2text | 17 | stack control exploitation, gdb-driven evidence lookup, pwntools-driven evidence lookup, command execution path, http evidence extraction |
| file-inclusion | 15 | file inclusion exploitation, http evidence extraction, reverse engineering, gdb-driven evidence lookup, memory artifact analysis |
| waf-bypass | 12 | http evidence extraction, waf bypass, checksec-driven evidence lookup, reverse engineering, stack control exploitation |
| crypto-analysis | 11 | http evidence extraction, reverse engineering, checksec-driven evidence lookup, cipher decoding, file inclusion exploitation |
| integer-overflow | 9 | http evidence extraction, command execution path, file inclusion exploitation, memory artifact analysis, reverse engineering |
| classical-crypto | 8 | http evidence extraction, reverse engineering, cipher decoding, file inclusion exploitation, stack control exploitation |
| service-enumeration | 7 | file inclusion exploitation, gdb-driven evidence lookup, http evidence extraction, command execution path, credential discovery |
| browser-forensics | 6 | file inclusion exploitation, http evidence extraction, command execution path, credential discovery, gdb-driven evidence lookup |
| format-string | 5 | http evidence extraction, reverse engineering, format-string control path, gdb-driven evidence lookup, stack control exploitation |
| image-analysis | 4 | http evidence extraction, memory artifact analysis, file inclusion exploitation, reverse engineering, checksec-driven evidence lookup |
| symbolic-execution | 4 | reverse engineering, http evidence extraction, stack control exploitation, checksec-driven evidence lookup, cipher decoding |
| misc-analysis | 3 | http evidence extraction, reverse engineering, checksec-driven evidence lookup, cipher decoding, constraint solving |
| privilege-escalation | 3 | file inclusion exploitation, command execution path, credential discovery, gdb-driven evidence lookup, http evidence extraction |
| qr-analysis | 2 | http evidence extraction, reverse engineering, checksec-driven evidence lookup, cipher decoding, constraint solving |
| malware-static | 1 | file inclusion exploitation, gdb-driven evidence lookup |
| mobile-forensics | 1 | http evidence extraction, jadx-driven evidence lookup |
| osint | 1 | checksec-driven evidence lookup, http evidence extraction, reverse engineering, stack control exploitation |
| php-tricks | 1 | cipher decoding, constraint solving, http evidence extraction, memory artifact analysis, reverse engineering |
| sql-injection | 1 | cipher decoding, constraint solving, http evidence extraction, memory artifact analysis, reverse engineering |
| stego-extraction | 1 | file inclusion exploitation, gdb-driven evidence lookup |

## Route Types

| Route type | Cases |
| --- | --- |
| stack control exploitation | 26 |
| http evidence extraction | 22 |
| gdb-driven evidence lookup | 18 |
| reverse engineering | 18 |
| file inclusion exploitation | 15 |
| memory artifact analysis | 12 |
| command execution path | 10 |
| netcat-driven evidence lookup | 10 |
| pwntools-driven evidence lookup | 10 |
| waf bypass | 8 |
| checksec-driven evidence lookup | 7 |
| credential discovery | 5 |
| cipher decoding | 4 |
| ida-driven evidence lookup | 4 |
| timeline reconstruction | 3 |
| 无-driven evidence lookup | 3 |
| format-string control path | 2 |
| constraint solving | 1 |
| evidence lookup | 1 |
| ghidra-driven evidence lookup | 1 |
| IDA Pro 非必须-driven evidence lookup | 1 |
| IDA pro-driven evidence lookup | 1 |
| IDA-driven evidence lookup | 1 |
| integer-overflow bypass | 1 |
| jadx-driven evidence lookup | 1 |
| radare2-driven evidence lookup | 1 |
| ropgadget-driven evidence lookup | 1 |
| sql injection exploitation | 1 |
| stego extraction | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [2019 D^3CTF unprintableV详细题解_ha1vk的博客-CSDN博客](../../../cards/docs-2019-d-3ctf-unprintablev-ha1vk-csdn.md) | 2019 D^3CTF unprintableV详细题解 |  | binary-exploitation, encoding-analysis, file-inclusion, format-string |
| [2021DNUICTF（东软杯CTF）的几个签到题writeup_Q1X1的博客-CSDN博客](../../../cards/docs-2021dnuictf-ctf-writeup-q1x1-csdn.md) | 2021DNUICTF（东软杯CTF）的几个签到题writeup |  | binary-exploitation, crypto-analysis, encoding-analysis, misc-analysis |
| [[BJDCTF 2020]babystack2.0](../../../cards/pwn-bjdctf-2020-babystack2-0.md) | BJDCTF 2020 |  | binary-exploitation, command-injection, http-analysis, integer-overflow |
| [[CISCN 2019华北]PWN1](../../../cards/pwn-ciscn-2019-pwn1.md) | CISCN 2019华北 |  | binary-exploitation, command-injection, http-analysis, ret2libc |
| [[FSCTF 2023]rdi](../../../cards/pwn-rdi.md) | FSCTF 2023 |  | binary-exploitation, http-analysis, ret2libc, ret2text |
| [[GFCTF 2021]where_is_shell](../../../cards/pwn-gfctf-2021-where-is-shell.md) | GFCTF 2021 |  | binary-exploitation, http-analysis, ret2libc, ret2text |
| [[GHCTF 2025]Hello_world](../../../cards/pwn-ghctf-2025-hello-world.md) | GHCTF 2025 |  | binary-exploitation, http-analysis, ret2text, reverse-engineering |
| [[GHCTF 2025]Hello_world](../../../cards/pwn-hello-world.md) | GHCTF 2025 |  | binary-exploitation, http-analysis, ret2libc, ret2text |
| [[HGAME 2023 week1]test_nc](../../../cards/pwn-test-nc.md) | HGAME 2023 week1 |  | binary-exploitation, encoding-analysis, http-analysis, reverse-engineering |
| [[HNCTF 2022 Week1]easyoverflow](../../../cards/pwn-hnctf-2022-week1-easyoverflow.md) | HNCTF 2022 Week1 |  | binary-exploitation, command-injection, file-inclusion, http-analysis |
| [[HNCTF 2022 WEEK4]checker](../../../cards/pwn-checker.md) | HNCTF 2022 WEEK4 |  | binary-exploitation, crypto-analysis, http-analysis, web-exploitation |
| [[LitCTF 2023]口算题卡](../../../cards/pwn-025e9586.md) | LitCTF 2023 |  | binary-exploitation, http-analysis, web-exploitation |
| [[MoeCTF 2021]ret2text_ez](../../../cards/pwn-ret2text-ez.md) | MoeCTF 2021 |  | binary-exploitation, http-analysis, ret2text, stack-overflow |
| [[NISACTF 2022]ezpie](../../../cards/pwn-ezpie.md) | NISACTF 2022 |  | binary-exploitation, http-analysis, ret2libc, ret2text |
| [[NISACTF 2022]ezpie](../../../cards/pwn-nisactf-2022-ezpie.md) | NISACTF 2022 |  | binary-exploitation, http-analysis, ret2text, reverse-engineering |
| [[NSSCTF 2022 Spring Recruit]R3m4ke?](../../../cards/pwn-r3m4ke.md) | NSSCTF 2022 Spring Recruit |  | binary-exploitation, http-analysis, ret2text, stack-overflow |
| [[SDCTF 2022]Horoscope](../../../cards/pwn-horoscope.md) | SDCTF 2022 |  | binary-exploitation, http-analysis, ret2text, stack-overflow |
| [[SUCTF 2018 招新赛]stack](../../../cards/pwn-stack.md) | SUCTF 2018 招新赛 |  | binary-exploitation, http-analysis, ret2text, stack-overflow |
| [[SWPUCTF 2021 新生赛]gift_pwn](../../../cards/pwn-swpuctf-2021-gift-pwn.md) | SWPUCTF 2021 新生赛 |  | binary-exploitation, command-injection, http-analysis, ret2libc |
| [[SWPUCTF 2022 新生赛]FindanotherWay](../../../cards/pwn-findanotherway.md) | SWPUCTF 2022 新生赛 |  | binary-exploitation, http-analysis, reverse-engineering, stack-overflow |
| [[SWPUCTF 2022 新生赛]Integer Overflow](../../../cards/pwn-integeroverflow.md) | SWPUCTF 2022 新生赛 |  | binary-exploitation, http-analysis, integer-overflow, ret2libc |
| [[SWPUCTF 2023 秋季新生赛]ezlibc](../../../cards/pwn-ezlibc.md) | SWPUCTF 2023 秋季新生赛 |  | binary-exploitation, encoding-analysis, http-analysis, ret2libc |
| [[SWPUCTF 2024 秋季新生赛]又是签到！？](../../../cards/pwn-63e2f2f1.md) | SWPUCTF 2024 秋季新生赛 |  | binary-exploitation, http-analysis, mobile-forensics, web-exploitation |
| [[WUSTCTF 2020]getshell2](../../../cards/pwn-wustctf-2020-getshell2.md) | WUSTCTF 2020 |  | binary-exploitation, command-injection, http-analysis, ret2libc |
| [[WUSTCTF 2020]level1](../../../cards/pwn-level1.md) | WUSTCTF 2020 |  | binary-exploitation, http-analysis, reverse-engineering, web-exploitation |
| [BugkuCTF-PWN题pwn7-repeater详细讲解多解法_彬彬有礼am_03的博客-CSDN博客](../../../cards/docs-bugkuctf-pwn-pwn7-repeater-am-03-csdn.md) | BugkuCTF |  | binary-exploitation, command-injection, encoding-analysis, format-string |
| [BUUCTF ciscn_2019_c_1__N1rvana_的博客-CSDN博客](../../../cards/docs-buuctf-ciscn-2019-c-1-n1rvana-csdn.md) | BUUCTF ciscn |  | binary-exploitation, crypto-analysis, encoding-analysis, http-analysis |
| [buuctf:ciscn_s_3题解_xi@0ji233的博客-CSDN博客](../../../cards/docs-buuctf-ciscn-s-3-xi-0ji233-csdn.md) | buuctf:ciscn |  | binary-exploitation, classical-crypto, file-inclusion, http-analysis |
| [buuctf解题记录_song-10的博客-CSDN博客_buuctf解题](../../../cards/docs-buuctf-song-10-csdn-buuctf.md) | buuctf解题记录 |  | binary-exploitation, command-injection, encoding-analysis, file-inclusion |
| [CG-ctf中RE Hello,RE和ReadAsm2超详细题解_jovy-rtt的博客-CSDN博客](../../../cards/docs-cg-ctf-re-hello-re-readasm2-jovy-rtt-csdn.md) | CG |  | http-analysis, reverse-engineering, web-exploitation |
| [ctf xor题_2020 KCTF秋季赛 | 第九题设计及解题思路_当下的幸福的博客-CSDN博客](../../../cards/docs-ctf-xor-2020-kctf-csdn.md) | ctf xor题 |  | binary-exploitation, file-inclusion, http-analysis, ret2libc |
| [get_started_3dsctf_2016 1_一路开花●-●的博客-CSDN博客](../../../cards/docs-get-started-3dsctf-2016-1-csdn.md) | get |  | binary-exploitation, classical-crypto, file-inclusion, reverse-engineering |
| [GXYCTF部分详细题解_合天网安实验室的博客-CSDN博客](../../../cards/docs-gxyctf-csdn.md) | GXYCTF部分详细题解 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [linux sort 0x7f,【真题解析】浅析CTF中PWN题型的解题思路_余曉波的博客-CSDN博客](../../../cards/docs-linux-sort-0x7f-ctf-pwn-csdn.md) | linux sort 0x7f,【真题解析】浅析CTF中PWN题型的解题思路 |  | binary-exploitation, encoding-analysis, format-string, http-analysis |
| [PWN bof [pwnable.kr]CTF writeup题解系列3_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-bof-pwnable-kr-ctf-writeup-3-3ric5r-csdn.md) | PWN bof [pwnable.kr]CTF writeup题解系列3 |  | binary-exploitation, command-injection, crypto-analysis, file-inclusion |
| [PWN input [pwnable.kr]CTF writeup题解系列7_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-input-pwnable-kr-ctf-writeup-7-3ric5r-csdn.md) | PWN input [pwnable.kr]CTF writeup题解系列7 |  | binary-exploitation, browser-forensics, command-injection, file-inclusion |
| [PWN mistake [pwnable.kr]CTF writeup题解系列8_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-mistake-pwnable-kr-ctf-writeup-8-3ric5r-csdn.md) | PWN mistake [pwnable.kr]CTF writeup题解系列8 |  | binary-exploitation, browser-forensics, command-injection, crypto-analysis |
| [PWN passcode [pwnable.kr]CTF writeup题解系列5_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-passcode-pwnable-kr-ctf-writeup-5-3ric5r-csdn.md) | PWN passcode |  | binary-exploitation, browser-forensics, command-injection, file-inclusion |
| [PWN random [pwnable.kr]CTF writeup题解系列6_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-random-pwnable-kr-ctf-writeup-6-3ric5r-csdn.md) | PWN random [pwnable.kr]CTF writeup题解系列6 |  | binary-exploitation, browser-forensics, command-injection, crypto-analysis |
| [PWN shellshock [pwnable.kr]CTF writeup题解系列9_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-shellshock-pwnable-kr-ctf-writeup-9-3ric5r-csdn.md) | PWN shellshock |  | binary-exploitation, browser-forensics, command-injection, file-inclusion |
| [PWN uaf [pwnable.kr]CTF writeup题解系列13_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-uaf-pwnable-kr-ctf-writeup-13-3ric5r-csdn.md) | PWN uaf [pwnable.kr]CTF writeup题解系列13 |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [shell [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列25_3riC5r的博客-CSDN博客](../../../cards/docs-shell-xctf-pwn-ctf-writeup-25-3ric5r-csdn.md) | shell [XCTF |  | binary-exploitation, file-inclusion, integer-overflow, reverse-engineering |
| [swpuctf2019 p1KkHeap 详细题解_ha1vk的博客-CSDN博客](../../../cards/docs-swpuctf2019-p1kkheap-ha1vk-csdn.md) | swpuctf2019 p1KkHeap 详细题解 |  | binary-exploitation, classical-crypto, encoding-analysis, file-inclusion |
| [【CTF题解NO.00002】minilCTF 2020 - write up by arttnba3_arttnba3的博客-CSDN博客](../../../cards/docs-ctf-no-00002-minilctf-2020-write-up-by-arttnba3-arttnba3-csdn.md) | 【CTF题解NO.00002】minilCTF 2020 |  | binary-exploitation, command-injection, http-analysis, integer-overflow |
| [【CTF题解NO.00003】moeCTF 2020 - official write up by arttnba3_arttnba3的博客-CSDN博客](../../../cards/docs-ctf-no-00003-moectf-2020-official-write-up-by-arttnba3-arttnba3-csdn.md) | 【CTF题解NO.00003】moeCTF 2020 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [【CTF题解NO.00007】VNCTF2021 - pwn - write up by arttnba3_arttnba3的博客-CSDN博客](../../../cards/docs-ctf-no-00007-vnctf2021-pwn-write-up-by-arttnba3-arttnba3-csdn.md) | 【CTF题解NO.00007】VNCTF2021 |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [【CTF题解NO.00008】mini-LCTF 2021 official write up by arttnba3_arttnba3的博客-CSDN博客](../../../cards/docs-ctf-no-00008-mini-lctf-2021-official-write-up-by-arttnba3-arttnba3-csdn.md) | 【CTF题解NO.00008】mini |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [【CTF题解NO.00009】CISCN2021-初赛-pwn write up by arttnba3_arttnba3的博客-CSDN博客](../../../cards/docs-ctf-no-00009-ciscn2021-pwn-write-up-by-arttnba3-arttnba3-csdn.md) | 【CTF题解NO.00009】CISCN2021 |  | binary-exploitation, crypto-analysis, encoding-analysis, image-analysis |
| [信息安全铁人三项赛真题解析_对 [CrackMe] 【ctf】2018信息安全铁人三项赛个人赛总决赛赛题分享 的一些补充..._weixin_39587238的博客-CSDN博客](../../../cards/docs-crackme-ctf-2018-weixin-39587238-csdn.md) | 信息安全铁人三项赛真题解析 |  | binary-exploitation, encoding-analysis, http-analysis, ret2libc |
| [由一道CTF pwn题深入理解libc2.26中的tcache机制_weixin_30363981的博客-CSDN博客](../../../cards/docs-ctf-pwn-libc2-26-tcache-weixin-30363981-csdn.md) | 由一道CTF pwn题深入理解libc2.26中的tcache机制 |  | binary-exploitation, http-analysis, ret2libc, web-exploitation |
| [砰砰砰！2021美团CTF决赛PWN题详解_代码熬夜敲的博客-CSDN博客](../../../cards/docs-2021-ctf-pwn-csdn.md) | 砰砰砰！2021美团CTF决赛PWN题详解 |  | binary-exploitation, command-injection, encoding-analysis, format-string |
| [辣卤客，我为你带来烩面啦！](../../../cards/pwn-gccctf-2025.md) | GCCCTF 2025 |  | binary-exploitation, command-injection, encoding-analysis, http-analysis |
