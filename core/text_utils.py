"""Text helpers used by reports and log analysis."""


def normalize_lines(text: str) -> list[str]:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return [line.strip() for line in text.splitlines() if line.strip()]
