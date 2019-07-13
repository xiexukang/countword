# -*- coding: utf-8 -*-
from tkinter import *
import tkinter
import tkinter.filedialog
import hashlib
import time
import chardet
import sys
import re
import json

# -*- coding: utf-8 -*-
LOG_LINE_NUM = 0
class WORD_GUI():
    def __init__(self,init_window_name):
        self.init_window_name=init_window_name


    def set_init_window(self):
        self.init_window_name.title("统计单词汉字V1.0 by 谢旭康")#界面名字
        self.init_window_name.geometry('1080x681+10+10')#界面大小及初始位置
        self.init_date_label = Label(self.init_window_name,text="待处理数据")
        self.init_date_label.grid(row=0,column=0)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=14)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        # 文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  # 原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=65, height=49)  # 处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        # 按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="转gbk16进制编码", bg="lightblue", width=15,
                                              command=self.str_trans_to_gbk)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=11)
            #文本统计单词字数需要从右边文本输入单词文本
        self.str_trans_to_md5_button1 = Button(self.init_window_name, text="文本单词汉字字数", bg="red", width=15,
                                              command=self.word)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button1.grid(row=2, column=11)

        self.upload_file_button = Button(self.init_window_name, text="文件上传", bg="blue", width=15,
                                               command=self.uploadfile)  # 调用内部方法  加()为直接调用
        self.upload_file_button.grid(row=0, column=2)
        #格式化json数据功能
        self.formatJson_button = Button(self.init_window_name,text="json格式化", bg="Teal", width=15,
                                        command = self.JSON)
        self.formatJson_button.grid(row=3,column=11)
        self.Ctourl_button = Button(self.init_window_name, text ="汉字转为URL",bg="yellow",
                                    width=15,command = self.tourl)
        self.Ctourl_button.grid(row=4,column=11)
        self.Ctourl_button = Button(self.init_window_name, text="URL转为汉字", bg="yellow",
                                    width=15, command=self.urltoc)
        self.Ctourl_button.grid(row=5, column=11)
        self.result_data_scrollbar_y = Scrollbar(self.init_window_name)  # 创建纵向滚动条
        self.result_data_scrollbar_y.config(command=self.result_data_Text.yview)  # 将创建的滚动条通过command参数绑定到需要拖动的Text上
        self.result_data_Text.config(yscrollcommand=self.result_data_scrollbar_y.set)# Text反向绑定滚动条
        self.result_data_scrollbar_y.grid(row=1, column=23, rowspan=15, sticky='NS')
    #汉字转url
    def tourl(self):
        import urllib.parse
        text = self.init_data_Text.get(1.0, END)
        url = urllib.parse.quote(text)
        self.result_data_Text.delete(1.0,END)
        self.result_data_Text.insert(1.0, '%s' % url)

    def urltoc(self):
        import urllib.parse
        text = self.init_data_Text.get(1.0, END)
        url = urllib.parse.unquote(text)
        self.result_data_Text.delete(1.0, END)
        self.result_data_Text.insert(1.0, '%s' % url)
    #json格式化
    def JSON(self):
        text = self.init_data_Text.get(1.0,END)
        js = json.dumps(text,sort_keys=True,indent=4,separators=(',', ':'))
        self.result_data_Text.insert(1.0, '%s'% js)


    def uploadfile(self):
        selectFileName = tkinter.filedialog.askopenfilename(title='选择文件,注意要是文本文件')  # 选择文件
        print(selectFileName)
        file1 = open('%s'% selectFileName,'rb')
        date = file1.read()

        m = chardet.detect(date)
        print(m)
        print('%s' % m['encoding'])
        if m['encoding'] is None:
            file = open('%s' % selectFileName, 'rb')

        else:
            file=open('%s'% selectFileName,'r',encoding='%s' % m['encoding'])
        self.init_data_Text.delete(1.0, END)
        self.init_data_Text.insert(1.0,'%s'% file.read())
        file.close()
        #统计单词字数
    # 思路 汉字一般是使用utf-8编码可以先转成unicode
    # 在unicode中常用汉字的范围一般是\u4e00-\u9fa5
    def word(self):
        text = self.init_data_Text.get(1.0,END)
        m = re.findall(r"(\b[a-zA-Z]+\b)",text)
        j = re.findall(r"([\u4e00-\u9fa5])",text)
        cpot = re.findall(r"([\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b])",text)
        epot = re.findall(r"([\.\?\!\,\:\-\_\(\)\'\"])" , text)
        print(cpot)
        print(epot)
        count = len(m)
        count1=len(j)
        count2=len(cpot)
        count3= len(epot)
        if count | count1:
            self.result_data_Text.delete(1.0, END)
            self.result_data_Text.insert(1.0, '单词数是:%d \n' % count)
            self.result_data_Text.insert(1.0,'汉字数量为:%d \n'% count1)
            self.result_data_Text.insert(1.0, '中文标点符号为:%d \n' % count2)
            self.result_data_Text.insert(1.0, '英文标点符号为:%d \n' % count3)
            self.write_log_to_Text("INFO:count word success")
        else:
            self.write_log_to_Text("INFO:your input have some bug")
    #汉字转16进制jbk编码
    def str_trans_to_gbk(self):
        text = self.init_data_Text.get(1.0 ,END).replace("\n","").encode('gbk')
        tar = repr(text)
        print(tar)
        self.result_data_Text.delete(1.0, END)
        self.result_data_Text.insert(1.0, '汉字转为16进制jbk编码为\n:%s'% tar)
        self.write_log_to_Text("INFO:str_trans_to_gbk success")
    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()

        # print("src =",src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                # print(myMd5_Digest)
                # 输出到界面
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")

            except:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")

#获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time
#日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)

def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    XUKGUI = WORD_GUI(init_window)
    # 设置根窗口默认属性
    XUKGUI.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()