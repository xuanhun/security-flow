# Endpoint Forensics / email

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| http-analysis | 22 | http evidence extraction, timeline reconstruction, dns pivot, credential discovery, db-browser-sqlite-driven evidence lookup |
| browser-forensics | 20 | http evidence extraction, timeline reconstruction, credential discovery, dns pivot, db-browser-sqlite-driven evidence lookup |
| timeline-analysis | 17 | http evidence extraction, timeline reconstruction, dns pivot, credential discovery, registry artifact correlation |
| dns-analysis | 14 | dns pivot, http evidence extraction, timeline reconstruction, credential discovery, event-log correlation |
| cti-enrichment | 12 | http evidence extraction, dns pivot, timeline reconstruction, event-log correlation, indicator enrichment |
| windows-event-analysis | 12 | http evidence extraction, dns pivot, timeline reconstruction, event-log correlation, db-browser-sqlite-driven evidence lookup |
| malware-static | 10 | http evidence extraction, credential discovery, indicator enrichment, memory artifact analysis, timeline reconstruction |
| stego-extraction | 9 | http evidence extraction, credential discovery, indicator enrichment, dns pivot, maldoc analysis |
| privilege-escalation | 7 | http evidence extraction, timeline reconstruction, credential discovery, event-log correlation, cyberchef-driven evidence lookup |
| registry-forensics | 7 | http evidence extraction, timeline reconstruction, registry artifact correlation, credential discovery, db-browser-sqlite-driven evidence lookup |
| maldoc-analysis | 5 | maldoc analysis, memory artifact analysis, dns pivot, http evidence extraction, olevba-driven evidence lookup |
| malware-dynamic | 5 | dns pivot, http evidence extraction, timeline reconstruction, credential discovery, event-log correlation |
| memory-forensics | 5 | indicator enrichment, maldoc analysis, memory artifact analysis, credential discovery, dns pivot |
| service-enumeration | 5 | credential discovery, http evidence extraction, timeline reconstruction, db-browser-sqlite-driven evidence lookup, dns pivot |
| password-cracking | 4 | http evidence extraction, credential discovery, indicator enrichment, timeline reconstruction, autopsy-driven evidence lookup |
| email-header-analysis | 2 | cyberchef-driven evidence lookup, dns pivot, event-log correlation, indicator enrichment, maldoc analysis |
| mobile-forensics | 1 | autopsy-driven evidence lookup, http evidence extraction, timeline reconstruction |
| network-forensics | 1 | cyberchef-driven evidence lookup, dns pivot, event-log correlation, indicator enrichment |
| reverse-engineering | 1 | dns pivot, reverse engineering |

## Route Types

| Route type | Cases |
| --- | --- |
| http evidence extraction | 17 |
| timeline reconstruction | 14 |
| credential discovery | 9 |
| dns pivot | 9 |
| db-browser-sqlite-driven evidence lookup | 6 |
| event-log correlation | 6 |
| indicator enrichment | 6 |
| memory artifact analysis | 6 |
| registry artifact correlation | 6 |
| maldoc analysis | 5 |
| file metadata extraction | 3 |
| ftk-imager-driven evidence lookup | 3 |
| autopsy-driven evidence lookup | 2 |
| cyberchef-driven evidence lookup | 2 |
| olevba-driven evidence lookup | 2 |
| evidence lookup | 1 |
| john-driven evidence lookup | 1 |
| oledump-driven evidence lookup | 1 |
| reverse engineering | 1 |
| service-to-access path | 1 |
| strings-driven evidence lookup | 1 |
| tls handshake inspection | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [AfricanFalls Lab](../../../cards/cyber-defenders-africanfalls-lab.md) | CyberDefenders | Medium | browser-forensics, password-cracking, service-enumeration, timeline-analysis |
| [BankingTroubles Lab](../../../cards/cyber-defenders-bankingtroubles-lab.md) | CyberDefenders | Hard | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Beta Gamer Lab](../../../cards/cyber-defenders-beta-gamer-lab.md) | CyberDefenders | Medium | browser-forensics, http-analysis, privilege-escalation, timeline-analysis |
| [Boogeyman 2](../../../cards/boogeyman2-writeup.md) | TryHackMe | Medium | http-analysis, maldoc-analysis, malware-static, memory-forensics |
| [CorporateSecrets Lab](../../../cards/cyber-defenders-corporatesecrets-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, registry-forensics |
| [Disgruntled](../../../cards/disgruntled.md) | TryHackMe | Easy | browser-forensics |
| [Fog Ransomware Lab](../../../cards/cyber-defenders-fog-ransomware-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, privilege-escalation |
| [HireMe Lab](../../../cards/cyber-defenders-hireme-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, registry-forensics |
| [Hunter Lab](../../../cards/cyber-defenders-hunter-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, registry-forensics |
| [KioskExpo7 Lab](../../../cards/cyber-defenders-kioskexpo7-lab.md) | CyberDefenders | Medium | browser-forensics, http-analysis, malware-dynamic, malware-static |
| [LummaStealer Lab](../../../cards/cyber-defenders-lummastealer-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [MeteorHit Lab](../../../cards/cyber-defenders-meteorhit-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, malware-dynamic |
| [MrRobot Lab](../../../cards/cyber-defenders-mrrobot-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [PwnedDC Lab](../../../cards/cyber-defenders-pwneddc-lab.md) | CyberDefenders | Hard | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [QBot Lab](../../../cards/cyber-defenders-qbot-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, maldoc-analysis |
| [RepoReaper Lab](../../../cards/cyber-defenders-reporeaper-lab.md) | CyberDefenders | Hard | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [RevengeHotels APT Lab](../../../cards/cyber-defenders-revengehotels-apt-lab.md) | CyberDefenders | Easy | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Silent Breach](../../../cards/cyber-defenders-silent-breach-lab.md) | CyberDefenders | Medium | browser-forensics, http-analysis, malware-static, stego-extraction |
| [Stealthy Ascent Lab](../../../cards/cyber-defenders-stealthy-ascent-lab.md) | CyberDefenders | Medium | browser-forensics, http-analysis, malware-static, password-cracking |
| [T1598.002 Lab](../../../cards/cyber-defenders-t1598-002-lab.md) | CyberDefenders | Easy | cti-enrichment, dns-analysis, email-header-analysis, http-analysis |
| [Tempest](../../../cards/temptest-writeup.md) | TryHackMe | Medium | cti-enrichment, dns-analysis, email-header-analysis, http-analysis |
| [TheTruth Lab](../../../cards/cyber-defenders-thetruth-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, malware-static |
| [VaultBreak Lab](../../../cards/cyber-defenders-vaultbreak-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, maldoc-analysis |
| [Zerologon Lab](../../../cards/cyber-defenders-zerologon-lab.md) | CyberDefenders | Hard | browser-forensics, dns-analysis, http-analysis, malware-dynamic |
