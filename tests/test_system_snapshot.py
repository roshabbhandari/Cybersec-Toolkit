from core.system_snapshot import SystemSnapshot

def test_snapshot_has_platform():
    result = SystemSnapshot.collect()
    assert result.get("platform")
