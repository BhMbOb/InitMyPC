import os
import datetime
import shutil
import json
import winreg
import subprocess
from ctypes import windll, c_int, c_wchar_p
from distutils.dir_util import copy_tree

DefineDosDevice = windll.kernel32.DefineDosDeviceW
DefineDosDevice.argtypes = [c_int, c_wchar_p, c_wchar_p]


def emptyFolder(root_dir):
    target_files = []
    target_folders = []

    files_to_ignore = ["desktop.ini"]

    for root, directories, filenames in os.walk(root_dir):
        for filename in filenames:
            if(filename not in files_to_ignore):
                target_files.append(os.path.join(root, directory))

        for directory in directories:
            target_folders.append(os.path.join(root, directory))

    for files in target_files:
        if(os.path.isfile(file)):
            os.remove(file)

    for directory in target_folders:
        shutil.rmtree(directory)


def createVirtualDrive(drive_letter, target_folder):
    if(os.path.exists(target_folder)):
        drive_letter = drive_letter.upper()[0] + ":"
        DefineDosDevice(0, drive_letter, target_folder)
        print("Created virtual drive " + drive_letter + " at " + target_folder)


def createVirtualDrives():
    path = os.path.abspath(os.path.join((os.path.dirname(__file__)) + "..\\..\\..\\..\\config\\virtual_drives.json"))
    with open(path) as json_data:
        data = json.load(json_data)
        for drive_letter, drive_path in data.items():
            if(os.path.exists(drive_path)):
                createVirtualDrive(drive_letter, drive_path)


createVirtualDrives()
