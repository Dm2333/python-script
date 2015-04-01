import re
mac = 'b8ac.6f2e.80c8'
f = open('C:\Users\jimluo\Desktop\PY\Mac.txt', 'r')
for info in f.readlines():
    p = re.compile(mac)
    q = p.search(info)
    if q:
        print info
        m = re.compile(r'Fa1/0/\d')
        match = m.findall(info)
        a = match[0]
        break
list={}
f = open('C:\Users\jimluo\Desktop\PY\core_list.txt', 'r')
for line in f.readlines():
    dk= line.split(" ")
    dk0 = dk[0]
    ip1 = dk[1]
    list[dk0]= ip1
print list




