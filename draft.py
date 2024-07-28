"""The module contains basic scenarios of using the 'cd' command for the Windows CLI."""

import os
import subprocess

import drive

CURRENT_PATH = os.getcwd()
MAIN_DRIVE_PATH = "C:\\"

class CMD:


    """Class for the 'cd' command methods."""

    def __init__(self) -> None:
        pass

    def if_dir(self, path: str) -> bool:

        """The function checks whether the entered path is a directory."""

        assert os.path.isdir(path), 'The directory is not a path.'

    def is_equal_dir(self, path: str) -> bool:

        """The function checks whether we are inside the current directory."""

        sub_ = subprocess.run("cd", cwd=path, check=False, shell=True, capture_output=True)
        stdout_as_str = sub_.stdout.decode("utf-8")[:-2]
        assert stdout_as_str == os.getcwd(), 'Directories are not equal.'

    def is_going_up_equal(self, path: str, split_path: list) -> bool:

        """The method goes up by one subfolder and checks whether it is up."""

        sub_ = subprocess.run("cd ..&&cd", cwd=path, check=False, shell=True, capture_output=True)
        stdout_as_str = sub_.stdout.decode("utf-8")[:-2]
        _path = split_path[0] + "\\" + "\\".join(split_path[1:-1])
        assert stdout_as_str == _path, 'Paths are not equal.'
    
    def is_going_down_equal(self, path: str) -> bool:

        """The method goes down by one subfolder and checks whether it is down."""
        
        list_of_subfolders_to_check = []
        for folder in drive_folders_list(path):
            sub_ = subprocess.run(f"cd {folder}&&cd", cwd=path, check=False, shell=True, capture_output=True)
            stdout_as_str = sub_.stdout.decode("utf-8")[:-2]
            list_of_subfolders_to_check.append(stdout_as_str)

        list_of_subfolders_etalons = []
        for i in range(len(CMD.dir_list(CMD, path))):
            _path = path + "\\" + CMD.dir_list(CMD, path)[i]
            list_of_subfolders_to_check.append(_path)
    
        assert list_of_subfolders_etalons == list_of_subfolders_to_check, 'Lists are not equal.'

    def is_to_root(self, path: str, split_path: list) -> bool:

        """The function checks whether the drive values are equal when going to root."""

        sub_ = subprocess.run("cd\\&&cd", cwd=path, check=False, shell=True, capture_output=True)
        stdout_as_str = sub_.stdout.decode("utf-8")[:-2]
        drive = split_path[0] + "\\"

        assert drive == stdout_as_str, 'Drive values are not equal.'

    def change_drive(self) -> bool:

        """The method changes the drive and asserts the drive is changed."""

        list_of_drives = []
        # the drive must be changed with the use of 'cd /d {drive}&&cd' as well
        for driver in CMD.drives_list(self):
            sub_ = subprocess.run(f"{driver}&&cd", cwd=MAIN_DRIVE_PATH, check=False, shell=True, capture_output=True)
            stdout_as_str = sub_.stdout.decode("utf-8")[:-2]
            list_of_drives.append(stdout_as_str)

        assert list_of_drives == os.listdrives()[:-1], "Lists are equal."
