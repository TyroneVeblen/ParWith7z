import threading

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QWidget, QMessageBox


class StateChecker(QThread):
    trigger = Signal(dict)

    def __init__(self, check: dict):
        super().__init__()
        self.check = check
        self.result = {"level": "none", "message": ""}

    def run(self):
        while 1:
            if self.check['7z'] != "not_test_yet" and self.check['par2'] != "not_test_yet":
                print(self.check)
                if self.check["7z"] == "pass" and self.check["par2"] == "pass":
                    self.result["level"] = "success"
                    break
                else:
                    if self.check["7z"] == "fail":
                        self.result["level"] = "error"
                        self.result["message"] = "7z文件验证失败"
                        break
                    elif self.check["par2"] == "fail":
                        self.result["level"] = "error"
                        self.result["message"] = "par2文件验证失败"
                        break
        self.trigger.emit(self.result)
