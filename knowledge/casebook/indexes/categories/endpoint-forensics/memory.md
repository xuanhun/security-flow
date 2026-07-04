# Endpoint Forensics / memory

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| memory-forensics | 31 | memory artifact analysis, http evidence extraction, timeline reconstruction, indicator enrichment, dns pivot |
| http-analysis | 25 | memory artifact analysis, http evidence extraction, timeline reconstruction, indicator enrichment, dns pivot |
| cti-enrichment | 19 | memory artifact analysis, indicator enrichment, http evidence extraction, timeline reconstruction, dns pivot |
| malware-static | 18 | http evidence extraction, memory artifact analysis, timeline reconstruction, indicator enrichment, credential discovery |
| stego-extraction | 16 | http evidence extraction, memory artifact analysis, timeline reconstruction, credential discovery, indicator enrichment |
| timeline-analysis | 15 | memory artifact analysis, http evidence extraction, timeline reconstruction, indicator enrichment, credential discovery |
| dns-analysis | 12 | dns pivot, http evidence extraction, memory artifact analysis, timeline reconstruction, indicator enrichment |
| browser-forensics | 10 | http evidence extraction, memory artifact analysis, indicator enrichment, credential discovery, dns pivot |
| service-enumeration | 5 | memory artifact analysis, indicator enrichment, credential discovery, timeline reconstruction, http evidence extraction |
| windows-event-analysis | 5 | http evidence extraction, dns pivot, event-log correlation, memory artifact analysis, registry artifact correlation |
| password-cracking | 4 | indicator enrichment, memory artifact analysis, dns pivot, http evidence extraction, john-driven evidence lookup |
| maldoc-analysis | 3 | maldoc analysis, memory artifact analysis, olevba-driven evidence lookup, dns pivot, event-log correlation |
| registry-forensics | 3 | timeline reconstruction, http evidence extraction, memory artifact analysis, registry artifact correlation, dns pivot |
| privilege-escalation | 2 | indicator enrichment, credential discovery, dns pivot, registry artifact correlation, service-to-access path |
| malware-dynamic | 1 | indicator enrichment, memory artifact analysis, timeline reconstruction |
| network-forensics | 1 | dns pivot, http evidence extraction, memory artifact analysis, registry artifact correlation, timeline reconstruction |

## Route Types

