import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
print host
s.bind((host, port))
s.listen(50)
filename='a'
state=0
option=0
while True:
    if state==0:
        c, addr = s.accept()
        print 'Got connection from', addr
        option =int(c.recv(1024))
        print 'option : ',option
        c.send(str(option))
        c.close()
	state=1
    elif state==1:
        c, addr = s.accept()
        print 'Got connection from', addr
        filename =str(c.recv(1024))
        print 'file name : ',filename
        c.send(filename)
        c.close()
        state+=1
        if option==2:
        	state=3
    elif state==2:
        c, addr = s.accept()
        print 'Got connection from', addr
        chunk_text =c.recv(4096)
        c.close()
        print 'Chunk : ',chunk_text
        f=open(filename,'wb+')
        f.write(chunk_text)
        f.close()
        print 'waiting for next'
        state = 0
    elif state==3:
        c, addr = s.accept()
        chunk_file = open(filename,'rb')
        c_txt=str(chunk_file.read())
        print 'Sending to', addr
        print c.recv(1024)
        c.send(c_txt)
        print c_txt
        c.close()
        chunk_file.close()
        state =0
        print 'Waiting for next'
s.close()
