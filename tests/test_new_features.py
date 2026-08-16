from core.file_integrity import FileIntegrity
from core.hash_generator import HashGenerator
from core.password_strength import PasswordStrength
from core.url_safety import URLSafety


def test_hash_generator():
    assert HashGenerator.text("hello", "sha256")


def test_password_strength():
    result = PasswordStrength.analyze("StrongPass!123")
    assert result["score"] > 0
    assert result["entropy_bits"] > 0


def test_url_safety():
    result = URLSafety.inspect("https://example.com")
    assert result["hostname"] == "example.com"
    assert result["suspicious"] is False


def test_file_integrity(tmp_path):
    target = tmp_path / "sample.txt"
    target.write_text("hello", encoding="utf-8")
    digest = FileIntegrity.sha256(str(target))
    assert FileIntegrity.verify(str(target), digest)
