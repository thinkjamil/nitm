#!/usr/bin/python
#Client server multi-client shop application using a python GUI.
#client part

import sys
import socket
import select
from Tkinter import *
import threading

host = '127.0.0.1'
port = 12345
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.settimeout(10)

class shopapp:

	def __init__(self):
		self.top = Tk()
		self.req_text=Text(self.top)
		self.req_text.grid(row=1,column=1,columnspan=3,rowspan=10)
		self.send_text=Entry(self.top)
		self.send_text.grid(row=0,column=0,columnspan=3)
		self.send_button = Button(self.top, text ="Buy", command = lambda:self.send_it())
		self.send_button.grid(row=0,column=3)
		
		server=threading.Thread(target=self.listenN,args=())
		server.start()
		self.top.mainloop()
	def listenN(self):
		try:
			mysocket.connect((host, port))
		except:
			self.req_text.insert(END,'Not ')
		self.req_text.insert(END,"Connected.\n")
		while 1:
			socket_list = [mysocket]
			ready_to_read,ready_to_write, in_error = select.select(socket_list, [], [], 0)
			for sock in ready_to_read:
		        	if sock == mysocket:
			                data = sock.recv(4096)
			        if not data:
						self.req_text.insert(END,'\nDisconnected from chat server')
						return 1
			        else:
			        	tmp=data.split('.')
			        	#self.req_text.delete('0',END)
			        	self.req_text.insert(END,"MANGO: {},BANANA: {},APPLE: {}\n".format(str(tmp[0]),str(tmp[1]),str(tmp[2])))
		
	def send_it(self):
		self.stxt=self.send_text.get()
   		mysocket.send(self.stxt)


app=shopapp()
