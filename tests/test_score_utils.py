import pytest

from core.score_utils import clamp_score


def test_clamp_score_bounds():
    assert clamp_score(-5) == 0
    assert clamp_score(50) == 50
    assert clamp_score(500) == 100


def test_invalid_bounds():
    with pytest.raises(ValueError):
        clamp_score(10, 100, 0)
