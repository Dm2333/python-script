
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
'''
���ƣ����ٶ��߳�ping����
������gyhong gyh9711
���ڣ�20:51 2011-04-25
'''
 
import pexpect
import datetime
from threading import Thread
 
host=["192.168.1.1","192.168.1.123","192.168.2.1",
"192.168.1.1","192.168.1.123","192.168.2.1",
"192.168.1.1","192.168.1.123","192.168.2.1",
"192.168.1.1","192.168.1.123","192.168.2.1",
"192.168.1.1"]
 
report_ok=[]
report_error=[]
class PING(Thread):
    def __init__(self,ip):
        Thread.__init__(self)
        self.ip=ip
    def run(self):
        Curtime = datetime.datetime.now()   
        #Scrtime = Curtime + datetime.timedelta(0,minute,0) 
        #print("[%s]����[%s]" % (Curtime,self.ip))
        ping=pexpect.spawn("ping -c1 %s" % (self.ip))
        check=ping.expect([pexpect.TIMEOUT,"1 packets transmitted, 1 received, 0% packet loss"],2)
        if check == 0:
            print("[%s] ��ʱ %s" % (Curtime,self.ip))
 
        elif check == 1:
            print ("[%s] %s �ɴ�" % (Curtime,self.ip))
 
        else:
            print("[%s] ����%s ���ɴ�" % (Curtime,self.ip))
 
 
#���߳�ͬʱִ��
T_thread=[]
for i in host:
    t=PING(i)
    T_thread.append(t)
for i in range(len(T_thread)):
    T_thread[i].start()
#
#print ("\n=========���������������==========\n")
#output(report_error)
#print ("\n=========���������������==========\n")
#output(report_ok)
 
