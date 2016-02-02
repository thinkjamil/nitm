import socket
from datetime import timedelta, datetime
vtable={}
def create_table():
	with open("version_data") as f:
		for line in f:
			tokens = line.split(':')
			vtable[tokens[0]] = [tokens[1],tokens[2:]]
def write_table():
	db=''
	for i,j in vtable.items():
		datestr=''
		k=j[1]
		datestr="{}:{}:{}:{}:{}".format(k[0],k[1],k[2],k[3],k[4])
		line="{}:{}:{}".format(i,j[0],datestr)
		db=db+line
	f=open("version_data",'w')
        f.write(db)
        f.close()
        create_table()
def findversion(filename):
	try:
		version_date=vtable[filename]
	except KeyError:
		return None
	return version_date[0]

create_table()

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
		elif option==4:
			state=4
	elif state==2:
		c, addr = s.accept()
		print 'Got connection from', addr
		chunk_text =c.recv(4096)
		c.close()
		print 'Chunk : ',chunk_text
		f=open(filename,'wb+')
		f.write(chunk_text)
		f.close()
		nowstr=datetime.now()
		versn="1"
		if findversion(filename):
			a=vtable[filename]
			versn=str(int(a[0])+1)
		vtable[filename]=[versn,[nowstr.year, nowstr.month, nowstr.day, nowstr.hour, str(nowstr.minute)+'\n']]
		write_table()
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
	elif state==4:
		c, addr = s.accept()
		a=vtable[filename]
		k=a[1]
		datestr="{}:{}:{}:{}:{}".format(k[0],k[1],k[2],k[3],k[4])
		detail="filename : {} version : {} date : {}".format(filename,a[0],datestr)
		print 'Sending detail to', addr
		print c.recv(1024)
		c.send(detail)
		print detail
		c.close()
		state =0
		print 'Waiting for next'
s.close()
