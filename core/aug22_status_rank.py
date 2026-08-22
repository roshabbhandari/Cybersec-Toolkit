"""Rank common defensive finding states."""
ORDER = {"critical": 4, "high": 3, "medium": 2, "low": 1, "info": 0}

def rank_status(status: str) -> int:
    return ORDER.get(str(status).strip().lower(), -1)
