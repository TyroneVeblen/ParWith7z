import sys

from PySide6.QtWidgets import QApplication
from src.ui_handle.MainWindowHandle import MyWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
