import nmap
nm = nmap.PortScanner()
def scan(IP):
    while True:
        stats = nm.scan(IP,arguments='-sn')
        print stats['nmap']['scanstats']
scan("10.10.0.100")


