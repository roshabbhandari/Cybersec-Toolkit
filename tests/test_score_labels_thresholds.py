from core.score_labels import label_score


def test_score_thresholds():
    assert label_score(24.99) == "critical"
    assert label_score(25) == "high"
    assert label_score(49.99) == "high"
    assert label_score(50) == "medium"
    assert label_score(74.99) == "medium"
    assert label_score(75) == "low"
