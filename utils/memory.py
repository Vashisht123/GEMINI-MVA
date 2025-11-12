import json
from datetime import datetime

class Memory:
    def __init__(self):
        self.data = []

    def add(self, role, content):
        entry = {
            "time": datetime.now().strftime("%H:%M:%S"),
            "role": role,
            "content": content
        }
        self.data.append(entry)

    def last_n(self, n=5):
        return json.dumps(self.data[-n:], indent=2)

    def clear(self):
        self.data = []
