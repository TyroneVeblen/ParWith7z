from abc import ABCMeta, abstractmethod


class SettingsHandleImpl(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def settings_load(self):
        pass

    @abstractmethod
    def settings_save(self):
        pass

    @abstractmethod
    def settings_cancel(self):
        pass

    @abstractmethod
    def closeEvent(self, event):
        pass
