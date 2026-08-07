import base64
import urllib.parse
import codecs

class DataEncoder:
    @staticmethod
    def encode(data: str, fmt: str) -> str:
        data_bytes = data.encode('utf-8')
        try:
            if fmt == "base64":
                return base64.b64encode(data_bytes).decode('utf-8')
            elif fmt == "hex":
                return data_bytes.hex()
            elif fmt == "binary":
                return ' '.join(format(byte, '08b') for byte in data_bytes)
            elif fmt == "url":
                return urllib.parse.quote(data)
            elif fmt == "rot13":
                return codecs.encode(data, 'rot_13')
            else:
                return "Unsupported format"
        except Exception as e:
            return f"Encoding error: {str(e)}"

    @staticmethod
    def decode(data: str, fmt: str) -> str:
        try:
            if fmt == "base64":
                return base64.b64decode(data).decode('utf-8')
            elif fmt == "hex":
                return bytes.fromhex(data).decode('utf-8')
            elif fmt == "binary":
                bytes_list = [int(b, 2) for b in data.split()]
                return bytes(bytes_list).decode('utf-8')
            elif fmt == "url":
                return urllib.parse.unquote(data)
            elif fmt == "rot13":
                return codecs.decode(data, 'rot_13')
            else:
                return "Unsupported format"
        except Exception as e:
            return f"Decoding error: {str(e)}"
