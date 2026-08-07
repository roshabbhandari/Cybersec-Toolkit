import jwt
import json

class JWTInspector:
    @staticmethod
    def inspect(token: str):
        results = {
            "header": None,
            "payload": None,
            "signature_valid": None,
            "error": None
        }
        try:
            header = jwt.get_unverified_header(token)
            payload = jwt.decode(token, options={"verify_signature": False})
            
            results["header"] = header
            results["payload"] = payload
            
            return results
        except jwt.PyJWTError as e:
            results["error"] = str(e)
            return results
        except Exception as e:
            results["error"] = f"Unexpected error: {str(e)}"
            return results
