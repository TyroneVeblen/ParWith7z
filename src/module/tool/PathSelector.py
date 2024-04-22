from PySide6.QtWidgets import QLineEdit, QFileDialog, QWidget


class PathSelector(QWidget):
    def __init__(self, widget: QWidget, line_edit: QLineEdit):
        super().__init__()
        self.line_edit = line_edit
        print(line_edit)
        self.widget = widget
        self.get_path()

    def get_path(self):
        try:
            print("启动")
            file_path = QFileDialog.getOpenFileName(self.widget, "选择文件")
            self.line_edit.setText(file_path[0])
            print(type(self.line_edit))
        except Exception as e:
            print(e)
