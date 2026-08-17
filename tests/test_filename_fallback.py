from core.filename_utils import FilenameUtils

def test_empty_filename_has_fallback():
    assert FilenameUtils.safe_name("...") == "report"
