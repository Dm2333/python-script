import telnetlib
import getpass
import sys

HOST = "172.17.1.7"
user = "test"
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
tn.write("show run\n")
while spacetime <= 20:
    tn.write(" ")
    spacetime = spacetime + 1
msg=tn.read_until("#")
tn.write("exit\n")
print msg
path = r"c:\config.txt"
f = file(path,"wb")
f.write(msg)
f.close()

tn.close

raw_input('please input any key exit')


