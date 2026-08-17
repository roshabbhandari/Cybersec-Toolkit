"""Filesystem safety helpers for local analysis."""
from pathlib import Path

class PathUtils:
    @staticmethod
    def normalize(path: str) -> str:
        return str(Path(path).expanduser().resolve())
