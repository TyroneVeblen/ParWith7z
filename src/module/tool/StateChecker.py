from PySide6.QtCore import QThread, Signal

from src.module.tool.TimeoutSetter import TimeoutSetter


class StateChecker(QThread):
    trigger = Signal(list)

    def __init__(self, check: dict):
        super().__init__()
        self.check = check
        self.results = []
        self.timeout = {"timeout": False}
        TimeoutSetter(self.timeout, 3).start()

    def check_pass(self):
        pass_count = 0
        for key, value in self.check.items():
            if value == "not_test_yet":
                self.results.append({"level": "timeout", "form": str(key)})
            elif value == "pass":
                pass_count += 1
            else:
                self.results.append({"level": str(value), "form": str(key)})
        if pass_count == len(self.check):
            self.results.append({"level": "success", "from": ""})
        self.trigger.emit(self.results)

    def run(self):
        done_count = 0
        while 1:
            if self.timeout["timeout"]:
                self.check_pass()
                break
            else:
                if done_count != len(self.check):
                    done_count = 0
                    for key, value in self.check.items():
                        if value != "not_test_yet":
                            done_count += 1
                else:
                    self.check_pass()
                    break
