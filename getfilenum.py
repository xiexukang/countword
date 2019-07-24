import os

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
j=0
def GetFile(dir):
    list2=[]
    list1=os.listdir(dir)
    l =len(list1)
    m=0
    while m<l:
        list1[m]=os.path.join(dir,list1[m])#使其子目录具有完整路径
        m +=1
    #用于测试，调试bug,print('初始长度',l)print('初始文件目录:',list1)
    for i in list1:

        newdir = i
        #print('测试1：',newdir)
        if os.path.isfile(newdir):
            list2.append(newdir)
            #测试：print('附加后的文件:',list1)
        else:

            for k in os.listdir(newdir):
                list1.append(os.path.join(newdir,k))
            #print('附加后的目录:',list1)
    return list2
n = input("输入你要使用的方式.1：递归检测，2：层次遍历检测")
File = input('输入你要检测的文件地址:')
if(int(n)==1):
    fileList = FileList('%s' % File, [])
else:
    fileList = GetFile('%s'% File)
for f in fileList:
    print(f)

print(Directorylist)
print('文件数量：',len(fileList))
print('文件夹数量:',len(Directorylist))