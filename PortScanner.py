#Python3

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

#setup host to scan from hack this site.com
#host = "137.74.187.100"
#port = 443
#Now making it user friendly
host = input("Plaese enter the IP you want to scan: ")
port = int(input("Please enter the port you want to scan:"))






def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:        
       print("The port is open")

portScanner(port)

    