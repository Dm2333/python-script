#!coding:utf-8
import sys
import re
text=r'google_.* = .*'
context =' '
iplist = '192.168.1.1'
def change_ip(argv):
    global context
    with open(argv, 'r') as f:
        info=f.readlines()
    for i in info:
        if (i.find('google_cn = ') >=0):
           i=  'google_cn = '+iplist+'\n'
           print i
        context = context + i
    open('new_proxy.ini','w').writelines(context)           
def main():
##    argv=sys.argv
##    print argv
    change_ip('D:\py\goagent_ip\proxy.ini')
    
        
if __name__ == '__main__':
    main()

