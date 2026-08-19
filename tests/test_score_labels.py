from core.score_labels import label_score


def test_score_labels_are_bounded():
    assert label_score(-10) == "critical"
    assert label_score(100) == "low"
