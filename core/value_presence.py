"""Check whether a report value is meaningfully present."""

class ValuePresence:
    @staticmethod
    def is_present(value) -> bool:
        if value is None:
            return False
        if isinstance(value, str):
            return bool(value.strip())
        return True
