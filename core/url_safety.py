"""Passive URL safety inspection. No network requests are made."""
from urllib.parse import urlparse


class URLSafety:
    SUSPICIOUS_TLDS = {".zip", ".mov", ".click", ".country", ".gq", ".tk"}

    @staticmethod
    def inspect(url: str) -> dict:
        value = url.strip()
        parsed = urlparse(value if "://" in value else f"https://{value}")
        host = (parsed.hostname or "").lower()
        flags = []
        if parsed.scheme not in {"http", "https"}:
            flags.append("non-http scheme")
        if "@" in parsed.netloc:
            flags.append("userinfo in URL")
        if host.startswith("xn--") or ".xn--" in host:
            flags.append("punycode hostname")
        if any(host.endswith(tld) for tld in URLSafety.SUSPICIOUS_TLDS):
            flags.append("uncommon file-like/suspicious TLD")
        if len(url) > 180:
            flags.append("unusually long URL")
        return {
            "normalized_url": parsed.geturl(),
            "hostname": host,
            "scheme": parsed.scheme,
            "suspicious": bool(flags),
            "flags": flags,
        }
