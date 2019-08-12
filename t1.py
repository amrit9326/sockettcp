import socket


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

l=input()
port=9999

s.bind((l,port))
s.listen(5)


while True:
    c,addr=s.accept()
    print(c,"socket running")
    g=c.recv(1024)
    print(g.decode('ascii'))
    c.send(input("Enter The Message:").encode('ascii'))
    continue
s.close()
