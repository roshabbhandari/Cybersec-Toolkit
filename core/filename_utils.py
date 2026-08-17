"""Filename validation for generated reports."""
import re

class FilenameUtils:
    @staticmethod
    def safe_name(name: str) -> str:
        cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", name.strip())
        return cleaned.strip(".") or "report"
