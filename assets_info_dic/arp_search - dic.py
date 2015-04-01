#coding:utf-8
import re
import pickle
import time
dic1 = {}
date = time.strftime('%Y-%m-%d')
testfile=open(r"arp_list_201524.txt")
teststr=testfile.read()
testfile.close()
reg=re.compile(r"Internet\s+(\d+\.\d+\.\d+\.\d+)\s+\d+\s+(.{14})\s+ARPA\s+(Vlan\d+)")
matchs=reg.finditer(teststr)
with open ('arp_dic.dump','rb') as f:
     try:
            dic = pickle.load (f)
     except EOFError:
            dic ={}
f.close()
for i in matchs:
    Ip = i.group(1).strip(" ")
    Mac = i.group(2).strip(" ")
    Product =i.group(3).strip(" ")
    dic1[Mac]={ 'IP':Ip,'product':Product}
    if dic.has_key(Mac):
        if dic[Mac]['IP']!= dic1[Mac]['IP']:
           dic.update(dic1)
           print Mac
    else:       
       dic[Mac]={'time':date,'IP':Ip,'product':Product}
       print 'new'
print dic
##for k,v in dic.items():
##   for i,j in v.items():
##           print j
f1 = open('arp_dic.dump', 'wb')
pickle.dump(dic, f1)
f1.close()



