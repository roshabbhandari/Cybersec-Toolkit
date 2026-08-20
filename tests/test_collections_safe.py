from core.collections_safe import CollectionsSafe

def test_unique_preserves_order():
    assert CollectionsSafe.unique(["a", "b", "a", "c"]) == ["a", "b", "c"]
