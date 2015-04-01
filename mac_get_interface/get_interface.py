import telnetlib
import getpass
import sys
import re
mac = raw_input("please input mac address:")
Password = 'Aaxis@1qaz'
cmd = 'show mac address-table address'+' '+mac
cmd1 = 'show ip arp'+' '+mac
##mac = 'b8ac.6f2e.80c8'
address = '172.17.7.1'
tn = telnetlib.Telnet(address)
tn.read_until("Password:")
tn.write(Password+"\n")
tn.read_until(">")
tn.write(cmd1+"\n")
print tn.read_until(">")
print '================================'
tn.write(cmd+"\n")
msg = tn.read_until(">")
print msg
print '================================'
tn.close
print msg.find(r'Fa')
print msg[251:258]
p = re.compile(mac)
q = p.search(msg)
if q:
    m = re.compile(r'Fa1/0/\d')
    match = m.findall(msg)
    print match
    print '================================'
    a = match[0]
list={}
f = open(r'C:\Users\jimluo\Desktop\PY\mac_get_interface\core_list.txt', 'r')
for line in f.readlines():
    dk= line.split(" ")
    dk0 = dk[0]
    ip1 = dk[1]
    list[dk0]= ip1
print "on the switch:"+list[a]
ip2 =list[a].strip()
print '================================'
tn = telnetlib.Telnet(ip2)
tn.write(Password+"\n")
tn.read_until(">")
tn.write("en\n")
tn.read_until("Password:")
tn.write(Password+"\n")
tn.read_until("#")
tn.write(cmd+"\n")
msg=tn.read_until("#")
print msg
raw_input("PRESS ANY KEY TO EXIT")

