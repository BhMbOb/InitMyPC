import winreg
import os
from win32com.shell import shell, shellcon
from shutil import copyfile


def getProjectRoot():
    try:
        reg_path = r"Software\\B3D\\InitMyPC"
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, "projectroot")
        return value
    except WindowsError:
        return ""


startup_file_path = os.path.join(getProjectRoot(), "modules\\startup\\main.py")
os.system("py " + startup_file_path)
