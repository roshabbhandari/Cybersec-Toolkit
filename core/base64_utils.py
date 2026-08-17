"""Strict Base64 helpers."""
import base64

class Base64Utils:
    @staticmethod
    def encode(text: str) -> str:
        return base64.b64encode(text.encode()).decode()

    @staticmethod
    def decode(value: str) -> str:
        return base64.b64decode(value.encode(), validate=True).decode()
