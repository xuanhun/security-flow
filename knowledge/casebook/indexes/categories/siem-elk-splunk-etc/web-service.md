# SIEM (ELK, Splunk, etc.) / web-service

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| dns-analysis | 2 | dns pivot, http evidence extraction, timeline reconstruction, elk-driven evidence lookup, service-to-access path |
| http-analysis | 2 | dns pivot, http evidence extraction, timeline reconstruction, elk-driven evidence lookup, service-to-access path |
| siem-query | 2 | dns pivot, http evidence extraction, timeline reconstruction, elk-driven evidence lookup, service-to-access path |
| web-enumeration | 2 | dns pivot, http evidence extraction, timeline reconstruction, elk-driven evidence lookup, service-to-access path |
| malware-static | 1 | dns pivot, http evidence extraction, service-to-access path, timeline reconstruction |
| password-cracking | 1 | dns pivot, http evidence extraction, service-to-access path, timeline reconstruction |
| service-enumeration | 1 | dns pivot, http evidence extraction, service-to-access path, timeline reconstruction |
| stego-extraction | 1 | dns pivot, http evidence extraction, service-to-access path, timeline reconstruction |
| timeline-analysis | 1 | dns pivot, http evidence extraction, service-to-access path, timeline reconstruction |

## Route Types

| Route type | Cases |
| --- | --- |
| dns pivot | 2 |
| http evidence extraction | 2 |
| timeline reconstruction | 2 |
| elk-driven evidence lookup | 1 |
| service-to-access path | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [Defaced](../../../cards/btlo-defaced.md) | BTLO | Easy | dns-analysis, http-analysis, siem-query, web-enumeration |
| [SlingShot](../../../cards/slingshot.md) | TryHackMe | Easy | dns-analysis, http-analysis, malware-static, password-cracking |
