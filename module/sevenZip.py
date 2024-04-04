import os
import subprocess as sub
import psutil

from PySide6.QtCore import Signal


software_location = r"bin\\7z.exe"
command = "a"

check = 1
flag = 1
child = None
pid = 0
file_index = 0


def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()


def compress(trigger: Signal, text_trigger: Signal, filedirs, config: dict):
    global flag
    global child
    global pid
    global file_index
    while file_index < len(filedirs):
        origin_files_location = filedirs[file_index]
        file_name = origin_files_location + ".7z"
        try:
            os.remove(file_name)
        except:
            print("没有文件可供删除")
        text_trigger.emit("正在压缩:{}".format(origin_files_location.split("/")[-1]))
        Popen_config = [software_location, command, file_name, origin_files_location, r"-mx=9", r"-mmt",
                        r"-aoa", r"-bsp1"]
        if config["password"] is not None or config["password"] != "":
            Popen_config.append(r"-p{}".format(config['password']))
        child = sub.Popen(
            Popen_config,
            shell=True, stdout=sub.PIPE, stderr=sub.STDOUT, universal_newlines=True, bufsize=1)
        pid = child.pid
        text_trigger.emit("当前正在压缩" + origin_files_location.split("/")[-1] + "\n")
        while child.poll() is None:
            for line in child.stdout:
                line = line.replace("\n", "")
                text_trigger.emit(line)
                if flag == 0:
                    try:
                        kill(pid)
                    except Exception as e:
                        print(e)
        child.wait()
        file_index += 1
        trigger.emit(file_index)
    file_index = 0
    text_trigger.emit("解压结束")
