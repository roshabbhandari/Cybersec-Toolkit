from core.password_strength import PasswordStrength

def test_empty_password_has_zero_entropy():
    result = PasswordStrength.analyze("")
    assert result["entropy_bits"] == 0.0

def test_long_password_score_is_capped():
    result = PasswordStrength.analyze("A" * 100)
    assert result["score"] <= 100
