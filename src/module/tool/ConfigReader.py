import os
import src.config.config as config


class ConfigReader:
    def __init__(self):
        self.full_config_file_path = None
        self.main_path = os.getcwd()
        self.config_path = "src\\config"
        self.config_file_name = "config.ini"
        self.check_config_file()

    def check_config_file(self):
        full_config_path = os.path.join(self.main_path, self.config_path)
        self.full_config_file_path = os.path.join(full_config_path, self.config_file_name)
        if not os.path.exists(full_config_path):
            os.makedirs(full_config_path)
        if not os.path.exists(self.full_config_file_path):
            file = open(self.full_config_file_path, "w")
            file.write("7zPath=" + self.main_path + "\\src\\bin\\7z.exe" + "\n")
            file.write("Par2Path=" + self.main_path + "\\src\\bin\\par2.exe" + "\n")
            file.write("DeleteFileAfterCompress=True"+"\n")
            file.write("VolumeSize=0"+"\n")
            file.write("FolderOnly=True"+"\n")
            file.write("PathRecursionDepth=0"+"\n")
            file.write("EncryptedFileName=False"+"\n")
            file.write("CompressLevel=-mx=5"+"\n")
            file.write("DeleteFileAfterDecompress=True"+"\n")
            file.write("CreateSubfolder=False"+"\n")
            file.write("TestZipFirst=False"+"\n")
            print("Config File Created")
            file.close()

    def get_config(self):
        with open(self.full_config_file_path, "r") as f:
            for line in f:
                split_index = line.find("=")
                key = line[:split_index]
                value = line[split_index + 1:].replace("\n", "").replace("\r", "")
                config.config[key] = value

    def set_config(self):
        with open(self.full_config_file_path, "w") as f:
            for key, value in config.config.items():
                f.write(key + "=" + str(value) + "\n")
