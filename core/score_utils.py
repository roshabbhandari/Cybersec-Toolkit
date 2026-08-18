"""Small helpers for bounded security scores."""


def clamp_score(value: int | float, minimum: int = 0, maximum: int = 100) -> int:
    if minimum > maximum:
        raise ValueError("minimum cannot exceed maximum")
    return int(max(minimum, min(maximum, value)))
