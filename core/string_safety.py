"""Small helpers for safe string handling."""

class StringSafety:
    @staticmethod
    def normalize(value: str) -> str:
        if not isinstance(value, str):
            raise TypeError("value must be a string")
        return " ".join(value.strip().split())
