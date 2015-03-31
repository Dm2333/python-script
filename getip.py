#coding:utf-8
##for cnt in range(15,1,-1):  
##    address='172.17.1.'+str(cnt)
##    f = open('C:\Users\jimluo\Desktop\PY\ip.txt', 'a')
##    f.write(address+'\n')
##    f.close()
##    print address
##with open('C:\Users\jimluo\Desktop\PY\ip.txt', 'r') as f:
##    print f.read()
result = list()
f = open('C:\Users\jimluo\Desktop\PY\ip.txt', 'r')
for line in f.readlines():                          
    line = line.strip()
    print line
    if not len(line) or line.startswith('#'):         
        continue                                      
    result.append(line)                             
result.sort()                                       
print result
