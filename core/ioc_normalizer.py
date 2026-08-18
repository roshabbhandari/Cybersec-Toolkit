"""Normalize common indicators of compromise for comparison."""
from urllib.parse import urlsplit


class IOCNormalizer:
    @staticmethod
    def normalize_domain(value: str) -> str:
        value = value.strip().lower().rstrip(".")
        if "://" in value:
            value = urlsplit(value).hostname or value
        return value

    @staticmethod
    def normalize_hash(value: str) -> str:
        return value.strip().lower()

    @staticmethod
    def normalize_ip(value: str) -> str:
        return value.strip()
