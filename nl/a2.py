#!/usr/bin/python
#Client server multi-client shop application using a python GUI.
#client part

import sys
import socket


host = '127.0.0.1'
port = 12345

class shopapp:

	def __init__(self):
		self.ask()
	def ask(self):
		reply=int(raw_input("\nEnter 1 to request qty or anything else to buy :"))
		if reply == 1:
			self.request()
		else:
			self.buy()
		self.ask()
	def request(self):
		s = socket.socket()
		s.connect((host, port))
		s.send('0.0.0')
		reply=str(s.recv(4096))
		s.close()
		tmp=reply.split('.')
		print "MANGO: {},BANANA: {},APPLE: {}\n".format(str(tmp[0]),str(tmp[1]),str(tmp[2]))

		
	def buy(self):
		b=str(raw_input("\nEnter amount in appropriate maner :"))
		s2 = socket.socket()
		s2.connect((host, port))
		s2.send(b)
		reply=str(s2.recv(4096))
		s2.close()
		tmp=reply.split('.')
		print "MANGO: {},BANANA: {},APPLE: {}\n".format(str(tmp[0]),str(tmp[1]),str(tmp[2]))

app=shopapp()
