# Cyber Threat Intelligence (CTI) / email

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| cti-enrichment | 4 | dns pivot, http evidence extraction, credential discovery, evidence lookup, indicator enrichment |
| http-analysis | 4 | dns pivot, credential discovery, http evidence extraction, evidence lookup, indicator enrichment |
| dns-analysis | 3 | dns pivot, http evidence extraction, credential discovery, indicator enrichment, memory artifact analysis |
| email-header-analysis | 1 | dns pivot, http evidence extraction, timeline reconstruction |
| malware-dynamic | 1 | credential discovery, dns pivot, memory artifact analysis, virustotal-driven evidence lookup |

## Route Types

| Route type | Cases |
| --- | --- |
| dns pivot | 3 |
| credential discovery | 2 |
| evidence lookup | 2 |
| http evidence extraction | 2 |
| indicator enrichment | 1 |
| memory artifact analysis | 1 |
| timeline reconstruction | 1 |
| virustotal-driven evidence lookup | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [GrabThePhiser](../../../cards/cyber-defenders-grab-the-phisher-lab.md) | CyberDefenders | Easy | http-analysis |
| [IcedID](../../../cards/cyber-defenders-icedid-lab.md) | CyberDefenders | Easy | cti-enrichment, dns-analysis, http-analysis |
| [Oski Lab](../../../cards/cyber-defenders-oski-lab.md) | CyberDefenders | Easy | cti-enrichment, dns-analysis, http-analysis, malware-dynamic |
| [PhishStrike Lab](../../../cards/cyber-defenders-phishstrike.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, email-header-analysis, http-analysis |
| [Trooper](../../../cards/trooper-writuep.md) | TryHackMe | Easy | cti-enrichment |
