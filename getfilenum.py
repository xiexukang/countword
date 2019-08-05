import os
from queue import Queue
Directorylist = []
#递归方式
def FileList(dir,fileList):
    newDir = dir
    if os.path.isfile(dir):   #判断是文件？是文件表示没有子文件
        fileList.append(dir)
    elif os.path.isdir(dir):   #为目录，检索此文件夹下是否还有文件
        Directorylist.append(dir)
        for s in os.listdir(dir):
            newDir = os.path.join(dir,s)
            print('测试',newDir)
            FileList(newDir,fileList)  #递归检索子文件夹
    return fileList
#使用层次遍历
def GetFile(dir):
    """
    :param dir:
    :return:fileList
    """
    fileList = []
    target_file = os.listdir(dir)
    target_file = [os.path.join(dir, element) for element in target_file]
    for dir_i in target_file:
        newdir = dir_i
        if os.path.isfile(newdir):
            fileList.append(newdir)
        else:
            for dir_k in os.listdir(newdir):
                target_file.append(os.path.join(newdir, dir_k))
    return fileList
def GetFile_Queue(dir):
    """
        :param dir:
        :return:(filelist)队列
        """
    filelist=Queue(maxsize=0)
    filelist.put(dir)
    while not filelist.empty():
        print(filelist.get())
    return []

choose_way = input("输入你要使用的方式.1：递归检测，2：层次遍历检测,3:队列方式")
File = input('输入你要检测的文件地址:')
if int(choose_way) == 1:
    fileList = FileList('%s' % File, [])
elif int(choose_way) == 2:
    fileList = GetFile('%s'% File)
else:
    fileList = GetFile_Queue('%s'% File)
for f in fileList:
    print(f)

print(Directorylist)
print('文件数量：',len(fileList))
print('文件夹数量:',len(Directorylist))