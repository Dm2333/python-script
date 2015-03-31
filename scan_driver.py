import os
import sys
###info=os.getcwd()
###listfile=os.listdir(os.getcwd())
info="D:\MyDrivers"
target = raw_input("任意键开始：")
while target != 'quit':
    target = raw_input("输入驱动字符串：")
    for root, dirs, files in os.walk(info):
        for fn in files:
            if  fn[-4:] == '.inf':
                filename = r"%s\%s" %(root,fn)
                print filename
##                out=open(filename,'r')
####                for line in out.readlines():
####                    if line.find(target)!= -1:
####                        print filename
####                        print line
####                        print '*********************'
####                        break

####filename=open(info+'file.txt','w')
####print listfile
###out=open(listfile,'r')
##
##for line in listfile:  #把目录下的文件都赋值给line这个参数
##    print line         #打印出赋值的内容
##    #filename.write(filename)
##    if line[-4:] == '.inf':
##    
##            print line
##            out=open(line,'r')    #定义读取line里面的内容，也就是读取每个文件的内容
##            for com in out:       #把每个文件的内容（也就是目录下的文件）赋值给com
##                filename.write(line+":  "  +com)
## 
##    else:
##       print (line+'  '+"该文件是目录形式")
##filename.close()
