from src.config.config import config
from src.module.tool.BaseTools import bool_check
from src.module.tool.ConfigReader import ConfigReader
from src.ui.PageForOtherSettings import Ui_PageForOtherSettings
from PySide6.QtWidgets import QWidget

from src.ui_handle.MetaClassHandle.PathConfigurationOptionsHandleMetaClass import \
    PathConfigurationOptionsHandleMetaClass
from src.ui_handle.impl.SettingsHandleImpl import SettingsHandleImpl


class PageForOtherSettingsHandle(QWidget, Ui_PageForOtherSettings, SettingsHandleImpl,
                                 metaclass=PathConfigurationOptionsHandleMetaClass):

    def __init__(self, parent=None):
        super(PageForOtherSettingsHandle, self).__init__(parent)
        self.setupUi(self)
        self.settings_load()
        self.save_settings.clicked.connect(self.settings_save)
        self.cancel_settings.clicked.connect(self.settings_cancel)
        self.is_enable_cache.toggled.connect(self.set_cache_enabled)

    def set_cache_enabled(self):
        if self.is_enable_cache.isChecked():
            self.cache_folder.setEnabled(True)
            self.label.setEnabled(True)
        else:
            self.cache_folder.setEnabled(False)
            self.label.setEnabled(False)

    def settings_load(self):
        try:
            self.is_enable_cache.setChecked(bool_check(config["EnableCache"]))
            self.cache_folder.setText(config["CacheFolder"])
        except Exception as e:
            pass
        self.set_cache_enabled()
        pass

    def settings_save(self):
        config["EnableCache"] = self.is_enable_cache.isChecked()
        config["CacheFolder"] = self.cache_folder.text()
        ConfigReader().set_config()
        self.close()

    def settings_cancel(self):
        pass

    def closeEvent(self, event):
        event.accept()
        self.deleteLater()
