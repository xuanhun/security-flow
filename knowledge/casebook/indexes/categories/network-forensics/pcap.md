# Network Forensics / pcap

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| network-forensics | 43 | http evidence extraction, dns pivot, conversation statistics, credential discovery, wireshark-driven evidence lookup |
| http-analysis | 42 | http evidence extraction, dns pivot, conversation statistics, credential discovery, wireshark-driven evidence lookup |
| dns-analysis | 30 | dns pivot, http evidence extraction, conversation statistics, credential discovery, indicator enrichment |
| cti-enrichment | 24 | dns pivot, http evidence extraction, conversation statistics, indicator enrichment, virustotal-driven evidence lookup |
| service-enumeration | 14 | dns pivot, http evidence extraction, conversation statistics, credential discovery, service-to-access path |
| timeline-analysis | 8 | http evidence extraction, conversation statistics, credential discovery, dns pivot, event-log correlation |
| malware-static | 7 | dns pivot, conversation statistics, http evidence extraction, credential discovery, wireshark-driven evidence lookup |
| stego-extraction | 7 | conversation statistics, dns pivot, credential discovery, http evidence extraction, file metadata extraction |
| reverse-engineering | 4 | conversation statistics, dns pivot, http evidence extraction, reverse engineering, indicator enrichment |
| web-enumeration | 4 | conversation statistics, http evidence extraction, credential discovery, cyberchef-driven evidence lookup, dns pivot |
| browser-forensics | 3 | dns pivot, http evidence extraction, conversation statistics, cyberchef-driven evidence lookup |
| windows-event-analysis | 2 | conversation statistics, event-log correlation, http evidence extraction, credential discovery, dns pivot |
| maldoc-analysis | 1 | conversation statistics, credential discovery, dns pivot, http evidence extraction, maldoc analysis |
| memory-forensics | 1 | credential discovery, dns pivot, http evidence extraction, layer-2 endpoint identification, volatility-driven evidence lookup |
| password-cracking | 1 | dns pivot |
| privilege-escalation | 1 | conversation statistics, credential discovery, dns pivot, event-log correlation, http evidence extraction |

## Route Types

