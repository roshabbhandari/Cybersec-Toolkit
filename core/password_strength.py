"""Password strength scoring helpers."""
import math
import string


class PasswordStrength:
    @staticmethod
    def analyze(password: str) -> dict:
        if not isinstance(password, str):
            raise TypeError("password must be a string")
        length = len(password)
        pool = 0
        if any(c.islower() for c in password):
            pool += 26
        if any(c.isupper() for c in password):
            pool += 26
        if any(c.isdigit() for c in password):
            pool += 10
        if any(c in string.punctuation for c in password):
            pool += len(string.punctuation)
        entropy = round(length * math.log2(pool), 2) if pool else 0.0
        score = 0
        score += min(length, 12) * 4
        score += 10 if any(c.islower() for c in password) else 0
        score += 10 if any(c.isupper() for c in password) else 0
        score += 10 if any(c.isdigit() for c in password) else 0
        score += 15 if any(c in string.punctuation for c in password) else 0
        score = min(score, 100)
        label = "Weak" if score < 40 else "Fair" if score < 65 else "Strong" if score < 85 else "Excellent"
        return {"length": length, "entropy_bits": entropy, "score": score, "strength": label}
