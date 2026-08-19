from core.safe_json import SafeJSON


def test_safe_json_handles_primitives():
    assert SafeJSON.dumps(True) == "true"
    assert SafeJSON.dumps(None) == "null"
