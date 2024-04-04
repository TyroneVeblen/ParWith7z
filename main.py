import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog

from module import sevenZip
from ui.untitled import Ui_MainWindow
from module.sevenZip import *


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.check = 1
        self.filedirs = ""
        self.work = None
        self.pushButton_2.clicked.connect(self.get_filenames)
        self.pushButton_3.clicked.connect(self.start)

    def closeEvent(self, event):
        try:
            if self.pushButton_3.text() == "开始":
                event.accept()
            else:
                sevenZip.flag = 0
                while sevenZip.child.poll() is None:
                    event.ignore()
                event.accept()
        except Exception as e:
            print(e)
            event.ignore()
            print("退出时出现问题")

    def get_filenames(self):
        """
        获取文件夹
        """
        try:
            dialog = QtWidgets.QFileDialog(self)
            dialog.setWindowTitle('请选择目录')
            dialog.setOption(QtWidgets.QFileDialog.Option.DontUseNativeDialog, True)
            dialog.setOption(QtWidgets.QFileDialog.Option.ShowDirsOnly)
            dialog.setFileMode(QFileDialog.FileMode.Directory)
            for view in dialog.findChildren(QtWidgets.QListView):
                if isinstance(view.model(), QtWidgets.QFileSystemModel):
                    view.setSelectionMode(
                        QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
            for view in dialog.findChildren(QtWidgets.QTreeView):
                if isinstance(view.model(), QtWidgets.QFileSystemModel):
                    view.setSelectionMode(
                        QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
            if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                self.filedirs = dialog.selectedFiles()
                self.textBrowser.clear()
                for dir in self.filedirs:
                    self.textBrowser.append(dir + "\n")
        except:
            print("error")

    def start(self):
        self.progressBar.reset()
        self.progressBar.setRange(0, len(self.filedirs))
        if self.pushButton_3.text() == "开始":
            config = {"password": self.customized_parameters_edit.text()}
            self.work = progressThread(filedirs=self.filedirs, config=config)
            sevenZip.flag = 1
            self.pushButton_3.setText("停止")
            self.work.start()
            self.work.trigger.connect(self.setValue)
            self.work.text_changed.connect(self.setText)
        else:
            sevenZip.flag = 0
            self.pushButton_3.setText("开始")
            self.work.finished.connect(self.finish)
            self.work = None

    def finish(self):
        self.textBrowser.setText("结束")

    def setValue(self, num):
        self.progressBar.setValue(num)

    def setText(self, text):
        if text == "解压结束":
            self.progressBar.setValue(0)
            self.pushButton_3.setText("开始")
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
