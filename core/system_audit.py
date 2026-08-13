import os
import platform
import shutil
import socket
import stat

class SystemAudit:
    @staticmethod
    def collect():
        total, used, free = shutil.disk_usage(os.path.abspath(os.sep))
        return {
            "OS": platform.platform(),
            "Hostname": socket.gethostname(),
            "Architecture": platform.machine(),
            "Python": platform.python_version(),
            "Processor": platform.processor() or "Unknown",
            "Disk Total (GB)": round(total / (1024 ** 3), 2),
            "Disk Used (GB)": round(used / (1024 ** 3), 2),
            "Disk Free (GB)": round(free / (1024 ** 3), 2),
        }

    @staticmethod
    def file_permissions(path):
        if not os.path.isfile(path):
            return {"error": "File not found"}
        mode = os.stat(path).st_mode
        return {
            "path": os.path.abspath(path),
            "owner_read": bool(mode & stat.S_IRUSR),
            "owner_write": bool(mode & stat.S_IWUSR),
            "owner_execute": bool(mode & stat.S_IXUSR),
            "group_write": bool(mode & stat.S_IWGRP),
            "other_write": bool(mode & stat.S_IWOTH),
        }
