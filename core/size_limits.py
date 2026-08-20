"""Simple bounds helpers for user-controlled values."""

class SizeLimits:
    @staticmethod
    def clamp(value: int, minimum: int, maximum: int) -> int:
        if minimum > maximum:
            raise ValueError("minimum cannot exceed maximum")
        return max(minimum, min(value, maximum))