| Route type | Cases |
| --- | --- |
| http evidence extraction | 33 |
| dns pivot | 29 |
| conversation statistics | 24 |
| credential discovery | 14 |
| wireshark-driven evidence lookup | 9 |
| indicator enrichment | 7 |
| virustotal-driven evidence lookup | 6 |
| layer-2 endpoint identification | 5 |
| service-to-access path | 4 |
| cyberchef-driven evidence lookup | 3 |
| event-log correlation | 2 |
| file metadata extraction | 2 |
| reverse engineering | 2 |
| timeline reconstruction | 2 |
| exiftool-driven evidence lookup | 1 |
| maldoc analysis | 1 |
| memory artifact analysis | 1 |
| registry artifact correlation | 1 |
| tls handshake inspection | 1 |
| tshark-driven evidence lookup | 1 |
| volatility-driven evidence lookup | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [Acoustic Lab](../../../cards/cyber-defenders-acoustic-lab.md) | CyberDefenders | Medium | dns-analysis, http-analysis, malware-static, network-forensics |
| [BlueSky Ransomware Lab](../../../cards/cyber-defenders-bluesky-ransomware-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, network-forensics |
| [Brute Force Attack](../../../cards/lets-defend-brute-force-attack.md) | LetsDefend | Medium | http-analysis, network-forensics, service-enumeration |
| [Carnage](../../../cards/carnage-writeup.md) | TryHackMe | Medium | cti-enrichment, dns-analysis, http-analysis, network-forensics |
| [DanaBot](../../../cards/cyber-defenders-dana-bot.md) | CyberDefenders | Easy | cti-enrichment, http-analysis, network-forensics |
| [HawkEye Lab](../../../cards/cyber-defenders-hawkeye-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, network-forensics |
| [HoneyBOT Lab](../../../cards/cyber-defenders-honeybot-lab.md) | CyberDefenders | Medium | cti-enrichment, http-analysis, network-forensics, service-enumeration |
| [HTTP Basic Auth](../../../cards/lets-defend-http-basic-auth.md) | LetsDefend | Easy | http-analysis, network-forensics |
| [JetBrains Lab](../../../cards/cyber-defenders-jetbrains-lab.md) | CyberDefenders | Easy | dns-analysis, http-analysis, network-forensics, timeline-analysis |
| [l337 S4uc3 Lab](../../../cards/cyber-defenders-l337-s4uc3-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, memory-forensics |
| [Malware Traffic Analysis 1 Lab](../../../cards/cyber-defenders-malware-traffic-analysis-1.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, network-forensics |
| [Malware Traffic Analysis 2 Lab](../../../cards/cyber-defenders-malware-traffic-analysis-2.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, network-forensics |
| [Malware Traffic Analysis 3 Lab](../../../cards/cyber-defenders-malware-traffic-analysis-3.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, network-forensics |
| [Malware Traffic Analysis 4 Lab](../../../cards/cyber-defenders-malware-traffic-analysis-4.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, network-forensics |
| [Malware Traffic Analysis 5 Lab](../../../cards/cyber-defenders-malware-traffic-analysis-5.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, maldoc-analysis |
| [Masterminds](../../../cards/masterminds.md) | TryHackMe | Medium | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Network Analysis - Ransomware](../../../cards/btlo-network-analysis-ransomware.md) | BTLO | Medium | cti-enrichment, dns-analysis, http-analysis, network-forensics |
| [Network Analysis - Web Shell](../../../cards/btlo-network-analysis-web-shell.md) | BTLO | Easy | http-analysis, malware-static, network-forensics, stego-extraction |
| [NukeTheBrowser Lab](../../../cards/cyber-defenders-nuke-the-browser-lab.md) | CyberDefenders | Hard | cti-enrichment, dns-analysis, http-analysis, network-forensics |
| [Openfire Lab](../../../cards/cyber-defenders-openfire-lab.md) | CyberDefenders | Easy | dns-analysis, http-analysis, network-forensics, service-enumeration |
| [OpenWire Lab](../../../cards/cyber-defenders-openwire-lab.md) | CyberDefenders | Medium | http-analysis, network-forensics, reverse-engineering |
| [PacketDetective](../../../cards/cyber-defenders-pakcet-defective-lab.md) | CyberDefenders | Easy | http-analysis, network-forensics, service-enumeration, timeline-analysis |
| [PacketMaze Lab](../../../cards/cyber-defenders-packetmaze-lab.md) | CyberDefenders | Medium | dns-analysis, http-analysis, network-forensics, service-enumeration |
| [Piggy](../../../cards/btlo-piggy.md) | BTLO | Easy | cti-enrichment, dns-analysis, http-analysis, network-forensics |
| [PoisonedCredentials](../../../cards/cyber-defenders-poisoned-credentials-lab.md) | CyberDefenders | Easy | dns-analysis, http-analysis, network-forensics, service-enumeration |
| [PsExec Hunt](../../../cards/cyber-defenders-psexec-hunt-lab.md) | CyberDefenders | Easy | dns-analysis, http-analysis, network-forensics, service-enumeration |
| [RCEMiner Lab](../../../cards/cyber-defenders-rceminer-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, malware-static |
| [RetailBreach Lab](../../../cards/cyber-defenders-retailbreach-lab.md) | CyberDefenders | Easy | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Shellshock Attack](../../../cards/lets-defend-shellshock.md) | LetsDefend | Easy | http-analysis, network-forensics |
| [Shiba Insider](../../../cards/btlo-shiba-insider.md) | BTLO | Easy | http-analysis, network-forensics, stego-extraction |
| [TomCat Takeover](../../../cards/cyber-defenders-tomcat-takeover-lab.md) | CyberDefenders | Easy | http-analysis, network-forensics, web-enumeration |
| [Trident Lab](../../../cards/cyber-defenders-trident-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, malware-static |
| [TShark](../../../cards/tshark.md) | TryHackMe | Medium | dns-analysis, malware-static, network-forensics |
| [TShark Challenge 1: Teamwork](../../../cards/tshark-challenge-1-teamwork.md) | TryHackMe | Easy | cti-enrichment, dns-analysis, http-analysis, network-forensics |
| [Tshark Challenge II: Directory](../../../cards/tshark-challenge-2-directory.md) | TryHackMe | Easy | cti-enrichment, dns-analysis, http-analysis, network-forensics |
| [Warzone 1](../../../cards/warzone1.md) | TryHackMe | Medium | cti-enrichment, dns-analysis, http-analysis, network-forensics |
| [Warzone 2](../../../cards/warzone-2-challenge.md) | TryHackMe | Medium | cti-enrichment, dns-analysis, http-analysis, network-forensics |
| [Web Investigation](../../../cards/cyber-defenders-web-investigation-lab.md) | CyberDefenders | Easy | http-analysis, network-forensics, timeline-analysis, web-enumeration |
| [WebStrike](../../../cards/cyber-defenders-webstrike-lab.md) | CyberDefenders | Easy | browser-forensics, http-analysis, network-forensics |
| [WireDive Lab](../../../cards/cyber-defenders-wiredive-lab.md) | CyberDefenders | Medium | dns-analysis, http-analysis, network-forensics, service-enumeration |
| [XMLRat Lab](../../../cards/cyber-defenders-xlmrat-lab.md) | CyberDefenders | Easy | cti-enrichment, dns-analysis, http-analysis, malware-static |
| [XXE Infiltration Lab](../../../cards/cyber-defenders-xxe-infiltration-lab.md) | CyberDefenders | Easy | http-analysis, network-forensics, timeline-analysis |
| [Zeek Exercises](../../../cards/zeek-exercises.md) | TryHackMe | Medium | cti-enrichment, dns-analysis, http-analysis, network-forensics |
