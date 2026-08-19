"""Deterministic JSON serialization for security reports."""
import json


class SafeJSON:
    @staticmethod
    def dumps(value) -> str:
        return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False)
