import shlex
import subprocess
import threading


class BinFileChecker(threading.Thread):
    def __init__(self, file_url: str, type: str, command: str, check: dict, timeout: int):
        super().__init__()
        self.file_url = file_url.replace("\\", "/")
        self.command = command
        self.type = type
        self.check = check
        self.timeout = timeout

    def run(self):
        try:
            complete_command = shlex.split(self.file_url + " " + self.command)
        except Exception as e:
            self.check[self.type] = "not_available"
            return
        try:
            child = subprocess.Popen(complete_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     shell=False, universal_newlines=True)
            stdout, stderr = child.communicate()  # 等待子进程完成并获取输出
            if "Igor Pavlov" in stdout:
                self.check["7z"] = "pass"
            elif "par2cmdline-turbo" in stdout:
                self.check["par2"] = "pass"
            else:
                self.check[self.type] = "fail"
            child.terminate()
        except Exception as e:
            self.check[self.type] = "not_available"
