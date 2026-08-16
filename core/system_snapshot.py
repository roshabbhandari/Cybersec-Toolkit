"""Read-only local system security snapshot."""
import platform
import socket
import sys


class SystemSnapshot:
    @staticmethod
    def collect() -> dict:
        return {
            "hostname": socket.gethostname(),
            "platform": platform.platform(),
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "python": sys.version.split()[0],
        }
