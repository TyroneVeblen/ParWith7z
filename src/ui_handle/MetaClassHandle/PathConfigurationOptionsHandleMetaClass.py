from PySide6.QtWidgets import QDialog

from src.ui_handle.impl.SettingsHandleImpl import SettingsHandleImpl

from abc import ABCMeta


class PathConfigurationOptionsHandleMetaClass(type(QDialog), type(SettingsHandleImpl)):
    pass