import telnetlib
import getpass
import sys
pwd = "Aaxis@1qaz"
f = open('C:\Users\jimluo\Desktop\PY\ip.txt', 'r')
for line in f.readlines():                          
    address = line.strip()
    if not len(line) or line.startswith('#'):         
        continue 
    tn = telnetlib.Telnet(address)
    print address
    print "tn.read_until(">")"
    if "tn.read_until(">")" == True:
        tn.read_until(">")
        tn.write("en\n")
        tn.read_until("Password:")
        tn.write(pwd+"\n")
        print "if"
    else:
        tn.write(pwd+"\n")
        tn.read_until(">")
        tn.write("en\n")
        tn.read_until("Password:")
        tn.write(pwd+"\n")
        print "else"
   
    tn.read_until("#")
    tn.write("copy running-config tftp:\n")
    print address+"copy"
    tn.read_until("?")
    tn.write("172.17.7.55\n")
    tn.read_until("?")
    tn.write("\n")
    print address+"copy+done"
    tn.read_until("#")
    print address+"copy+done+!!!"
    tn.write("exit\n")
    print address+"done"
    tn.close
    print address+"close"
