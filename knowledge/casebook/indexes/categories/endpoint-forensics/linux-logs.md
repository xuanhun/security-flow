# Endpoint Forensics / linux-logs

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| http-analysis | 7 | credential discovery, http evidence extraction, timeline reconstruction, evidence lookup, memory artifact analysis |
| service-enumeration | 6 | credential discovery, http evidence extraction, timeline reconstruction, evidence lookup, memory artifact analysis |
| browser-forensics | 4 | http evidence extraction, credential discovery, timeline reconstruction, evidence lookup, ftk-imager-driven evidence lookup |
| stego-extraction | 4 | credential discovery, http evidence extraction, timeline reconstruction, exiftool-driven evidence lookup, ftk-imager-driven evidence lookup |
| malware-static | 3 | credential discovery, http evidence extraction, exiftool-driven evidence lookup, indicator enrichment, john-driven evidence lookup |
| privilege-escalation | 2 | credential discovery, http evidence extraction, indicator enrichment, john-driven evidence lookup, timeline reconstruction |
| cti-enrichment | 1 | credential discovery, http evidence extraction, indicator enrichment, timeline reconstruction |
| dns-analysis | 1 | credential discovery, exiftool-driven evidence lookup, http evidence extraction, memory artifact analysis |
| password-cracking | 1 | credential discovery, http evidence extraction, john-driven evidence lookup |

## Route Types

| Route type | Cases |
| --- | --- |
| http evidence extraction | 6 |
| timeline reconstruction | 6 |
| credential discovery | 5 |
| evidence lookup | 4 |
| memory artifact analysis | 2 |
| exiftool-driven evidence lookup | 1 |
| ftk-imager-driven evidence lookup | 1 |
| indicator enrichment | 1 |
| john-driven evidence lookup | 1 |
| tls handshake inspection | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [Brutus](../../../cards/brutus.md) | HackTheBox | Easy | http-analysis, service-enumeration |
| [Disgruntled](../../../cards/disgruntled.md) | TryHackMe | Easy | browser-forensics |
| [Hammered Lab](../../../cards/cyber-defenders-hammered-lab.md) | CyberDefenders | Medium | dns-analysis, http-analysis, malware-static, service-enumeration |
| [Insider Lab](../../../cards/cyber-defenders-insider-lab.md) | CyberDefenders | Easy | browser-forensics, http-analysis, stego-extraction |
| [IronShade](../../../cards/ironshade.md) | TryHackMe | Medium | http-analysis, service-enumeration |
| [Stealthy Ascent Lab](../../../cards/cyber-defenders-stealthy-ascent-lab.md) | CyberDefenders | Medium | browser-forensics, http-analysis, malware-static, password-cracking |
| [Tardigrade](../../../cards/tardigrade.md) | TryHackMe | Medium | http-analysis, service-enumeration |
| [XMRig Lab](../../../cards/cyber-defenders-xmrig-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, malware-static |
