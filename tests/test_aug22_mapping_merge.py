from core.aug22_mapping_merge import merge_maps

def test_merge_maps():
    assert merge_maps({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}
