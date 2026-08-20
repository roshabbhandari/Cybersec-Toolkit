from core.date_utils import DateUtils

def test_utc_iso_format():
    value = DateUtils.utc_iso()
    assert value.endswith("Z")
    assert "T" in value
