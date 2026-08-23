from core.report_join import join_lines


def test_join_lines():
    assert join_lines([" one ", "", "two"]) == "one\ntwo"
