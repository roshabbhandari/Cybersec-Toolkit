from core.score_labels import label_score


def test_score_labels_accept_numeric_strings():
    assert label_score("75") == "low"
