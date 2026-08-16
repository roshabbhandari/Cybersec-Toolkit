"""File integrity utilities based on SHA-256."""
import hashlib
from pathlib import Path


class FileIntegrity:
    @staticmethod
    def sha256(path: str, chunk_size: int = 1024 * 1024) -> str:
        file_path = Path(path)
        if not file_path.is_file():
            raise FileNotFoundError(f"File not found: {path}")
        digest = hashlib.sha256()
        with file_path.open("rb") as handle:
            while chunk := handle.read(chunk_size):
                digest.update(chunk)
        return digest.hexdigest()

    @staticmethod
    def verify(path: str, expected_sha256: str) -> bool:
        return FileIntegrity.sha256(path).lower() == expected_sha256.strip().lower()
