import threading
import time


class TimeoutSetter(threading.Thread):
    def __init__(self, state: dict, t: int):
        super().__init__()
        self.state = state
        self.time = t

    def run(self):
        flag = 0
        for i in range(self.time*10):
            time.sleep(0.1)
            if self.state["useless"]:
                flag = 1
                break
        if flag:
            self.state["timeout"] = True
