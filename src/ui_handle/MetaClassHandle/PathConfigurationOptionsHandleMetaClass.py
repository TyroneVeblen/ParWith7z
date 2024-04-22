from PySide6.QtWidgets import QDialog

from src.ui_handle.impl.SettingsHandleImpl import SettingsHandleImpl


class PathConfigurationOptionsHandleMetaClass(type(QDialog), type(SettingsHandleImpl)):
    pass
