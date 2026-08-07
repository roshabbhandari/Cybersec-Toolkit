import hashlib
import os

class HashToolkit:
    @staticmethod
    def hash_string(text, algo='sha256'):
        try:
            h = hashlib.new(algo)
            h.update(text.encode('utf-8'))
            return h.hexdigest()
        except ValueError:
            return None

    @staticmethod
    def hash_file(file_path, algo='sha256'):
        if not os.path.exists(file_path):
            return None
        try:
            h = hashlib.new(algo)
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    h.update(chunk)
            return h.hexdigest()
        except ValueError:
            return None
            
    @staticmethod
    def identify_hash(hash_val):
        hash_len = len(hash_val)
        if not all(c in '0123456789abcdefABCDEF' for c in hash_val):
            return "Invalid hexadecimal hash"
            
        if hash_len == 32:
            return "MD5 (or similar 128-bit hash)"
        elif hash_len == 40:
            return "SHA-1 (or similar 160-bit hash)"
        elif hash_len == 64:
            return "SHA-256 (or similar 256-bit hash)"
        elif hash_len == 128:
            return "SHA-512 (or similar 512-bit hash)"
        else:
            return "Unknown hash format based on length"
