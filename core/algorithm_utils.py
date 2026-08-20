"""Validate supported hashing algorithms."""

SUPPORTED_HASHES = ("md5", "sha1", "sha256", "sha512")

class AlgorithmUtils:
    @staticmethod
    def normalize_hash(name: str) -> str:
        value = name.strip().lower()
        if value not in SUPPORTED_HASHES:
            raise ValueError("unsupported hash algorithm")
        return value
