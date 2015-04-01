import subprocess
import re
##key =re.compile("agcn1-wkeng\d*")
##key1=re.compile("AAXISCHINA\\s*")
user = 'jimluo'
password = 'Lj5653350'
f = open("C:\Users\jimluo\Desktop\PY\ip.txt",'r')
for line in f.readlines():
    ip = line.strip()
    print ip
    f1 = open("C:\Users\jimluo\Desktop\PY\computer_info.txt",'a')
    cmd = "wmic /node:%s /user:%s /password:%s COMPUTERSYSTEM get username,caption,model" %(ip,user,password)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line
        f1.write(line)
    f1.close()   

##    if line.find("agcn1-wkeng"):
##        print line[line.find("agcn1-wkeng"):line.find("agcn1-wkeng")+14]
##    if line.find("aaxischina"):
##        print line[line.find("aaxischina"):line.find("aaxischina")+14]
f.close()
retval = p.wait()
