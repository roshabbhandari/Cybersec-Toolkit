"""Deterministic collection helpers."""

class CollectionsSafe:
    @staticmethod
    def unique(values):
        seen = set()
        result = []
        for value in values:
            marker = repr(value)
            if marker not in seen:
                seen.add(marker)
                result.append(value)
        return result
