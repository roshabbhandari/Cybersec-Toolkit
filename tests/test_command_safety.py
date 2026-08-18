from core.command_safety import is_safe_command_name


def test_safe_command_name():
    assert is_safe_command_name("pytest") is True
    assert is_safe_command_name("tool-1.0") is True


def test_unsafe_command_name():
    assert is_safe_command_name("rm -rf") is False
    assert is_safe_command_name(123) is False
