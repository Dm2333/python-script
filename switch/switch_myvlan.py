import telnetlib
import getpass
import sys
import time

HOST = "172.17.1.7"
id = raw_input('please input the vlan id:')
vlanid = "switchport access vlan %s\n" %id
password = "Aaxis@1qaz"
spacetime = 1

tn = telnetlib.Telnet(HOST)
tn.read_until("Password:")
tn.write(password+"\n")
tn.read_until(">")
tn.write("en\n")
tn.read_until("Password:")
tn.write(password+"\n")
tn.read_until("#")
tn.write("conf t\n")
tn.read_until("#")
tn.write("int fa0/3\n")
tn.read_until("#")
time.sleep(5)
print tn.read_very_eager()
tn.write(vlanid)
print tn.read_until("#")
tn.close
raw_input('please input any key exit')


