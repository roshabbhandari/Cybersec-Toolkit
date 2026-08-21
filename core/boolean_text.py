"""Normalize boolean values for human-readable reports."""

class BooleanText:
    @staticmethod
    def render(value: bool) -> str:
        if not isinstance(value, bool):
            raise TypeError("value must be boolean")
        return "yes" if value else "no"
