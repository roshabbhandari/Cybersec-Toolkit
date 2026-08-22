from core.aug22_key_filter import select_keys


def test_select_keys():
    data = {"a": 1, "b": 2}
    assert select_keys(data, ["b"]) == {"b": 2}
