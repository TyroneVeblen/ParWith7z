from PySide6 import QtWidgets
from PySide6.QtWidgets import QLineEdit, QMessageBox, QWidget, QFileDialog


def number_check(qt_compose: QLineEdit):
    value = str(qt_compose.text())
    if value.isdigit():
        return value
    else:
        messagebox = QMessageBox()
        widget = QWidget()
        messagebox.critical(widget, "错误", "{}:值错误，请输入数字;已将值设置为默认值".format(qt_compose.objectName()))
        widget.deleteLater()
        messagebox.deleteLater()
        return 0


def bool_check(config_text: str):
    config_text = str(config_text)
    if config_text == "True":
        return True
    else:
        return False


def get_command(key: str):
    if key == "7z":
        return "-h"
    elif key == "par2":
        return "-V"


def create_file_select_browser_dialog():
    dialog = QtWidgets.QFileDialog()
    dialog.setWindowTitle('请选择路径')
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
    return dialog
