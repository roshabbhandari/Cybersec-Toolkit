"""Common labels for bounded security scores."""


def label_score(score: float) -> str:
    value = max(0.0, min(100.0, float(score)))
    if value < 25:
        return "critical"
    if value < 50:
        return "high"
    if value < 75:
        return "medium"
    return "low"
