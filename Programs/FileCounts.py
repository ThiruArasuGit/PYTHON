"""
Count the total number of files in a given directory and validate the same by splitting files by its extension
and it should be matching the total count
"""
import json
import os
import collections

path = r'C:\AnypointStudio_7.5.1\HUB\JConn_CPS\SapAdapter\Development\master'
cnt = collections.Counter()

"""
This loop will lookout for the list of file extension and count the file types and load a json string
"""
for (direct, sub_direct, files) in os.walk(path):
    if len(files) > 0:
        for f in files:
            ext = f.split('.')[-1]
            cnt[ext] += 1

print(f' Converting the collection output to json format: \n {json.dumps(cnt, indent=2)}')
print(f'Total number of file available in the give file path {path} are: \n {sum(cnt.values())}')
