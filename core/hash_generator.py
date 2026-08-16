"""Convenience hash generation for text and files."""
import hashlib
from pathlib import Path


class HashGenerator:
    ALGORITHMS = {"md5", "sha1", "sha256", "sha512"}

    @staticmethod
    def text(value: str, algorithm: str = "sha256") -> str:
        algorithm = algorithm.lower()
        if algorithm not in HashGenerator.ALGORITHMS:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
        return hashlib.new(algorithm, value.encode("utf-8")).hexdigest()

    @staticmethod
    def file(path: str, algorithm: str = "sha256") -> str:
        algorithm = algorithm.lower()
        if algorithm not in HashGenerator.ALGORITHMS:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
        digest = hashlib.new(algorithm)
        with Path(path).open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()
