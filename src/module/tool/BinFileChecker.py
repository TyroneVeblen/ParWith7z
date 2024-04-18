import shlex
import shutil
import subprocess
import threading

from PySide6.QtWidgets import QWidget


class BinFileChecker(threading.Thread):
    def __init__(self, file_url: str, check: dict):
        super().__init__()
        self.file_url = file_url
        self.command = None
        self.type = None
        self.check = check

    def get_command(self):
        if "7z" in self.file_url.split("/")[-1]:
            self.command = "-h"
            self.type = "7z"
        elif "par2" in self.file_url.split("/")[-1]:
            self.command = "-V"
            self.type = "par2"

    def run(self):
        self.get_command()
        complete_command = shlex.split(self.file_url + " " + self.command)
        child = subprocess.Popen(complete_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 universal_newlines=True, bufsize=1)
        flag = 1
        while child.poll() is None:
            for line in child.stdout:
                if self.type == "7z" and "Igor Pavlov" in line:
                    self.check["7z"] = "pass"
                    flag = 0
                    break
                elif self.type == "par2" and "par2cmdline-turbo" in line:
                    self.check["par2"] = "pass"
                    flag = 0
                    break
        if flag:
            self.check[self.type] = "fail"
