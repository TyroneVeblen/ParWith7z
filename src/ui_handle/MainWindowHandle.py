from PySide6 import QtWidgets
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QMainWindow, QFileDialog, QWidget

from src.module import sevenZip
from src.module.tool.BaseTools import create_file_select_browser_dialog
from src.module.sevenZip import *
from src.module.tool.ConfigReader import ConfigReader
from src.ui.MainWindowUI import Ui_MainWindow
from src.ui_handle.PageFor7zConfigHandle import PageFor7zConfigHandle
from src.ui_handle.PageForPar2ConfigHandle import PageForPar2ConfigHandle
from src.ui_handle.PathConfigurationOptionsHandle import PathConfigurationOptionsHandle


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.dialog = {}
        self.check = 1
        self.filedirs = ""
        self.work = None
        self.config = None
        self.select_folders.clicked.connect(self.get_filenames)
        self.start_and_end.clicked.connect(self.start)
        self.config_for_bin_file_path.triggered.connect(self.open_bin_file_path_settings_page)
        self.config_for_7z.clicked.connect(self.open_7z_config_page)
        self.config_for_par2.clicked.connect(self.open_par2_config_page)
        ConfigReader().get_config()

    def open_par2_config_page(self):
        self.dialog["PageForPar2Config"] = PageForPar2ConfigHandle()
        self.dialog["PageForPar2Config"].show()

    def open_7z_config_page(self):
        self.dialog["PageFor7zConfig"] = PageFor7zConfigHandle()
        self.dialog["PageFor7zConfig"].show()

    def open_bin_file_path_settings_page(self):
        self.dialog["PageForPathConfigurationOptions"] = PathConfigurationOptionsHandle()
        self.dialog["PageForPathConfigurationOptions"].show()

    def closeEvent(self, event):
        for widget in self.dialog:
            if self.dialog[widget] is not None:
                self.dialog[widget].close()
                self.dialog[widget].deleteLater()
        try:
            if self.start_and_end.text() == "开始":
                event.accept()
                self.deleteLater()
            else:
                sevenZip.flag = 0
                while sevenZip.child.poll() is None:
                    event.ignore()
                event.accept()
                self.deleteLater()
        except Exception as e:
            print(e)
            event.ignore()
            print("退出时出现问题")

    def get_filenames(self):
        """
        获取文件夹
        """
        try:
            dialog = create_file_select_browser_dialog()
            if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                self.filedirs = dialog.selectedFiles()
                self.textBrowser.clear()
                for folder in self.filedirs:
                    self.textBrowser.append(folder + "\n")
            dialog.deleteLater()
        except:
            print("error")

    def start(self):
        self.progressBar.reset()
        self.progressBar.setRange(0, len(self.filedirs))
        if self.start_and_end.text() == "开始":
            self.textBrowser.clear()
            config = {"password": self.customized_parameters_edit.text()}
            self.work = progressThread(filedirs=self.filedirs, config=config)
            sevenZip.flag = 1
            self.start_and_end.setText("停止")
            self.work.start()
            self.work.trigger.connect(self.setValue)
            self.work.text_changed.connect(self.setText)
        else:
            sevenZip.flag = 0
            self.start_and_end.setText("开始")
            self.work.finished.connect(self.finish)
            self.work = None

    def finish(self):
        self.textBrowser.setText("结束")

    def setValue(self, num):
        self.progressBar.setValue(num)

    def setText(self, text):
        if text == "解压结束":
            self.progressBar.setValue(0)
            self.start_and_end.setText("开始")
        self.textBrowser.append(text)


class progressThread(QThread):
    trigger = Signal(int)
    text_changed = Signal(str)

    def __init__(self, filedirs, config: dict):
        super(progressThread, self).__init__()
        self.filedirs = filedirs
        self.config = config

    def run(self):
        compress(self.trigger, self.text_changed, self.filedirs, self.config)
