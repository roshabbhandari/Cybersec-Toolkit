from core.boolean_text import BooleanText


def test_boolean_text():
    assert BooleanText.render(True) == "yes"
    assert BooleanText.render(False) == "no"
