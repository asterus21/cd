"""The module contains functions to proccess the current path and to return a list of drives."""

import os


def drive_split(path: str) -> list:

    """The function accepts the current path and 
    returns a list of folders and the name of the drive."""

    # input: C:\\folder\\subfolder
    # output: ['C']

    split_drive = next(os.walk(path))#[0].split('\\')

    # print(split_drive)

    return split_drive

def drive_join_split(path: str) -> str:

    """Another method to get a drive from the whole tree."""

    split_join_drive = os.path.join(path)

    return split_join_drive

def parent_dir(path: str) -> str:

    """Method to get a parent directory."""

    parent = os.path.dirname(path)

    return parent

def drive_folders(path: str) -> list:

    """The function lists all folders of the directory."""

    # input: C:\\folder\\subfolder
    # output: ['folder', 'subfolder']

    folders_drive = next(os.walk(path))[1]

    if 'System Volume Information' in folders_drive:
        folders_drive.remove('System Volume Information')

    return folders_drive

    # print(next(os.walk(path))[1])

def drive_inlist() -> list:

    """The function accepts a list of drives to split them according to a separator."""

    # output: ['C:\\', 'D:\\', 'F:\\']

    inlist_drive = list(os.listdrives())

    # print(list(os.listdrives()))

    return inlist_drive
