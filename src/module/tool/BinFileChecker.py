import shlex
import shutil
import subprocess
import threading

from PySide6.QtWidgets import QWidget


class BinFileChecker(threading.Thread):
    def __init__(self, widget: QWidget, file_url: str,check: dict):
        super().__init__()
        self.widget = widget
        self.file_url = file_url
        self.command = None
        self.check = check

    def get_command(self):
        if "7z" in self.file_url.split("/")[-1]:
            self.command = "-h"
        elif "par2" in self.file_url.split("/")[-1]:
            self.command = "-V"

    def run(self):
        self.get_command()
        complete_command = shlex.split(self.file_url + " " + self.command)
        child = subprocess.Popen(complete_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 universal_newlines=True, bufsize=1)
        while child.poll() is None:
            for line in child.stdout:
                print(line)
