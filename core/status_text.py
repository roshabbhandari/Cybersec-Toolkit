"""Normalize basic finding status labels."""

class StatusText:
    ALLOWED = {"pass", "warn", "fail", "info"}

    @classmethod
    def normalize(cls, value: str) -> str:
        if not isinstance(value, str):
            raise TypeError("value must be a string")
        normalized = value.strip().lower()
        if normalized not in cls.ALLOWED:
            raise ValueError(f"unsupported status: {value}")
        return normalized
