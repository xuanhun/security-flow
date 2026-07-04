from __future__ import annotations

import socket
import ssl
from datetime import datetime, timezone


def inspect_tls(host: str, port: int = 443, timeout: int = 10) -> dict:
    result = {"host": host, "port": port, "ok": False}
    context = ssl.create_default_context()
    try:
        with socket.create_connection((host, port), timeout=timeout) as sock:
            with context.wrap_socket(sock, server_hostname=host) as wrapped:
                cert = wrapped.getpeercert()
                result.update(
                    {
                        "ok": True,
                        "version": wrapped.version(),
                        "cipher": wrapped.cipher(),
                        "subject": cert.get("subject", []),
                        "issuer": cert.get("issuer", []),
                        "not_before": cert.get("notBefore"),
                        "not_after": cert.get("notAfter"),
                    }
                )
                if cert.get("notAfter"):
                    expires = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")
                    expires = expires.replace(tzinfo=timezone.utc)
                    result["days_until_expiry"] = (expires - datetime.now(timezone.utc)).days
    except Exception as exc:  # noqa: BLE001 - CLI evidence should capture cause
        result.update({"error": f"{exc.__class__.__name__}: {exc}"})
    return result
