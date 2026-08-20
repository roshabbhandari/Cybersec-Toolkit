"""Basic hostname normalization helpers."""

class HostnameUtils:
    @staticmethod
    def normalize(hostname: str) -> str:
        if not isinstance(hostname, str):
            raise TypeError("hostname must be a string")
        return hostname.strip().rstrip(".").lower()
