import winreg
import os
import shutil
from win32com.shell import shell, shellcon

startup_dir = shell.SHGetFolderPath(0, (shellcon.CSIDL_STARTUP, shellcon.CSIDL_COMMON_STARTUP)[0], None, 0)


def createRegistryItem(name, value):
    try:
        reg_path = r"Software\\B3D\\InitMyPC"
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)
        print("Successfully created key!")
    except WindowsError:
        pass


# Store the projects root in the registry
project_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..\\..\\"))
createRegistryItem("projectroot", project_folder)

# Copy the startup files to shell:startup
shutil.copyfile(
    os.path.join(project_folder, "bin\\impc_startup.bat"),
    os.path.join(startup_dir, "impc_startup.bat")
)
shutil.copyfile(
    os.path.join(project_folder, "bin\\impc_startup.py"),
    os.path.join(startup_dir, "impc_startup.py")
)
