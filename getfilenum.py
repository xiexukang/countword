import os

Directorylist = []
def FileList(dir,fileList):
    newDir = dir
    if os.path.isfile(dir):   #判断是文件？是文件表示没有子文件
        fileList.append(dir)
    elif os.path.isdir(dir):   #为目录，检索此文件夹下是否还有文件
        Directorylist.append(dir)
        for s in os.listdir(dir):
            newDir = os.path.join(dir,s)
            FileList(newDir,fileList)  #递归检索子文件夹
    return fileList
File = input('输入你要检测的文件地址:')
fileList =FileList('%s'% File,[])
for f in fileList:
    print(f)

print(Directorylist)
print('文件数量：',len(fileList))
print('文件夹数量:',len(Directorylist))