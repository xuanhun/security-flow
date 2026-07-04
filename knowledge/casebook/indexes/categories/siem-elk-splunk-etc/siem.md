# SIEM (ELK, Splunk, etc.) / siem

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| siem-query | 21 | dns pivot, http evidence extraction, elk-driven evidence lookup, credential discovery, event-log correlation |
| dns-analysis | 20 | dns pivot, http evidence extraction, elk-driven evidence lookup, credential discovery, event-log correlation |
| http-analysis | 20 | dns pivot, http evidence extraction, elk-driven evidence lookup, credential discovery, event-log correlation |
| windows-event-analysis | 15 | dns pivot, http evidence extraction, credential discovery, elk-driven evidence lookup, event-log correlation |
| password-cracking | 7 | dns pivot, http evidence extraction, timeline reconstruction, credential discovery, memory artifact analysis |
| service-enumeration | 7 | dns pivot, http evidence extraction, credential discovery, elk-driven evidence lookup, memory artifact analysis |
| cti-enrichment | 6 | dns pivot, elk-driven evidence lookup, event-log correlation, credential discovery, http evidence extraction |
| malware-static | 4 | dns pivot, credential discovery, event-log correlation, http evidence extraction, elk-driven evidence lookup |
| timeline-analysis | 4 | http evidence extraction, dns pivot, timeline reconstruction, credential discovery, event-log correlation |
| browser-forensics | 2 | http evidence extraction, credential discovery, dns pivot, event-log correlation, timeline reconstruction |
| privilege-escalation | 2 | dns pivot, elk-driven evidence lookup, http evidence extraction, credential discovery, memory artifact analysis |
| stego-extraction | 2 | dns pivot, http evidence extraction, indicator enrichment, service-to-access path, splunk-driven evidence lookup |
| web-enumeration | 2 | dns pivot, http evidence extraction, timeline reconstruction, elk-driven evidence lookup, service-to-access path |
| malware-dynamic | 1 | credential discovery, dns pivot, elk-driven evidence lookup, event-log correlation |
| network-forensics | 1 | dns pivot, indicator enrichment, splunk-driven evidence lookup |

## Route Types

| Route type | Cases |
| --- | --- |
| dns pivot | 19 |
| http evidence extraction | 16 |
| elk-driven evidence lookup | 12 |
| credential discovery | 10 |
| event-log correlation | 8 |
| timeline reconstruction | 8 |
| memory artifact analysis | 5 |
| cyberchef-driven evidence lookup | 1 |
| indicator enrichment | 1 |
| registry artifact correlation | 1 |
| service-to-access path | 1 |
| splunk-driven evidence lookup | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [Benign](../../../cards/benign.md) | TryHackMe | Medium | dns-analysis, http-analysis, siem-query, windows-event-analysis |
| [Boogeyman 3](../../../cards/boogeyman3-writeup.md) | TryHackMe | Medium | dns-analysis, http-analysis, siem-query, windows-event-analysis |
| [Conti](../../../cards/conti.md) | TryHackMe | Medium | dns-analysis, http-analysis, malware-dynamic, malware-static |
| [Defaced](../../../cards/btlo-defaced.md) | BTLO | Easy | dns-analysis, http-analysis, siem-query, web-enumeration |
| [ElasticCase Lab](../../../cards/cyber-defenders-elasticcase-lab.md) | CyberDefenders | Medium | dns-analysis, http-analysis, privilege-escalation, service-enumeration |
| [GitTheGate Lab](../../../cards/cyber-defenders-gitthegate-lab.md) | CyberDefenders | Medium | dns-analysis, password-cracking, service-enumeration, siem-query |
| [HafinumAPT Lab](../../../cards/cyber-defenders-hafinumapt-lab.md) | CyberDefenders | Hard | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Investigating with Splunk](../../../cards/investigating-with-splunk.md) | TryHackMe | Medium | dns-analysis, http-analysis, password-cracking, siem-query |
| [ItsyBitsy](../../../cards/itsybitsy.md) | TryHackMe | Medium | browser-forensics, http-analysis, password-cracking, siem-query |
| [Kerberoasted Lab](../../../cards/cyber-defenders-kerberoasted-lab.md) | CyberDefenders | Medium | dns-analysis, http-analysis, password-cracking, siem-query |
| [Middle Mayhem](../../../cards/btlo-middle-mayhem.md) | BTLO | Easy | http-analysis, service-enumeration, siem-query |
| [Monday Monitor](../../../cards/monday-monitor.md) | TryHackMe | Easy | dns-analysis, http-analysis, password-cracking, service-enumeration |
| [NerisBot Lab](../../../cards/cyber-defenders-nerisbot-lab.md) | CyberDefenders | Easy | cti-enrichment, dns-analysis, http-analysis, malware-static |
| [New Hire Old Artifacts](../../../cards/new-hire-old-artifacts.md) | TryHackMe | Medium | dns-analysis, http-analysis, malware-static, siem-query |
| [Peak](../../../cards/btlo-peak.md) | BTLO | Medium | dns-analysis, http-analysis, password-cracking, privilege-escalation |
| [PS Eclipse](../../../cards/pseclipse.md) | TryHackMe | Medium | cti-enrichment, dns-analysis, http-analysis, siem-query |
| [REvil Lab](../../../cards/cyber-defenders-revil-lab.md) | CyberDefenders | Easy | cti-enrichment, dns-analysis, http-analysis, siem-query |
| [SlingShot](../../../cards/slingshot.md) | TryHackMe | Easy | dns-analysis, http-analysis, malware-static, password-cracking |
| [SOC Alpha 1](../../../cards/btlo-soc-alpha-1.md) | BTLO | Easy | dns-analysis, http-analysis, siem-query, windows-event-analysis |
| [SOC Alpha 2](../../../cards/btlo-soc-alpha-2.md) | BTLO | Easy | cti-enrichment, dns-analysis, siem-query, windows-event-analysis |
| [SOC Alpha 3](../../../cards/btlo-soc-alpha-3.md) | BTLO | Medium | cti-enrichment, dns-analysis, http-analysis, siem-query |
| [T1110-003 Lab](../../../cards/cyber-defenders-t1110-003-lab.md) | CyberDefenders | Easy | dns-analysis, http-analysis, service-enumeration, siem-query |
