"""Safely preview token-like text without exposing all content."""

class TokenPreview:
    @staticmethod
    def preview(value: str, visible: int = 4) -> str:
        if not isinstance(value, str):
            raise TypeError("value must be a string")
        if visible < 0:
            raise ValueError("visible must be non-negative")
        if len(value) <= visible:
            return "*" * len(value)
        return value[:visible] + "..."
