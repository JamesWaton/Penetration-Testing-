#end map scanner


import nmap


scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<---------------------------------------------------------------------->")

ip_addr = input("Please enter the IP address ypu want to scan:   ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run 
                         1)SYN ACK Scan
                         2)UDP Scan
                         3) Comprehensive Scan \n""")
print("You have selceted option: " , resp)


if resp =='1':
    print("Nmap Version: ", scanner.nmap_version())  #same as a usual nmap scan in console
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip status: ", scanner[ip_addr].state()) #to tell if online or offline
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp =='2':
    print("Nmap Version: ", scanner.nmap_version())  #same as a usual nmap scan in console
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Ip status: ", scanner[ip_addr].state()) #to tell if online or offline
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())    
