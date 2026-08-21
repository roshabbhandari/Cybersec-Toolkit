"""Map numeric security scores into stable buckets."""

class ScoreBucket:
    @staticmethod
    def label(score: int) -> str:
        if not isinstance(score, (int, float)):
            raise TypeError("score must be numeric")
        score = max(0, min(100, score))
        if score < 40:
            return "low"
        if score < 70:
            return "medium"
        if score < 90:
            return "high"
        return "critical"
