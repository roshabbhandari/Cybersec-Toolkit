from urllib.request import Request, urlopen
from urllib.parse import urlparse

class SecurityHeaders:
    REQUIRED = [
        "Content-Security-Policy",
        "Strict-Transport-Security",
        "X-Content-Type-Options",
        "X-Frame-Options",
        "Referrer-Policy",
        "Permissions-Policy",
    ]

    @classmethod
    def check(cls, url):
        if not urlparse(url).scheme:
            url = "https://" + url
        request = Request(url, headers={"User-Agent": "Cybersec-Toolkit/2.1"})
        try:
            with urlopen(request, timeout=8) as response:
                headers = {k.lower(): v for k, v in response.headers.items()}
                result = {}
                for header in cls.REQUIRED:
                    value = headers.get(header.lower())
                    result[header] = value if value else "MISSING"
                result["status"] = response.status
                result["final_url"] = response.geturl()
                return result
        except Exception as exc:
            return {"error": str(exc)}
