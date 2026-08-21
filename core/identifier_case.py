"""Normalize report identifiers without changing their meaning."""

class IdentifierCase:
    @staticmethod
    def normalize(value: str) -> str:
        if not isinstance(value, str):
            raise TypeError("value must be a string")
        return value.strip().casefold()
