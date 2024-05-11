from PySide6.QtWidgets import QWidget

from src.config.config import config
from src.module.tool.BaseTools import number_check,bool_check
from src.module.tool.ConfigReader import ConfigReader
from src.ui.PageFor7zSettings import Ui_PageFor7zSettings
from src.ui_handle.MetaClassHandle.PathConfigurationOptionsHandleMetaClass import \
    PathConfigurationOptionsHandleMetaClass
from src.ui_handle.impl.SettingsHandleImpl import SettingsHandleImpl


class PageFor7zSettingsHandle(QWidget, Ui_PageFor7zSettings, SettingsHandleImpl,
                              metaclass=PathConfigurationOptionsHandleMetaClass):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings_load()
        self.save_settings.clicked.connect(self.settings_save)
        self.cancel_settings.clicked.connect(self.settings_cancel)

    def settings_cancel(self):
        self.close()

    def settings_load(self):
        try:
            self.is_delete_file_after_compress.setChecked(bool_check(config["DeleteFileAfterCompress"]))
            self.compress_level.setCurrentIndex(["-mx=0", "-mx=5", "-mx=9"].index(config["CompressLevel"]))
            self.volume_size.setText(config["VolumeSize"])
            self.is_encrypted_file_name.setChecked(bool_check(config["EncryptedFileName"]))
            self.is_folder_only.setChecked(bool_check(config["FolderOnly"]))
            self.path_recursion_depth.setText(config["PathRecursionDepth"])
            self.is_delete_file_after_decompress.setChecked(bool_check(config["DeleteFileAfterDecompress"]))
            self.is_create_subfolder.setChecked(bool_check(config["CreateSubfolder"]))
            self.is_test_zip_first.setChecked(bool_check(config["TestZipFirst"]))
        except Exception as e:
            print(e)

    def settings_save(self):
        config["DeleteFileAfterCompress"] = self.is_delete_file_after_compress.isChecked()
        config["CompressLevel"] = "-mx={}".format([0, 5, 9][self.compress_level.currentIndex()])
        config["VolumeSize"] = number_check(self.volume_size)
        config["EncryptedFileName"] = self.is_encrypted_file_name.isChecked()
        config["FolderOnly"] = self.is_folder_only.isChecked()
        config["PathRecursionDepth"] = number_check(self.path_recursion_depth)
        config["DeleteFileAfterDecompress"] = self.is_delete_file_after_decompress.isChecked()
        config["CreateSubfolder"] = self.is_create_subfolder.isChecked()
        config["TestZipFirst"] = self.is_test_zip_first.isChecked()
        ConfigReader().set_config()
        self.close()

    def closeEvent(self, event):
        event.accept()
        self.deleteLater()
