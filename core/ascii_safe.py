"""ASCII-safe text normalization for terminal-oriented reports."""

class ASCIISafe:
    @staticmethod
    def normalize(value: str) -> str:
        if not isinstance(value, str):
            raise TypeError("value must be a string")
        return value.encode("ascii", "replace").decode("ascii")
