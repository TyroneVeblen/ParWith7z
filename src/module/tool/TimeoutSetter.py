import threading
import time


class TimeoutSetter(threading.Thread):
    def __init__(self, state: dict, t: int):
        super().__init__()
        self.state = state
        self.time = t

    def run(self):
        time.sleep(self.time)
        self.state["timeout"] = True
