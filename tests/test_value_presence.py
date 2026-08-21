from core.value_presence import ValuePresence


def test_value_presence():
    assert not ValuePresence.is_present(None)
    assert not ValuePresence.is_present("  ")
    assert ValuePresence.is_present("ok")
    assert ValuePresence.is_present(0)
