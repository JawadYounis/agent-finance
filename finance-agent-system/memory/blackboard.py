import threading
from datetime import datetime

class GlobalBlackboard:
    _instance = None
    _lock = threading.RLock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(GlobalBlackboard, cls).__new__(cls)
                cls._instance.data = {}
                cls._instance.logs = []
        return cls._instance

    def write(self, key, value):
        with self._lock:
            self.data[key] = value
            self.append_log(f"Write: {key} = {value}")

    def read(self, key, default=None):
        with self._lock:
            return self.data.get(key, default)

    def append_log(self, message):
        with self._lock:
            timestamp = datetime.now().isoformat()
            self.logs.append({
                "timestamp": timestamp,
                "message": message
            })

    def get_all(self):
        with self._lock:
            return {
                "data": self.data,
                "logs": self.logs
            }
