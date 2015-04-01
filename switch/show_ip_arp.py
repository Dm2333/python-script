import telnetlib
import getpass
import sys

HOST = "172.17.7.1"
user = "test"
password = "Aaxis@1qaz"
spacetime = 1
def tl(ip):
    global spacetime
    tn = telnetlib.Telnet(ip)
    tn.read_until("Password:")
    tn.write(password+"\n")
    tn.read_until(">")
    tn.write("en\n")
    tn.read_until("Password:")
    tn.write(password+"\n")
    tn.read_until("#")
    tn.write("show ip arp\n")
    while spacetime <= 20:
        tn.write(" ")
        spacetime = spacetime + 1
    msg=tn.read_until("#")
    tn.write("exit\n")
    tn.close
    return msg
msg = tl(HOST)
print msg
with open(r"c:\arp.txt",'wb') as f:
    f.write(msg)
##path = r"c:\config.txt"
##f = file(path,"wb")
##f.write(msg)
##f.close()
##
##tn.close

raw_input('please input any key exit')


