import os
import subprocess

import drive

path = os.getcwd()

driver = drive.drive_split(path)[0]
driver = driver + "\\"
print(driver)
print(type(driver))


def is_to_root(path: str, split_path: list) -> bool:

    """The function checks whether the drive values are equal when going to root."""

    sub_ = subprocess.run(
        "cd\\&&cd",
        cwd=path,
        check=False,
        shell=True,
        capture_output=True)

    stdout_as_str = sub_.stdout.decode("utf-8")[:-2]
    print(stdout_as_str)
    print(type(stdout_as_str))
    # split_path = driver + "\\"
    # print(split_path)
    # print(type(split_path))

    assert driver == stdout_as_str, 'Drive values are not equal.'

is_to_root(path, driver)
