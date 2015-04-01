#coding:utf-8
import re
import pickle
import time
date = time.strftime('%Y-%m-%d')
testfile=open(r"arp_list_201524.txt")
teststr=testfile.read()
testfile.close()
reg=re.compile(r"Internet\s+(\d+\.\d+\.\d+\.\d+)\s+\d+\s+(.{14})\s+ARPA\s+(Vlan\d+)")
matchs=reg.finditer(teststr)
with open ('arp.dump','rb') as f:
     try:
            d = pickle.load (f)
     except EOFError:
            d={}
f.close()
for i in matchs:
    Ip = i.group(1).strip(" ")
    Mac = i.group(2).strip(" ")
    Product =i.group(3).strip(" ")
    d[Mac] = [Ip,date,Product,'null']

f1 = open('arp.dump', 'wb')
pickle.dump(d, f1)
f1.close()



