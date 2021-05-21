import os

path = r'C:\Users\1022589\AppData\Roaming\RedPrairie\DLXClient\20200_1\SL\forms'
files = os.listdir(path)

for file in files:
    newFileName1 = file.replace('20200_1_1','')
    os.rename(path+'/'+file, path+'/'+newFileName1)
    print (f'old file name: {file} | new file name: {newFileName1}')

for file in files:
    newFileName1 = file.replace('20200_1_3','')
    os.rename(path+'/'+file, path+'/'+newFileName1)
    print (f'old file name: {file} | new file name: {newFileName1}')

for file in files:
    newFileName1 = file.replace('20200_1_4','')
    os.rename(path+'/'+file, path+'/'+newFileName1)
    print (f'old file name: {file} | new file name: {newFileName1}')

for file in files:
    newFileName1 = file.replace('20200_1_2','')
    os.rename(path+'/'+file, path+'/'+newFileName1)
    print (f'old file name: {file} | new file name: {newFileName1}')

