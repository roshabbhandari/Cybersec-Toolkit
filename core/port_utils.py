"""Defensive helpers for validating TCP port values."""

class PortUtils:
    @staticmethod
    def validate(port: int) -> int:
        if not isinstance(port, int) or isinstance(port, bool):
            raise TypeError("port must be an integer")
        if not 1 <= port <= 65535:
            raise ValueError("port must be between 1 and 65535")
        return port
