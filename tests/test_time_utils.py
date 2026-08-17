from core.time_utils import TimeUtils

def test_utc_iso_contains_timezone():
    assert TimeUtils.utc_iso().endswith("+00:00")
