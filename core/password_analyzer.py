import math
import re

class PasswordAnalyzer:
    def __init__(self, password):
        self.password = password

    def calculate_entropy(self):
        if not self.password:
            return 0
        pool_size = 0
        if re.search(r'[a-z]', self.password): pool_size += 26
        if re.search(r'[A-Z]', self.password): pool_size += 26
        if re.search(r'[0-9]', self.password): pool_size += 10
        if re.search(r'[^a-zA-Z0-9]', self.password): pool_size += 32
        
        if pool_size == 0:
            return 0
        
        entropy = len(self.password) * math.log2(pool_size)
        return round(entropy, 2)

    def check_heuristics(self):
        warnings = []
        if len(self.password) < 8:
            warnings.append("Password is too short (less than 8 characters).")
        if re.search(r'(.)\1{2,}', self.password):
            warnings.append("Contains repeated characters (e.g., 'aaa').")
        if re.search(r'123|abc|qwerty|password', self.password.lower()):
            warnings.append("Contains common predictable patterns.")
        
        # Sequential numbers
        for i in range(len(self.password) - 2):
            if self.password[i:i+3].isdigit():
                if int(self.password[i+1]) == int(self.password[i]) + 1 and int(self.password[i+2]) == int(self.password[i]) + 2:
                    warnings.append("Contains sequential numbers.")
                    break
                    
        return warnings

    def analyze(self):
        entropy = self.calculate_entropy()
        warnings = self.check_heuristics()
        
        if entropy < 28:
            strength = "Very Weak"
        elif entropy < 36:
            strength = "Weak"
        elif entropy < 60:
            strength = "Reasonable"
        elif entropy < 128:
            strength = "Strong"
        else:
            strength = "Very Strong"
            
        return {
            "entropy": entropy,
            "strength": strength,
            "warnings": warnings
        }
