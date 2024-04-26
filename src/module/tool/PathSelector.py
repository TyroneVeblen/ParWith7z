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
            file_path = QFileDialog.getOpenFileName(self.widget, "选择文件")
            self.line_edit.setText(file_path[0])
            return file_path[0]
        except Exception as e:
            print(e)
