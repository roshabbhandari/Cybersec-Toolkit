import os
from cryptography.hazmat.primitives.asymmetric import rsa, ed25519
from cryptography.hazmat.primitives import serialization

class SSHKeyGenerator:
    @staticmethod
    def generate_rsa(key_size: int = 4096, output_dir: str = "."):
        try:
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=key_size,
            )
            return SSHKeyGenerator._save_keys(private_key, "id_rsa", output_dir)
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def generate_ed25519(output_dir: str = "."):
        try:
            private_key = ed25519.Ed25519PrivateKey.generate()
            return SSHKeyGenerator._save_keys(private_key, "id_ed25519", output_dir)
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def _save_keys(private_key, filename: str, output_dir: str):
        os.makedirs(output_dir, exist_ok=True)
        priv_path = os.path.join(output_dir, filename)
        pub_path = priv_path + ".pub"

        priv_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.OpenSSH,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(priv_path, "wb") as f:
            f.write(priv_bytes)
            
        pub_bytes = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH
        )
        with open(pub_path, "wb") as f:
            f.write(pub_bytes)

        return {"private_key": priv_path, "public_key": pub_path}
