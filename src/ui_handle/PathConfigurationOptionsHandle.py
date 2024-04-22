import functools
import src.module.tool.LittleTools as LittleTools
from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog

from src.config.config import config
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
    def __init__(self, config_reader: ConfigReader):
        QWidget.__init__(self)
        SettingsHandleImpl.__init__(self)
        self.config_reader = config_reader
        self.state_checker = None
        self.setupUi(self)
        self.set_custom_config()
        self.file_select_buttons = {"7z": self.select_7z_bin_file, "par2": self.select_par2_bin_file}
        self.file_path_line_edits = {"7z": self.SevenZip_bin_path, "par2": self.par2_bin_path}
        self.save.clicked.connect(self.settings_save)
        self.cancel.clicked.connect(self.settings_cancel)
        self.file_selector()

    def set_custom_config(self):
        self.SevenZip_bin_path.setText(config["7zPath"])
        self.par2_bin_path.setText(config["Par2Path"])

    def file_selector(self):
        for key, button in self.file_select_buttons.items():
            button.clicked.connect(
                functools.partial(PathSelector, self, self.file_path_line_edits[key])
            )

    def message_call(self, results: list):
        print("进入call")
        for result in results:
            print(result)
            if result["level"] == "timeout":
                QMessageBox.warning(self, "错误", "{}可执行文件检测超时".format(result["form"]))
            if result["level"] == "fail":
                QMessageBox.warning(self, "错误", "{}可执行文件检测错误".format(result["form"]))
            if result["level"] == "not_available":
                QMessageBox.warning(self, "错误", "你选择的{}可执行文件不是一个可执行文件".format(result["form"]))
            if result["level"] == "success":
                QMessageBox.information(self, "成功", "所有文件验证成功")

    def settings_save(self):
        self.reset_check_pass()
        self.state_checker = StateChecker(self.get_check_pass())
        self.state_checker.trigger.connect(self.message_call)
        self.state_checker.start()
        print(self.file_path_line_edits)
        for key, line_edit in self.file_path_line_edits.items():
            if line_edit.text() == "":
                QMessageBox.warning(self, "错误", "{}路径为空".format(line_edit.objectName().split("_")[0]))
            else:
                checker = BinFileChecker(line_edit.text(), key, LittleTools.get_command(key), self.get_check_pass(), 3)
                checker.start()

    def settings_cancel(self):
        self.close()
