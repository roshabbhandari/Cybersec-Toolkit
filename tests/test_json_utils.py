from core.json_utils import JSONUtils

def test_pretty_is_sorted():
    assert JSONUtils.pretty({"b": 1, "a": 2}).find('"a"') < JSONUtils.pretty({"b": 1, "a": 2}).find('"b"')
