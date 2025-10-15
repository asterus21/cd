import os
import subprocess
import pytest


# arrange
@pytest.fixture(name="path")
def get_path():

    """Returns the current working directory."""

    return os.getcwd()


def execute_command(command: str, path: str):

    """Executes the passed command to run."""

    subprocess_run = subprocess.run(
        command,
        cwd=path,
        check=False,
        shell=True,
        capture_output=True
        )

    return subprocess_run.stdout.decode("utf-8").strip()


def test_folder(path: str):

    """Сhecks whether the entered path is a folder."""
    # assert
    assert os.path.isdir(path), 'The path is not a directory.'


def test_current(path: str):

    """Сhecks whether we stay on the same level."""
    # act
    result = execute_command('cd', path)
    # assert
    assert result == os.getcwd(), 'Directories are not equal.'


def test_drive(path: str):

    """Check wether we change the drive"""

    drives = os.listdrives()
    result = []
    # act
    for drive in drives:        
        result.append(execute_command(f'cd /d {drive} && cd', path))

    # assert
    assert drives == result


def test_root(path: str):

    """Check wether we go back to the root of the current directory."""
    # act
    result = execute_command('cd \ && cd', path)
    # assert
    assert result == os.getcwd()[0:3]


def test_up(path: str):

    """Сhecks whether we go one level up."""
    # act
    result = execute_command('cd .. && cd', path)
    # assert
    assert result == os.path.dirname(path), 'Directories are not equal.'


def test_down(path: str):

    """Сhecks whether we go one level down."""

    folders = [f.path for f in os.scandir(path) if f.is_dir()]
    result = []
    # act
    for folder in folders:
        result.append(execute_command(f'cd {folder} && cd', path))

    # assert
    assert folders == result, 'Directories are not equal.'
