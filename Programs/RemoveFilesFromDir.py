import fnmatch
import os

from envs.Files.Lib.fnmatch import fnmatch

file_path = r'C:\Users\1022589\Downloads'
pattern = 'Zoom*.exe'

for item in os.listdir(file_path):
    valid = fnmatch(item, pattern)
    if valid:
        print(f'Deleting the item {item}')
        os.remove(file_path + "/" + item)

print(f'There are no {pattern} type files found')
