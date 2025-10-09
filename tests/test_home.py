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

def test_up(get_path: str):

    """Goes back one level up."""

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


def test_down(get_path: str):
    pass
    

def test_current(get_path: str):

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
