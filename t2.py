import socket


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

l=input()
port=9999

s.connect((l,port))

while True:
     g=input("Enter The Input:")
     s.send(g.encode('ascii'))
     print(s.recv(1024).decode('ascii'))
     continue
s.close()
