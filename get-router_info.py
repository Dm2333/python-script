import telnetlib
import getpass
import sys
##mac = raw_input("please input mac address:")
Password = 'Aaxis@net12315'
cmd = 'show ip nat statistics \n'
cmd1 = 'show crypto isakmp sa \n'
##mac = 'b8ac.6f2e.80c8'
username = 'ciscort01'
print 0
tn = telnetlib.Telnet("10.2.0.5")
tn.read_until("Username:")
print 1
tn.write(username+"\n")
tn.read_until("Password:")
tn.write(Password+"\n")
print 2
tn.read_until("#")
print 3
while True :
    tn.write(cmd+"\n")
    print tn.read_until("#")
    tn.write(cmd1+"\n")
    print tn.read_until("#")
    print 'continue....please press enter'
    a=raw_input("please input quit:")
    if a == 'quit':
        break
    else:
        print 'continue'
tn.close()

