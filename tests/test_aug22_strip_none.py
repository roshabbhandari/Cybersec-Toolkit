from core.aug22_strip_none import drop_none

def test_drop_none():
    assert drop_none({'a': 1, 'b': None}) == {'a': 1}
