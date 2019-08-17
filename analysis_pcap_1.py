#!/usr/bin/env python
#coding=utf-8
import binascii
import struct
class analysis_pcap:
    # 给出文件的初始地址
    def __init__(self, analyze_file="1.pcap", target_dict={}):
        self.analyze_file = analyze_file
        self.target_dict = target_dict

    def analysis_run(self):
        #将文件数据以二进制形式读取
        pcap_file = open("%s"% self.analyze_file, 'rb')
        file_data = pcap_file.read()
        #开始包数据解析
        pcap_num = 0       #记录pcap文件中数据包数量
        statics = {}        #记录包中的数据
        pcap_packet = {}
        file_locate = 24             #包头24字节舍去
        while file_locate < len(file_data):
            pcap_packet['len'] = file_data[file_locate + 12:file_locate + 16]
            packet_len = struct.unpack('I', pcap_packet['len'])[0]
            temp_dict = {}
            temp_dict["dmac"] = self.format_Mac(str(binascii.b2a_hex(file_data[file_locate+16:file_locate+22]).decode("utf8")))
            temp_dict["smac"] = self.format_Mac(str(binascii.b2a_hex(file_data[file_locate+22:file_locate+28]).decode("utf8")))
            temp_dict["sip"] = self.format_IP(str(binascii.b2a_hex(file_data[file_locate+42:file_locate+46]).decode("utf8")))
            temp_dict["dip"] = self.format_IP(str(binascii.b2a_hex(file_data[file_locate+46:file_locate+50]).decode("utf8")))
            file_locate = file_locate + packet_len + 16
            pcap_num += 1
            #将临时字典放入数据字典中
            statics["num_%d" % pcap_num] = temp_dict
        self.target_dict["pcap_num"] = pcap_num
        self.target_dict["statics"] = statics
        return self.target_dict

    def format_Mac(self, string=""):
        len_string = len(string)
        dst_string = ""
        i = 0
        while i <= len_string-2:
            if  dst_string != "":
                dst_string = dst_string+":"+string[i:i+2]
            else:
                dst_string += string[i:i+2]
            i += 2
        return dst_string

    def format_IP(self, string=""):
        len_string = len(string)
        dst_string = ""
        i = 0
        while i <= len_string-2:
            if  dst_string != "":
                dst_string = dst_string+"."+str(int(string[i:i+2], 16))
            else:
                dst_string += str(int(string[i:i+2], 16))
            i += 2
        return dst_string

# def main():
#     target_dict = analysis_pcap()
#     print(target_dict.analysis_run())
# if __name__ == '__main__':
#     main()