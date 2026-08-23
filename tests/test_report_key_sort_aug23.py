from core.report_key_sort import sort_report_keys


def test_sort_report_keys_case_insensitive():
    assert list(sort_report_keys({"z": 1, "A": 2, "b": 3})) == ["A", "b", "z"]
