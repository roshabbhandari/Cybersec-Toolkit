"""Decode JWT header/payload locally without verification."""
import base64
import json


def _decode_part(part: str) -> dict:
    padding = "=" * (-len(part) % 4)
    raw = base64.urlsafe_b64decode(part + padding)
    return json.loads(raw.decode("utf-8"))


class JWTDecoder:
    @staticmethod
    def decode(token: str) -> dict:
        parts = token.strip().split(".")
        if len(parts) != 3:
            raise ValueError("Invalid JWT format")
        return {"header": _decode_part(parts[0]), "payload": _decode_part(parts[1]), "signature_present": bool(parts[2])}
