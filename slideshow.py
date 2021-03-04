import os, subprocess, time
import tkinter as tk
# Getting the current work directory (cwd)
thisdir = os.getcwd()
path = input('Enter the path to display pictures from (default is this directory): ')
if len(path) != 0:
    thisdir = path
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(thisdir):
    for file in f:
        if file.endswith(".jpg") or file.endswith(".gif") or file.endswith(".png"):#what file type looking for
            files.append(file)
print(files)
pos = 0
length = (len(files))
for i in range(length):
    print(files[pos])
    os.startfile(path + files[pos])
    pos = pos + 1
    time.sleep(5)
    os.system('TASKKILL /F /IM Microsoft.Photos.exe')
    time.sleep(1)
print('Finished')
