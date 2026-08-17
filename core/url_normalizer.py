"""Normalize URLs for consistent defensive reporting."""
from urllib.parse import urlsplit, urlunsplit

class URLNormalizer:
    @staticmethod
    def normalize(url: str) -> str:
        value = url.strip()
        if "://" not in value:
            value = "https://" + value
        parts = urlsplit(value)
        scheme = parts.scheme.lower()
        host = (parts.hostname or "").lower()
        port = parts.port
        netloc = host
        if port and not ((scheme == "http" and port == 80) or (scheme == "https" and port == 443)):
            netloc = f"{host}:{port}"
        return urlunsplit((scheme, netloc, parts.path or "/", parts.query, ""))
