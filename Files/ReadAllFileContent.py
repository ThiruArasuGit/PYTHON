import os
import PyPDF2

indir = "C:\\Softwares\\TALEND\\Input\\investpdf\\"

def allFiles(indir):
    fileNames = os.listdir(indir)
    for fileName in fileNames:
        print('*********************************' + fileName + '******************************************************')
        fullname =indir+fileName
        print("Fully qualified name: " +fullname)
        print('-------------------------------------------------------------------------------------------------------')
        fileObj = open(fullname,'rb')
        filereader = PyPDF2.PdfFileReader(fileObj)
        filepageObj = filereader.getPage(0)
        print(filepageObj.extractText())


if __name__ == '__main__':
    if 1==2:
        allFiles(indir)
    else:
        allFiles(indir)

