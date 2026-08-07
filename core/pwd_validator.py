import re

class PasswordValidator:
    @staticmethod
    def validate(password: str, min_length: int = 12):
        results = {
            "is_valid": False,
            "length_ok": len(password) >= min_length,
            "has_upper": bool(re.search(r'[A-Z]', password)),
            "has_lower": bool(re.search(r'[a-z]', password)),
            "has_digit": bool(re.search(r'\d', password)),
            "has_special": bool(re.search(r'[^a-zA-Z\d]', password)),
            "issues": []
        }
        
        if not results["length_ok"]:
            results["issues"].append(f"Password must be at least {min_length} characters long.")
        if not results["has_upper"]:
            results["issues"].append("Password must contain at least one uppercase letter.")
        if not results["has_lower"]:
            results["issues"].append("Password must contain at least one lowercase letter.")
        if not results["has_digit"]:
            results["issues"].append("Password must contain at least one number.")
        if not results["has_special"]:
            results["issues"].append("Password must contain at least one special character.")
            
        if not results["issues"]:
            results["is_valid"] = True
            
        return results
