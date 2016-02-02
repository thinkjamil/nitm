import socket
import thread

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12446
print host
s.bind((host, port))
s.listen(50)
filename='a'
chunk_text=''
state=0
option=0




def send_to_brother(ch,fn,ht,pt):
	print 'sending '+fn+'\n'+ch+'\n'+ht+':'+str(pt)
	send_option(1,ht,pt)
	send_filename(fn,ht,pt)
	send_chunk(ch,ht,pt)

def send_option(opt,h,p):
	so=socket.socket()
	so.connect((h, p))
	so.send(str(opt))
	op=int(so.recv(1024))
	if opt==op:
	    print "option sent"
	so.close()    
def send_chunk(ch,h,p):
	sc=socket.socket()
	sc.connect((h, p))
	sc.send(ch)
	sc.close()

def send_filename(fnm,h,p):
	sf=socket.socket()
	sf.connect((h, p))
	sf.send(fnm)
	if filename == str(sf.recv(1024)):
	   	print "filename sent"
	sf.close()



while True:
	if state==0:
		c, addr = s.accept()
		print '0 : Got connection from', addr
		option =int(c.recv(1024))
		print 'option : ',option
		c.send(str(option))
		c.close()
		state=1
	elif state==1:
		c, addr = s.accept()
		print '1 : Got connection from', addr
		filename =str(c.recv(1024))
		print 'file name : ',filename
		c.send(filename)
		c.close()
		state+=1
		if option==2:
			state=3
	elif state==2:
		c, addr = s.accept()
		print '2 : Got connection from', addr
		chunk_text =c.recv(4096)
		c.close()
		print 'Chunk : ',chunk_text
		f=open(filename,'wb+')
		f.write(chunk_text)
		f.close()
		print 'waiting for next'
		state = 0
		if option==4:
			state = 4
	elif state==3:
		c, addr = s.accept()
		print '3 : Got connection from', addr
		chunk_file = open(filename,'rb')
		c_txt=str(chunk_file.read())
		print 'Sending to', addr
		print c.recv(1024)
		c.send(c_txt)
		print c_txt
		c.close()
		chunk_file.close()
		state=0
		print 'Waiting for next'
	elif state==4:
		c, addr = s.accept()
		print '4 : Got connection from', addr
		hip =str(c.recv(1024))
		c.close()
		ad=hip.split(":")
		try:
			print 'creating thread'
			#thread.start_new_thread(send_to_brother,(chunk_text,filename,ad[0],int(ad[1]),))
			send_to_brother(chunk_text,filename,ad[0],int(ad[1]))
		except:
			print 'Thread Error\n'
		state=0
s.close()

