from core.safe_json import SafeJSON


def test_safe_json_keeps_unicode():
    assert "नेपाल" in SafeJSON.dumps({"name": "नेपाल"})
