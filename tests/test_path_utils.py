from core.path_utils import PathUtils

def test_expands_home():
    assert "~" not in PathUtils.normalize("~/report.json")
