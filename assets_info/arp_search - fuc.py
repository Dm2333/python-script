#coding:utf-8
import re
import pickle
import time
date =	time.strftime('%Y-%m-%d')
path =	r'arp_list_201524.txt'
def open_file(path):
        with open(path) as testfile:
                teststr=testfile.read()
        return teststr
def read_dump():
        with open ('arp.dump','rb') as f:
                try:
                        d = pickle.load (f)
                except EOFError:
                        d={}
        return d
def re_arp(files,dict):
        reg=re.compile(r"Internet\s+(\d+\.\d+\.\d+\.\d+)\s+\d+\s+(.{14})\s+ARPA\s+(Vlan\d+)")
        matchs=reg.finditer(files)
        for i in matchs:
                Ip = i.group(1).strip(" ")
                Mac = i.group(2).strip(" ")
                Product =i.group(3).strip(" ")
                dict[Mac] = [Ip,date,Product,'null']
        return dict
def write_dump(data):
        with open('arp.dump', 'wb') as f1:
                pickle.dump(data, f1)
if __name__ == '__main__':
        teststr = open_file(path)
        d = read_dump()
        print re_arp(teststr,d)



