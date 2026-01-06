# kernel/process.py

class Process:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name
        self.state = "READY"

    def to_dict(self):
        return {
            "pid": self.pid,
            "name": self.name,
            "state": self.state
        }
