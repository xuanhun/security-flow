from __future__ import annotations

import ssl
import urllib.error
import urllib.request
from urllib.parse import urlparse


SECURITY_HEADERS = [
    "content-security-policy",
    "strict-transport-security",
    "x-content-type-options",
    "x-frame-options",
    "referrer-policy",
    "permissions-policy",
]


def normalize_url(target: str) -> str:
    parsed = urlparse(target)
    if parsed.scheme:
        return target
    return f"https://{target}"


def fetch_baseline(url: str, timeout: int = 15) -> dict:
    url = normalize_url(url)
    request = urllib.request.Request(url, headers={"User-Agent": "kali-skill-baseline/1.0"})
    result = {"url": url, "ok": False}
    try:
        context = ssl.create_default_context()
        with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
            headers = {key.lower(): value for key, value in response.headers.items()}
            body = response.read(2048)
            result.update(
                {
                    "ok": True,
                    "status": response.status,
                    "final_url": response.url,
                    "headers": headers,
                    "missing_security_headers": [
                        header for header in SECURITY_HEADERS if header not in headers
                    ],
                    "sample_bytes": len(body),
                }
            )
    except urllib.error.HTTPError as exc:
        result.update({"ok": False, "status": exc.code, "error": str(exc)})
    except Exception as exc:  # noqa: BLE001 - keep CLI evidence explicit
        result.update({"ok": False, "error": f"{exc.__class__.__name__}: {exc}"})
    return result
