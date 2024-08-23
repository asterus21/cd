"""The module contains test assertions to check the basic scenario of using the 'cd' command"""

import os
import subprocess

import drive

path_current = os.getcwd()
folders = drive.drive_folders(path_current)
# print(drive.drive_split(path_current))


# ----------------------------------------------------------------
# Here we check whether we are inside the directory.
# ----------------------------------------------------------------

def current_path() -> bool:

    """Сheck whether we are inside the current directory."""

    path_ = subprocess.run(
        "cd",
        cwd=path_current,
        check=False,
        shell=True,
        capture_output=True
        )

    # remove the last two elements of the line, i.e. \r and \n
    stdout_as_str = path_.stdout.decode("utf-8")[:-2]
    print(stdout_as_str)
    assert path_current == stdout_as_str, "Paths are not equal!"

# ----------------------------------------------------------------
# Here we check whether we are down one folder.
# ----------------------------------------------------------------

def test_is_down_equal(_path: str) -> bool:

    """The method goes down by one folder and checks whether it is down."""

    # list_of_subfolders_etalons = []

    # for i, folder in enumerate(folders):
    #     p_ath = _path + '\\' + folders[i]
    #     list_of_subfolders_etalons.append(p_ath)

    subfolders = [ f.path for f in os.scandir(path_current) if f.is_dir() ]

    list_of_subfolders_to_check = []

    for folder in folders:

        sub_down = subprocess.run(
            f"cd {folder}&&cd",
            cwd=_path,
            check=False,
            shell=True,
            capture_output=True
            )
        # remove the last two elements of the line, i.e. \r and \n
        stdout_as_str = sub_down.stdout.decode("utf-8")[:-2]

        list_of_subfolders_to_check.append(stdout_as_str)

    print(subfolders)
    print(list_of_subfolders_to_check)
    assert subfolders == list_of_subfolders_to_check, 'Lists are not equal.'

# ----------------------------------------------------------------
# Here we check whether we are up one folder.
# ----------------------------------------------------------------

def test_is_up_equal(path: str) -> bool:

    """The method goes up by one folder and checks whether it is up."""

    sub_upper = subprocess.run(
        "cd ..&&cd",
        cwd=path,
        check=False,
        shell=True,
        capture_output=True
        )

    # remove the last two elements of the line, i.e. \r and \n
    stdout_as_str = sub_upper.stdout.decode("utf-8")[:-2]

    # get the path as a list and remove the last element
    upper_path = drive.parent_dir(path_current) # [:-1]

    # join the elements of the list
    # path_upper = '\\'.join(upper_path)

    print(stdout_as_str)
    print(upper_path)
    assert stdout_as_str == upper_path, 'Paths are not equal!'

current_path()
test_is_down_equal(path_current)
test_is_up_equal(path_current)
