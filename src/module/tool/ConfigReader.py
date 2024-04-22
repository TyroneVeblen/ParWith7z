import os
import src.config.config as config


class ConfigReader:
    def __init__(self):
        self.full_config_file_path = None
        self.main_path = os.getcwd()
        self.config_path = "src\\config"
        self.config_file_name = "config.ini"
        self.check_config_file()
        self.get_config()

    def check_config_file(self):
        print(self.main_path)
        full_config_path = os.path.join(self.main_path, self.config_path)
        self.full_config_file_path = os.path.join(full_config_path, self.config_file_name)
        print(self.full_config_file_path)
        if not os.path.exists(full_config_path):
            os.makedirs(full_config_path)
        if not os.path.exists(self.full_config_file_path):
            file = open(self.full_config_file_path, "w")
            file.write("7zPath=" + self.main_path + "\\src\\bin\\7z.exe" + "\n")
            file.write("Par2Path=" + self.main_path + "\\src\\bin\\par2.exe" + "\n")
            print("Config File Created")
            file.close()

    def get_config(self):
        with open(self.full_config_file_path, "r") as f:
            for line in f:
                print(line)
                line_config = line.split("=")
                if len(line_config) == 2:
                    config.config[line_config[0]] = line_config[1]

    def set_config(self):
        print("执行")
        with open(self.full_config_file_path, "w") as f:
            for key, value in config.config.items():
                print(key, value)
                f.write(key + "=" + value + "\n")
