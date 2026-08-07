import socket
import ssl
import datetime

class SSLChecker:
    def __init__(self, hostname, port=443):
        self.hostname = hostname
        self.port = port

    def check(self):
        context = ssl.create_default_context()
        try:
            with socket.create_connection((self.hostname, self.port), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=self.hostname) as ssock:
                    cert = ssock.getpeercert()
                    
                    subject = dict(x[0] for x in cert['subject'])
                    issuer = dict(x[0] for x in cert['issuer'])
                    
                    not_before = datetime.datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z")
                    not_after = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
                    
                    days_left = (not_after - datetime.datetime.utcnow()).days
                    
                    cipher = ssock.cipher()
                    
                    return {
                        "subject": subject.get('commonName', 'Unknown'),
                        "issuer": issuer.get('organizationName', 'Unknown'),
                        "expires": not_after.strftime('%Y-%m-%d'),
                        "days_left": days_left,
                        "cipher": f"{cipher[0]} ({cipher[2]} bits)"
                    }
        except Exception as e:
            return {"error": str(e)}
