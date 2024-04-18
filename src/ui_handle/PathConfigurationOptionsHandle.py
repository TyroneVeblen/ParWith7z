import functools

from PySide6.QtWidgets import QWidget, QMessageBox

from src.module.tool.BinFileChecker import BinFileChecker
from src.module.tool.PathSelector import PathSelector
from src.module.tool.StateChecker import StateChecker
from src.ui.PathConfigurationOptionsUI import Ui_PathConfigurationOptionsUI

from src.ui_handle.impl.SettingsHandleImpl import SettingsHandleImpl

from src.ui_handle.MetaClassHandle.PathConfigurationOptionsHandleMetaClass import \
    PathConfigurationOptionsHandleMetaClass


class PathConfigurationOptionsHandle(QWidget, Ui_PathConfigurationOptionsUI, SettingsHandleImpl,
                                     metaclass=PathConfigurationOptionsHandleMetaClass):
    def __init__(self):
        QWidget.__init__(self)
        SettingsHandleImpl.__init__(self)
        self.state_checker = None
        self.setupUi(self)
        self.file_select_buttons = [self.select_7z_bin_file, self.select_par2_bin_file]
        self.file_path_line_edits = [self.SevenZip_bin_path, self.par2_bin_path]
        self.save.clicked.connect(self.settings_save)
        self.cancel.clicked.connect(self.settings_cancel)
        self.file_selector()

    def file_selector(self):
        for i in range(len(self.file_select_buttons)):
            self.file_select_buttons[i].clicked.connect(
                functools.partial(PathSelector, self, self.file_path_line_edits[i]))

    def message_call(self, result: dict):
        if result['level'] == "success":
            QMessageBox.information(self, "成功", "验证成功")
            self.close()
        elif result['level'] == "error":
            QMessageBox.warning(self, "错误", result["message"])

    def settings_save(self):
        self.reset_check_pass()
        self.state_checker = StateChecker(self.get_check_pass())
        self.state_checker.trigger.connect(self.message_call)
        self.state_checker.start()
        for line_edit in self.file_path_line_edits:
            if line_edit.text() == "":
                QMessageBox.warning(self, "错误", "{}路径为空".format(line_edit.objectName().split("_")[0]))
            else:
                checker = BinFileChecker(line_edit.text(), self.get_check_pass())
                checker.start()

    def settings_cancel(self):
        self.close()
