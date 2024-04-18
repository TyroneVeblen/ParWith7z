from abc import ABCMeta, abstractmethod


class SettingsHandleImpl(metaclass=ABCMeta):

    def __init__(self):
        self.__check_pass = {"7z": "not_test_yet", "par2": "not_test_yet"}

    def set_check_pass(self, check_pass):
        self.__check_pass = check_pass

    def get_check_pass(self):
        return self.__check_pass

    def reset_check_pass(self):
        self.__check_pass = {"7z": "not_test_yet", "par2": "not_test_yet"}

    @abstractmethod
    def settings_save(self):
        pass

    @abstractmethod
    def settings_cancel(self):
        pass
