import nmap
np=nmap.PortScanner()
print(np.nmap_version())
np.scan('192.168.0.1','22-445','-v --version-all')
#print(np.scaninfo())
#print(np.csv())
print(np.scanstats())
#print(np.all_hosts())
#print(np['192.168.0.1'].state())
#print(np['192.168.0.1'].all_protocols())
#print(np['192.168.0.1']['tcp'].keys())
print(np['192.168.0.1'].has_tcp(22))