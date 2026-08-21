"""Produce stable labels for host-oriented reports."""

class HostLabel:
    @staticmethod
    def make(host: str) -> str:
        if not isinstance(host, str):
            raise TypeError("host must be a string")
        value = host.strip().lower().rstrip(".")
        return value or "unknown-host"
