from core.list_text import ListText


def test_list_text():
    assert ListText.render(["a", " b ", ""]) == "a, b"
    assert ListText.render([]) == "none"
