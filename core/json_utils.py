"""Consistent JSON serialization helpers."""
import json

class JSONUtils:
    @staticmethod
    def pretty(value) -> str:
        return json.dumps(value, indent=2, sort_keys=True, default=str)
