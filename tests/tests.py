import os
import subprocess
import pytest


# arrange
@pytest.fixture
def get_path():
    return os.getcwd()


def test_folder(get_path: str) -> bool:

    """Сhecks whether the entered path is a folder."""
    # assert
    assert os.path.isdir(get_path), 'The path is not a directory.'


def test_current(get_path: str) -> bool:

    """Сhecks whether we stay on the same level."""

    command = 'cd'
    # act
    subprocess_run = subprocess.run(
        command,
        cwd=get_path,
        check=True,
        shell=True,
        capture_output=True
        )
    
    stdout_as_str = subprocess_run.stdout.decode("utf-8")[:-2]                  # remove \r and \n
    # assert
    assert stdout_as_str == os.getcwd(), 'Directories are not equal.'


def test_drive(get_path: str) -> bool:

    """Check wether we change the drive"""

    drives = os.listdrives()
    test = []

    for drive in drives:
        # act
        subprocess_run = subprocess.run(
            f'cd /d {drive} && cd',
            cwd=get_path,
            check=False,
            shell=True,
            capture_output=True
        )

        stdout_as_str = subprocess_run.stdout.decode("utf-8")[:-2]              # remove \r and \n
        test.append(stdout_as_str)

    # assert
    assert drives == test


def test_root(get_path: str) -> bool:

    """Check wether we go back to the root."""

    command = 'cd \ && cd'
    # act
    subprocess_run = subprocess.run(
        command,
        cwd=get_path,
        check=False,
        shell=True,
        capture_output=True
    )

    stdout_as_str = subprocess_run.stdout.decode("utf-8")[:-2]                  # remove \r and \n
    # assert
    assert stdout_as_str == os.getcwd()[0:3]


def test_up(get_path: str) -> bool:

    """Сhecks whether we go one level up."""

    command = 'cd .. && cd'
    # act
    subprocess_run = subprocess.run(
        command,
        cwd=get_path,
        check=False,
        shell=True,
        capture_output=True
        )
    
    stdout_as_str = subprocess_run.stdout.decode("utf-8")[:-2]                  # remove \r and \n
    # assert
    assert stdout_as_str == os.path.dirname(get_path), 'Directories are not equal.'


def test_down(get_path: str) -> bool:

    """Сhecks whether we go one level down."""

    folders = [f.path for f in os.scandir(get_path) if f.is_dir()]
    test = []

    for folder in folders:

        # act
        subprocess_run = subprocess.run(
            f'cd {folder} && cd',
            cwd=get_path,
            check=False,
            shell=True,
            capture_output=True
            )
        
        stdout_as_str = subprocess_run.stdout.decode("utf-8")[:-2]              # remove \r and \n    
        test.append(stdout_as_str)

    # assert
    assert folders == test, 'Directories are not equal.'
