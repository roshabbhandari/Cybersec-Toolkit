from core.ascii_safe import ASCIISafe


def test_ascii_safe_replaces_unicode():
    assert ASCIISafe.normalize("Cafe\u00e9") == "Cafe?"
