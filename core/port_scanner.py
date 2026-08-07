import socket
import threading
from concurrent.futures import ThreadPoolExecutor

class PortScanner:
    def __init__(self, target, ports):
        self.target = target
        self.ports = ports
        self.open_ports = []
        self.lock = threading.Lock()

    def grab_banner(self, s):
        try:
            s.settimeout(2)
            banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
            return banner
        except:
            return ""

    def scan_port(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((self.target, port))
                if result == 0:
                    banner = self.grab_banner(s)
                    with self.lock:
                        self.open_ports.append((port, banner))
        except Exception:
            pass

    def run(self):
        with ThreadPoolExecutor(max_workers=50) as executor:
            executor.map(self.scan_port, self.ports)
        return sorted(self.open_ports, key=lambda x: x[0])
