import time
import os
import shutil

source = input("Enter the file name : ")
days = input("The file exists for how many days ? ")

if(os.path.exists(path) == "True"):
    print("Path Exists")
else:
    print("Path does not exist")