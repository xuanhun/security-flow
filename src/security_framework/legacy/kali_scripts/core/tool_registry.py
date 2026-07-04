from __future__ import annotations

import platform
from dataclasses import dataclass
from pathlib import Path

from .runner import run_command, which


@dataclass(frozen=True)
class Tool:
    name: str
    binary: str
    apt: str
    module: str
    risk: str = "safe"


TOOLS: dict[str, Tool] = {
    "nmap": Tool("nmap", "nmap", "nmap", "information-gathering"),
    "masscan": Tool("masscan", "masscan", "masscan", "information-gathering", "medium"),
    "amass": Tool("amass", "amass", "amass", "information-gathering"),
    "dnsrecon": Tool("dnsrecon", "dnsrecon", "dnsrecon", "information-gathering"),
    "whois": Tool("whois", "whois", "whois", "information-gathering"),
    "whatweb": Tool("whatweb", "whatweb", "whatweb", "web-applications"),
    "nikto": Tool("nikto", "nikto", "nikto", "web-applications", "medium"),
    "gobuster": Tool("gobuster", "gobuster", "gobuster", "web-applications", "medium"),
    "ffuf": Tool("ffuf", "ffuf", "ffuf", "web-applications", "medium"),
    "sqlmap": Tool("sqlmap", "sqlmap", "sqlmap", "database-assessment", "high"),
    "lynis": Tool("lynis", "lynis", "lynis", "vulnerability-analysis"),
    "nuclei": Tool("nuclei", "nuclei", "nuclei", "vulnerability-analysis", "medium"),
    "searchsploit": Tool("searchsploit", "searchsploit", "exploitdb", "vulnerability-analysis"),
    "john": Tool("john", "john", "john", "password-audit", "medium"),
    "hashcat": Tool("hashcat", "hashcat", "hashcat", "password-audit", "medium"),
    "hydra": Tool("hydra", "hydra", "hydra", "password-audit", "high"),
    "aircrack-ng": Tool("aircrack-ng", "aircrack-ng", "aircrack-ng", "wireless", "high"),
    "burpsuite": Tool("burpsuite", "burpsuite", "burpsuite", "web-applications", "medium"),
    "metasploit": Tool("metasploit", "msfconsole", "metasploit-framework", "exploitation", "high"),
    "netexec": Tool("netexec", "nxc", "netexec", "information-gathering", "medium"),
    "responder": Tool("responder", "responder", "responder", "sniffing-spoofing", "high"),
    "wireshark": Tool("wireshark", "wireshark", "wireshark", "sniffing-spoofing", "high"),
    "tcpdump": Tool("tcpdump", "tcpdump", "tcpdump", "sniffing-spoofing", "high"),
    "binwalk": Tool("binwalk", "binwalk", "binwalk", "reverse-engineering"),
    "radare2": Tool("radare2", "radare2", "radare2", "reverse-engineering"),
    "gdb": Tool("gdb", "gdb", "gdb", "reverse-engineering"),
    "binutils": Tool("binutils", "objdump", "binutils", "reverse-engineering"),
    "checksec": Tool("checksec", "checksec", "checksec", "reverse-engineering"),
    "strace": Tool("strace", "strace", "strace", "reverse-engineering"),
    "ltrace": Tool("ltrace", "ltrace", "ltrace", "reverse-engineering"),
    "apktool": Tool("apktool", "apktool", "apktool", "mobile"),
    "jadx": Tool("jadx", "jadx", "jadx", "mobile"),
    "adb": Tool("adb", "adb", "android-tools-adb", "mobile"),
    "aapt": Tool("aapt", "aapt", "aapt", "mobile"),
    "qemu-system-x86": Tool("qemu-system-x86", "qemu-system-x86_64", "qemu-system-x86", "reverse-engineering"),
    "hashdeep": Tool("hashdeep", "hashdeep", "hashdeep", "forensics"),
    "exiftool": Tool("exiftool", "exiftool", "libimage-exiftool-perl", "forensics"),
    "foremost": Tool("foremost", "foremost", "foremost", "forensics"),
    "tshark": Tool("tshark", "tshark", "tshark", "forensics", "medium"),
    "ffmpeg": Tool("ffmpeg", "ffmpeg", "ffmpeg", "forensics"),
    "steghide": Tool("steghide", "steghide", "steghide", "forensics"),
    "sleuthkit": Tool("sleuthkit", "fls", "sleuthkit", "forensics"),
    "testdisk": Tool("testdisk", "testdisk", "testdisk", "forensics"),
    "pcapfix": Tool("pcapfix", "pcapfix", "pcapfix", "forensics"),
    "imagemagick": Tool("imagemagick", "convert", "imagemagick", "forensics"),
    "zbar-tools": Tool("zbar-tools", "zbarimg", "zbar-tools", "forensics"),
    "qrencode": Tool("qrencode", "qrencode", "qrencode", "forensics"),
    "sagemath": Tool("sagemath", "sage", "sagemath", "crypto"),
    "yara": Tool("yara", "yara", "yara", "malware"),
    "jq": Tool("jq", "jq", "jq", "reporting"),
    "curl": Tool("curl", "curl", "curl", "web-applications"),
}


