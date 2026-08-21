from core.score_bucket import ScoreBucket


def test_score_bucket_boundaries():
    assert ScoreBucket.label(-1) == "low"
    assert ScoreBucket.label(50) == "medium"
    assert ScoreBucket.label(80) == "high"
    assert ScoreBucket.label(95) == "critical"
