#coding:utf-8
import re
import pickle
import time
date = time.strftime('%Y-%m-%d')
testfile=open(r"TAISlist.txt")
teststr=testfile.read()
reg=re.compile(r"Nmap scan report for (\d+\.\d+\.\d+\.\d+)\n.+\n.+?:(.{18})\((.+)\)",re.M)
matchs=reg.finditer(teststr)
testfile.close()
with open ('dump.txt','rb') as f:
     try:
            d = pickle.load (f)
     except EOFError:
            d={}
f.close()
for i in matchs:
    Ip = i.group(1).strip(" ")
    Mac = i.group(2).strip(" ")
    Product =i.group(3).strip(" ")
    d[Mac] = [date,Ip,Product]
f1 = open('dump.txt', 'wb')
pickle.dump(d, f1)
f1.close()




