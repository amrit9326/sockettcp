import socket


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

l=input()
port=9999

s.bind((l,port))
s.listen(5)
def many(c):
	while True:
		g=c.recv(1024)
		print(g.decode('ascii'))
		p=input("Enter The Message:").encode('ascii')
		c.send(p)


while True:
    c,addr=s.accept()
    print(c,"socket running")
    many(c)

   
s.close()
