# SIEM (ELK, Splunk, etc.) / windows-events

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| dns-analysis | 12 | dns pivot, http evidence extraction, credential discovery, elk-driven evidence lookup, event-log correlation |
| windows-event-analysis | 12 | dns pivot, http evidence extraction, credential discovery, elk-driven evidence lookup, event-log correlation |
| siem-query | 11 | dns pivot, elk-driven evidence lookup, event-log correlation, http evidence extraction, credential discovery |
| http-analysis | 10 | dns pivot, http evidence extraction, credential discovery, elk-driven evidence lookup, event-log correlation |
| cti-enrichment | 5 | dns pivot, elk-driven evidence lookup, event-log correlation, credential discovery, http evidence extraction |
| password-cracking | 4 | dns pivot, http evidence extraction, credential discovery, memory artifact analysis, timeline reconstruction |
| malware-static | 2 | credential discovery, dns pivot, event-log correlation, elk-driven evidence lookup, http evidence extraction |
| service-enumeration | 2 | dns pivot, memory artifact analysis, credential discovery, cyberchef-driven evidence lookup, http evidence extraction |
| timeline-analysis | 2 | credential discovery, dns pivot, event-log correlation, http evidence extraction, timeline reconstruction |
| browser-forensics | 1 | credential discovery, dns pivot, event-log correlation, http evidence extraction |
| malware-dynamic | 1 | credential discovery, dns pivot, elk-driven evidence lookup, event-log correlation |

## Route Types

| Route type | Cases |
| --- | --- |
| dns pivot | 12 |
| http evidence extraction | 7 |
| credential discovery | 6 |
| elk-driven evidence lookup | 6 |
| event-log correlation | 6 |
| memory artifact analysis | 3 |
| timeline reconstruction | 3 |
| cyberchef-driven evidence lookup | 1 |
| registry artifact correlation | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [Conti](../../../cards/conti.md) | TryHackMe | Medium | dns-analysis, http-analysis, malware-dynamic, malware-static |
| [GitTheGate Lab](../../../cards/cyber-defenders-gitthegate-lab.md) | CyberDefenders | Medium | dns-analysis, password-cracking, service-enumeration, siem-query |
| [HafinumAPT Lab](../../../cards/cyber-defenders-hafinumapt-lab.md) | CyberDefenders | Hard | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Investigating with Splunk](../../../cards/investigating-with-splunk.md) | TryHackMe | Medium | dns-analysis, http-analysis, password-cracking, siem-query |
| [Kerberoasted Lab](../../../cards/cyber-defenders-kerberoasted-lab.md) | CyberDefenders | Medium | dns-analysis, http-analysis, password-cracking, siem-query |
| [Monday Monitor](../../../cards/monday-monitor.md) | TryHackMe | Easy | dns-analysis, http-analysis, password-cracking, service-enumeration |
| [New Hire Old Artifacts](../../../cards/new-hire-old-artifacts.md) | TryHackMe | Medium | dns-analysis, http-analysis, malware-static, siem-query |
| [PS Eclipse](../../../cards/pseclipse.md) | TryHackMe | Medium | cti-enrichment, dns-analysis, http-analysis, siem-query |
| [REvil Lab](../../../cards/cyber-defenders-revil-lab.md) | CyberDefenders | Easy | cti-enrichment, dns-analysis, http-analysis, siem-query |
| [SOC Alpha 1](../../../cards/btlo-soc-alpha-1.md) | BTLO | Easy | dns-analysis, http-analysis, siem-query, windows-event-analysis |
| [SOC Alpha 2](../../../cards/btlo-soc-alpha-2.md) | BTLO | Easy | cti-enrichment, dns-analysis, siem-query, windows-event-analysis |
| [SOC Alpha 3](../../../cards/btlo-soc-alpha-3.md) | BTLO | Medium | cti-enrichment, dns-analysis, http-analysis, siem-query |
