import os
import subprocess


filepath="C:\\Softwares\\jda\\platform\\config\\bin\\platform\\installPatch.cmd"
p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

stdout, stderr = p.communicate()
print (p.returncode) # is 0 if success