#coding:utf-8
import re
import pickle
import time
date = time.strftime('%Y-%m-%d')
testfile=open(r"dns201524.txt")
teststr=testfile.read()
testfile.close()
reg=re.compile(r"(\w{5}-\w*)\s+Host\s+\(A\)\s+(172\.17\.\d+\.\d+)",re.M)

matchs=reg.finditer(teststr)
with open ('arp_dic.dump','rb') as f:
     try:
            dic = pickle.load (f)
     except EOFError:
            dic={}
f.close()
for i in matchs:
    IT_tag = i.group(1).strip(" ")
    IP = i.group(2).strip(" ")
    dic1 ={'IP':IP,'IT_tag':IT_tag}
    for key, info in dic.items():
           for k,v in info.items():
                  if dic[key]["IP"] == IP:
                     dic[key].update(dic1)
                     print "update%s\n" %IP

f1 = open('arp_dic.dump', 'wb')
pickle.dump(dic, f1)
f1.close()

