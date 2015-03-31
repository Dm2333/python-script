#!/usr/bin/env python
#coding:utf-8
import socket
import time
i = 1
address= raw_input ('please input ip address:')
port= int(raw_input ('please input port:'))
while i <= 100:
  i += 1
  if __name__=='__main__':
    s = socket.socket()
    request_string = "GET %s HTTP/1.1\r\nHost: %s\r\n\r\n" % ("/78311.htm", address)
    print "Attempting to connect to %s on port %s" % (address, port)
    try:
        s.connect((address, port))
        print "Connected to %s on port %s" % (address, port)
        s.send(request_string)
        #获取前100个字节
        print request_string
        rsp = s.recv(100)
        print '%d' %i
        print 'Received 100 bytes of HTTP response'
        print '|||%s|||' % rsp
    except socket.error, e:
        print "Connection to %s on port %s failed: %s" % (address, port, e)
        break
    time.sleep(5)
print "connetion down "
