# -*- coding: utf-8 -*-
import threading
import time
import pickle
import threading, time, random
import subprocess
from Queue import Queue
q = Queue()
NUM = 5
user = 'jimluo'
password = 'Lj5653350'
ip_list = []
f = open('arp.dump', 'rb')
d = pickle.load(f)
f.close()
i=0
mutex = threading.Lock()
for (k,v) in d.items():
##    print "mac:%s----date:%s----IP:%s----product:%s\n" %(k,v[0],v[1],v[2])
    i+=1
    ip_list.append(v[1])
print ip_list
class SubThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global user,password,mutex
        while True:
            ip = q.get()
            print q.qsize()
            print "current has %d threads\n" % (threading.activeCount() - 1)
            cmd = "wmic /node:%s /user:%s /password:%s COMPUTERSYSTEM get username,caption,model" %(ip,user,password)
            print ip
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in p.stdout.readlines():
                print line
            q.task_done()
        
if __name__ == '__main__':
      for i in range(NUM):
        t = SubThread()
        t.setDaemon(True)
        t.start()
      
    #把JOBS排入队列
      for i in ip_list:
        q.put(i)
    #等待所有JOBS完成
      print 'all done'
