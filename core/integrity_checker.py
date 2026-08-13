import hashlib
import os

class IntegrityChecker:
    @staticmethod
    def sha256(path):
        if not os.path.isfile(path):
            return {"error": "File not found"}
        digest = hashlib.sha256()
        with open(path, "rb") as file:
            for chunk in iter(lambda: file.read(1024 * 1024), b""):
                digest.update(chunk)
        return {"path": os.path.abspath(path), "sha256": digest.hexdigest(), "size": os.path.getsize(path)}
