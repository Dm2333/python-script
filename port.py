#!/usr/bin/env python

import socket
from threading import Thread,activeCount,Lock
from time import ctime
mutex = Lock()
class Loop(Thread):
    def __init__(self,ip,port,que):
        Thread.__init__(self)
        self.ip     = ip
        self.port   = port
        self.que    = que
    def run(self):
        global mutex
        try:
            client = socket.socket()
            indicator = client.connect_ex((self.ip,self.port))
            if mutex.acquire(1):
                if indicator == 0:
                    que.append(self.ip+'\t'+str(self.port))
                else:
                    print self.ip,'\t',str(self.port),'不可达'
                mutex.release()
        except:
            if mutex.acquire(1):
                print self.ip,'\t',str(self.port),'不可达'
                mutex.release()
class Main(Thread):
    def __init__(self,ip,que):
        Thread.__init__(self)
        self.ip  = ip
        self.que = que
    def run(self):
        i = 0
        while i < 65536:
            if activeCount() <= 200:
                Loop(ip=self.ip,port=i,que=self.que).start()
                i = i + 1
if __name__ == '__main__':
    que = []
    ip = raw_input('IP=')
    main = Main(ip = ip,que = que)
    main.start()
    while True:
        if activeCount() <= 1 and main.isAlive() == False:
            break
    print ''
    f = open('portOpen.py','a')
    f.write("'''")
    f.write(ctime()+'\n')
    f.flush()
    for i in range(0,len(que)):
        print que[i]
        f.write('\t'+que[i]+'\n')
        f.flush()
    f.write("'''")
    f.close()
    raw_input()
##import socket  
##if __name__=='__main__':
##    print __name__
##    port=135  
##    s=socket.socket()  
##    for cnt in range(2,255):  
##        address='172.17.7.'+str(cnt)  
##        try:  
##            s.connect((address,port))  
##            print address  
##        except socket.error,e:  
##            print address+'Error OR Port Not Opened'
##
