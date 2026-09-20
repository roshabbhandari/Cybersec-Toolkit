from core.list_text import ListText


def test_render_skips_whitespace_only_values():
    assert ListText.render(['  ', '\t', 'dns']) == 'dns'
