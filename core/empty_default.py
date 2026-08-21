"""Return caller-friendly defaults for optional report values."""

class EmptyDefault:
    @staticmethod
    def get(value, default="N/A"):
        if value is None or (isinstance(value, str) and not value.strip()):
            return default
        return value
