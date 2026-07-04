#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote, unquote


SKILL_ROOT = Path(__file__).resolve().parents[1]
RUNTIME_ROOT = Path(os.environ.get("KALI_SKILL_RUNTIME", Path.home() / ".cache" / "kali-skill"))
PDF_RUNTIME = RUNTIME_ROOT / "pdf"
DEFAULT_CASEBOOK_ROOT = SKILL_ROOT / "assets" / "casebook"

MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
MARKDOWN_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
TAG_RE = re.compile(r"`([^`]+)`")
IPV4_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
HASH_RE = re.compile(r"\b[a-fA-F0-9]{32,64}\b")
CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b", re.IGNORECASE)
EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
URL_RE = re.compile(r"https?://[^\s)>\]]+")
DOMAIN_RE = re.compile(r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b")

MARKDOWN_REPO_CATEGORY_MAP = {
    "web": "Web",
    "crypto": "Crypto",
    "pwn": "Pwn",
    "reverse": "Reverse",
    "misc": "Misc",
    "ai": "AI and Digital Watermark",
    "overthewire": "Pentesting",
    "应急响应": "Incident Response",
}

DEFAULT_CATEGORY_ARTIFACTS = {
    "Web": ["web-app"],
    "Crypto": ["ciphertext"],
    "Pwn": ["binary"],
    "Reverse": ["binary"],
    "Misc": ["stego-media"],
    "Incident Response": ["linux-logs"],
    "AI and Digital Watermark": ["stego-media"],
    "Pentesting": ["web-service"],
    "Training and Meta": ["notes"],
}

DEFAULT_CATEGORY_TECHNIQUES = {
    "Web": ["web-exploitation"],
    "Crypto": ["crypto-analysis"],
    "Pwn": ["binary-exploitation"],
    "Reverse": ["reverse-engineering"],
    "Misc": ["misc-analysis"],
    "Incident Response": ["timeline-analysis"],
    "AI and Digital Watermark": ["image-analysis"],
    "Pentesting": ["service-enumeration"],
    "Training and Meta": ["study-guide"],
}


ARTIFACT_TERMS = {
    "pcap": ["pcap", "pcapng", "packet capture", "wireshark", "tshark", "zeek"],
    "windows-events": ["evtx", "event log", "windows event", "sysmon"],
    "linux-logs": ["/var/log", "auth.log", "syslog", "linux forensics"],
    "memory": ["memory dump", "volatility", "memprocfs", "dump.raw", "vmem"],
    "disk-image": ["disk image", "ftk imager", "autopsy", "mft", "$mft"],
    "registry": ["registry", "ntuser.dat", "sam hive", "system hive", "registry explorer"],
    "email": ["email", ".eml", "phishing", "message header", "spf", "dkim"],
    "office-document": ["maldoc", "macro", "olevba", "oledump", "docm", "xlsm"],
    "pe-malware": ["pe file", "pestudio", "detect it easy", "capa", "floss", "dnspy"],
    "apk-mobile": ["apk", "android", "jadx", "mobile forensics"],
    "web-service": ["nmap", "gobuster", "dirb", "wpscan", "nikto", "burp"],
    "web-app": [
        "web",
        "http",
        "php",
        "flask",
        "jsp",
        "upload",
        "ssti",
        "sql注入",
        "sql injection",
        "反序列化",
        "deserialize",
        "include",
        "文件包含",
    ],
    "binary": ["elf", "pwn", "checksec", "ida", "ghidra", "程序是64位", "栈溢出", "逆向", "reverse"],
    "ciphertext": ["cipher", "crypto", "密文", "解密", "caesar", "rc4", "rsa", "aes", "base64"],
    "stego-media": ["二维码", "隐写", "音频", "视频", "watermark", "水印"],
    "siem": ["splunk", "elk", "elastic", "kibana", "wazuh"],
    "ids": ["snort", "suricata", "ids", "ips"],
}

TECHNIQUE_TERMS = {
    "network-forensics": ["wireshark", "tshark", "pcap", "zeek", "suricata", "networkminer"],
    "http-analysis": ["http", "user-agent", "uri", "host header", "web shell"],
    "dns-analysis": ["dns", "domain", "query", "txt record"],
    "siem-query": ["splunk", "elk", "elastic", "index=", "sourcetype=", "kql"],
    "windows-event-analysis": ["event log", "evtx", "sysmon", "event id"],
    "timeline-analysis": ["timeline", "mft", "mftecmd", "pecmd", "timeline explorer"],
    "registry-forensics": ["registry explorer", "ntuser.dat", "shimcache", "amcache"],
    "browser-forensics": ["browser history", "chrome", "firefox", "history"],
    "memory-forensics": ["volatility", "memprocfs", "malfind", "pslist", "netscan"],
    "malware-static": ["strings", "floss", "capa", "pestudio", "detect it easy"],
    "malware-dynamic": ["procmon", "process explorer", "fakenet", "any.run", "triage"],
    "maldoc-analysis": ["olevba", "oledump", "macro", "vba", "maldoc"],
    "reverse-engineering": ["ida", "ghidra", "radare2", "cutter", "dnspy", "dotpeek"],
    "cti-enrichment": ["virustotal", "urlhaus", "malpedia", "malwarebazaar", "opencti"],
    "email-header-analysis": ["spf", "dkim", "dmarc", "message header", "mxtoolbox"],
    "web-enumeration": ["gobuster", "dirb", "ffuf", "nikto", "wpscan"],
    "service-enumeration": ["nmap", "enum4linux", "smb", "ftp", "ssh"],
    "password-cracking": ["hydra", "john", "hashcat", "wordlist"],
    "privilege-escalation": ["privilege escalation", "sudo -l", "suid", "linpeas"],
    "stego-extraction": ["binwalk", "steghide", "exiftool", "strings"],
    "mobile-forensics": ["android", "apk", "jadx", "aleapp", "mobile forensics"],
    "web-exploitation": ["web", "http", "request", "响应", "回显", "payload"],
    "ssti": ["ssti", "jinja", "template", "flask", "模板注入"],
    "sql-injection": ["sql injection", "sql注入", "盲注", "报错注入", "union select", "堆叠注入", "mysql"],
    "deserialization": ["deserialize", "deserialization", "反序列化", "pop chain", "popchains", "__wakeup", "__destruct"],
    "file-upload": ["file upload", "upload", "文件上传"],
    "file-inclusion": ["file inclusion", "include", "lfi", "rfi", "php://filter", "文件包含"],
    "command-injection": ["command injection", "rce", "命令执行", "os.popen", "system(", "eval("],
    "xss": ["xss", "cross site scripting", "跨站脚本"],
    "waf-bypass": ["waf", "绕过", "bypass", "blacklist", "黑名单"],
    "jwt-analysis": ["jwt", "json web token"],
    "php-tricks": ["php特性", "弱比较", "类型转换", "md5", "数组绕过", "序列化"],
    "binary-exploitation": ["pwn", "pwntools", "checksec", "栈溢出", "rop", "ret2text", "ret2libc"],
    "stack-overflow": ["stack overflow", "栈溢出", "gets(", "buffer overflow"],
    "ret2text": ["ret2text", "backdoor"],
    "ret2libc": ["ret2libc", "/bin/sh", "system(", "one_gadget"],
    "integer-overflow": ["integer overflow", "整数溢出", "unsigned int"],
    "format-string": ["format string", "格式化字符串"],
    "symbolic-execution": ["angr", "z3", "constraint", "约束求解", "符号执行"],
    "crypto-analysis": ["crypto", "cipher", "解密", "密文", "key", "密钥"],
    "classical-crypto": ["caesar", "凯撒", "rot", "base64", "维吉尼亚", "栅栏"],
    "stream-cipher": ["rc4", "stream cipher"],
    "encoding-analysis": ["编码分析", "base64", "hex", "unicode", "url编码"],
    "osint": ["osint", "地图", "图片搜索", "社工", "搜索引擎"],
    "traffic-analysis": ["流量分析", "pcap", "wireshark", "tshark"],
    "qr-analysis": ["二维码", "qr"],
    "image-analysis": ["watermark", "隐写", "二维码", "channel", "lsb", "残差", "dark watermark"],
    "misc-analysis": ["misc", "编码分析", "隐写", "压缩包", "二维码", "流量分析"],
}

TOOL_ALIASES = {
    "nmap": ["nmap"],
    "gobuster": ["gobuster", "gobuster"],
    "dirb": ["dirb"],
    "ffuf": ["ffuf"],
    "nikto": ["nikto"],
    "wpscan": ["wpscan"],
    "burp": ["burp", "burp suite"],
    "hydra": ["hydra"],
    "john": ["john"],
    "hashcat": ["hashcat"],
    "wireshark": ["wireshark"],
    "tshark": ["tshark"],
    "zeek": ["zeek"],
    "snort": ["snort"],
    "suricata": ["suricata"],
    "splunk": ["splunk"],
    "elk": ["elk", "elastic", "kibana"],
    "wazuh": ["wazuh"],
    "volatility": ["volatility", "volatility 2", "volatility3"],
    "memprocfs": ["memprocfs"],
    "autopsy": ["autopsy"],
    "ftk-imager": ["ftk imager"],
    "mftecmd": ["mftecmd"],
    "pecmd": ["pecmd"],
    "evtxecmd": ["evtxecmd"],
    "registry-explorer": ["registry explorer"],
    "db-browser-sqlite": ["db browser for sqlite"],
    "olevba": ["olevba"],
    "oledump": ["oledump"],
    "capa": ["capa"],
    "floss": ["floss"],
    "pestudio": ["pestudio", "pe studio"],
    "detect-it-easy": ["detect it easy", "die"],
    "ida": ["ida", "ida pro", "ida free"],
    "ghidra": ["ghidra"],
    "radare2": ["radare2", "r2"],
    "cutter": ["cutter"],
    "dnspy": ["dnspy"],
    "jadx": ["jadx"],
    "gdb": ["gdb", "pwndbg"],
    "checksec": ["checksec"],
    "pwntools": ["pwntools", "from pwn import", "pwnlib"],
    "ropgadget": ["ropgadget"],
    "one-gadget": ["one_gadget", "one-gadget"],
    "yakit": ["yakit"],
    "sqlmap": ["sqlmap"],
    "antsword": ["antsword", "中国蚁剑"],
    "angr": ["angr"],
    "z3": ["z3"],
    "stegsolve": ["stegsolve"],
    "foremost": ["foremost"],
    "netcat": ["nc", "netcat"],
    "cyberchef": ["cyberchef"],
    "virustotal": ["virustotal"],
    "urlhaus": ["urlhaus"],
    "malpedia": ["malpedia"],
    "malwarebazaar": ["malwarebazaar", "malware bazaar"],
    "binwalk": ["binwalk"],
    "steghide": ["steghide"],
    "exiftool": ["exiftool"],
    "strings": ["strings"],
}

COMMAND_HINT_RE = re.compile(
    r"\b(?:sudo|nmap|gobuster|dirb|ffuf|nikto|wpscan|hydra|john|hashcat|tshark|"
    r"zeek|snort|suricata|volatility|vol\.py|python3?|curl|wget|ssh|ftp|smbclient|"
    r"enum4linux|searchsploit|msfconsole|msfvenom|binwalk|steghide|exiftool|strings|"
    r"olevba|oledump|floss|capa|yara|radare2|r2|jq|grep|awk|sed|cut|uniq|gdb|checksec|"
    r"pwntools|ropgadget|one_gadget|netcat|nc|sqlmap|angr|z3)\b",
    re.IGNORECASE,
)
QUESTION_START_RE = re.compile(
    r"^(?:Q\d+|Question\s+\d+[.)]?|Task\s+\d+[.)]?|#?\s*\d+[.)])\s+(.+)$",
    re.IGNORECASE,
)
ANSWER_RE = re.compile(r"^(?:Answer|Flag|User Flag|Root Flag|Solution)\s*:\s*(.*)$", re.IGNORECASE)
ACTION_HINT_RE = re.compile(
    r"\b(?:use|using|run|filter|search|query|navigate|open|inspect|extract|decode|"
    r"follow|look|check|click|expand|convert|upload|grep|find|identify|enumerate|scan|"
    r"observe|construct|verify|bypass|exploit|查看|访问|观察|分析|构造|传递|验证|绕过|利用|执行|上传|搜索|运行)\b",
    re.IGNORECASE,
)
EVIDENCE_HINT_RE = re.compile(
    r"\b(?:we can see|this means|found|shows|reveals|contains|indicates|there are|"
    r"result|output|credential|password|hash|domain|ip address|mac address|timestamp|"
    r"可以看到|发现|说明|证明|存在|成功|回显|输出|返回|泄露|拿到)\b",
    re.IGNORECASE,
)
FILTER_HINT_RE = re.compile(
    r"(?:==|!=|\bcontains\b|\bframe\.|\bip\.|\btcp\.|\budp\.|\bhttp\.|\bdns\.|\btls\.|\beth\.|"
    r"\bindex=|\bsourcetype=|\bEventCode=|\bevent\.code|\|)",
    re.IGNORECASE,
)
COMMAND_LINE_RE = re.compile(
    r"^(?:sudo\s+)?(?:nmap|gobuster|dirb|ffuf|nikto|wpscan|hydra|john|hashcat|"
    r"tshark|zeek|snort|suricata|volatility|vol\.py|python3?|curl|wget|ssh|ftp|"
    r"smbclient|enum4linux|searchsploit|msfconsole|msfvenom|binwalk|steghide|"
    r"exiftool|strings|olevba|oledump|floss|capa|yara|radare2|r2|jq|grep|awk|"
    r"gdb|checksec|sqlmap|netcat|nc|angr|z3|"
    r"sed|cut|uniq)\b",
    re.IGNORECASE,
)
NATURAL_QUESTION_RE = re.compile(
    r"^(?:what|which|who|when|where|why|how|find|identify|determine|submit|"
    r"recover|extract|decode|what's|whats|如何|什么|为什么|怎样|哪一个|哪个)\b",
    re.IGNORECASE,
)

CATEGORY_PLAYBOOKS = {
    "Network Forensics": [
        "Inventory capture files and identify dominant protocols, endpoints, and conversations.",
        "Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.",
        "Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.",
        "When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.",
    ],
    "Endpoint Forensics": [
        "Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.",
        "Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.",
        "Correlate logs with file and registry evidence before trusting one artifact alone.",
        "Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.",
    ],
    "SIEM (ELK, Splunk, etc.)": [
        "Translate the question into searchable fields such as host, user, process, index, sourcetype, URI, IP, hash, or event code.",
        "Run broad time-bounded searches first, then narrow by event type, field value, and correlation chain.",
        "Keep the exact query shape and the evidence field that proves each answer.",
    ],
    "Malware Analysis": [
        "Classify the artifact and packer/runtime before deep reversing.",
        "Extract strings, imports, capabilities, configuration, embedded URLs, hashes, and persistence behavior.",
        "Correlate static indicators with sandbox or process-monitor evidence when available.",
    ],
    "Email Analysis": [
        "Inspect headers first: sender path, SPF/DKIM/DMARC, received chain, reply-to, attachments, and URLs.",
        "Decode attachments, URLs, and embedded payloads in an isolated workflow.",
        "Enrich domains, IPs, and hashes only after extracting them locally.",
    ],
    "Cyber Threat Intelligence (CTI)": [
        "Extract observables first, then enrich with threat intelligence sources.",
        "Map hashes, domains, malware names, TTPs, and infrastructure to campaigns or actors only when evidence supports it.",
    ],
    "Pentesting": [
        "Begin with service discovery and directory/application enumeration.",
        "Map each exposed service to default credentials, known CVEs, misconfiguration, or content leaks.",
        "After initial access, enumerate local privilege escalation paths before exploitation.",
    ],
    "Reverse Engineering": [
        "Identify file type, architecture, symbols, strings, imports, and obvious validation routines.",
        "Work from observable input/output behavior into static control flow and comparison points.",
    ],
    "Mobile Forensics": [
        "Inventory app/database artifacts, timestamps, media, account records, and package metadata.",
        "Extract SQLite, plist/XML/JSON, and app-specific records before guessing behavior.",
    ],
    "IDS/IPS": [
        "Start from alerts/signatures, then validate them against packet context and endpoint/network indicators.",
        "Tune signatures only after confirming the malicious flow and payload boundaries.",
    ],
    "Web": [
        "Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.",
        "Validate the suspected primitive with the smallest payload that proves code/data/control influence.",
        "Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.",
    ],
    "Crypto": [
        "Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.",
        "Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.",
        "Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.",
    ],
    "Pwn": [
        "Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.",
        "Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.",
        "Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.",
    ],
    "Reverse": [
        "Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.",
        "Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.",
        "Prefer the smallest static or dynamic proof that explains the flag or accepted input.",
    ],
    "Misc": [
        "Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.",
        "Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.",
        "Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.",
    ],
    "Incident Response": [
        "Anchor the case in the supplied host, log, or traffic artifact and build a time-bounded incident narrative.",
        "Correlate users, processes, files, timestamps, and network indicators before trusting any single log line.",
        "Preserve the exact log field or recovered artifact that proves each conclusion.",
    ],
    "AI and Digital Watermark": [
        "Inventory channels, metadata, layout, repeated motifs, and model- or watermark-specific residue before editing pixels.",
        "Test cheap residual views such as channel differences, modulo masks, OCR crops, and simple transforms before deeper reconstruction.",
        "Keep the final interpretation tied to the exact rendered artifact that exposes the hidden signal.",
    ],
    "Training and Meta": [
        "Treat the document as study guidance: extract challenge taxonomy, workflow rules, tool references, and reusable habits.",
        "Record platform names, topic tags, and tool examples so later queries can reach the right note quickly.",
        "Prefer compact summaries that preserve lookup value over full-text duplication.",
    ],
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slugify(value: str) -> str:
    raw = value.strip()
    lowered = raw.lower()
    lowered = lowered.replace(os.sep, "-").replace("/", "-")
    slug = re.sub(r"[^a-z0-9]+", "-", lowered).strip("-")
    if not slug:
        return f"case-{hashlib.sha1(raw.encode('utf-8')).hexdigest()[:10]}"
    if re.search(r"[^\x00-\x7F]", raw) and len(slug) < 8:
        return f"{slug}-{hashlib.sha1(raw.encode('utf-8')).hexdigest()[:8]}"
    return slug


def split_list_values(value: str) -> list[str]:
    if not value:
        return []
    raw = re.sub(r"[()（）]", " ", value)
    pieces = re.split(r"[、,，;/|]+|\s{2,}", raw)
    items = []
    for piece in pieces:
        cleaned = re.sub(r"\s+", " ", piece).strip()
        if cleaned:
            items.append(cleaned)
    return first_unique(items, 40)


def normalize_heading_title(title: str) -> str:
    cleaned = title.strip()
    cleaned = re.sub(r"^[#\s]+", "", cleaned)
    cleaned = re.sub(r"^[0-9一二三四五六七八九十]+[、.．)\-]\s*", "", cleaned)
    return cleaned.strip()


def canonical_section_title(title: str) -> str:
    lowered = normalize_heading_title(title).lower()
    aliases = {
        "基本信息": "metadata",
        "解题思路": "approach",
        "看到什么": "observation",
        "想到什么解题思路": "approach",
        "尝试过程和结果记录": "attempts",
        "尝试过程与结果记录": "attempts",
        "过程和结果记录": "attempts",
        "总结": "summary",
        "总结与反思": "summary",
        "总结反思": "summary",
        "how to solve": "approach",
        "solution": "attempts",
    }
    for key, value in aliases.items():
        if key in lowered:
            return value
    return lowered


def parse_markdown_sections(text: str) -> list[dict[str, Any]]:
    sections: list[dict[str, Any]] = []
    current = {"level": 0, "title": "Document", "lines": []}
    for raw_line in text.splitlines():
        stripped = raw_line.strip()
        match = MARKDOWN_HEADING_RE.match(stripped)
        if match:
            if current["lines"] or current["title"] != "Document":
                sections.append(current)
            current = {"level": len(match.group(1)), "title": normalize_heading_title(match.group(2)), "lines": []}
            continue
        current["lines"].append(raw_line.rstrip())
    if current["lines"] or current["title"] != "Document":
        sections.append(current)
    return sections


def parse_markdown_metadata(sections: list[dict[str, Any]], lines: list[str]) -> dict[str, str]:
    metadata: dict[str, str] = {}
    candidate_lines: list[str] = []
    for section in sections[:3]:
        title = canonical_section_title(section["title"])
        if title == "metadata":
            candidate_lines.extend(clean_lines("\n".join(section["lines"])))
    if not candidate_lines:
        candidate_lines = [line for line in lines[:30] if line.startswith("- ")]
    for line in candidate_lines:
        match = re.match(r"^[-*]\s*([^:：]{1,40})\s*[:：]\s*(.+)$", line)
        if not match:
            continue
        key = re.sub(r"\s+", "", match.group(1))
        value = re.sub(r"\s+", " ", match.group(2)).strip()
        if key and value:
            metadata[key] = value
    return metadata


def infer_markdown_title(markdown_path: Path, metadata: dict[str, str], sections: list[dict[str, Any]], lines: list[str]) -> str:
    for key in ("题目名称", "题目", "title", "Title"):
        if metadata.get(key):
            return metadata[key]
    for section in sections:
        title = normalize_heading_title(section["title"])
        if title and title.lower() not in {"document", "metadata", "基本信息"}:
            return title
    for line in lines[:20]:
        if line.startswith("- "):
            continue
        stripped = re.sub(r"^[#\s]+", "", line).strip()
        if stripped:
            return stripped
    return markdown_path.stem


def infer_platform_name(title: str, metadata: dict[str, str], rel_path: Path) -> str:
    for candidate in [metadata.get("题目名称", ""), title, rel_path.stem]:
        if not candidate:
            continue
        match = re.match(r"^\[([^\]]+)\]", candidate)
        if match:
            return match.group(1).strip()
        match = re.match(r"^(.+?)(?:[-_]\s*| {2,}|(?<!^)\s+-\s+)", candidate)
        if match:
            maybe = match.group(1).strip()
            if 2 <= len(maybe) <= 40:
                return maybe
        match = re.match(r"^([A-Za-z0-9# +]{3,40})", candidate)
        if match:
            maybe = match.group(1).strip()
            if " " in maybe or "CTF" in maybe.upper():
                return maybe
    top = rel_path.parts[0] if rel_path.parts else ""
    if top == "overthewire":
        return "OverTheWire"
    return top or ""


def map_markdown_repo_category(rel_path: Path) -> str:
    top = rel_path.parts[0] if rel_path.parts else ""
    return MARKDOWN_REPO_CATEGORY_MAP.get(top, "Training and Meta")


def infer_markdown_repo_category(rel_path: Path, title: str, signal_text: str) -> str:
    category = map_markdown_repo_category(rel_path)
    if category != "Training and Meta":
        return category
    probe = " ".join(
        [
            str(rel_path.with_suffix("")),
            title,
            signal_text[:4000],
        ]
    ).lower()
    keyword_sets = {
        "Web": [
            "web",
            "http",
            "php",
            "sql",
            "sqli",
            "xss",
            "csrf",
            "ssrf",
            "ssti",
            "upload",
            "rce",
            "waf",
            "flask",
            "thinkphp",
            "node",
            "javaweb",
            "文件上传",
            "注入",
            "反序列化",
            "命令执行",
            "文件包含",
        ],
        "Crypto": [
            "crypto",
            "rsa",
            "aes",
            "des",
            "md5",
            "sha",
            "base64",
            "base32",
            "caesar",
            "morse",
            "rot13",
            "密码",
            "凯撒",
            "摩斯",
            "栅栏",
            "维吉尼亚",
            "哈希",
        ],
        "Pwn": [
            "pwn",
            "rop",
            "ret2",
            "libc",
            "heap",
            "stack",
            "canary",
            "uaf",
            "shellcode",
            "checksec",
            "pwntools",
            "溢出",
            "格式化字符串",
            "堆",
            "栈",
        ],
        "Reverse": [
            "reverse",
            "reversing",
            "rev",
            "crackme",
            "ida",
            "jadx",
            "android",
            "apk",
            "逆向",
            "脱壳",
            "反编译",
        ],
        "Misc": [
            "misc",
            "steg",
            "forensic",
            "pcap",
            "wireshark",
            "binwalk",
            "foremost",
            "png",
            "jpg",
            "zip",
            "rar",
            "qr",
            "隐写",
            "取证",
            "流量",
            "压缩包",
            "二维码",
            "图片",
        ],
    }
    scores = {
        candidate: sum(1 for keyword in keywords if keyword in probe)
        for candidate, keywords in keyword_sets.items()
    }
    best_category, best_score = max(scores.items(), key=lambda item: item[1])
    return best_category if best_score else category


def default_artifacts_for_category(category: str) -> list[str]:
    return DEFAULT_CATEGORY_ARTIFACTS.get(category, ["notes"])


def default_techniques_for_category(category: str) -> list[str]:
    return DEFAULT_CATEGORY_TECHNIQUES.get(category, ["study-guide"])


def build_github_blob_url(repo_url: str, commit: str, relative_path: Path) -> str:
    target_ref = commit or "main"
    quoted = "/".join(quote(part) for part in relative_path.parts)
    return f"{repo_url.rstrip('/')}/blob/{target_ref}/{quoted}"


def extract_markdown_image_paths(text: str, markdown_path: Path, repo_root: Path) -> list[str]:
    assets: list[str] = []
    for href in MARKDOWN_IMAGE_RE.findall(text):
        resolved = resolve_repo_relative_path(repo_root, markdown_path, href)
        if resolved:
            assets.append(resolved)
    return first_unique(assets, 200)


def resolve_repo_relative_path(repo_root: Path, current_file: Path, href: str) -> str | None:
    value = href.strip()
    if not value or value.startswith(("http://", "https://", "data:", "mailto:")):
        return None
    value = unquote(value.split("#", 1)[0].split("?", 1)[0]).strip()
    if not value:
        return None
    candidate = (current_file.parent / value).resolve()
    try:
        relative = candidate.relative_to(repo_root.resolve())
    except ValueError:
        return None
    return str(relative).replace(os.sep, "/")


def detect_asset_kind(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".md":
        return "markdown"
    if suffix in {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"}:
        return "image"
    if suffix in {".py", ".sh", ".js", ".php"}:
        return "script"
    if suffix in {".json", ".txt", ".sample", ".lst", ".idx", ".rev"}:
        return "data"
    return suffix.lstrip(".") or "file"


def clean_markdown_signal_text(text: str) -> str:
    cleaned = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    cleaned = re.sub(r"\[[^\]]+\]\((https?://[^)]+)\)", " ", cleaned)
    return cleaned


def normalize_sources(index: dict[str, Any]) -> list[dict[str, Any]]:
    sources = index.get("sources") or []
    if sources:
        return sources
    repo = index.get("source_repo")
    if repo:
        return [
            {
                "name": repo.rsplit("/", 1)[-1],
                "repo": repo,
                "commit": index.get("source_commit") or "",
                "kind": "legacy-casebook-source",
                "case_count": index.get("case_count") or len(index.get("cases") or []),
            }
        ]
    return []


def copy_repo_mirror(src_root: Path, dst_root: Path) -> None:
    if dst_root.exists():
        shutil.rmtree(dst_root)
    shutil.copytree(src_root, dst_root, ignore=shutil.ignore_patterns(".git"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def ensure_pypdf():
    try:
        from pypdf import PdfReader  # type: ignore
        return PdfReader
    except Exception:
        pass
    PDF_RUNTIME.mkdir(parents=True, exist_ok=True)
    if str(PDF_RUNTIME) not in sys.path:
        sys.path.insert(0, str(PDF_RUNTIME))
    try:
        from pypdf import PdfReader  # type: ignore
        return PdfReader
    except Exception:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--quiet", "--target", str(PDF_RUNTIME), "pypdf"],
            check=True,
        )
        from pypdf import PdfReader  # type: ignore
        return PdfReader


def markdown_link(cell: str) -> tuple[str | None, str | None]:
    match = MARKDOWN_LINK_RE.search(cell)
    if not match:
        return None, None
    return match.group(1).strip(), match.group(2).strip()


def normalize_difficulty(cell: str) -> str:
    lowered = cell.lower()
    if "easy" in lowered:
        return "Easy"
    if "medium" in lowered:
        return "Medium"
    if "hard" in lowered:
        return "Hard"
    return re.sub(r"\s+", " ", cell).strip()


def parse_readme(readme_path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    category = None
    for line in readme_path.read_text(encoding="utf-8", errors="replace").splitlines():
        heading = re.match(r"### \*\*(.+?)\*\*", line.strip())
        if heading:
            category = heading.group(1).strip()
            continue
        if not category or not line.startswith("|") or "[PDF]" not in line:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        title = re.sub(r"\s+", " ", cells[0]).strip()
        _, pdf_url = markdown_link(cells[1])
        platform, challenge_url = markdown_link(cells[2])
        difficulty = normalize_difficulty(cells[3])
        rating = cells[4].count("⭐")
        tags_cell = cells[5] if len(cells) > 5 else ""
        tags = [re.sub(r"\s+", " ", tag).strip() for tag in TAG_RE.findall(tags_cell)]
        if not pdf_url:
            continue
        pdf_name = pdf_url.rsplit("/", 1)[-1]
        slug = slugify(Path(pdf_name).stem)
        rows.append(
            {
                "slug": slug,
                "title": title,
                "category": category,
                "platform": platform or "",
                "challenge_url": challenge_url or "",
                "difficulty": difficulty,
                "rating": rating,
                "tags": tags,
                "source_pdf_url": pdf_url,
                "pdf_name": pdf_name,
            }
        )
    return rows


def extract_pdf_text(pdf_path: Path) -> tuple[str, dict[str, Any]]:
    PdfReader = ensure_pypdf()
    reader = PdfReader(str(pdf_path))
    pages: list[dict[str, Any]] = []
    parts: list[str] = []
    for index, page in enumerate(reader.pages, 1):
        try:
            text = page.extract_text() or ""
        except Exception as exc:
            text = f"[page extraction failed: {exc}]"
        text = text.replace("\x00", "")
        pages.append({"page": index, "chars": len(text), "sample": text[:500]})
        parts.append(f"\n\n===== PAGE {index} =====\n{text}")
    full_text = "\n".join(parts).strip() + "\n"
    metadata = {
        "pages": len(reader.pages),
        "encrypted": bool(reader.is_encrypted),
        "metadata": {str(k): str(v) for k, v in (reader.metadata or {}).items()},
        "page_summaries": pages,
    }
    return full_text, metadata


def clean_lines(text: str) -> list[str]:
    lines: list[str] = []
    for raw in text.splitlines():
        line = re.sub(r"\s+", " ", raw).strip()
        if not line or line.startswith("===== PAGE "):
            continue
        lines.append(line)
    return lines


def first_unique(items: list[str], limit: int) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        key = item.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
        if len(out) >= limit:
            break
    return out


def detect_named_sets(text: str, term_map: dict[str, list[str]]) -> list[str]:
    lowered = text.lower()
    hits = []
    for name, terms in term_map.items():
        if any(term.lower() in lowered for term in terms):
            hits.append(name)
    return sorted(hits)


def detect_tools(tags: list[str], text: str) -> list[str]:
    joined = " ".join(tags) + "\n" + text
    lowered = joined.lower()
    tools = []
    for tool, aliases in TOOL_ALIASES.items():
        if any(alias.lower() in lowered for alias in aliases):
            tools.append(tool)
    return sorted(tools)


def extract_iocs(text: str) -> dict[str, list[str]]:
    domains = [d for d in DOMAIN_RE.findall(text) if not d.lower().endswith((".png", ".jpg", ".pdf"))]
    return {
        "ipv4": first_unique(IPV4_RE.findall(text), 30),
        "hashes": first_unique(HASH_RE.findall(text), 30),
        "cves": first_unique([c.upper() for c in CVE_RE.findall(text)], 20),
        "emails": first_unique(EMAIL_RE.findall(text), 20),
        "urls": first_unique(URL_RE.findall(text), 30),
        "domains": first_unique(domains, 30),
    }


def extract_commands(lines: list[str]) -> list[str]:
    candidates = []
    for line in lines:
        if COMMAND_HINT_RE.search(line):
            if len(line) <= 240:
                candidates.append(line)
    return first_unique(candidates, 40)


def extract_questions(lines: list[str]) -> list[str]:
    candidates = []
    for line in lines:
        if len(line) > 220:
            continue
        if line.endswith(("?", "？")) or re.match(r"^(?:Q\d+|Question\s+\d+|Task\s+\d+|#?\s*\d+[.)])\s+", line, re.I):
            candidates.append(line)
    return first_unique(candidates, 30)


def extract_outline(lines: list[str]) -> list[str]:
    candidates = []
    for line in lines:
        if len(line) > 120:
            continue
        if re.match(r"^(?:#+\s*)?(?:Task|Question|Scenario|Investigation|Analysis|Enumeration|Forensics|Answer|Tools|Conclusion|Root|Initial Access|Privilege Escalation)\b", line, re.I):
            candidates.append(line)
        elif re.match(r"^(?:#+\s*)?(?:基本信息|解题思路|看到什么|想到什么解题思路|尝试过程.*结果记录|过程和结果记录|总结|总结与反思|工具清单|考点清单)\b", line):
            candidates.append(line)
        elif re.match(r"^\d+(?:\.\d+)*\s+[A-Z][A-Za-z0-9 /_-]{3,}$", line):
            candidates.append(line)
    return first_unique(candidates, 30)


def is_question_line(line: str) -> bool:
    if len(line) > 240:
        return False
    if QUESTION_START_RE.match(line):
        return True
    if NATURAL_QUESTION_RE.match(line) and len(line.split()) >= 3:
        return True
    if line.endswith("?") and len(line.split()) >= 3:
        return True
    return False


def looks_like_heading(line: str) -> bool:
    if len(line) > 100:
        return False
    if line.endswith(":"):
        return False
    return bool(
        re.match(
            r"^(?:Scenario|Summary|Tools Used|Enumeration|Initial Access|Privilege Escalation|"
            r"Forensics|Analysis|Investigation|Root|User|Conclusion|Task\s+\d+|"
            r"基本信息|解题思路|看到什么|想到什么解题思路|尝试过程.*结果记录|总结|总结与反思)\b",
            line,
            re.IGNORECASE,
        )
    )


def extract_answer(lines: list[str]) -> str:
    for i, line in enumerate(lines):
        match = ANSWER_RE.match(line)
        if not match:
            continue
        value = match.group(1).strip()
        if value:
            return value[:300]
        for follower in lines[i + 1 : i + 4]:
            if follower and not is_question_line(follower):
                return follower[:300]
    joined = "\n".join(lines)
    phrase = re.search(r"\bit is (?:a |an )?(.+?) which is the answer\b", joined, re.IGNORECASE)
    if phrase:
        return phrase.group(1).strip()[:300]
    for pattern in (
        CVE_RE,
        re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}:\d{1,5}\b"),
        IPV4_RE,
        HASH_RE,
        re.compile(r"\b[a-zA-Z0-9_-]+\.(?:exe|dll|doc|rtf|ps1|bat|sh|php|jsp|aspx)\b"),
    ):
        found = pattern.search(joined)
        if found:
            return found.group(0)[:300]
    for line in reversed(lines):
        stripped = line.strip()
        if not stripped or stripped == "```" or stripped.startswith("![](") or is_question_line(stripped) or len(stripped) > 160:
            continue
        if ACTION_HINT_RE.search(stripped) or EVIDENCE_HINT_RE.search(stripped):
            continue
        if (
            CVE_RE.search(stripped)
            or IPV4_RE.search(stripped)
            or HASH_RE.search(stripped)
            or re.search(r"\b[a-zA-Z0-9_-]+\.(?:exe|dll|doc|rtf|ps1|bat|sh|php|jsp|aspx)\b", stripped)
            or len(stripped.split()) <= 8
        ):
            return stripped[:300]
    return ""


def classify_route(goal: str, body: str, tools: list[str], techniques: list[str]) -> str:
    haystack = f"{goal}\n{body}".lower()
    if any(term in haystack for term in ["ssti", "template", "jinja", "模板注入"]):
        return "ssti exploitation"
    if any(term in haystack for term in ["sql injection", "sql注入", "盲注", "union select", "报错注入"]):
        return "sql injection exploitation"
    if any(term in haystack for term in ["deserialize", "deserialization", "反序列化", "pop chain", "popchains"]):
        return "deserialization chain"
    if any(term in haystack for term in ["file upload", "upload", "文件上传"]):
        return "file upload bypass"
    if any(term in haystack for term in ["file inclusion", "lfi", "rfi", "include", "文件包含", "php://filter"]):
        return "file inclusion exploitation"
    if any(term in haystack for term in ["command injection", "rce", "命令执行", "os.popen", "system("]):
        return "command execution path"
    if any(term in haystack for term in ["xss", "跨站脚本"]):
        return "xss route"
    if any(term in haystack for term in ["waf", "绕过", "blacklist", "黑名单"]):
        return "waf bypass"
    if any(term in haystack for term in ["jwt", "json web token"]):
        return "jwt trust-boundary abuse"
    if any(term in haystack for term in ["栈溢出", "stack overflow", "buffer overflow", "ret2text", "ret2libc", "pwntools"]):
        return "stack control exploitation"
    if any(term in haystack for term in ["integer overflow", "整数溢出", "unsigned int"]):
        return "integer-overflow bypass"
    if any(term in haystack for term in ["format string", "格式化字符串"]):
        return "format-string control path"
    if any(term in haystack for term in ["angr", "z3", "constraint", "约束求解", "符号执行"]):
        return "constraint solving"
    if any(term in haystack for term in ["caesar", "凯撒", "base64", "rot", "cipher", "密文", "解密", "rc4", "rsa", "aes"]):
        return "cipher decoding"
    if any(term in haystack for term in ["二维码", "qr", "隐写", "watermark", "lsb", "channel"]):
        return "stego extraction"
    if any(term in haystack for term in ["日志", "auth.log", "syslog", "incident", "应急响应"]):
        return "incident timeline reconstruction"
    if any(term in haystack for term in ["mac address", "manufacturer", "ethernet", "oui"]):
        return "layer-2 endpoint identification"
    if any(term in haystack for term in ["dns", "domain", "query"]):
        return "dns pivot"
    if any(term in haystack for term in ["udp packets", "tcp packets", "conversation", "statistics", "packets sent"]):
        return "conversation statistics"
    if any(term in haystack for term in ["camera model", "exif", "metadata", "image metadata"]):
        return "file metadata extraction"
    if any(term in haystack for term in ["tls", "client random", "session id", "handshake", "certificate"]):
        return "tls handshake inspection"
    if "reverse-engineering" in techniques:
        return "reverse engineering"
    if "maldoc-analysis" in techniques and any(term in haystack for term in ["macro", "maldoc", "olevba", "oledump", "document", ".doc", ".rtf"]):
        return "maldoc analysis"
    if any(term in haystack for term in ["credential", "password", "login", "ftp", "basic auth"]):
        return "credential discovery"
    if any(term in haystack for term in ["http", "url", "uri", "host", "user-agent", "web"]):
        return "http evidence extraction"
    if any(term in haystack for term in ["event id", "event log", "sysmon", "evtx"]):
        return "event-log correlation"
    if any(term in haystack for term in ["registry", "ntuser", "amcache", "shimcache"]):
        return "registry artifact correlation"
    if any(term in haystack for term in ["timeline", "timestamp", "created", "modified", "time"]):
        return "timeline reconstruction"
    if any(term in haystack for term in ["hash", "virustotal", "malwarebazaar", "malpedia"]):
        return "indicator enrichment"
    if any(term in haystack for term in ["macro", "maldoc", "olevba", "oledump"]):
        return "maldoc analysis"
    if any(term in haystack for term in ["memory", "volatility", "process", "pslist", "netscan"]):
        return "memory artifact analysis"
    if any(term in haystack for term in ["nmap", "gobuster", "smb", "ssh", "privilege escalation"]):
        return "service-to-access path"
    if tools:
        return f"{tools[0]}-driven evidence lookup"
    return "evidence lookup"


def infer_probe(goal: str, body: str, route_type: str, tools: list[str], filters: list[str]) -> str:
    tool_text = ", ".join(tools[:4]) if tools else "the artifact-specific tool"
    if filters:
        return f"Use {tool_text} with the extracted filter/query `{filters[0]}` and inspect the matching evidence."
    probes = {
        "ssti exploitation": f"Use {tool_text} to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.",
        "sql injection exploitation": f"Use {tool_text} to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.",
        "deserialization chain": f"Use {tool_text} to confirm object injection and map the gadget or magic-method path before building the final payload.",
        "file upload bypass": f"Use {tool_text} to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.",
        "file inclusion exploitation": f"Use {tool_text} to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.",
        "command execution path": f"Use {tool_text} to verify command execution or shell expansion with a tiny proof command before reading the target file.",
        "xss route": f"Use {tool_text} to verify the sink, context, and trigger condition before choosing the smallest executable payload.",
        "waf bypass": f"Use {tool_text} to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.",
        "jwt trust-boundary abuse": f"Use {tool_text} to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.",
        "stack control exploitation": f"Use {tool_text} to confirm the overwrite boundary, control target, and calling path before sending the final payload.",
        "integer-overflow bypass": f"Use {tool_text} to verify the numeric edge case and how it changes the downstream size or bounds check.",
        "format-string control path": f"Use {tool_text} to map readable and writable stack positions before attempting the final primitive.",
        "constraint solving": f"Use {tool_text} to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.",
        "cipher decoding": f"Use {tool_text} to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.",
        "stego extraction": f"Use {tool_text} to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.",
        "incident timeline reconstruction": f"Use {tool_text} to anchor the event in time, user, host, and file/process context before answering.",
        "conversation statistics": f"Use {tool_text} to inspect conversation statistics or packet counts for the constrained endpoints and protocol.",
        "layer-2 endpoint identification": f"Use {tool_text} to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.",
        "file metadata extraction": f"Use {tool_text} to recover or open the referenced file and inspect its metadata fields.",
        "tls handshake inspection": f"Use {tool_text} to filter the relevant TLS handshake and inspect session, random, key, or certificate fields.",
        "credential discovery": f"Use {tool_text} to inspect credentials, authentication fields, or followed streams before deeper analysis.",
        "dns pivot": f"Use {tool_text} to filter DNS traffic and pivot from source host to queried domain or resolver.",
        "http evidence extraction": f"Use {tool_text} to inspect HTTP requests, hosts, URIs, headers, and response bodies.",
        "event-log correlation": f"Use {tool_text} to search the relevant event IDs and correlate user, process, host, and timestamp fields.",
        "registry artifact correlation": f"Use {tool_text} to inspect registry hives or parsed registry artifacts for persistence and user activity.",
        "timeline reconstruction": f"Use {tool_text} to align timestamps and identify the event that satisfies the question.",
        "indicator enrichment": f"Extract local indicators first, then enrich hashes, domains, IPs, or malware names.",
        "maldoc analysis": f"Use {tool_text} to extract macros, streams, embedded URLs, and decoded script content.",
        "memory artifact analysis": f"Use {tool_text} to enumerate processes, network sockets, injected regions, and command lines.",
        "service-to-access path": f"Use {tool_text} to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.",
        "reverse engineering": f"Use {tool_text} to locate strings, comparisons, and control-flow decisions relevant to the input.",
    }
    return probes.get(route_type, f"Use {tool_text} to collect the smallest evidence slice that answers the goal.")


def infer_evidence_rule(route_type: str, evidence: list[str], result: str) -> str:
    if evidence:
        return "Trust the result only when the extracted evidence line or field directly supports it."
    if result:
        return "Treat the extracted answer as proven only after locating the source artifact field that produced it."
    rules = {
        "ssti exploitation": "The proof is the rendered template output or file/command result that survives the server-side filter path.",
        "sql injection exploitation": "The proof is the database-backed response difference, error, or extracted row tied to the injected parameter.",
        "deserialization chain": "The proof is the gadget-triggered behavior or sink output caused by the supplied serialized object.",
        "file upload bypass": "The proof is the reachable uploaded artifact and the server behavior that executes or parses it unexpectedly.",
        "file inclusion exploitation": "The proof is the included file content or wrapper output returned by the controlled path.",
        "command execution path": "The proof is the returned command output or filesystem effect from the injected command.",
        "xss route": "The proof is the actual script execution in the intended rendering context, not the payload string alone.",
        "waf bypass": "The proof is the blocked primitive working through the filter path, not just a payload variation that reflects.",
        "jwt trust-boundary abuse": "The proof is the server accepting the mutated claims or signature and exposing the gated action.",
        "stack control exploitation": "The proof is the controlled return or call path, plus the program behavior that reaches the target win path.",
        "integer-overflow bypass": "The proof is the numeric conversion outcome and the downstream memory or logic effect it enables.",
        "format-string control path": "The proof is the exact read/write effect at the intended stack or memory location.",
        "constraint solving": "The proof is the recovered input satisfying the exact validation branch or symbolic condition.",
        "cipher decoding": "The proof is the plaintext structure or key schedule step that explains why the decoded output is correct.",
        "stego extraction": "The proof is the recovered hidden content from the concrete channel, not a guess from surrounding hints.",
        "incident timeline reconstruction": "The proof is the timestamped log or artifact field tied to the incident action in context.",
        "conversation statistics": "The proof is the packet/conversation statistic matching the exact endpoints and protocol.",
        "layer-2 endpoint identification": "The proof is the Ethernet address field or OUI lookup tied to the relevant host.",
        "file metadata extraction": "The proof is the recovered file metadata field, not the filename alone.",
        "tls handshake inspection": "The proof is the TLS handshake field from the packet matching the session or host constraint.",
        "credential discovery": "The proof is the authentication field or stream showing the credential value.",
        "dns pivot": "The proof is the DNS packet, resolver, queried domain, or response record.",
        "http evidence extraction": "The proof is the request or response field such as Host, URI, header, body, or status.",
        "event-log correlation": "The proof is the event record and correlated timestamp/user/process fields.",
        "registry artifact correlation": "The proof is the parsed registry key/value and its timestamp or user context.",
        "timeline reconstruction": "The proof is the timestamped artifact that matches the question constraint.",
        "indicator enrichment": "The proof is the locally extracted indicator plus the enrichment source result.",
        "maldoc analysis": "The proof is the decoded macro, stream, URL, command, or embedded payload.",
        "memory artifact analysis": "The proof is the memory plugin output tied to process/socket/module evidence.",
        "service-to-access path": "The proof is the service enumeration result and the exact access or escalation condition.",
        "reverse engineering": "The proof is the code path, comparison, constant, or decoded data that explains the answer.",
    }
    return rules.get(route_type, "The proof is the smallest artifact field that directly answers the goal.")


def infer_reusable_pattern(route_type: str, category: str) -> str:
    patterns = {
        "ssti exploitation": "SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.",
        "sql injection exploitation": "SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.",
        "deserialization chain": "Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.",
        "file upload bypass": "Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.",
        "file inclusion exploitation": "Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.",
        "command execution path": "Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.",
        "xss route": "XSS cases should classify the rendering context before payload design.",
        "waf bypass": "WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.",
        "jwt trust-boundary abuse": "JWT cases hinge on understanding what the server actually trusts: signature, claim, header, or backend lookup.",
        "stack control exploitation": "Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.",
        "integer-overflow bypass": "Numeric edge cases matter when they alter a length, signedness, allocation, or control-flow boundary.",
        "format-string control path": "Format-string routes start with stack discovery and end with the smallest precise read or write.",
        "constraint solving": "Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.",
        "cipher decoding": "Crypto cases should peel encodings first and keep every transformation individually checkable.",
        "stego extraction": "Stego cases should test cheap channels before assuming heavy custom hiding logic.",
        "incident timeline reconstruction": "Incident-response cases become reusable when every claim is anchored to timestamped artifact correlation.",
        "conversation statistics": "Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.",
        "layer-2 endpoint identification": "MAC/OUI questions should start from the relevant endpoint conversation, then verify the address in Ethernet fields.",
        "file metadata extraction": "When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.",
        "tls handshake inspection": "TLS questions usually require filtering the specific handshake and reading the requested field directly.",
        "credential discovery": "When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.",
        "dns pivot": "DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.",
        "http evidence extraction": "HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.",
        "event-log correlation": "Event-log cases should be solved by field correlation, not by reading logs chronologically.",
        "registry artifact correlation": "Registry artifacts are strongest when paired with timestamp and user context.",
        "timeline reconstruction": "Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.",
        "indicator enrichment": "Threat-intel enrichment is only useful after local extraction of stable indicators.",
        "maldoc analysis": "Maldoc routes start with stream/macro extraction and decoding before behavior claims.",
        "memory artifact analysis": "Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.",
        "service-to-access path": "Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.",
        "reverse engineering": "Reverse routes pivot from strings/imports into the exact validation or decoding logic.",
    }
    return patterns.get(route_type, f"For {category}, keep every answer tied to one artifact, one probe, and one proof field.")


def extract_filters(lines: list[str]) -> list[str]:
    filters = []
    for line in lines:
        stripped = line.lstrip("•-* ").strip()
        if stripped.endswith(":"):
            continue
        if MARKDOWN_LINK_RE.search(stripped) and not COMMAND_LINE_RE.search(stripped):
            continue
        if len(stripped) <= 220 and FILTER_HINT_RE.search(stripped):
            filters.append(stripped)
        elif len(stripped) <= 220 and COMMAND_LINE_RE.search(stripped):
            filters.append(stripped)
    return first_unique(filters, 8)


def split_reasoning_sections(lines: list[str]) -> list[dict[str, Any]]:
    sections: list[dict[str, Any]] = []
    current_title = "Case Triage"
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_lines, current_title
        body = [line for line in current_lines if line != current_title]
        if body:
            sections.append({"goal": current_title, "lines": body})
        current_lines = []

    def question_continues(title: str, line: str) -> bool:
        stripped = line.strip()
        if len(stripped) > 120:
            return False
        if (
            CVE_RE.search(stripped)
            or IPV4_RE.search(stripped)
            or HASH_RE.search(stripped)
            or URL_RE.search(stripped)
            or re.search(r"\b[a-zA-Z0-9_-]+\.(?:exe|dll|doc|rtf|ps1|bat|sh|php|jsp|aspx)\b", stripped)
        ):
            return False
        if stripped.endswith("?") or stripped.endswith(")"):
            return True
        if len(stripped.split()) <= 4 and not ACTION_HINT_RE.search(stripped):
            return True
        return title.rstrip().lower().endswith(
            (
                " with",
                " of",
                " from",
                " to",
                " for",
                " in",
                " on",
                " at",
                " the",
                " a",
                " an",
                " these",
                " this",
                " victim",
                " format:",
                " id:",
            )
        )

    for line in lines:
        if is_question_line(line) or (looks_like_heading(line) and current_lines):
            flush()
            current_title = QUESTION_START_RE.match(line).group(1).strip() if QUESTION_START_RE.match(line) else line
            current_lines = [line]
        elif (
            current_lines
            and len(current_lines) == 1
            and (NATURAL_QUESTION_RE.match(current_title) or current_title.endswith("(Format:") or current_title.endswith("with"))
            and not ANSWER_RE.match(line)
            and not ACTION_HINT_RE.search(line)
            and not looks_like_heading(line)
            and len(line) <= 160
            and question_continues(current_title, line)
        ):
            current_title = f"{current_title} {line}".strip()
            current_lines[0] = current_title
        else:
            current_lines.append(line)
    flush()
    return sections


def build_reasoning_routes(row: dict[str, Any], lines: list[str], signals: dict[str, Any]) -> list[dict[str, Any]]:
    routes = []
    sections = split_reasoning_sections(lines)
    for number, section in enumerate(sections, 1):
        goal = section["goal"].strip()
        if re.match(r"^(?:case triage|summary|scenario|tools used|challenge|platform|category|difficulty)\b", goal, re.IGNORECASE):
            continue
        body_lines = section["lines"]
        body = "\n".join(body_lines)
        if len(goal) < 3 or (number > 1 and goal.lower().startswith("answer")):
            continue
        section_tools = detect_tools(row["tags"], body)
        section_techniques = detect_named_sets(" ".join(row["tags"]) + "\n" + body, TECHNIQUE_TERMS)
        route_type = classify_route(goal, body, section_tools or signals["tools"], section_techniques or signals["techniques"])
        action_lines = first_unique([line for line in body_lines if ACTION_HINT_RE.search(line) and len(line) <= 220], 6)
        evidence_lines = first_unique([line for line in body_lines if EVIDENCE_HINT_RE.search(line) and len(line) <= 220], 6)
        filters = extract_filters(body_lines)
        result = extract_answer(body_lines)
        if not (action_lines or evidence_lines or filters or result or is_question_line(goal)):
            continue
        routes.append(
            {
                "step": len(routes) + 1,
                "goal": goal[:220],
                "route_type": route_type,
                "why_this_route": infer_reusable_pattern(route_type, row["category"]),
                "probe": infer_probe(goal, body, route_type, section_tools or signals["tools"], filters),
                "reasoning_chain": [
                    f"Recognize the goal as {route_type}.",
                    infer_probe(goal, body, route_type, section_tools or signals["tools"], filters),
                    infer_evidence_rule(route_type, evidence_lines, result),
                ],
                "tools": section_tools or signals["tools"][:5],
                "filters_or_commands": filters,
                "evidence_to_check": evidence_lines,
                "evidence_rule": infer_evidence_rule(route_type, evidence_lines, result),
                "result": result,
            }
        )
        if len(routes) >= 40:
            break
    if not routes:
        body_lines = [
            line
            for line in lines
            if not re.match(r"^(?:Source|Title|Category|Extracted):", line, re.IGNORECASE)
        ]
        body = "\n".join(body_lines)
        route_type = classify_route(row["title"], body, signals["tools"], signals["techniques"])
        filters = extract_filters(body_lines)
        evidence_lines = first_unique([line for line in body_lines if EVIDENCE_HINT_RE.search(line) and len(line) <= 220], 6)
        result = extract_answer(body_lines)
        routes.append(
            {
                "step": 1,
                "goal": f"Apply the case-level route for {row['title']}",
                "route_type": route_type,
                "why_this_route": infer_reusable_pattern(route_type, row["category"]),
                "probe": infer_probe(row["title"], body, route_type, signals["tools"], filters),
                "reasoning_chain": [
                    f"Recognize the case as {route_type}.",
                    infer_probe(row["title"], body, route_type, signals["tools"], filters),
                    infer_evidence_rule(route_type, evidence_lines, result),
                ],
                "tools": signals["tools"][:5],
                "filters_or_commands": filters,
                "evidence_to_check": evidence_lines,
                "evidence_rule": infer_evidence_rule(route_type, evidence_lines, result),
                "result": result,
            }
        )
    return routes


def build_case_playbook(row: dict[str, Any], signals: dict[str, Any], routes: list[dict[str, Any]]) -> dict[str, Any]:
    categories = CATEGORY_PLAYBOOKS.get(row["category"], ["Inventory the provided artifacts.", "Choose the cheapest probe that can confirm or reject the first hypothesis.", "Keep each conclusion tied to one evidence field."])
    first_routes = [route["route_type"] for route in routes[:8]]
    return {
        "case_intent": f"Use this case as a {row['category']} reference for {', '.join(signals['artifacts'][:3]) or 'artifact-driven'} challenges.",
        "input_signals": {
            "artifacts": signals["artifacts"],
            "tools": signals["tools"],
            "techniques": signals["techniques"],
            "tags": row.get("tags") or [],
        },
        "first_principles_route": categories,
        "dominant_route_types": first_unique(first_routes, 10),
        "reuse_checklist": [
            "Match the new challenge's artifact and question shape against this case before copying any tool sequence.",
            "Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.",
            "Promote any repeated manual action into a skill command before relying on it for the final solve.",
        ],
    }


def write_case_card(output_root: Path, case: dict[str, Any]) -> str:
    card_path = output_root / "cards" / f"{case['slug']}.md"
    card_path.parent.mkdir(parents=True, exist_ok=True)
    playbook = case["solve_thinking"]
    source_lines = []
    if case.get("source_repo"):
        source_lines.append(f"- Source repository: `{case['source_repo']}`")
    if case.get("source_commit"):
        source_lines.append(f"- Source commit: `{case['source_commit']}`")
    if case.get("source_pdf_url"):
        source_lines.append(f"- Source PDF: `{case['source_pdf_url']}`")
    if case.get("source_path"):
        source_lines.append(f"- Source file: `{case['source_path']}`")
    if case.get("source_url"):
        source_lines.append(f"- Source URL: `{case['source_url']}`")
    if case.get("local_source_path"):
        source_lines.append(f"- Local source mirror: `{case['local_source_path']}`")
    lines = [
        f"# {case['title']}",
        "",
        "## Case Metadata",
        "",
        f"- Category: `{case['category']}`",
        f"- Platform: `{case.get('platform') or 'unknown'}`",
        f"- Difficulty: `{case.get('difficulty') or 'unknown'}`",
    ]
    lines.extend(source_lines)
    if case.get("challenge_url"):
        lines.append(f"- Challenge URL: `{case['challenge_url']}`")
    lines.extend(
        [
            "",
            "## Why This Case Matters",
        "",
        playbook["case_intent"],
        "",
        "## Input Signals",
        "",
        f"- Artifacts: {', '.join(playbook['input_signals']['artifacts']) or 'not detected'}",
        f"- Tools: {', '.join(playbook['input_signals']['tools']) or 'not detected'}",
        f"- Techniques: {', '.join(playbook['input_signals']['techniques']) or 'not detected'}",
        "",
        "## First-Principles Route",
        "",
        ]
    )
    for item in playbook["first_principles_route"]:
        lines.append(f"- {item}")
    if case.get("linked_assets"):
        lines.extend(["", "## Linked Assets", ""])
        lines.append(f"- Referenced assets: `{case.get('linked_asset_count') or len(case['linked_assets'])}`")
        for asset in case["linked_assets"][:12]:
            lines.append(f"- `{asset}`")
        remaining = len(case["linked_assets"]) - 12
        if remaining > 0:
            lines.append(f"- ... and `{remaining}` more")
    lines.extend(["", "## Solve Thinking", ""])
    if not case["reasoning_routes"]:
        lines.append("- No reliable route sections were extracted; inspect the source writeup or refresh the casebook.")
    for route in case["reasoning_routes"]:
        lines.extend(
            [
                f"### Step {route['step']}: {route['goal']}",
                "",
                f"- Route type: `{route['route_type']}`",
                f"- Why: {route['why_this_route']}",
                f"- Probe: {route['probe']}",
            ]
        )
        if route["tools"]:
            lines.append(f"- Tools: {', '.join(route['tools'])}")
        if route["filters_or_commands"]:
            lines.append("- Filters or commands:")
            for command in route["filters_or_commands"][:6]:
                lines.append(f"  - `{command}`")
        lines.append("- Reasoning chain:")
        for item in route.get("reasoning_chain", []):
            lines.append(f"  - {item}")
        lines.append(f"- Evidence rule: {route['evidence_rule']}")
        if route["result"]:
            lines.append(f"- Result: `{route['result']}`")
        lines.append("")
    lines.extend(["## Reuse Checklist", ""])
    for item in playbook["reuse_checklist"]:
        lines.append(f"- {item}")
    card_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return str(card_path.relative_to(output_root))


def summarize_method(case: dict[str, Any], signals: dict[str, Any]) -> list[str]:
    bits = []
    title = case["title"]
    category = case["category"]
    platform = case.get("platform") or "unknown platform"
    bits.append(f"{title} is a {category} case from {platform}.")
    artifacts = signals["artifacts"][:5]
    tools = signals["tools"][:8]
    techniques = signals["techniques"][:6]
    if artifacts:
        bits.append("Primary artifact signals: " + ", ".join(artifacts) + ".")
    if tools:
        bits.append("Tool route: " + ", ".join(tools) + ".")
    if techniques:
        bits.append("Reusable techniques: " + ", ".join(techniques) + ".")
    if signals["questions"]:
        bits.append("Use the extracted task/question list to drive evidence-first answering.")
    return bits


def build_case(row: dict[str, Any], pdf_path: Path, output_root: Path) -> dict[str, Any]:
    text, pdf_meta = extract_pdf_text(pdf_path)
    sha256 = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
    lines = clean_lines(text)
    signals = {
        "tools": detect_tools(row["tags"], text),
        "artifacts": detect_named_sets(text, ARTIFACT_TERMS),
        "techniques": detect_named_sets(" ".join(row["tags"]) + "\n" + text, TECHNIQUE_TERMS),
        "commands": extract_commands(lines),
        "questions": extract_questions(lines),
        "outline": extract_outline(lines),
        "iocs": extract_iocs(text),
    }
    reasoning_routes = build_reasoning_routes(row, lines, signals)
    solve_thinking = build_case_playbook(row, signals, reasoning_routes)
    case = {
        **row,
        "source_repo": "https://github.com/tim-barc/ctf_writeups",
        "source_commit": "",
        "local_pdf": str(pdf_path),
        "pdf_sha256": sha256,
        "pdf": pdf_meta,
        "text_chars": len(text),
        "signals": signals,
        "solve_thinking": solve_thinking,
        "reasoning_routes": reasoning_routes,
        "route_count": len(reasoning_routes),
        "method_summary": summarize_method(row, signals),
    }
    case["card"] = write_case_card(output_root, case)
    return case


def build_markdown_reasoning_routes(
    row: dict[str, Any], sections: list[dict[str, Any]], lines: list[str], signals: dict[str, Any]
) -> list[dict[str, Any]]:
    routes: list[dict[str, Any]] = []
    for section in sections:
        canonical = canonical_section_title(section["title"])
        if canonical in {"metadata", "summary"}:
            continue
        body_lines = clean_lines("\n".join(section["lines"]))
        if not body_lines:
            continue
        goal = normalize_heading_title(section["title"]) or f"{row['title']} route"
        body = "\n".join(body_lines)
        section_tools = detect_tools(row.get("tags") or [], body)
        section_techniques = detect_named_sets(" ".join(row.get("tags") or []) + "\n" + body, TECHNIQUE_TERMS)
        route_type = classify_route(goal, body, section_tools or signals["tools"], section_techniques or signals["techniques"])
        filters = extract_filters(body_lines)
        evidence_lines = first_unique(
            [
                line
                for line in body_lines
                if (EVIDENCE_HINT_RE.search(line) or "flag" in line.lower() or "回显" in line or "成功" in line)
                and len(line) <= 220
            ],
            6,
        )
        result = extract_answer(body_lines)
        routes.append(
            {
                "step": len(routes) + 1,
                "goal": goal[:220],
                "route_type": route_type,
                "why_this_route": infer_reusable_pattern(route_type, row["category"]),
                "probe": infer_probe(goal, body, route_type, section_tools or signals["tools"], filters),
                "reasoning_chain": [
                    f"Recognize the section as {route_type}.",
                    infer_probe(goal, body, route_type, section_tools or signals["tools"], filters),
                    infer_evidence_rule(route_type, evidence_lines, result),
                ],
                "tools": section_tools or signals["tools"][:5],
                "filters_or_commands": filters,
                "evidence_to_check": evidence_lines,
                "evidence_rule": infer_evidence_rule(route_type, evidence_lines, result),
                "result": result,
            }
        )
        if len(routes) >= 12:
            break
    if routes:
        return routes
    return build_reasoning_routes(row, lines, signals)


def build_markdown_case(
    repo_root: Path,
    markdown_path: Path,
    output_root: Path,
    repo_url: str,
    source_commit: str,
    repo_slug: str,
    mirrored_repo_root: Path | None,
) -> dict[str, Any]:
    text = markdown_path.read_text(encoding="utf-8", errors="replace")
    signal_text = clean_markdown_signal_text(text)
    lines = clean_lines(text)
    sections = parse_markdown_sections(text)
    metadata = parse_markdown_metadata(sections, lines)
    rel_path = markdown_path.relative_to(repo_root)
    title = infer_markdown_title(markdown_path, metadata, sections, lines)
    category = infer_markdown_repo_category(rel_path, title, signal_text)
    challenge_url = metadata.get("题目链接") or metadata.get("链接") or ""
    tags = split_list_values(metadata.get("考点清单", ""))
    payload_tags = split_list_values(metadata.get("payloads", ""))
    tool_tags = split_list_values(metadata.get("工具清单", ""))
    row = {
        "slug": slugify(str(rel_path.with_suffix("")).replace(os.sep, "-")),
        "title": title,
        "category": category,
        "platform": infer_platform_name(title, metadata, rel_path),
        "challenge_url": challenge_url,
        "difficulty": metadata.get("难度", ""),
        "rating": 0,
        "tags": first_unique(tags + payload_tags + [rel_path.parts[0]] if rel_path.parts else tags + payload_tags, 30),
    }
    image_assets = extract_markdown_image_paths(text, markdown_path, repo_root)
    signals = {
        "tools": first_unique(tool_tags + detect_tools(row["tags"], signal_text), 20),
        "artifacts": detect_named_sets(signal_text, ARTIFACT_TERMS),
        "techniques": detect_named_sets(" ".join(row["tags"]) + "\n" + signal_text, TECHNIQUE_TERMS),
        "commands": extract_commands(lines),
        "questions": extract_questions(lines),
        "outline": extract_outline(lines),
        "iocs": extract_iocs(signal_text),
    }
    if not signals["artifacts"]:
        signals["artifacts"] = default_artifacts_for_category(category)
    if not signals["techniques"]:
        signals["techniques"] = default_techniques_for_category(category)
    reasoning_routes = build_markdown_reasoning_routes(row, sections, lines, signals)
    solve_thinking = build_case_playbook(row, signals, reasoning_routes)
    local_source_path = ""
    if mirrored_repo_root is not None:
        local_source_path = str((mirrored_repo_root / rel_path).relative_to(output_root)).replace(os.sep, "/")
    case = {
        **row,
        "source_repo": repo_url,
        "source_commit": source_commit,
        "source_path": str(rel_path).replace(os.sep, "/"),
        "source_url": build_github_blob_url(repo_url, source_commit, rel_path),
        "local_source_path": local_source_path,
        "linked_assets": image_assets,
        "linked_asset_count": len(image_assets),
        "text_chars": len(text),
        "signals": signals,
        "solve_thinking": solve_thinking,
        "reasoning_routes": reasoning_routes,
        "route_count": len(reasoning_routes),
        "method_summary": summarize_method(row, signals),
        "repo_slug": repo_slug,
    }
    case["card"] = write_case_card(output_root, case)
    return case


def build_compact_case(case: dict[str, Any]) -> dict[str, Any]:
    compact = {
        "slug": case["slug"],
        "title": case["title"],
        "category": case["category"],
        "platform": case.get("platform") or "",
        "difficulty": case.get("difficulty") or "",
        "rating": case.get("rating") or 0,
        "tags": case.get("tags") or [],
        "tools": case.get("signals", {}).get("tools") or case.get("tools") or [],
        "techniques": case.get("signals", {}).get("techniques") or case.get("techniques") or [],
        "artifacts": case.get("signals", {}).get("artifacts") or case.get("artifacts") or [],
        "route_types": case.get("solve_thinking", {}).get("dominant_route_types")
        or case.get("route_types")
        or first_unique([route.get("route_type", "") for route in case.get("reasoning_routes") or [] if route.get("route_type")], 10),
        "route_count": case.get("route_count") or len(case.get("reasoning_routes") or []),
        "card": case["card"],
    }
    for key in (
        "method_summary",
        "solve_thinking",
        "reasoning_routes",
        "source_repo",
        "source_commit",
        "source_pdf_url",
        "source_url",
        "source_path",
        "local_source_path",
        "linked_assets",
        "linked_asset_count",
        "challenge_url",
        "repo_slug",
    ):
        value = case.get(key)
        if value not in (None, "", [], {}):
            compact[key] = value
    signals = case.get("signals") or {}
    if signals:
        compact["signals"] = {
            "tools": signals.get("tools") or [],
            "artifacts": signals.get("artifacts") or [],
            "techniques": signals.get("techniques") or [],
            "outline": (signals.get("outline") or [])[:20],
            "questions": (signals.get("questions") or [])[:20],
            "commands": (signals.get("commands") or [])[:20],
        }
    return compact


def build_index_data(
    cases: list[dict[str, Any]],
    *,
    sources: list[dict[str, Any]],
    missing: list[dict[str, Any]] | None = None,
    asset_entries: list[dict[str, Any]] | None = None,
    source_note: str = "",
) -> dict[str, Any]:
    missing = missing or []
    asset_entries = asset_entries or []
    category_counts = Counter(case["category"] for case in cases)
    platform_counts = Counter(case.get("platform") or "unknown" for case in cases)
    difficulty_counts = Counter(case.get("difficulty") or "unknown" for case in cases)
    tool_counts: Counter[str] = Counter()
    technique_counts: Counter[str] = Counter()
    tag_counts: Counter[str] = Counter()
    route_type_counts: Counter[str] = Counter()
    for case in cases:
        tool_counts.update(case.get("tools") or [])
        technique_counts.update(case.get("techniques") or [])
        tag_counts.update(case.get("tags") or [])
        route_type_counts.update(case.get("route_types") or [])
    asset_kind_counts = Counter(asset.get("kind") or "file" for asset in asset_entries)
    source_repo = sources[0]["repo"] if len(sources) == 1 else ""
    source_commit = sources[0].get("commit", "") if len(sources) == 1 else ""
    return {
        "casebook_schema": "compact-hierarchy-index-v3",
        "generated_at": utc_now(),
        "source_repo": source_repo,
        "source_commit": source_commit,
        "sources": sources,
        "source_note": source_note or "Distilled local cards from external CTF repositories plus searchable raw asset inventories.",
        "layout": {
            "index": "index.json",
            "taxonomy": "taxonomy.json",
            "root_index": "indexes/root.md",
            "sources_index": "indexes/sources/root.md",
            "overview": "overview.md",
            "cards": "cards/*.md",
            "mirrors": "sources/*/repo/**",
        },
        "case_count": len(cases),
        "missing_count": len(missing),
        "asset_count": len(asset_entries),
        "stats": {
            "categories": dict(sorted(category_counts.items())),
            "platforms": dict(sorted(platform_counts.items())),
            "difficulties": dict(sorted(difficulty_counts.items())),
            "top_tags": tag_counts.most_common(50),
            "top_tools": tool_counts.most_common(50),
            "top_techniques": technique_counts.most_common(50),
            "top_route_types": route_type_counts.most_common(50),
            "asset_kinds": asset_kind_counts.most_common(20),
        },
        "cases": cases,
        "missing": missing,
        "assets": asset_entries,
    }


def write_overview(output_root: Path, index: dict[str, Any]) -> None:
    categories = index["stats"]["categories"]
    tools = index["stats"]["top_tools"][:20]
    techniques = index["stats"]["top_techniques"][:20]
    route_types = index["stats"].get("top_route_types", [])[:20]
    asset_kinds = index["stats"].get("asset_kinds", [])[:20]
    sources = normalize_sources(index)
    lines = [
        "# CTF Casebook",
        "",
        "This is a compact local reasoning casebook distilled from external CTF writeups and mirrored study repositories.",
        "Use `scripts/ctf_casebook.py browse` to walk category, artifact, technique, and route before starting a new CTF route.",
        "",
        f"- Cases parsed: `{index['case_count']}`",
        f"- Mirrored assets: `{index.get('asset_count') or 0}`",
        f"- Generated: `{index['generated_at']}`",
        f"- Root index: `indexes/root.md`",
        f"- Source index: `indexes/sources/root.md`",
        f"- Taxonomy: `taxonomy.json`",
        "",
        "## Sources",
        "",
    ]
    for source in sources:
        bits = [f"`{source.get('name') or source.get('repo')}`"]
        if source.get("repo"):
            bits.append(source["repo"])
        if source.get("commit"):
            bits.append(f"commit `{source['commit']}`")
        if source.get("case_count") is not None:
            bits.append(f"cases `{source['case_count']}`")
        if source.get("asset_count") is not None:
            bits.append(f"assets `{source['asset_count']}`")
        lines.append("- " + " | ".join(bits))
    lines.extend(
        [
            "",
        "## Categories",
        "",
        ]
    )
    for category, count in categories.items():
        lines.append(f"- `{category}`: {count}")
    lines.extend(["", "## Top Tools", ""])
    for name, count in tools:
        lines.append(f"- `{name}`: {count}")
    lines.extend(["", "## Top Techniques", ""])
    for name, count in techniques:
        lines.append(f"- `{name}`: {count}")
    lines.extend(["", "## Top Route Types", ""])
    for name, count in route_types:
        lines.append(f"- `{name}`: {count}")
    if asset_kinds:
        lines.extend(["", "## Asset Kinds", ""])
        for name, count in asset_kinds:
            lines.append(f"- `{name}`: {count}")
    lines.extend(
        [
            "",
            "## Browse",
            "",
            "```bash",
            "./skills/kali/scripts/ctf_casebook.py browse",
            "./skills/kali/scripts/ctf_casebook.py browse --category 'Network Forensics'",
            "./skills/kali/scripts/ctf_casebook.py browse --category 'Network Forensics' --artifact pcap",
            "./skills/kali/scripts/ctf_casebook.py browse --category 'Network Forensics' --artifact pcap --technique http-analysis --cards",
            "./skills/kali/scripts/ctf_casebook.py show --slug cyber-defenders-packetmaze-lab",
            "./skills/kali/scripts/ctf_casebook.py search --query ssti",
            "./skills/kali/scripts/ctf_casebook.py search --query yakit --type asset",
            "```",
            "",
            "Browse results point to local cards under `cards/`. Search results can also point into mirrored raw repository assets under `sources/`.",
            "Read the card first; refresh the casebook only when the compact card lacks enough context.",
        ]
    )
    (output_root / "overview.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def command_ingest_tim_barc(args: argparse.Namespace) -> None:
    repo = Path(args.repo).expanduser().resolve()
    readme = repo / "README.md"
    writeups = repo / "writeups"
    if not readme.exists() or not writeups.exists():
        raise SystemExit(f"expected a supported writeups clone with README.md and writeups/: {repo}")
    output_root = Path(args.output).expanduser().resolve() if args.output else DEFAULT_CASEBOOK_ROOT
    output_root.mkdir(parents=True, exist_ok=True)
    rows = parse_readme(readme)
    source_commit = (args.source_commit or "").strip() or subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    ).stdout.strip()
    cases = []
    missing = []
    for index, row in enumerate(rows, 1):
        pdf_path = writeups / row["pdf_name"]
        if not pdf_path.exists():
            missing.append(row)
            continue
        case = build_case(row, pdf_path, output_root)
        case["source_commit"] = source_commit
        cases.append(case)
        if args.progress and (index == 1 or index % args.progress == 0 or index == len(rows)):
            print(f"[{index}/{len(rows)}] parsed {row['slug']}", flush=True)
    compact_cases = [build_compact_case(case) for case in cases]
    index_data = build_index_data(
        compact_cases,
        sources=[
            {
                "name": "tim-barc/ctf_writeups",
                "repo": "https://github.com/tim-barc/ctf_writeups",
                "commit": source_commit,
                "kind": "pdf-writeups",
                "case_count": len(compact_cases),
                "asset_count": 0,
            }
        ],
        missing=missing,
        source_note="Distilled local cards from public CTF writeups; lookup is by category, artifact, technique, route, and card.",
    )
    write_json(output_root / "index.json", index_data)
    write_overview(output_root, index_data)
    write_casebook_indexes(output_root, index_data)
    print(
        json.dumps(
            {
                "status": "ok",
                "output": str(output_root),
                "cases": len(cases),
                "missing": len(missing),
                "source_commit": source_commit,
                "root_index": str(output_root / "indexes" / "root.md"),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def load_index(casebook: Path) -> dict[str, Any]:
    path = casebook.expanduser().resolve() / "index.json"
    if not path.exists():
        raise SystemExit(f"missing casebook index: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def count_values(cases: list[dict[str, Any]], key: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    for case in cases:
        values = case.get(key) or []
        if isinstance(values, str):
            values = [values]
        counts.update(value for value in values if value)
    return counts


def sorted_counts(counts: Counter[str]) -> list[tuple[str, int]]:
    return sorted(counts.items(), key=lambda item: (-item[1], item[0].lower()))


def resolve_choice(value: str | None, choices: list[str], label: str) -> str | None:
    if not value:
        return None
    normalized = value.lower()
    for choice in choices:
        if choice.lower() == normalized:
            return choice
    valid = ", ".join(choices[:30])
    raise SystemExit(f"unknown {label}: {value}\nvalid {label}s: {valid}")


def filter_cases(
    cases: list[dict[str, Any]],
    *,
    category: str | None = None,
    artifact: str | None = None,
    technique: str | None = None,
    route_type: str | None = None,
    tool: str | None = None,
) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    for case in cases:
        if category and case.get("category") != category:
            continue
        if artifact and artifact not in (case.get("artifacts") or []):
            continue
        if technique and technique not in (case.get("techniques") or []):
            continue
        if route_type and route_type not in (case.get("route_types") or []):
            continue
        if tool and tool not in (case.get("tools") or []):
            continue
        selected.append(case)
    return selected


def compact_case(root: Path, case: dict[str, Any]) -> dict[str, Any]:
    return {
        "slug": case["slug"],
        "title": case["title"],
        "category": case["category"],
        "platform": case.get("platform") or "",
        "difficulty": case.get("difficulty") or "",
        "artifacts": case.get("artifacts") or [],
        "techniques": case.get("techniques") or [],
        "route_types": case.get("route_types") or [],
        "tools": case.get("tools") or [],
        "card_path": str(root / case.get("card", "")),
    }


def markdown_table(headers: list[str], rows: list[list[str]]) -> list[str]:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return lines


def relative_link(from_path: Path, to_path: Path) -> str:
    return os.path.relpath(to_path, from_path.parent).replace(os.sep, "/")


def write_casebook_indexes(root: Path, index: dict[str, Any]) -> None:
    indexes_dir = root / "indexes"
    if indexes_dir.exists():
        for path in sorted(indexes_dir.rglob("*"), reverse=True):
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                path.rmdir()
    indexes_dir.mkdir(parents=True, exist_ok=True)
    cases = index.get("cases") or []
    categories = [name for name, _count in sorted_counts(Counter(case["category"] for case in cases))]
    taxonomy: dict[str, Any] = {
        "levels": ["category", "artifact", "technique", "route_type", "card"],
        "root_index": "indexes/root.md",
        "categories": {},
    }

    root_path = indexes_dir / "root.md"
    root_rows: list[list[str]] = []
    for category in categories:
        category_cases = filter_cases(cases, category=category)
        category_slug = slugify(category)
        category_path = indexes_dir / "categories" / f"{category_slug}.md"
        root_rows.append(
            [
                f"[{category}]({relative_link(root_path, category_path)})",
                str(len(category_cases)),
                str(len(count_values(category_cases, "artifacts"))),
                str(len(count_values(category_cases, "techniques"))),
            ]
        )
        artifacts = [name for name, _count in sorted_counts(count_values(category_cases, "artifacts"))]
        taxonomy["categories"][category] = {
            "count": len(category_cases),
            "index": str(category_path.relative_to(root)).replace(os.sep, "/"),
            "artifacts": {},
        }
        category_lines = [
            f"# {category}",
            "",
            "Navigation: root -> category -> artifact -> technique/route -> card.",
            "",
            "## Artifacts",
            "",
        ]
        artifact_rows: list[list[str]] = []
        for artifact in artifacts:
            artifact_cases = filter_cases(category_cases, artifact=artifact)
            artifact_slug = slugify(artifact)
            artifact_path = indexes_dir / "categories" / category_slug / f"{artifact_slug}.md"
            artifact_rows.append(
                [
                    f"[{artifact}]({relative_link(category_path, artifact_path)})",
                    str(len(artifact_cases)),
                    str(len(count_values(artifact_cases, "techniques"))),
                    str(len(count_values(artifact_cases, "route_types"))),
                ]
            )
            techniques = [name for name, _count in sorted_counts(count_values(artifact_cases, "techniques"))]
            taxonomy["categories"][category]["artifacts"][artifact] = {
                "count": len(artifact_cases),
                "index": str(artifact_path.relative_to(root)).replace(os.sep, "/"),
                "techniques": {
                    technique: {
                        "count": len(filter_cases(artifact_cases, technique=technique)),
                        "routes": {
                            route: len(filter_cases(artifact_cases, technique=technique, route_type=route))
                            for route, _count in sorted_counts(
                                count_values(filter_cases(artifact_cases, technique=technique), "route_types")
                            )
                        },
                    }
                    for technique in techniques
                },
            }
            artifact_lines = [
                f"# {category} / {artifact}",
                "",
                "Navigation: root -> category -> artifact -> technique/route -> card.",
                "",
                "## Techniques",
                "",
            ]
            artifact_lines.extend(
                markdown_table(
                    ["Technique", "Cases", "Common routes"],
                    [
                        [
                            technique,
                            str(len(filter_cases(artifact_cases, technique=technique))),
                            ", ".join(
                                route
                                for route, _count in sorted_counts(
                                    count_values(filter_cases(artifact_cases, technique=technique), "route_types")
                                )[:5]
                            ),
                        ]
                        for technique in techniques
                    ],
                )
            )
            artifact_lines.extend(["", "## Route Types", ""])
            artifact_lines.extend(
                markdown_table(
                    ["Route type", "Cases"],
                    [[route, str(count)] for route, count in sorted_counts(count_values(artifact_cases, "route_types"))],
                )
            )
            artifact_lines.extend(["", "## Cards", ""])
            card_rows = []
            for case in sorted(artifact_cases, key=lambda item: (item["title"].lower(), item["slug"])):
                card_path = root / case["card"]
                card_rows.append(
                    [
                        f"[{case['title']}]({relative_link(artifact_path, card_path)})",
                        case.get("platform") or "",
                        case.get("difficulty") or "",
                        ", ".join((case.get("techniques") or [])[:4]),
                    ]
                )
            artifact_lines.extend(markdown_table(["Case", "Platform", "Difficulty", "Techniques"], card_rows))
            artifact_path.parent.mkdir(parents=True, exist_ok=True)
            artifact_path.write_text("\n".join(artifact_lines).rstrip() + "\n", encoding="utf-8")
        category_lines.extend(markdown_table(["Artifact", "Cases", "Techniques", "Routes"], artifact_rows))
        category_lines.extend(["", "## Techniques Overview", ""])
        category_lines.extend(
            markdown_table(
                ["Technique", "Cases"],
                [[technique, str(count)] for technique, count in sorted_counts(count_values(category_cases, "techniques"))],
            )
        )
        category_lines.extend(["", "## Route Overview", ""])
        category_lines.extend(
            markdown_table(
                ["Route type", "Cases"],
                [[route, str(count)] for route, count in sorted_counts(count_values(category_cases, "route_types"))],
            )
        )
        category_path.parent.mkdir(parents=True, exist_ok=True)
        category_path.write_text("\n".join(category_lines).rstrip() + "\n", encoding="utf-8")

    root_lines = [
        "# Casebook Root Index",
        "",
        "Navigation: choose a category, then an artifact, then a technique or route, then a card.",
        "Do not use fuzzy keyword search for normal case lookup.",
        "",
        "## Categories",
        "",
    ]
    root_lines.extend(markdown_table(["Category", "Cases", "Artifacts", "Techniques"], root_rows))
    root_lines.extend(
        [
            "",
            "## CLI Navigation",
            "",
            "```bash",
            "python3 skills/kali/scripts/ctf_casebook.py browse",
            "python3 skills/kali/scripts/ctf_casebook.py browse --category 'Network Forensics'",
            "python3 skills/kali/scripts/ctf_casebook.py browse --category 'Network Forensics' --artifact pcap",
            "python3 skills/kali/scripts/ctf_casebook.py browse --category 'Network Forensics' --artifact pcap --technique http-analysis --cards",
            "```",
        ]
    )
    root_path.write_text("\n".join(root_lines).rstrip() + "\n", encoding="utf-8")
    write_json(root / "taxonomy.json", taxonomy)
    write_source_indexes(root, index)


def write_source_indexes(root: Path, index: dict[str, Any]) -> None:
    assets = index.get("assets") or []
    sources = normalize_sources(index)
    sources_dir = root / "indexes" / "sources"
    sources_dir.mkdir(parents=True, exist_ok=True)
    root_path = sources_dir / "root.md"
    if not assets and not sources:
        root_path.write_text("# Source Index\n\nNo mirrored source inventory is available.\n", encoding="utf-8")
        return

    assets_by_repo: dict[str, list[dict[str, Any]]] = {}
    for asset in assets:
        assets_by_repo.setdefault(asset.get("source_repo") or "", []).append(asset)

    root_lines = [
        "# Source Index",
        "",
        "This tree summarizes mirrored external repositories and raw asset inventories that back the local casebook.",
        "",
    ]
    source_rows: list[list[str]] = []
    for source in sources:
        repo = source.get("repo") or ""
        source_slug = slugify(source.get("name") or repo or "source")
        source_path = sources_dir / f"{source_slug}.md"
        source_assets = assets_by_repo.get(repo, [])
        kind_counts = sorted_counts(Counter(asset.get("kind") or "file" for asset in source_assets))
        category_counts = sorted_counts(Counter(asset.get("category") or "Training and Meta" for asset in source_assets))
        source_rows.append(
            [
                f"[{source.get('name') or repo}]({relative_link(root_path, source_path)})",
                str(source.get("case_count") or 0),
                str(source.get("asset_count") or len(source_assets)),
                ", ".join(f"{kind}:{count}" for kind, count in kind_counts[:4]),
            ]
        )
        lines = [
            f"# {source.get('name') or repo}",
            "",
        ]
        if repo:
            lines.append(f"- Repository: `{repo}`")
        if source.get("commit"):
            lines.append(f"- Commit: `{source['commit']}`")
        if source.get("mirror"):
            lines.append(f"- Local mirror: `{source['mirror']}`")
        lines.extend(
            [
                f"- Cases: `{source.get('case_count') or 0}`",
                f"- Assets: `{source.get('asset_count') or len(source_assets)}`",
                "",
                "## Categories",
                "",
            ]
        )
        lines.extend(markdown_table(["Category", "Files"], [[name, str(count)] for name, count in category_counts]))
        lines.extend(["", "## Asset Kinds", ""])
        lines.extend(markdown_table(["Kind", "Files"], [[name, str(count)] for name, count in kind_counts]))
        markdown_assets = [asset for asset in source_assets if asset.get("kind") == "markdown"]
        if markdown_assets:
            lines.extend(["", "## Markdown Files", ""])
            rows = []
            for asset in sorted(markdown_assets, key=lambda item: item.get("relative_path", "")):
                local_path = asset.get("local_path") or asset.get("relative_path") or ""
                rows.append(
                    [
                        asset.get("relative_path") or "",
                        asset.get("category") or "",
                        asset.get("case_slug") or "",
                        local_path,
                    ]
                )
            lines.extend(markdown_table(["Path", "Category", "Case slug", "Local mirror"], rows[:200]))
            if len(rows) > 200:
                lines.extend(["", f"Only the first 200 markdown files are listed here. Full inventory remains in `index.json` assets."])
        source_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    root_lines.extend(markdown_table(["Source", "Cases", "Assets", "Kinds"], source_rows))
    root_path.write_text("\n".join(root_lines).rstrip() + "\n", encoding="utf-8")


def command_reindex(args: argparse.Namespace) -> None:
    root = Path(args.casebook).expanduser().resolve()
    index = load_index(root)
    write_casebook_indexes(root, index)
    print(
        json.dumps(
            {
                "status": "ok",
                "root_index": str(root / "indexes" / "root.md"),
                "taxonomy": str(root / "taxonomy.json"),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def score_match(query_tokens: list[str], haystack: str) -> int:
    lowered = haystack.lower()
    score = 0
    for token in query_tokens:
        if token in lowered:
            score += 3 if f" {token} " in f" {lowered} " else 1
    return score


def command_search(args: argparse.Namespace) -> None:
    root = Path(args.casebook).expanduser().resolve()
    index = load_index(root)
    query_tokens = [token.lower() for token in re.split(r"\s+", args.query.strip()) if token]
    if not query_tokens:
        raise SystemExit("query must not be empty")

    case_hits: list[dict[str, Any]] = []
    if args.type in {"all", "case"}:
        for case in index.get("cases") or []:
            haystack = "\n".join(
                [
                    case.get("title") or "",
                    case.get("category") or "",
                    case.get("platform") or "",
                    case.get("difficulty") or "",
                    " ".join(case.get("tags") or []),
                    " ".join(case.get("tools") or []),
                    " ".join(case.get("techniques") or []),
                    " ".join(case.get("artifacts") or []),
                    case.get("source_path") or "",
                    case.get("source_url") or "",
                    " ".join(case.get("method_summary") or []),
                    " ".join((case.get("signals") or {}).get("outline") or []),
                    " ".join((case.get("signals") or {}).get("questions") or []),
                ]
            )
            score = score_match(query_tokens, haystack)
            if score:
                case_hits.append(
                    {
                        "kind": "case",
                        "score": score,
                        "slug": case["slug"],
                        "title": case["title"],
                        "category": case["category"],
                        "card_path": str(root / case.get("card", "")),
                        "source_path": case.get("source_path") or "",
                    }
                )

    asset_hits: list[dict[str, Any]] = []
    if args.type in {"all", "asset"}:
        for asset in index.get("assets") or []:
            haystack = "\n".join(
                [
                    asset.get("relative_path") or "",
                    asset.get("kind") or "",
                    asset.get("category") or "",
                    asset.get("source_repo") or "",
                    " ".join(asset.get("referenced_by") or []),
                ]
            )
            score = score_match(query_tokens, haystack)
            if score:
                asset_hits.append(
                    {
                        "kind": "asset",
                        "score": score,
                        "relative_path": asset.get("relative_path") or "",
                        "local_path": str(root / (asset.get("local_path") or asset.get("relative_path") or "")),
                        "category": asset.get("category") or "",
                        "asset_type": asset.get("kind") or "",
                        "referenced_by": asset.get("referenced_by") or [],
                    }
                )

    hits = sorted(case_hits + asset_hits, key=lambda item: (-item["score"], item.get("title") or item.get("relative_path") or ""))[: args.limit]
    payload = {"query": args.query, "count": len(hits), "results": hits}
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return
    print(f"Query: {args.query}")
    print(f"Results: {len(hits)}")
    for hit in hits:
        if hit["kind"] == "case":
            print(f"\n- [case] {hit['title']} ({hit['category']})")
            print(f"  slug: {hit['slug']}")
            print(f"  card: {hit['card_path']}")
            if hit.get("source_path"):
                print(f"  source: {hit['source_path']}")
        else:
            print(f"\n- [asset] {hit['relative_path']} ({hit['asset_type']})")
            print(f"  category: {hit['category']}")
            print(f"  local: {hit['local_path']}")
            if hit.get("referenced_by"):
                print(f"  referenced_by: {', '.join(hit['referenced_by'][:5])}")


def command_ingest_markdown_repo(args: argparse.Namespace) -> None:
    repo = Path(args.repo).expanduser().resolve()
    if not repo.exists():
        raise SystemExit(f"missing repository path: {repo}")
    output_root = Path(args.output).expanduser().resolve() if args.output else DEFAULT_CASEBOOK_ROOT
    output_root.mkdir(parents=True, exist_ok=True)
    repo_url = args.repo_url.rstrip("/")
    repo_slug = slugify(args.repo_name or repo.name)
    source_commit = (args.source_commit or "").strip() or subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    ).stdout.strip()
    existing_index = load_index(output_root) if (output_root / "index.json").exists() else {"cases": [], "assets": [], "sources": []}
    existing_cases = [
        case for case in (existing_index.get("cases") or []) if (case.get("source_repo") or "") != repo_url
    ]
    existing_assets = [
        asset for asset in (existing_index.get("assets") or []) if (asset.get("source_repo") or "") != repo_url
    ]
    existing_sources = [source for source in normalize_sources(existing_index) if source.get("repo") != repo_url]

    mirrored_repo_root: Path | None = None
    if args.copy_source:
        mirrored_repo_root = output_root / "sources" / repo_slug / "repo"
        copy_repo_mirror(repo, mirrored_repo_root)

    markdown_files = sorted(path for path in repo.rglob("*.md") if ".git" not in path.parts)
    cases = []
    reference_map: dict[str, list[str]] = {}
    for index, markdown_path in enumerate(markdown_files, 1):
        case = build_markdown_case(
            repo_root=repo,
            markdown_path=markdown_path,
            output_root=output_root,
            repo_url=repo_url,
            source_commit=source_commit,
            repo_slug=repo_slug,
            mirrored_repo_root=mirrored_repo_root,
        )
        compact = build_compact_case(case)
        cases.append(compact)
        for asset in compact.get("linked_assets") or []:
            reference_map.setdefault(asset, []).append(compact["slug"])
        if args.progress and (index == 1 or index % args.progress == 0 or index == len(markdown_files)):
            print(f"[{index}/{len(markdown_files)}] parsed {compact['slug']}", flush=True)

    case_by_source_path = {case.get("source_path", ""): case for case in cases}
    case_category_by_slug = {case["slug"]: case["category"] for case in cases}
    asset_entries: list[dict[str, Any]] = []
    for file_path in sorted(path for path in repo.rglob("*") if path.is_file() and ".git" not in path.parts):
        rel_path = file_path.relative_to(repo)
        rel_path_key = str(rel_path).replace(os.sep, "/")
        local_path = ""
        if mirrored_repo_root is not None:
            local_path = str((mirrored_repo_root / rel_path).relative_to(output_root)).replace(os.sep, "/")
        case_slug = next((case["slug"] for case in cases if case.get("source_path") == rel_path_key), "")
        referenced_by = sorted(reference_map.get(rel_path_key, []))
        asset_category = ""
        if case_slug:
            asset_category = case_category_by_slug.get(case_slug, "")
        elif referenced_by:
            asset_category = case_category_by_slug.get(referenced_by[0], "")
        elif rel_path_key in case_by_source_path:
            asset_category = case_by_source_path[rel_path_key].get("category", "")
        if not asset_category:
            asset_category = map_markdown_repo_category(rel_path)
        asset_entries.append(
            {
                "source_repo": repo_url,
                "source_commit": source_commit,
                "relative_path": rel_path_key,
                "local_path": local_path,
                "kind": detect_asset_kind(file_path),
                "size": file_path.stat().st_size,
                "category": asset_category,
                "referenced_by": referenced_by,
                "source_url": build_github_blob_url(repo_url, source_commit, rel_path),
                "case_slug": case_slug,
            }
        )

    combined_cases = sorted(existing_cases + cases, key=lambda item: (item["title"].lower(), item["slug"]))
    combined_assets = existing_assets + asset_entries
    source_record = {
        "name": args.repo_name or "CUCCS/ctf-wps",
        "repo": repo_url,
        "commit": source_commit,
        "kind": "markdown-repo",
        "case_count": len(cases),
        "asset_count": len(asset_entries),
        "mirror": str((mirrored_repo_root or (output_root / "sources" / repo_slug / "repo")).relative_to(output_root)).replace(os.sep, "/")
        if args.copy_source
        else "",
    }
    index_data = build_index_data(
        combined_cases,
        sources=existing_sources + [source_record],
        asset_entries=combined_assets,
        source_note="Merged compact case cards with mirrored markdown repositories, their raw assets, and searchable inventory metadata.",
    )
    write_json(output_root / "index.json", index_data)
    write_overview(output_root, index_data)
    write_casebook_indexes(output_root, index_data)
    print(
        json.dumps(
            {
                "status": "ok",
                "output": str(output_root),
                "repo": repo_url,
                "source_commit": source_commit,
                "imported_cases": len(cases),
                "imported_assets": len(asset_entries),
                "total_cases": len(combined_cases),
                "root_index": str(output_root / "indexes" / "root.md"),
                "source_index": str(output_root / "indexes" / "sources" / "root.md"),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def command_browse(args: argparse.Namespace) -> None:
    root = Path(args.casebook).expanduser().resolve()
    index = load_index(root)
    cases = index.get("cases") or []
    categories = [name for name, _count in sorted_counts(Counter(case["category"] for case in cases))]
    category = resolve_choice(args.category, categories, "category")
    selected = filter_cases(cases, category=category)
    artifacts = [name for name, _count in sorted_counts(count_values(selected, "artifacts"))]
    artifact = resolve_choice(args.artifact, artifacts, "artifact") if category else None
    if artifact:
        selected = filter_cases(selected, artifact=artifact)
    techniques = [name for name, _count in sorted_counts(count_values(selected, "techniques"))]
    technique = resolve_choice(args.technique, techniques, "technique") if artifact else None
    if technique:
        selected = filter_cases(selected, technique=technique)
    route_types = [name for name, _count in sorted_counts(count_values(selected, "route_types"))]
    route_type = resolve_choice(args.route_type, route_types, "route type") if technique else None
    if route_type:
        selected = filter_cases(selected, route_type=route_type)
    tools = [name for name, _count in sorted_counts(count_values(selected, "tools"))]
    tool = resolve_choice(args.tool, tools, "tool") if args.tool else None
    if tool:
        selected = filter_cases(selected, tool=tool)

    payload: dict[str, Any] = {
        "path": {
            "category": category,
            "artifact": artifact,
            "technique": technique,
            "route_type": route_type,
            "tool": tool,
        },
        "case_count": len(selected),
        "next": {},
    }
    if not category:
        payload["next"]["categories"] = [{"name": name, "count": count} for name, count in sorted_counts(Counter(case["category"] for case in cases))]
    elif not artifact:
        payload["next"]["artifacts"] = [{"name": name, "count": count} for name, count in sorted_counts(count_values(selected, "artifacts"))]
    elif not technique:
        payload["next"]["techniques"] = [{"name": name, "count": count} for name, count in sorted_counts(count_values(selected, "techniques"))]
    elif not route_type:
        payload["next"]["route_types"] = [{"name": name, "count": count} for name, count in sorted_counts(count_values(selected, "route_types"))]

    if args.cards or route_type:
        payload["cards"] = [compact_case(root, case) for case in sorted(selected, key=lambda item: (item["title"].lower(), item["slug"]))[: args.limit]]
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    labels = [value for value in [category, artifact, technique, route_type, tool] if value]
    print("Path: " + (" -> ".join(labels) if labels else "root"))
    print(f"Cases: {len(selected)}")
    for key in ["categories", "artifacts", "techniques", "route_types"]:
        if key in payload["next"]:
            print(f"\nNext {key}:")
            for item in payload["next"][key]:
                print(f"- {item['name']} ({item['count']})")
    for case in payload.get("cards") or []:
        print(f"\n- {case['title']} [{case['category']} / {case['difficulty']}]")
        print(f"  slug: {case['slug']}")
        print(f"  card: {case['card_path']}")


def command_show(args: argparse.Namespace) -> None:
    root = Path(args.casebook).expanduser().resolve()
    index = load_index(root)
    by_slug = {case["slug"]: case for case in index["cases"]}
    if args.slug not in by_slug:
        raise SystemExit(f"unknown slug: {args.slug}")
    compact = by_slug[args.slug]
    card_path = root / compact.get("card", "")
    payload = {
        "slug": compact["slug"],
        "title": compact["title"],
        "category": compact["category"],
        "platform": compact.get("platform") or "",
        "difficulty": compact.get("difficulty") or "",
        "rating": compact.get("rating") or 0,
        "tags": compact.get("tags") or [],
        "method_summary": compact.get("method_summary") or [],
        "solve_thinking": compact.get("solve_thinking") or {},
        "reasoning_routes": (compact.get("reasoning_routes") or [])[: args.limit],
        "signals": compact.get("signals") or {},
        "source_repo": compact.get("source_repo") or "",
        "source_commit": compact.get("source_commit") or "",
        "source_path": compact.get("source_path") or "",
        "source_url": compact.get("source_url") or compact.get("source_pdf_url") or "",
        "linked_assets": compact.get("linked_assets") or [],
        "card_path": str(card_path),
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return
    if not card_path.exists():
        raise SystemExit(f"missing casebook card: {card_path}")
    print(card_path.read_text(encoding="utf-8", errors="replace"))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build and browse local CTF writeup casebooks")
    sub = parser.add_subparsers(dest="command", required=True)

    ingest = sub.add_parser("ingest-writeups", help="parse supported writeup PDFs into a compact local casebook")
    ingest.add_argument("--repo", required=True, help="path to a supported writeups clone with README.md and writeups/")
    ingest.add_argument("--source-commit", default="", help="upstream commit SHA when importing from an archive without .git metadata")
    ingest.add_argument("--output", default=str(DEFAULT_CASEBOOK_ROOT))
    ingest.add_argument("--progress", type=int, default=25)
    ingest.set_defaults(func=command_ingest_tim_barc)

    ingest_markdown = sub.add_parser(
        "ingest-markdown-repo",
        help="merge a markdown-heavy CTF repository into the local casebook and mirror its raw assets",
    )
    ingest_markdown.add_argument("--repo", required=True, help="path to a local markdown-heavy repository clone")
    ingest_markdown.add_argument("--repo-url", required=True, help="canonical upstream repository URL")
    ingest_markdown.add_argument("--repo-name", default="", help="display name for the imported source")
    ingest_markdown.add_argument("--source-commit", default="", help="upstream commit SHA when importing from an archive without .git metadata")
    ingest_markdown.add_argument("--output", default=str(DEFAULT_CASEBOOK_ROOT))
    ingest_markdown.add_argument("--progress", type=int, default=25)
    ingest_markdown.add_argument("--copy-source", action="store_true", help="mirror the repository working tree into casebook sources/")
    ingest_markdown.set_defaults(func=command_ingest_markdown_repo)

    reindex = sub.add_parser("reindex", help="rebuild deterministic multi-level casebook index documents")
    reindex.add_argument("--casebook", default=str(DEFAULT_CASEBOOK_ROOT))
    reindex.set_defaults(func=command_reindex)

    search = sub.add_parser("search", help="search compact cards and mirrored source assets by keyword")
    search.add_argument("--casebook", default=str(DEFAULT_CASEBOOK_ROOT))
    search.add_argument("--query", required=True)
    search.add_argument("--type", choices=["all", "case", "asset"], default="all")
    search.add_argument("--limit", type=int, default=20)
    search.add_argument("--json", action="store_true")
    search.set_defaults(func=command_search)

    browse = sub.add_parser("browse", help="browse the casebook by category, artifact, technique, route, and card")
    browse.add_argument("--casebook", default=str(DEFAULT_CASEBOOK_ROOT))
    browse.add_argument("--category")
    browse.add_argument("--artifact")
    browse.add_argument("--technique")
    browse.add_argument("--route-type")
    browse.add_argument("--tool")
    browse.add_argument("--cards", action="store_true", help="show matching cards at the current level")
    browse.add_argument("--limit", type=int, default=20)
    browse.add_argument("--json", action="store_true")
    browse.set_defaults(func=command_browse)

    show = sub.add_parser("show", help="show a structured case summary")
    show.add_argument("--casebook", default=str(DEFAULT_CASEBOOK_ROOT))
    show.add_argument("--slug", required=True)
    show.add_argument("--limit", type=int, default=20)
    show.add_argument("--json", action="store_true")
    show.set_defaults(func=command_show)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
