import re
from collections import defaultdict

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.failed_logins = defaultdict(int)

    def analyze(self):
        try:
            with open(self.log_file, 'r', encoding='utf-8', errors='ignore') as file:
                for line in file:
                    match = re.search(r'Failed password for .* from (\d+\.\d+\.\d+\.\d+)', line)
                    if match:
                        ip = match.group(1)
                        self.failed_logins[ip] += 1
            
            results = sorted(self.failed_logins.items(), key=lambda x: x[1], reverse=True)
            return results
        except FileNotFoundError:
            return None
        except Exception as e:
            return str(e)
