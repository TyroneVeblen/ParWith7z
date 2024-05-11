from PySide6.QtWidgets import QWidget
from src.module.tool.BaseTools import number_check
from src.module.tool.ConfigReader import ConfigReader
from src.ui.PageForPar2Config import Ui_PageForPar2Config
from src.ui_handle.MetaClassHandle.PathConfigurationOptionsHandleMetaClass import PathConfigurationOptionsHandleMetaClass
from src.ui_handle.impl.SettingsHandleImpl import SettingsHandleImpl
from src.config.config import config


class PageForPar2ConfigHandle(QWidget, Ui_PageForPar2Config, SettingsHandleImpl,
                              metaclass=PathConfigurationOptionsHandleMetaClass):
    def __init__(self):
        QWidget.__init__(self)
        SettingsHandleImpl.__init__(self)
        self.setupUi(self)
        self.settings_load()
        self.save_settings.clicked.connect(self.settings_save)
        self.cancel_settings.clicked.connect(self.settings_cancel)

    def settings_load(self):
        try:
            self.par2_block_size.setText(config["Par2BlockSize"])
        except KeyError:
            pass

    def settings_save(self):
        config["Par2BlockSize"] = number_check(self.par2_block_size)
        ConfigReader().set_config()
        self.close()

    def settings_cancel(self):
        self.close()

    def closeEvent(self, event):
        event.accept()
        self.deleteLater()
