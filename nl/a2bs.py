#!/usr/bin/python
#Client server multi-client shop application using a python GUI.
#Server part


import sys
import socket
import select

host = '127.0.0.1'
port = 12345
recv_buffer = 4096

class shopserver:
	def __init__(self):
		self.serv_list=[]
		self.mango=10
		self.banana=20
		self.apple=25
		ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ssocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
		ssocket.bind((host,port))
		ssocket.listen(10)
		self.serv_list.append(ssocket)
		print "Starting server on port: "+host+":", str(port)
		while 1:
			rtread, rtwrite, in_error = select.select(self.serv_list, [],[],0)
			for sock in rtread:
				print rtread
				print sock
				if sock == ssocket:
					sockfd, addr = ssocket.accept()
					self.serv_list.append(sockfd)
					print("Client Added: (%s, %s) " % addr)
					self.broadcast(ssocket,sockfd, str(self.mango)+'.'+str(self.banana)+'.'+str(self.apple))
        		else:
					try:
						data = str(sock.recv(recv_buffer))
						if data:
							print data
							tmp=data.split('.')
							self.mango=self.mango-int(tmp[0])
							self.banana=self.banana-int(tmp[1])
							self.apple=self.apple-int(tmp[2])
							print '\nbrd'
							self.broadcast(ssocket,sockfd, str(self.mango)+'.'+str(self.banana)+'.'+str(self.apple))
							print 'brd done'
					except:
						hiu=0
		ssocket.close()
	def broadcast(self,ssocket, sock, message):
		for socket in self.serv_list:
			if socket != ssocket:
				try:
					socket.send(message)
				except:
					socket.close()
					if socket in self.serv_list:
						self.serv_list.remove(socket)

mango_shop=shopserver()
