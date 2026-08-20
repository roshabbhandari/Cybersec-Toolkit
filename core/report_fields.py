"""Normalize common report field names."""

ALIASES = {
    "ip": "ip_address",
    "ipaddr": "ip_address",
    "host": "hostname",
    "url": "url",
}

class ReportFields:
    @staticmethod
    def normalize(name: str) -> str:
        value = name.strip().lower().replace("-", "_").replace(" ", "_")
        return ALIASES.get(value, value)