PROFILES: dict[str, list[str]] = {
    "safe-core": ["nmap", "whois", "curl", "jq", "whatweb"],
    "information-gathering": ["nmap", "masscan", "amass", "dnsrecon", "whois", "whatweb"],
    "web": ["whatweb", "nikto", "gobuster", "ffuf", "sqlmap", "curl"],
    "vulnerability": ["nmap", "nikto", "nuclei", "lynis", "searchsploit"],
    "passwords": ["john", "hashcat"],
    "wireless": ["aircrack-ng"],
    "reverse-engineering": ["binwalk", "radare2"],
    "forensics": ["hashdeep", "binwalk"],
    "reporting": ["jq"],
    "ctf-web": ["whatweb", "gobuster", "ffuf", "sqlmap", "curl", "jq"],
    "ctf-crypto": ["sagemath", "hashcat", "john"],
    "ctf-forensics": [
        "hashdeep",
        "binwalk",
        "foremost",
        "exiftool",
        "tshark",
        "ffmpeg",
        "steghide",
        "sleuthkit",
        "testdisk",
        "pcapfix",
        "imagemagick",
        "zbar-tools",
        "qrencode",
    ],
    "ctf-reverse": [
        "gdb",
        "binutils",
        "radare2",
        "binwalk",
        "strace",
        "ltrace",
        "qemu-system-x86",
    ],
    "ctf-pwn": ["gdb", "checksec", "binutils", "strace", "ltrace"],
    "ctf-mobile": ["apktool", "jadx", "adb", "aapt", "radare2", "gdb"],
    "ctf-osint": ["whois", "dnsrecon", "nmap", "exiftool", "curl"],
    "ctf-malware": ["yara", "exiftool", "tshark", "binwalk", "strace", "ltrace", "gdb"],
    "top10-lab": ["aircrack-ng", "burpsuite", "hydra", "john", "metasploit", "netexec", "nmap", "responder", "sqlmap", "wireshark"],
}

KALI_METAPACKAGES: dict[str, str] = {
    "information-gathering": "kali-tools-information-gathering",
    "web": "kali-tools-web",
    "vulnerability": "kali-tools-vulnerability",
    "passwords": "kali-tools-passwords",
    "wireless": "kali-tools-wireless",
    "reverse-engineering": "kali-tools-reverse-engineering",
    "forensics": "kali-tools-forensics",
    "reporting": "kali-tools-reporting",
    "ctf-web": "kali-tools-web",
    "ctf-forensics": "kali-tools-forensics",
    "ctf-reverse": "kali-tools-reverse-engineering",
    "ctf-pwn": "kali-tools-exploitation",
    "ctf-mobile": "kali-tools-reverse-engineering",
    "ctf-osint": "kali-tools-information-gathering",
    "top10-lab": "kali-tools-top10",
}


def is_kali_linux() -> bool:
    os_release = Path("/etc/os-release")
    if not os_release.exists():
        return False
    text = os_release.read_text(encoding="utf-8", errors="ignore").lower()
    return "id=kali" in text or "id_like=kali" in text


def tool_status() -> list[dict]:
    return [
        {
            "name": tool.name,
            "binary": tool.binary,
            "installed": which(tool.binary) is not None,
            "path": which(tool.binary),
            "module": tool.module,
            "risk": tool.risk,
            "apt": tool.apt,
        }
        for tool in TOOLS.values()
    ]


def profile_packages(profile: str) -> list[str]:
    if profile not in PROFILES:
        raise SystemExit(f"unknown profile: {profile}")
    if is_kali_linux() and profile in KALI_METAPACKAGES:
        return [KALI_METAPACKAGES[profile]]
    return [TOOLS[name].apt for name in PROFILES[profile] if name in TOOLS]


def install_command(profile: str) -> list[str]:
    return ["sudo", "apt-get", "install", "-y", *profile_packages(profile)]


def install_profile(profile: str, project_dir: Path, execute: bool = False) -> dict:
    command = install_command(profile)
    if platform.system().lower() != "linux":
        return {
            "profile": profile,
            "execute": execute,
            "command": command,
            "status": "unsupported-platform",
            "message": "automatic apt installation is only supported on Linux",
        }
    if not execute:
        return {
            "profile": profile,
            "execute": False,
            "command": command,
            "status": "planned",
        }
    result = run_command(command, project_dir, timeout=1800)
    return {
        "profile": profile,
        "execute": True,
        "command": command,
        "status": "completed" if result["returncode"] == 0 else "failed",
        "returncode": result["returncode"],
    }
