"""Count findings by simple category."""

class SummaryCount:
    @staticmethod
    def count(items: list[dict], field: str = "category") -> dict:
        result = {}
        for item in items:
            key = item.get(field, "uncategorized")
            result[key] = result.get(key, 0) + 1
        return result
