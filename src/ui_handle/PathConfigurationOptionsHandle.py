import functools

from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog, QPushButton, QLineEdit

from src.config.config import config
from src.module.tool import BaseTools
from src.module.tool.BinFileChecker import BinFileChecker
from src.module.tool.ConfigReader import ConfigReader
from src.module.tool.PathSelector import PathSelector
from src.module.tool.StateChecker import StateChecker
from src.ui.PathConfigurationOptionsUI import Ui_PathConfigurationOptionsUI
from src.ui_handle.MetaClassHandle.PathConfigurationOptionsHandleMetaClass import \
    PathConfigurationOptionsHandleMetaClass
from src.ui_handle.impl.SettingsHandleImpl import SettingsHandleImpl


class PathConfigurationOptionsHandle(QWidget, Ui_PathConfigurationOptionsUI, SettingsHandleImpl,
                                     metaclass=PathConfigurationOptionsHandleMetaClass):
    def __init__(self):
        QWidget.__init__(self)
        SettingsHandleImpl.__init__(self)
        self.state_checker = None
        self.check_pass = {"7z": "not_test_yet", "par2": "not_test_yet"}
        self.setupUi(self)
        self.settings_load()
        self.file_select_buttons = {"7z": self.select_7z_bin_file, "par2": self.select_par2_bin_file}
        self.file_path_line_edits = {"7z": self.SevenZip_bin_path, "par2": self.par2_bin_path}
        self.save.clicked.connect(self.settings_save)
        self.settings_save_start = False
        self.cancel.clicked.connect(self.settings_cancel)
        self.file_selector()

    def settings_load(self):
        self.SevenZip_bin_path.setText(config["7zPath"])
        self.par2_bin_path.setText(config["Par2Path"])

    def file_selector(self):
        for key, button in self.file_select_buttons.items():
            button.clicked.connect(
                functools.partial(PathSelector, self, self.file_path_line_edits[key])
            )

    def message_call(self, results: list):
        self.settings_save_start = False
        messagebox = QMessageBox()
        widget = QWidget()
        for result in results:
            if result["level"] == "timeout":
                messagebox.warning(widget, "错误", "{}可执行文件检测超时".format(result["form"]))
            if result["level"] == "fail":
                QMessageBox.warning(widget, "错误", "{}可执行文件检测错误".format(result["form"]))
            if result["level"] == "not_available":
                QMessageBox.warning(widget, "错误", "你选择的{}可执行文件不是一个可执行文件".format(result["form"]))
            if result["level"] == "success":
                messagebox.information(widget,"成功", "所有文件验证成功")
                ConfigReader().set_config()
        widget.deleteLater()
        messagebox.deleteLater()
        self.close()

    def settings_save(self):
        if not self.settings_save_start:
            self.check_pass = {"7z": "not_test_yet", "par2": "not_test_yet"}
            self.settings_save_start = True
            self.state_checker = StateChecker(self.check_pass)
            self.state_checker.trigger.connect(self.message_call)
            self.state_checker.start()
            for key, line_edit in self.file_path_line_edits.items():
                if line_edit.text() == "":
                    QMessageBox.warning(self, "错误", "{}路径为空".format(line_edit.objectName().split("_")[0]))
                else:
                    checker = BinFileChecker(line_edit.text(), key, BaseTools.get_command(key), self.check_pass)
                    checker.start()
        else:
            pass

    def settings_cancel(self):
        self.close()

    def closeEvent(self, event):
        event.accept()
        self.deleteLater()
