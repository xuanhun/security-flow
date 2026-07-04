from __future__ import annotations

import socket
from concurrent.futures import ThreadPoolExecutor, as_completed


COMMON_PORTS = [21, 22, 25, 53, 80, 110, 135, 139, 143, 443, 445, 587, 993, 995, 1433, 1521, 3306, 3389, 5432, 5900, 6379, 8080, 8443, 9200]


def parse_ports(value: str | None) -> list[int]:
    if not value:
        return COMMON_PORTS
    ports: set[int] = set()
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start, end = [int(item) for item in part.split("-", 1)]
            ports.update(range(start, end + 1))
        else:
            ports.add(int(part))
    return sorted(port for port in ports if 1 <= port <= 65535)


def scan_port(host: str, port: int, timeout: float = 1.5) -> dict:
    result = {"host": host, "port": port, "open": False, "banner": ""}
    try:
        with socket.create_connection((host, port), timeout=timeout) as sock:
            result["open"] = True
            sock.settimeout(0.8)
            try:
                sock.sendall(b"\r\n")
                banner = sock.recv(128)
                result["banner"] = banner.decode("utf-8", errors="replace").strip()
            except OSError:
                pass
    except OSError as exc:
        result["error"] = exc.__class__.__name__
    return result


def tcp_scan(host: str, ports: list[int], concurrency: int = 8, timeout: float = 1.5) -> list[dict]:
    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=max(1, concurrency)) as executor:
        futures = [executor.submit(scan_port, host, port, timeout) for port in ports]
        for future in as_completed(futures):
            results.append(future.result())
    return sorted(results, key=lambda item: item["port"])
