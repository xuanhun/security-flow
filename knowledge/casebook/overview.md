# CTF Casebook

This is a compact local reasoning casebook distilled from external CTF writeups and mirrored study repositories.
Use `scripts/ctf_casebook.py browse` to walk category, artifact, technique, and route before starting a new CTF route.

- Cases parsed: `991`
- Mirrored assets: `8585`
- Generated: `2026-06-24T00:38:30+00:00`
- Root index: `indexes/root.md`
- Source index: `indexes/sources/root.md`
- Taxonomy: `taxonomy.json`

## Sources

- `ctf_writeups` | https://github.com/tim-barc/ctf_writeups | commit `0dde10d9fa516621040828b60a2a91584ba07515` | cases `209`
- `CUCCS/ctf-wps` | https://github.com/CUCCS/ctf-wps | commit `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70` | cases `112` | assets `661`
- `apachecn/apachecn-ctf-wiki` | https://github.com/apachecn/apachecn-ctf-wiki | commit `762ca130572c95196cf120e5f4ad5fbdd88b1b93` | cases `670` | assets `7924`

## Categories

- `AI and Digital Watermark`: 1
- `Crypto`: 121
- `Cyber Threat Intelligence (CTI)`: 8
- `Email Analysis`: 5
- `Endpoint Forensics`: 82
- `IDS/IPS`: 2
- `Incident Response`: 6
- `Malware Analysis`: 20
- `Misc`: 108
- `Mobile Forensics`: 3
- `Network Forensics`: 44
- `Pentesting`: 21
- `Pwn`: 118
- `Reverse`: 56
- `Reverse Engineering`: 3
- `SIEM (ELK, Splunk, etc.)`: 22
- `Training and Meta`: 30
- `Web`: 341

## Top Tools

- `netcat`: 445
- `ida`: 164
- `pwntools`: 116
- `radare2`: 90
- `detect-it-easy`: 90
- `virustotal`: 88
- `burp`: 82
- `wireshark`: 80
- `strings`: 71
- `gdb`: 63
- `cyberchef`: 55
- `binwalk`: 52
- `z3`: 43
- `nmap`: 41
- `volatility`: 37
- `stegsolve`: 37
- `checksec`: 33
- `sqlmap`: 32
- `john`: 32
- `foremost`: 29

## Top Techniques

- `http-analysis`: 594
- `web-exploitation`: 558
- `crypto-analysis`: 381
- `encoding-analysis`: 380
- `classical-crypto`: 299
- `command-injection`: 265
- `waf-bypass`: 199
- `php-tricks`: 197
- `binary-exploitation`: 190
- `reverse-engineering`: 183
- `dns-analysis`: 183
- `misc-analysis`: 162
- `file-inclusion`: 159
- `ret2libc`: 137
- `sql-injection`: 136
- `stego-extraction`: 118
- `qr-analysis`: 117
- `service-enumeration`: 112
- `image-analysis`: 105
- `network-forensics`: 98

## Top Route Types

- `http evidence extraction`: 601
- `cipher decoding`: 236
- `netcat-driven evidence lookup`: 197
- `evidence lookup`: 173
- `reverse engineering`: 165
- `credential discovery`: 119
- `command execution path`: 119
- `file inclusion exploitation`: 106
- `dns pivot`: 104
- `sql injection exploitation`: 95
- `waf bypass`: 77
- `timeline reconstruction`: 77
- `memory artifact analysis`: 77
- `burp-driven evidence lookup`: 67
- `stego extraction`: 64
- `file upload bypass`: 54
- `stack control exploitation`: 53
- `indicator enrichment`: 52
- `detect-it-easy-driven evidence lookup`: 51
- `deserialization chain`: 38

## Asset Kinds

- `image`: 7663
- `markdown`: 782
- `script`: 46
- `ttf`: 21
- `woff`: 20
- `woff2`: 20
- `css`: 11
- `file`: 9
- `svg`: 7
- `data`: 4
- `html`: 2

## Browse

```bash
./skills/kali/scripts/ctf_casebook.py browse
./skills/kali/scripts/ctf_casebook.py browse --category 'Network Forensics'
./skills/kali/scripts/ctf_casebook.py browse --category 'Network Forensics' --artifact pcap
./skills/kali/scripts/ctf_casebook.py browse --category 'Network Forensics' --artifact pcap --technique http-analysis --cards
./skills/kali/scripts/ctf_casebook.py show --slug cyber-defenders-packetmaze-lab
./skills/kali/scripts/ctf_casebook.py search --query ssti
./skills/kali/scripts/ctf_casebook.py search --query yakit --type asset
```

Browse results point to local cards under `cards/`. Search results can also point into mirrored raw repository assets under `sources/`.
Read the card first; refresh the casebook only when the compact card lacks enough context.
