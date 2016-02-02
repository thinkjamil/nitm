#!/usr/bin/python
#Client server multi-client shop application using a python GUI.
#Server part


import sys
import socket
import select

host = '127.0.0.1'
port = 12345

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
		while True:
			c, addr = ssocket.accept()
			data = str(c.recv(4096))
			print data
			if data == '0.0.0':
				print 'sending qty'
			else :
				tmp=data.split('.')
				self.mango=self.mango-int(tmp[0])
				self.banana=self.banana-int(tmp[1])
				self.apple=self.apple-int(tmp[2])
			c.send(str(self.mango)+'.'+str(self.banana)+'.'+str(self.apple))
			c.close()
		ssocket.close()

mango_shop=shopserver()
