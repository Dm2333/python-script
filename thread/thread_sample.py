# -*- coding: utf-8 -*-
import threading
import time
ip_range = raw_input("ip range:")
ip_list=[]
for i in range(0,255):
    ip = "%s.%s"% (ip_range,i)
    ip_list.append(ip)
print ip_list
mutex = threading.Lock()
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
 
    def run(self):
        global ip_list, mutex
        time.sleep(1);
        if mutex.acquire():
            print "I am %s, set counter:%s" % (self.name, ip_list[0])
            del ip_list[0]
            mutex.release()
 
if __name__ == "__main__":
    while True:
       for i in range(0, 10):
          my_thread = MyThread()
          my_thread.start()
       my_thread.join()
            
