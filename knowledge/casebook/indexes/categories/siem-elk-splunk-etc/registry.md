# SIEM (ELK, Splunk, etc.) / registry

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| dns-analysis | 7 | dns pivot, http evidence extraction, credential discovery, elk-driven evidence lookup, memory artifact analysis |
| http-analysis | 7 | dns pivot, http evidence extraction, credential discovery, elk-driven evidence lookup, memory artifact analysis |
| siem-query | 6 | dns pivot, http evidence extraction, elk-driven evidence lookup, credential discovery, event-log correlation |
| windows-event-analysis | 6 | dns pivot, http evidence extraction, credential discovery, elk-driven evidence lookup, event-log correlation |
| password-cracking | 3 | dns pivot, http evidence extraction, credential discovery, timeline reconstruction, cyberchef-driven evidence lookup |
| service-enumeration | 2 | dns pivot, http evidence extraction, memory artifact analysis, credential discovery, cyberchef-driven evidence lookup |
| cti-enrichment | 1 | dns pivot, elk-driven evidence lookup, http evidence extraction, memory artifact analysis, registry artifact correlation |
| malware-static | 1 | credential discovery, dns pivot, event-log correlation, http evidence extraction |
| privilege-escalation | 1 | dns pivot, elk-driven evidence lookup, http evidence extraction, memory artifact analysis |
| timeline-analysis | 1 | credential discovery, dns pivot, event-log correlation, http evidence extraction, timeline reconstruction |

## Route Types

| Route type | Cases |
| --- | --- |
| dns pivot | 7 |
| http evidence extraction | 7 |
| credential discovery | 3 |
| elk-driven evidence lookup | 3 |
| memory artifact analysis | 3 |
| event-log correlation | 2 |
| timeline reconstruction | 2 |
| cyberchef-driven evidence lookup | 1 |
| registry artifact correlation | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [ElasticCase Lab](../../../cards/cyber-defenders-elasticcase-lab.md) | CyberDefenders | Medium | dns-analysis, http-analysis, privilege-escalation, service-enumeration |
| [Investigating with Splunk](../../../cards/investigating-with-splunk.md) | TryHackMe | Medium | dns-analysis, http-analysis, password-cracking, siem-query |
| [Kerberoasted Lab](../../../cards/cyber-defenders-kerberoasted-lab.md) | CyberDefenders | Medium | dns-analysis, http-analysis, password-cracking, siem-query |
| [Monday Monitor](../../../cards/monday-monitor.md) | TryHackMe | Easy | dns-analysis, http-analysis, password-cracking, service-enumeration |
| [New Hire Old Artifacts](../../../cards/new-hire-old-artifacts.md) | TryHackMe | Medium | dns-analysis, http-analysis, malware-static, siem-query |
| [SOC Alpha 1](../../../cards/btlo-soc-alpha-1.md) | BTLO | Easy | dns-analysis, http-analysis, siem-query, windows-event-analysis |
| [SOC Alpha 3](../../../cards/btlo-soc-alpha-3.md) | BTLO | Medium | cti-enrichment, dns-analysis, http-analysis, siem-query |
