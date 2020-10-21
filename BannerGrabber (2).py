#import socket


#s = socket.socket()

#ip = input("please enter IP:")
#port = str(input("Please enter the port:"))
##two parameter needed for the connection
#s.connect((ip, int(port)))
      ##max size of data
#print(s.recv(1024))



#now with functions 
import socket

def main(ip, port):
s = socket.socket()
s.connect((ip, int(port)))
s.settimeout(5)
print(str(s.recv(1024)).strip('b'))# getting rid of b string strip method


ip = input("Please enter the IP: ")
port = str(input("Please enter the port:"))
banner(ip, port)
main()
