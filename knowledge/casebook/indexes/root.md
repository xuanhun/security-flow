# Casebook Root Index

Navigation: choose a category, then an artifact, then a technique or route, then a card.
Do not use fuzzy keyword search for normal case lookup.

## Categories

| Category | Cases | Artifacts | Techniques |
| --- | --- | --- | --- |
| [Web](categories/web.md) | 341 | 15 | 44 |
| [Crypto](categories/crypto.md) | 121 | 12 | 35 |
| [Pwn](categories/pwn.md) | 118 | 8 | 29 |
| [Misc](categories/misc.md) | 108 | 12 | 34 |
| [Endpoint Forensics](categories/endpoint-forensics.md) | 82 | 13 | 20 |
| [Reverse](categories/reverse.md) | 56 | 6 | 26 |
| [Network Forensics](categories/network-forensics.md) | 44 | 11 | 17 |
| [Training and Meta](categories/training-and-meta.md) | 30 | 6 | 25 |
| [SIEM (ELK, Splunk, etc.)](categories/siem-elk-splunk-etc.md) | 22 | 11 | 15 |
| [Pentesting](categories/pentesting.md) | 21 | 4 | 11 |
| [Malware Analysis](categories/malware-analysis.md) | 20 | 9 | 13 |
| [Cyber Threat Intelligence (CTI)](categories/cyber-threat-intelligence-cti.md) | 8 | 3 | 8 |
| [Incident Response](categories/incident-response.md) | 6 | 5 | 14 |
| [Email Analysis](categories/email-analysis.md) | 5 | 1 | 5 |
| [Mobile Forensics](categories/mobile-forensics.md) | 3 | 3 | 3 |
| [Reverse Engineering](categories/reverse-engineering.md) | 3 | 1 | 5 |
| [IDS/IPS](categories/ids-ips.md) | 2 | 2 | 5 |
| [AI and Digital Watermark](categories/ai-and-digital-watermark.md) | 1 | 2 | 7 |

## CLI Navigation

```bash
python3 skills/kali/scripts/ctf_casebook.py browse
python3 skills/kali/scripts/ctf_casebook.py browse --category 'Network Forensics'
python3 skills/kali/scripts/ctf_casebook.py browse --category 'Network Forensics' --artifact pcap
python3 skills/kali/scripts/ctf_casebook.py browse --category 'Network Forensics' --artifact pcap --technique http-analysis --cards
```
