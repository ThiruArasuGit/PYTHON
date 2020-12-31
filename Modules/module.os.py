import os

print ("current working directory: " + os.getcwd())

#Navigate to new directory 'C:\Softwares\PyCharm\PyCharm Community Edition 2019.1'
os.chdir('C:\Softwares\PyCharm\PyCharm Community Edition 2019.1')
print("New Directory: "+os.getcwd())

#List of files and folders in the current working directory
print(os.listdir())

#Create directory in the path 'C:\LearnPython'
os.chdir('C:\LearnPython')
#os.mkdir('Demo-1') # If directoy already exists it will through error

#Create directory and subdiretories
print(os.getcwd())
#os.makedirs('Demo-3')
print(os.listdir())

#Delete directory or directories
#os.rmdir("Demo-1")
print(os.listdir())
#os.removedirs('Demo-2/sub-demo-1/sub-demo-2')
print(os.listdir())

#Rename files or folders
os.chdir('C:\LearnPython\Demo-2')
os.rename('sub-demo-1','sub_demo_1')
print(os.listdir())


