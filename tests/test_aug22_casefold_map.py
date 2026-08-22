from core.aug22_casefold_map import get_casefold

def test_get_casefold():
    assert get_casefold({'Host': 'example.com'}, 'host') == 'example.com'
    assert get_casefold({}, 'missing', 'fallback') == 'fallback'
