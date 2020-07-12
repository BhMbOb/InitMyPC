import os
import datetime
import shutil
import json
import winreg
import subprocess
from ctypes import windll, c_int, c_wchar_p
from distutils.dir_util import copy_tree


def launchPrograms():
    path = os.path.abspath(os.path.join((os.path.dirname(__file__)) + "..\\..\\..\\..\\config\\startup_apps.json"))
    with open(path) as json_data:
        data = json.load(json_data)
        for key, value in data.items():
            for v in value:
                command = r'Powershell -Command "& { Start-Process \"'
                command += v
                command += r'''\" -ArgumentList @(\"C:\\Windows\\System32\\drivers\\etc\\hosts\") -Verb RunAs } " '''
                os.system(command)


launchPrograms()
