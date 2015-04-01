import pickle
def find():
        f = open('arp.dump', 'rb')
        d = pickle.load(f)
        f.close()
        i=0
        dell=0
        vmware=0
        f1 = open('result.txt','w')
        for k,v in d.items():
        ##        print "mac:%s----info%s" %(k,v)
                i+=1
                if len(v)>=4:
                        dell+=1
        ##        if v[2] == 'Dell': dell+=1
        ##        elif v[2] == 'VMware': vmware+=1
                f1.write("mac:%s----info%s\n" %(k,v))
        return "total number:%s@dell:%s@vmware:%s" %(i,dell,vmware)
        
        f1.close()
