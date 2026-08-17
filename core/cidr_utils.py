"""CIDR membership helpers for defensive network analysis."""
import ipaddress

class CIDRUtils:
    @staticmethod
    def contains(network: str, address: str) -> bool:
        return ipaddress.ip_address(address.strip()) in ipaddress.ip_network(network.strip(), strict=False)
