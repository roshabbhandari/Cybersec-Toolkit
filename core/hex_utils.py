"""Hex encoding validation helpers."""
import re

class HexUtils:
    @staticmethod
    def is_hex(value: str) -> bool:
        return bool(re.fullmatch(r"[0-9a-fA-F]+", value.strip())) and len(value.strip()) % 2 == 0
