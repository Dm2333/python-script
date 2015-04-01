import pickle
f = open('arp_dic.dump', 'rb')
d = pickle.load(f)
f.close()
i=0
dell=0
vmware=0
f1 = open('result_dic.txt','w')
for k,v in d.items():
##      print "mac:%s----info%s" %(k,v)
      i+=1
      for x,y in v.items():
            if x == "IT_tag":
                  dell+=1
##        if v[2] == 'Dell': dell+=1
##        elif v[2] == 'VMware': vmware+=1
      f1.write("mac:%s----info%s\n" %(k,v))
print "total number:%s@dell:%s@vmware:%s" %(i,dell,vmware)
f1.close()
raw_input("quit")
