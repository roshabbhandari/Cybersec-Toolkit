from core.filename_utils import FilenameUtils

def test_sanitizes_filename():
    assert FilenameUtils.safe_name("my report!.json") == "my_report_.json"
