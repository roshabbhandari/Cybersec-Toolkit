from core.report_null_cleanup import drop_none_fields
from core.report_bool_normalizer import normalize_bool


def test_drop_none_fields():
    assert drop_none_fields({"a": 1, "b": None}) == {"a": 1}


def test_normalize_bool():
    assert normalize_bool("YES") is True
    assert normalize_bool("no") is False