| Route type | Cases |
| --- | --- |
| memory artifact analysis | 24 |
| http evidence extraction | 21 |
| timeline reconstruction | 16 |
| indicator enrichment | 15 |
| dns pivot | 10 |
| registry artifact correlation | 8 |
| credential discovery | 7 |
| strings-driven evidence lookup | 4 |
| virustotal-driven evidence lookup | 4 |
| event-log correlation | 3 |
| maldoc analysis | 3 |
| john-driven evidence lookup | 2 |
| layer-2 endpoint identification | 2 |
| olevba-driven evidence lookup | 2 |
| tls handshake inspection | 2 |
| volatility-driven evidence lookup | 2 |
| cyberchef-driven evidence lookup | 1 |
| evtxecmd-driven evidence lookup | 1 |
| ftk-imager-driven evidence lookup | 1 |
| memprocfs-driven evidence lookup | 1 |
| radare2-driven evidence lookup | 1 |
| service-to-access path | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [Akira Lab](../../../cards/cyber-defenders-akira-lab.md) | CyberDefedners | Medium | dns-analysis, http-analysis, malware-static, memory-forensics |
| [Amadey Lab](../../../cards/cyber-defenders-amadey-lab.md) | CyberDefenders | Easy | http-analysis, malware-static, memory-forensics, stego-extraction |
| [Andromeda Bot Lab](../../../cards/cyber-defenders-andromeda-bot-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, memory-forensics |
| [BankingTroubles Lab](../../../cards/cyber-defenders-bankingtroubles-lab.md) | CyberDefenders | Hard | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [BlackEnergy Lab](../../../cards/cyber-defenders-black-energy-lab.md) | CyberDefenders | Medium | cti-enrichment, http-analysis, malware-static, memory-forensics |
| [Boogeyman 2](../../../cards/boogeyman2-writeup.md) | TryHackMe | Medium | http-analysis, maldoc-analysis, malware-static, memory-forensics |
| [Brave](../../../cards/cyber-defenders-brave-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, memory-forensics |
| [Chollima Lab](../../../cards/cyber-defenders-weblogic-lab.md) | CyberDefenders | Medium | http-analysis, malware-static, memory-forensics, stego-extraction |
| [Critical](../../../cards/critical.md) | TryHackMe | Easy | dns-analysis, http-analysis, malware-static, memory-forensics |
| [DarkCrystal Lab](../../../cards/cyber-defenders-darkcrystal-lab.md) | CyberDefenders | Medium | http-analysis, malware-static, memory-forensics, stego-extraction |
| [Dead End?](../../../cards/dead-end.md) | TryHackMe | Hard | cti-enrichment, memory-forensics |
| [DeepDive Lab](../../../cards/cyber-defenders-deepdive-lab.md) | CyberDefenders | Hard | cti-enrichment, http-analysis, memory-forensics, password-cracking |
| [DumpMe Lab](../../../cards/cyber-defenders-dumpme-lab.md) | CyberDefenders | Medium | cti-enrichment, malware-dynamic, memory-forensics, registry-forensics |
| [Forensics](../../../cards/forensics.md) | TryHackMe | Hard | browser-forensics, cti-enrichment, malware-static, memory-forensics |
| [IcedID 2 Lab](../../../cards/cyber-defenders-icedid-2-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, memory-forensics |
| [Injector Lab](../../../cards/cyber-defenders-injector-lab.md) | CyberDefenders | Medium | http-analysis, malware-static, memory-forensics, registry-forensics |
| [Lockbit](../../../cards/lockbit.md) | LetsDefend | Easy | cti-enrichment, http-analysis, memory-forensics, privilege-escalation |
| [Memory Analysis](../../../cards/lets-defend-memory-analysis.md) | LetsDefend | Medium | cti-enrichment, dns-analysis, memory-forensics, password-cracking |
| [Memory Analysis - Ransomware](../../../cards/btlo-memory-analysis-ransomware.md) | BTLO | Medium | cti-enrichment, memory-forensics |
| [MrRobot Lab](../../../cards/cyber-defenders-mrrobot-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [NintendoHunt Lab](../../../cards/cyber-defenders-nintendohunt-lab.md) | CyberDefenders | Hard | http-analysis, malware-static, memory-forensics, service-enumeration |
| [PwnedDC Lab](../../../cards/cyber-defenders-pwneddc-lab.md) | CyberDefenders | Hard | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [QBot Lab](../../../cards/cyber-defenders-qbot-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, maldoc-analysis |
| [Ramnit](../../../cards/cyber-defenders-ramnit-lab.md) | CyberDefenders | Easy | browser-forensics, cti-enrichment, dns-analysis, malware-static |
| [Redline](../../../cards/cyber-defenders-redline-lab.md) | CyberDefenders | Easy | cti-enrichment, http-analysis, malware-static, memory-forensics |
| [Reveal](../../../cards/cyber-defenders-reveal-lab.md) | CyberDefenders | Easy | cti-enrichment, http-analysis, memory-forensics, timeline-analysis |
| [REvil Corp](../../../cards/revil-corp.md) | TryHackMe | Medium | browser-forensics, cti-enrichment, http-analysis, memory-forensics |
| [Seized Lab](../../../cards/cyber-defenders-seized-lab.md) | CyberDefenders | Medium | browser-forensics, http-analysis, malware-static, memory-forensics |
| [Szechuan Sauce Lab](../../../cards/cyber-defenders-szechuan-suace-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, memory-forensics |
| [Volatility Traces Lab](../../../cards/cyber-defenders-volatility-traces-lab.md) | CyberDefenders | Easy | dns-analysis, http-analysis, malware-static, memory-forensics |
| [WinRar 0-Day](../../../cards/win-rar-0-day.md) | LetsDefend | Medium | dns-analysis, http-analysis, memory-forensics |
