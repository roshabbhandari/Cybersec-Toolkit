import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

class FileCrypto:
    def __init__(self, password):
        self.password = password.encode()
        self.salt_size = 16

    def _generate_key(self, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.password))
        return key

    def encrypt_file(self, file_path, output_path=None):
        if not output_path:
            output_path = file_path + ".enc"
            
        salt = os.urandom(self.salt_size)
        key = self._generate_key(salt)
        f = Fernet(key)
        
        with open(file_path, "rb") as file:
            file_data = file.read()
            
        encrypted_data = f.encrypt(file_data)
        
        with open(output_path, "wb") as file:
            file.write(salt + encrypted_data)
            
        return output_path

    def decrypt_file(self, file_path, output_path=None):
        if not output_path:
            if file_path.endswith(".enc"):
                output_path = file_path[:-4]
            else:
                output_path = file_path + ".dec"

        with open(file_path, "rb") as file:
            salt = file.read(self.salt_size)
            encrypted_data = file.read()
            
        key = self._generate_key(salt)
        f = Fernet(key)
        
        try:
            decrypted_data = f.decrypt(encrypted_data)
        except Exception as e:
            raise ValueError("Invalid password or corrupted file.")
            
        with open(output_path, "wb") as file:
            file.write(decrypted_data)
            
        return output_path
