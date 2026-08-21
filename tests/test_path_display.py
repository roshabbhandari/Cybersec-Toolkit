from core.path_display import PathDisplay


def test_path_display():
    assert PathDisplay.compact("/very/long/path/to/a/report.txt", 20).startswith("...")
