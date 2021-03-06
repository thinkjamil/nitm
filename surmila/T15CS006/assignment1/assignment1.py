# Assignment 1
#encrypt, cut and send file to server
#download, and update the file part to server

import socket
import os

host = '192.168.5.58' #'127.0.0.7'
port = 12345
alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","@","*","%","1","2","3","4","5","6","7","8","9","0","$","\n","'",'"','(',')','-',"+",'/','\\','.',',',':','\t']
total_alpha=len(alphabet)

def client_read_file():
    filename=str(raw_input("Enter the file name :"))
    chunk_no=str(raw_input("Enter chunk number :"))
    key=str(raw_input("Enter key to decrypt :"))
    send_filename(filename)
    send_chunk_no(chunk_no)
    c_txt=read_chunk()
    p_txt=decrypt(c_txt,key)
    pfile=open(filename+str(chunk_no),'wb')
    pfile.write(p_txt)
    print "File Downloaded."
    
    
def client_update_chunk():
	filename=str(raw_input("Enter file name : "))
	key=str(raw_input("Enter key for encrytion : "))
	chunk_no=int(raw_input("Enter chunk no : "))
	chunk_size=os.stat(filename+str(chunk_no)).st_size
	send_option(3)
	encrypt(filename+str(chunk_no),key)
	send_chunk_size(chunk_size)
	file=open(filename+str(chunk_no)+'c','rb')
	cfile_txt=file.read()
	send_filename(filename+'c'+str(chunk_no))
	send_chunk(cfile_txt)

def client_input_file():
    filename=str(raw_input("Enter file name : "))
    key=str(raw_input("Enter key for encrytion : "))
    chunk_size=int(raw_input("Enter chunk size : "))
    encrypt(filename,key)
    filename=filename+'c'
    file=open(filename,'rb')
    filesize=os.stat(filename).st_size
    send_option(1)
    send_chunk_size(chunk_size)
    send_filename(filename)
    send_filesize(filesize)
    flag=1
    file_index=0
    chunk_no=0
    while (flag):
        file.seek(file_index)
        file_txt=str(file.read(chunk_size))
        print file_txt
        chunk_no+=1
        if (file_txt==""):
            flag=0
        else:
            send_chunk(file_txt)
        file_index+=chunk_size
#	os.remove(filename)
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
    s.connect((host, port))
    s.send("Requested")
    c_txt=str(s.recv(1024))
    s.close()
    return c_txt
def send_option(option):
    s=socket.socket()
    s.connect((host, port))
    s.send(str(option))
    op=int(s.recv(1024))
    if option==op:
        print "option sent"
    s.close()
    
def send_chunk(chunk):
    s=socket.socket()
    s.connect((host, port))
    s.send(chunk)
    print s.recv(1024)
    s.close()
def send_chunk_size(chunk_size):
    s=socket.socket()
    s.connect((host, port))
    s.send(str(chunk_size))
    cs=int(s.recv(1024))
    if chunk_size==cs:
        print "chunk size sent"
    s.close()
def send_chunk_no(chunk_no):
    s=socket.socket()
    s.connect((host, port))
    s.send(str(chunk_no))
    #cs=int(s.recv(1024))
    #if chunk_no==cs:
    #    print "chunk no sent"
    c_txt=str(s.recv(1024))
    s.close()
def send_filename(filename):
    s=socket.socket()
    s.connect((host, port))
    s.send(filename)
    if filename == str(s.recv(1024)):
        print "filename sent"
    s.close()
def send_filesize(fsize):
    s=socket.socket()
    s.connect((host, port))
    s.send(str(fsize))
    if fsize == int(s.recv(1024)):
        print "file size sent"
    s.close()

def start_me():
    option = int(raw_input("Enter 1 to send file, 2 to fetch file chunk, 3 to update a file chunk :"))
    if option ==1:
        client_input_file()
    elif option ==2:
        send_option(2)
        client_read_file()
    elif option==3:
		client_update_chunk() 
    else:
        print "Good Bye"
        
start_me()
