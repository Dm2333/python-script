import os
import sys
###info=os.getcwd()
###listfile=os.listdir(os.getcwd())
info="D:\MyDrivers"
target = raw_input("�������ʼ��")
while target != 'quit':
    target = raw_input("���������ַ�����")
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
##for line in listfile:  #��Ŀ¼�µ��ļ�����ֵ��line�������
##    print line         #��ӡ����ֵ������
##    #filename.write(filename)
##    if line[-4:] == '.inf':
##    
##            print line
##            out=open(line,'r')    #�����ȡline��������ݣ�Ҳ���Ƕ�ȡÿ���ļ�������
##            for com in out:       #��ÿ���ļ������ݣ�Ҳ����Ŀ¼�µ��ļ�����ֵ��com
##                filename.write(line+":  "  +com)
## 
##    else:
##       print (line+'  '+"���ļ���Ŀ¼��ʽ")
##filename.close()
