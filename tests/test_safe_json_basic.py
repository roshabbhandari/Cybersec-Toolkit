from core.safe_json import SafeJSON


def test_safe_json_is_sorted():
    assert SafeJSON.dumps({"b": 1, "a": 2}).find('"a"') < SafeJSON.dumps({"b": 1, "a": 2}).find('"b"')
