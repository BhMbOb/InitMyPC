import os
import datetime
import shutil
import json
from distutils.dir_util import copy_tree


def emptyDir(target_dir):
    files_to_delete = []
    folders_to_delete = []

    for root, directories, filenames in os.walk(target_dir):
        for filename in filenames:
            if(filename not in ["desktop.ini"]):
                files_to_delete.append(os.path.join(root, filename))

        for directory in directories:
            folders_to_delete.append(os.path.join(root, directory))

    for file in files_to_delete:
        if(os.path.isfile(file)):
            os.remove(file)

    for directory in folders_to_delete:
        shutil.rmtree(directory)


def getUserBackupDir():
    path = os.path.abspath(os.path.join((os.path.dirname(__file__)) + "..\\..\\..\\..\\config\\user_paths.json"))
    with open(path) as json_data:
        data = json.load(json_data)
        return data["backup_dir"]


# Clean the desktop
date_string = '{date:%Y-%m-%d}'.format( date=datetime.datetime.now() )
backup_dir = getUserBackupDir()

# Copy all desktop files to the temp folder
desktop_dir = os.path.expanduser("~/Desktop")
desktop_files = os.listdir(desktop_dir)

if not((len(desktop_files) == 1) and ("desktop.ini" == desktop_files[0])):
    if(len(desktop_files) > 0):
        copy_tree(desktop_dir, backup_dir + "\\" + date_string + "\\" + "Desktop")
        emptyDir(desktop_dir)
