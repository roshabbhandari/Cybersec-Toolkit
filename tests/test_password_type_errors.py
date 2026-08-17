import pytest
from core.password_strength import PasswordStrength

def test_password_strength_rejects_non_string():
    with pytest.raises(TypeError):
        PasswordStrength.analyze(None)
