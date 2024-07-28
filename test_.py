import os
import subprocess

PATH = os.getcwd()
path = "C:\\"

# print(os.listdrives()[:-1])

drives_list = []

for drive in os.listdrives():
    drive = drive.split("\\")
    drives_list.append(drive[0])
    # drive = drive[0]
    # print(drive[0])
    

print(drives_list)

def change_drive(path: str) -> bool:

    """The method changes the drive and asserts the drive is changed."""

    list_of_drives = []    

    for driver in drives_list[:-1]:
        sub_ = subprocess.run(f"{driver}&&cd", cwd="C:\\", check=False, shell=True, capture_output=True)
        stdout_as_str = sub_.stdout.decode("utf-8")[:-2]
        list_of_drives.append(stdout_as_str)
    
    assert list_of_drives == os.listdrives()[:-1], "Lists are equal."

   

def return_root(path: str) -> bool:

    """The method returns the drive and asserts the drive is returned (i.e. goes to the root of the path)."""

    sub_ = subprocess.run("cd\&&cd", cwd="C:\\", check=False, shell=True, capture_output=True)
    stdout_as_str = sub_.stdout.decode("utf-8")
    print(stdout_as_str)

return_root(path)
