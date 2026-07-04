# SIEM (ELK, Splunk, etc.) / ids

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| http-analysis | 9 | dns pivot, http evidence extraction, elk-driven evidence lookup, credential discovery, event-log correlation |
| siem-query | 9 | dns pivot, http evidence extraction, elk-driven evidence lookup, credential discovery, event-log correlation |
| dns-analysis | 8 | dns pivot, elk-driven evidence lookup, http evidence extraction, credential discovery, event-log correlation |
| windows-event-analysis | 6 | dns pivot, elk-driven evidence lookup, http evidence extraction, credential discovery, event-log correlation |
| cti-enrichment | 3 | dns pivot, elk-driven evidence lookup, http evidence extraction, indicator enrichment, memory artifact analysis |
| malware-static | 3 | dns pivot, credential discovery, event-log correlation, elk-driven evidence lookup, http evidence extraction |
| password-cracking | 2 | http evidence extraction, dns pivot, timeline reconstruction |
| browser-forensics | 1 | http evidence extraction, timeline reconstruction |
| malware-dynamic | 1 | credential discovery, dns pivot, elk-driven evidence lookup, event-log correlation |
| network-forensics | 1 | dns pivot, indicator enrichment, splunk-driven evidence lookup |
| privilege-escalation | 1 | dns pivot, elk-driven evidence lookup, http evidence extraction, memory artifact analysis |
| service-enumeration | 1 | dns pivot, elk-driven evidence lookup, http evidence extraction, memory artifact analysis |
| stego-extraction | 1 | dns pivot, indicator enrichment, splunk-driven evidence lookup |
| timeline-analysis | 1 | http evidence extraction, timeline reconstruction |

## Route Types

| Route type | Cases |
| --- | --- |
| dns pivot | 8 |
| http evidence extraction | 6 |
| elk-driven evidence lookup | 5 |
| credential discovery | 2 |
| event-log correlation | 2 |
| memory artifact analysis | 2 |
| timeline reconstruction | 2 |
| indicator enrichment | 1 |
| registry artifact correlation | 1 |
| splunk-driven evidence lookup | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [Benign](../../../cards/benign.md) | TryHackMe | Medium | dns-analysis, http-analysis, siem-query, windows-event-analysis |
| [Conti](../../../cards/conti.md) | TryHackMe | Medium | dns-analysis, http-analysis, malware-dynamic, malware-static |
| [ElasticCase Lab](../../../cards/cyber-defenders-elasticcase-lab.md) | CyberDefenders | Medium | dns-analysis, http-analysis, privilege-escalation, service-enumeration |
| [Investigating with Splunk](../../../cards/investigating-with-splunk.md) | TryHackMe | Medium | dns-analysis, http-analysis, password-cracking, siem-query |
| [ItsyBitsy](../../../cards/itsybitsy.md) | TryHackMe | Medium | browser-forensics, http-analysis, password-cracking, siem-query |
| [NerisBot Lab](../../../cards/cyber-defenders-nerisbot-lab.md) | CyberDefenders | Easy | cti-enrichment, dns-analysis, http-analysis, malware-static |
| [New Hire Old Artifacts](../../../cards/new-hire-old-artifacts.md) | TryHackMe | Medium | dns-analysis, http-analysis, malware-static, siem-query |
| [PS Eclipse](../../../cards/pseclipse.md) | TryHackMe | Medium | cti-enrichment, dns-analysis, http-analysis, siem-query |
| [SOC Alpha 3](../../../cards/btlo-soc-alpha-3.md) | BTLO | Medium | cti-enrichment, dns-analysis, http-analysis, siem-query |
