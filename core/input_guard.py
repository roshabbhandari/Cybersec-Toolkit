"""Small validation helpers for defensive CLI inputs."""

class InputGuard:
    @staticmethod
    def non_empty(value: str, field: str = "value") -> str:
        value = value.strip()
        if not value:
            raise ValueError(f"{field} cannot be empty")
        return value

    @staticmethod
    def bounded_int(value: int, minimum: int, maximum: int) -> int:
        value = int(value)
        if not minimum <= value <= maximum:
            raise ValueError(f"value must be between {minimum} and {maximum}")
        return value
