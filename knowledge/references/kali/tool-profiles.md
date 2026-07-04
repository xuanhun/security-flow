# Tool Profiles

`scripts/kali.py install-tools` prints an install plan by default. Add
`--execute` only after user approval.

## Profiles

- `safe-core`: `nmap`, `whois`, `curl`, `jq`, `whatweb`.
- `information-gathering`: `nmap`, `masscan`, `amass`, `dnsrecon`, `whois`,
  `whatweb`.
- `web`: `whatweb`, `nikto`, `gobuster`, `ffuf`, `sqlmap`, `curl`.
- `vulnerability`: `nmap`, `nikto`, `nuclei`, `lynis`, `exploitdb`.
- `passwords`: `john`, `hashcat`.
- `wireless`: `aircrack-ng`.
- `reverse-engineering`: `binwalk`, `radare2`.
- `forensics`: `hashdeep`, `binwalk`.
- `reporting`: `jq`.
- `ctf-web`: `whatweb`, `gobuster`, `ffuf`, `sqlmap`, `curl`, `jq`.
- `ctf-crypto`: `sagemath`, `hashcat`, `john`, `go`.
- `ctf-forensics`: `hashdeep`, `binwalk`, `foremost`, `exiftool`, `tshark`,
  `ffmpeg`, `steghide`, `sleuthkit`, `testdisk`, `pcapfix`, `imagemagick`,
  `zbar-tools`, `qrencode`.
- `ctf-reverse`: `gdb`, `binutils`, `radare2`, `binwalk`, `strace`, `ltrace`,
  `qemu-system-x86`.
- `ctf-pwn`: `gdb`, `checksec`, `binutils`, `strace`, `ltrace`.
- `ctf-mobile`: `apktool`, `jadx`, `adb`, `aapt`, `radare2`, `gdb`.
- `ctf-osint`: `whois`, `dnsrecon`, `nmap`, `exiftool`, `curl`.
- `ctf-malware`: `yara`, `exiftool`, `tshark`, `binwalk`, `strace`, `ltrace`,
  `gdb`.
- `top10-lab`: Kali top tools such as aircrack-ng, burpsuite, hydra, john,
  metasploit, netexec, nmap, responder, sqlmap, and wireshark.

## Kali Hosts

On Kali Linux, selected profiles may use Kali metapackages such as
`kali-tools-information-gathering`, `kali-tools-vulnerability`,
`kali-tools-web`, `kali-tools-passwords`, `kali-tools-wireless`,
`kali-tools-reverse-engineering`, `kali-tools-forensics`,
`kali-tools-reporting`, `kali-tools-web`, `kali-tools-exploitation`,
`kali-tools-information-gathering`, and `kali-tools-top10`.

CTF profiles may map to Kali metapackages on Kali hosts and to individual apt
packages on Debian/Ubuntu hosts.

## Debian Or Ubuntu Hosts

Do not add Kali apt repositories to a non-Kali system. Use the host package
manager packages that are already available, or install project-specific tools
manually after reviewing their upstream instructions.

## Tool Invocation Policy

- Missing tools should degrade to Python checks when possible.
- Go can be installed as a skill-local runtime under
  `~/.cache/kali-skill/go-runtime/go/bin/go` when system packages are
  unavailable.
- Tool commands must be recorded in `commands.jsonl`.
- Heavy tools need human confirmation or a written scope note.
- High-risk tools may be installed but should not run automatically.
