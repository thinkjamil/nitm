import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.connect((host, port))
print 'Got connected'
s.send("Hello from client")
msg=str(s.recv(1024))
print 'server : ',msg
s.close()

