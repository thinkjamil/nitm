import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
print host
s.bind((host, port))
s.listen(500)
while True:
	c, addr = s.accept()
	print 'Got connection from', addr
	msg =str(c.recv(1024))
	print 'client : ',msg
	c.send("Access Denied. GoodBye")
	c.close()
s.close()
