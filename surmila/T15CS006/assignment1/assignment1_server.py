import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '192.168.5.41'
port = 12345
print host
s.bind((host, port))
s.listen(500)
flag=1
filename='a'
filesize=0
chunk_so_far=0
state=0
chunk_size=0
chunk_no=0
option=0
while flag==1:
    if state==0:
        c, addr = s.accept()
        print 'Got connection from', addr
        option =int(c.recv(1024))
        print 'option : ',option
        c.send(str(option))
        c.close()
        if option ==1:
          state=1
        elif option==2:
          state=5
	elif option==3:
	  state=1
    elif state==1:
        chunk_so_far=0
        chunk_no=0
        c, addr = s.accept()
        print 'Got connection from', addr
        chunk_size =int(c.recv(1024))
        print 'chunk size : ',chunk_size
        c.send(str(chunk_size))
        c.close()
        state+=1
    elif state==2:
        c, addr = s.accept()
        print 'Got connection from', addr
        filename =str(c.recv(1024))
        print 'file name : ',filename
        c.send(filename)
        c.close()
        state+=1
        if option==3:
        	state=8
    elif state==3:
        c, addr = s.accept()
        print 'Got connection from', addr
        filesize =int(c.recv(1024))
        print 'file size : ',filesize
        c.send(str(filesize))
        c.close()
        state+=1
    elif state==4:
        c, addr = s.accept()
        print 'Got connection from', addr
        chunk_text =str(c.recv(1024))
        print 'Chunk : ',chunk_text
        f=open(filename+str(chunk_no),'wb+')
        f.write(chunk_text)
        chunk_no+=1
        c.send(chunk_text)
        c.close()
        chunk_so_far +=len(chunk_text)
        if chunk_so_far >= filesize:
            state = 0
    elif state==5:
        c, addr = s.accept()
        print 'Got connection from', addr
        filename =str(c.recv(1024))
        print 'file name : ',filename
        c.send(filename)
        c.close()
        state+=1
    elif state==6:
        c, addr = s.accept()
        print 'Got connection from', addr
        chunk_no =int(c.recv(1024))
        print 'Chunk no : ',chunk_no
        c.send(str(chunk_no))
        c.close()
        state+=1
    elif state==7:
        chunk_file = open(filename+'c'+str(chunk_no),'rb')
        c_txt=str(chunk_file.read())
        c, addr = s.accept()
        print '7.Got connection from', addr
        print c.recv(1024)
        c.send(c_txt)
        print c_txt
        c.close()
        state =0
        print 'Waiting for next'
    elif state==8:
	c, addr = s.accept()
	cf=open(filename,'wb')
        print 'Got chunk from', addr
        chunk_text =str(c.recv(chunk_size))
	cf.write(chunk_text)
	cf.close()
	print 'Chunk : ',chunk_text
        c.send(chunk_text)
        c.close()
        state = 0
        print 'Waiting for next'
    else:
        flag=0
s.close()
