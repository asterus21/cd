"""The module contains basic scenarios of using the 'cd' command for the Windows CLI."""

import os
import subprocess
import pytest

import drive

# CURRENT_PATH = os.getcwd()
# MAIN_DRIVE_PATH = "C:\\"

@pytest.fixture(scope="class")
def path():

    """Fixture to contain the current path."""

    return os.getcwd()


# the point is that the fixture below takes a value for the 'drive_split' method
# from the fixture above, i.e. an error occurs

@pytest.fixture(scope="class")
def current_driver():

    """Fixture to get the value of the current drive."""

    current_drive = drive.drive_split(os.getcwd())[0]

    return  current_drive

class TestCMD:


    """Class for the 'cd' command methods."""

    # ----------------------------------------------------------------
    # Initiating a class.
    # ----------------------------------------------------------------

    # def __init__(self) -> None:
    #   pass

    # ----------------------------------------------------------------
    # Here we check whether the folder is directory.
    # ----------------------------------------------------------------

    def test_is_dir(self, path: str) -> bool:

        """Сheck whether the entered path is a directory."""

        assert os.path.isdir(path), 'The path is not a directory.'

    # ----------------------------------------------------------------
    # Here we check whether we are inside the directory.
    # ----------------------------------------------------------------

    def test_is_inside(self, path: str) -> bool:

        """Сheck whether we are inside the current directory."""

        sub_current = subprocess.run(
            "cd",
            cwd=path,
            check=False,
            shell=True,
            capture_output=True
            )

        # remove the last two elements of the line, i.e. \r and \n
        stdout_as_str = sub_current.stdout.decode("utf-8")[:-2]
        assert stdout_as_str == os.getcwd(), 'Directories are not equal.'

    # ----------------------------------------------------------------
    # Here we check whether we are up one folder.
    # ----------------------------------------------------------------

    def test_is_up_equal(self, path: str) -> bool:

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
        upper_path = drive.drive_split(path)[:-1]
        # join the elements of the list
        path_upper = '\\'.join(upper_path)

        assert stdout_as_str == path_upper, 'Paths are not equal!'

    # ----------------------------------------------------------------
    # Here we check whether we are down one folder.
    # ----------------------------------------------------------------

    def test_is_down_equal(self, path: str) -> bool:

        """The method goes down by one folder and checks whether it is down."""

        list_of_subfolders_etalons = []

        for i in range(len(drive.drive_folders(path))):
            _path = path + "\\" + drive.drive_folders(path)[i]
            list_of_subfolders_etalons.append(_path)


        list_of_subfolders_to_check = []

        for folder in drive.drive_folders(path):

            sub_down = subprocess.run(
                f"cd {folder}&&cd",
                cwd=path,
                check=False,
                shell=True,
                capture_output=True
                )

            # remove the last two elements of the line, i.e. \r and \n
            stdout_as_str = sub_down.stdout.decode("utf-8")[:-2]
            list_of_subfolders_to_check.append(stdout_as_str)

        assert list_of_subfolders_etalons == list_of_subfolders_to_check, 'Lists are not equal.'

    # ----------------------------------------------------------------
    # Here we check whether we the drives are equal.
    # ----------------------------------------------------------------

    def test_is_to_root(self, path: str, current_driver: list) -> bool:

        """The function checks whether the drive values are equal when going to root."""

        sub_ = subprocess.run(
            "cd\\&&cd",
            cwd=path,
            check=False,
            shell=True,
            capture_output=True)

        stdout_as_str = sub_.stdout.decode("utf-8")[:-2]
        current_driver = current_driver + "\\"

        assert current_driver == stdout_as_str, 'Drive values are not equal.'
