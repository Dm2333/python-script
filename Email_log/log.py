import re
f =open("C:\Users\jimluo\Desktop\sys20150209.txt","r")
f1 =open("C:\Users\jimluo\Desktop\info.txt","w")
#f1 =open("C:\Users\jimluo\Desktop\sys20150130_final1.txt","w")
reg=re.compile(r"ccea000000ee0174")
d = {}
for i in f.readlines():
     match = reg.search(i)
     if match:
          print i
          f1.write(i)
##     if match:
##          key = match.group()
##          if d.has_key(key):
##               d[key].append(i)
##               print "yes"
##          else:
##               print "no"
##               d[key]=[]
##               d[key].append(i)
         #f1.write(i)
f1.close()
f.close()       
#f1.close()
