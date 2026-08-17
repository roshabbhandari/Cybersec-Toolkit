from core.list_utils import ListUtils

def test_unique_preserves_order():
    assert ListUtils.unique([2, 1, 2, 3, 1]) == [2, 1, 3]
