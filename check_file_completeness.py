import re
import os
#检测是否全部是文件夹
def check_all_isfolder(folder_list, path):
    for folder in folder_list:
        temp_file = os.path.join(path, folder)
        if not os.path.isdir(temp_file):
            print(path, "中 %s 不是文件夹形式,请检查！！！" % folder)
        else:
            pass

#检查文件完整性
def check_file_intact(need_check_path):
    if os.path.isdir(need_check_path):
        pattern = re.findall(r"_([^\\]*$)", need_check_path)
        file_list = os.listdir(need_check_path)
        for file_name in file_list:
            if pattern[0] in file_name or file_name.endswith(".html") or "预期配置" in file_name:
                temp_dir = os.path.join(need_check_path, file_name)
                if os.path.isdir(temp_dir):
                    check_pcap_intact(temp_dir, pattern[0])
                else:
                    pass
            else:
                print("%s ERROR file,delete running" % file_name)
                delete_abnormal_file(os.path.join(need_check_path, file_name))
        if len(os.listdir(need_check_path)) == 2 or len(os.listdir(need_check_path)) == 5:
            #print("%s 下目录很完备！"% need_check_path)
            pass
        else:
            print("%s 下目录有问题，需要检查！" % need_check_path)
#检测pcap文件
from pypinyin import *
def check_pcap_intact(need_check_path, pattern):
    new_pattern = ""
    for _ in pinyin(pattern, style=NORMAL):
        new_pattern += _[0]

    file_list = os.listdir(need_check_path)
    for file_name in file_list:
        if new_pattern in file_name and file_name.endswith(".pcap"):
            pass
        else:
            print("%s ERROR file,delete running" % file_name)
            delete_abnormal_file(os.path.join(need_check_path, file_name))


#删除不规则文件
def delete_abnormal_file(file_path):
    if os.path.isdir(file_path):
        os.removedirs(file_path)
    else:
        os.remove(file_path)
base_dir = "F:\\test\\appdir"
file_list_classes = os.listdir(base_dir)
check_all_isfolder(file_list_classes, base_dir)
for folder in file_list_classes:
    new_dir_path = os.path.join(base_dir, folder)
    if os.path.isdir(new_dir_path):
        app_son_file_list = os.listdir(new_dir_path)

        check_all_isfolder(app_son_file_list, new_dir_path)
        for app in app_son_file_list:
            need_check_path = os.path.join(new_dir_path, app)

            check_file_intact(need_check_path)

    else:
        pass
