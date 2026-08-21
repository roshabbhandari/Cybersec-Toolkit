"""Create compact display paths for reports."""
from pathlib import Path

class PathDisplay:
    @staticmethod
    def compact(path: str, maximum: int = 80) -> str:
        if not isinstance(path, str):
            raise TypeError("path must be a string")
        if maximum < 8:
            raise ValueError("maximum must be at least 8")
        value = str(Path(path))
        if len(value) <= maximum:
            return value
        return "..." + value[-(maximum - 3):]
