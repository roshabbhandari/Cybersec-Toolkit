"""Bound text collections to safe report sizes."""

class LineLimit:
    @staticmethod
    def clamp(lines: list[str], maximum: int) -> list[str]:
        if not isinstance(maximum, int) or maximum < 0:
            raise ValueError("maximum must be a non-negative integer")
        return list(lines[:maximum])
