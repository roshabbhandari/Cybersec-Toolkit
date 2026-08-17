"""Safe IP classification helpers."""
import ipaddress

class IPUtils:
    @staticmethod
    def classify(value: str) -> dict:
        address = ipaddress.ip_address(value.strip())
        return {
            "ip": str(address),
            "version": address.version,
            "private": address.is_private,
            "loopback": address.is_loopback,
            "multicast": address.is_multicast,
            "global": address.is_global,
        }
