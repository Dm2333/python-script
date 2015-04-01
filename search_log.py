
import sys
import re
mail = r'\w*@aaxischina.com'
a = {'':''}
k =[]
print a
key = re.compile(r"\(\w{16}\)")
user = re.compile(mail)
f = open('C:\Users\jimluo\Desktop\log.txt', 'r')
for line in f.readlines():
    m = key.search(line)
    n = user.search(line)
    if m and n:
        k = m.group()
        u = n.group()
        if u in a:
            a
        a[u]= k
print a            
##print a
##for zu in a:
##    print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
##    print zu
##    f = open('C:\Users\jimluo\Desktop\PY\log.txt', 'r')
##    for line in f.readlines():
##        
##        log = line.find(r"%s"%zu)
##        if log != -1 :
##            print line




            
##for i, v in enumerate(a):
##    if v not in b:
##        b[v] = []
##    b[v].append(i)

##f = open('C:\Users\jimluo\Desktop\log.txt', 'r')
##for line in f.readlines():
##    log = line.find(r'93350005ff2273f5')
##    
##    if log != -1 :
##
##        print line


##while newstr.find("a") >= 0:
##
##  newstr = newstr[newstr.find("a")+1:]

##a = ['a','b','c','d','a','b','c','d','a','b','c','d']
##b = {}
##for i, v in enumerate(a):
##    if v not in b:
##        b[v] = []
##    b[v].append(i)
##
##print b
### {'a': [0, 4, 8], 'c': [2, 6, 10], 'b': [1, 5, 9], 'd': [3, 7, 11]}
