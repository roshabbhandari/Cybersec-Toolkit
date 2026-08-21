from core.field_order import FieldOrder


def test_field_order():
    assert list(FieldOrder.apply({"b": 2, "a": 1}, ["a"])) == ["a", "b"]
