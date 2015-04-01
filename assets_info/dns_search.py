#coding:utf-8
import re
import pickle
import time
date = time.strftime('%Y-%m-%d')
testfile=open(r"dns201524.txt")
teststr=testfile.read()
testfile.close()
d ={}
reg=re.compile(r"(\w{5}-\w*)\s+Host\s+\(A\)\s+(172\.17\.\d+\.\d+)",re.M)
matchs=reg.finditer(teststr)
with open ('arp.dump','rb') as f:
     try:
            d = pickle.load (f)
     except EOFError:
            d={}
f.close()
for i in matchs:
    IT_tag = i.group(1).strip(" ")
    IP = i.group(2).strip(" ")
    for key, info in d.items():
        if  info[0] == IP:
            d[key][3] = IT_tag 
##for key, info in d.items():
##    print info
f1 = open('arp.dump', 'wb')
pickle.dump(d, f1)
f1.close()

