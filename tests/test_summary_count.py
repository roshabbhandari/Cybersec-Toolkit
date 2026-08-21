from core.summary_count import SummaryCount


def test_summary_count():
    items = [{"category": "high"}, {"category": "high"}, {"category": "low"}]
    assert SummaryCount.count(items) == {"high": 2, "low": 1}
