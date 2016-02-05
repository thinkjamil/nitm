#!/usr/bin/python
#Multi-client chat application keeping chat records.
#Server part


import sys
import socket
import threading
host = '127.0.0.1'
port = 12345
recv_buffer = 4096
class Server:
	def __init__(self):
		self.filename='a3_history'
		self.client_list=[]
		self.ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.ssocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
		self.ssocket.bind((host,port))
		self.ssocket.listen(10)
		print "Starting server, listening on port: "+host+":", str(port)
		while True:
			csock,caddr = self.ssocket.accept()
			print("Client Added: (%s, %s) " % caddr)
			self.client_list.append(csock)
			self.send_new_client(csock)
			cl_handler=threading.Thread(target=self.client_handler,args=(csock,caddr))
			cl_handler.start()
		
		
	def client_handler(self,sock,addr):
		while True:
			msg = sock.recv(recv_buffer)
			self.broadcast(msg)
			f=open(self.filename,'a+')
			f.write(msg)
			f.close()
			
	def broadcast(self,message):
		for sock in self.client_list:
			try:
				sock.send(message)
			except:
				sock.close()
				self.client_list.remove(sock)
				
	def send_new_client(self,sock):
		f=open(self.filename,'r+')
		oldmsg=str(f.read())
		f.close()
		sock.send(oldmsg)
		print oldmsg
s=Server()
