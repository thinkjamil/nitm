# Assignment 2
#encrypt, cut file to 9 parts and make another part by taking exor of all 9 parts
#send file to server and  also send the server command to upload/update the file to other server
#download from server 1 or server 2 if former fails, and update the file part to server
#server list for all files is stored in a file, which is read every time the client starts


import socket
import os
from math import floor
import time

table={}
hosta = ''
hostb = ''
porta = 12446
portb =12456
tryb=False
alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","@","*","%","1","2","3","4","5","6","7","8","9","0","$","\n","'",'"','(',')','-',"+",'/','\\','.',',',':','\t']
total_alpha=len(alphabet)

def create_table():
	count=1
	with open("asg2_file") as f:
		for line in f:
			(a, b) = line.split(':')
			table[count] = [a,b[:-1]]
			count+=1
	print table
def set_host(cno):
	edge_list=table[cno]
	global hosta
	hosta=edge_list[0]
	global hostb
	hostb=edge_list[1]
	print 'hosta', hosta
	print 'hostb', hostb


def client_read_file():
    filename=str(raw_input("Enter the file name :"))
    chunk_no=int(raw_input("Enter chunk number :"))
    key=str(raw_input("Enter key to decrypt :"))
    set_host(chunk_no)
    send_option(2)
    send_filename2(filename+'c'+str(chunk_no))
    c_txt=read_chunk()
    p_txt=decrypt(c_txt,key)
    pfile=open(filename+str(chunk_no),'wb')
    pfile.write(p_txt)
    print "File Downloaded."
    
    
def client_update_chunk():
	filename=str(raw_input("Enter file name : "))
	key=str(raw_input("Enter key for encrytion : "))
	chunk_no=int(raw_input("Enter chunk no : "))
	set_host(chunk_no)
	send_option(3)
	encrypt(filename+str(chunk_no),key)
	file=open(filename+str(chunk_no)+'c','rb')
	cfile_txt=file.read()
	send_filename(filename+'c'+str(chunk_no))
	send_chunk(cfile_txt)

def client_input_file():
	filename=str(raw_input("Enter file name : "))
	key=str(raw_input("Enter key for encrytion : "))
	encrypt(filename,key)
	filename=filename+'c'
	file=open(filename,'rb')
	filesize=os.stat(filename).st_size
	chunk_size=int(floor(filesize/9))
	if filesize%9 > 0:
		chunk_size=chunk_size+1
	count=1
	file_index=0
	part10="\x00"*chunk_size
	while (count <10):
		set_host(count)
		send_option(4)
		send_filename(filename+str(count),4)
		file.seek(file_index)
		file_txt=str(file.read(chunk_size))
		part10=strxor(part10,file_txt)
		print '----parity----------'+part10
		print '-----file-----------'+file_txt
		count+=1
		send_chunk(file_txt,4)
		send_command(hostb+':'+str(portb))
		file_index+=chunk_size
		time.sleep(1)
	set_host(count)
	send_option(4)
	send_filename(filename+str(count),4)
	send_chunk(part10,4)
	send_command(hostb+':'+str(portb))
	time.sleep(1)
	print 'All chunks sent'

def encrypt(filename,key):
    file=open(filename,'rb')
    cfile=open(filename+'c','wb')
    plain=str(file.read())
    str_list=[]
    key_list=[]
    c1=[]
    c2=[]
    key_len=len(key)
    text_len=len(plain)
    
    overLap= text_len % key_len
    leftover= key[:overLap]
    random= text_len-overLap
    random = text_len/key_len
    key = (int(random)*key)+leftover
    
    for i in key:
        n=alphabet.index(i)
        key_list.append(n)
    for i in plain:
        n=alphabet.index(i)
        str_list.append(n)
    i=0
    while i<text_len:
        c1.append((str_list[i]+key_list[i])%total_alpha)
        i+=1
    for i in c1:
        c2.append(alphabet[i])
    cypher=''.join(c2)
    cfile.write(cypher)
    
def decrypt(text,key):
    str_list=[]
    key_list=[]
    p1=[]
    p2=[]
    key_len=len(key)
    text_len=len(text)
    
    overLap= text_len % key_len
    leftover= key[:overLap]
    random= text_len-overLap
    random = text_len/key_len
    key = (int(random)*key)+leftover
    
    for i in key:
        n=alphabet.index(i)
        key_list.append(n)
    for i in text:
        n=alphabet.index(i)
        str_list.append(n)
    i=0
    while i<text_len:
        p1.append((str_list[i]-key_list[i])%total_alpha)
        i+=1
    for i in p1:
        p2.append(alphabet[i])
    plain=''.join(p2)
    return plain
    
def read_chunk():
    s=socket.socket()
    if tryb:
    	s.connect((hostb, portb))
    else:
    	s.connect((hosta, porta))
    s.send("Requested")
    c_txt=str(s.recv(4096))
    s.close()
    return c_txt
def send_option(option):
	if option==4:
		s=socket.socket()
		s.connect((hosta, porta))
		s.send(str(option))
		op=int(s.recv(1024))
		if option==op:
		    print "option sent"
		s.close()
	else:
		s=socket.socket()
		s.connect((hosta, porta))
		s.send(str(option))
		op=int(s.recv(1024))
		if option==op:
		    print "option sent"
		s.close()
		s=socket.socket()
		if (option!=op and option==2) or option!=2:
			s.connect((hostb, portb))
			s.send(str(option))
			op=int(s.recv(1024))
			if option==op:
				print "option sent"
			s.close()
			tryb=True
    
def send_chunk(chunk,option=1):
	if option==4:
		s=socket.socket()
		s.connect((hosta, porta))
		s.send(chunk)
		s.close()
	else:
		s=socket.socket()
		s.connect((hosta, porta))
		s.send(chunk)
		s.close()
		s=socket.socket()
		s.connect((hostb, portb))
		s.send(chunk)
		s.close()

def send_filename(filename,option=1):
	if option==4:
		s=socket.socket()
		s.connect((hosta, porta))
		s.send(filename)
		if filename == str(s.recv(1024)):
		   	print "filename sent"
		s.close()
	else:
		s=socket.socket()
		s.connect((hosta, porta))
		s.send(filename)
		if filename == str(s.recv(1024)):
		   	print "filename sent"
		s.close()
		s=socket.socket()
		s.connect((hostb, portb))
		s.send(filename)
		if filename == str(s.recv(1024)):
		   	print "filename sent"
		s.close()
def send_filename2(filename):
    if not tryb:
    	s=socket.socket()
    	s.connect((hosta, porta))
    	s.send(filename)
    	if filename == str(s.recv(1024)):
        	print "filename sent"
    	s.close()
    else:
    	s=socket.socket()
    	s.connect((hostb, portb))
    	s.send(filename)
    	if filename == str(s.recv(1024)):
        	print "filename sent"
    	s.close()
def send_command(hostad):
	print 'Sending command\n'
	s=socket.socket()
	s.connect((hosta, porta))
	s.send(hostad)
	print "host port sent"
	s.close()
    	
    	
    
def strxor (s0, s1):
	l = [ chr ( ord (a) ^ ord (b) ) for a,b in zip (s0, s1) ]
	return ''.join (l)

def start_me():
    option = int(raw_input("Enter 4 to send file, 2 to fetch file chunk, 3 to update a file chunk"))
    if option ==4:
        client_input_file()
    elif option ==2:
        client_read_file()
    elif option==3:
		client_update_chunk() 
    else:
        print "Good Bye"
        
create_table()
start_me()
