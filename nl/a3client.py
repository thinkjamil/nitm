#!/usr/bin/python
#Multi-client chat application keeping chat records.
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

class chatapp:

	def __init__(self):
		self.top = Tk()
		self.chat_text=Text(self.top)
		self.chat_text.grid(row=1,column=1,columnspan=3,rowspan=10)
		self.send_text=Entry(self.top)
		self.name_text=Entry(self.top)
		self.send_text.grid(row=0,column=0,columnspan=2)
		self.name_text.grid(row=0,column=2,columnspan=1)
		self.send_button = Button(self.top, text ="send", command = lambda:self.send_it())
		self.send_button.grid(row=0,column=3)
		
		server=threading.Thread(target=self.listenN,args=())
		server.start()
		self.top.mainloop()
	def listenN(self):
		try:
			mysocket.connect((host, port))
		except:
			self.chat_text.insert(END,'Not ')
		self.chat_text.insert(END,"Connected.\n")
		while 1:
			socket_list = [mysocket]
			ready_to_read,ready_to_write, in_error = select.select(socket_list, [], [], 0)
			for sock in ready_to_read:
		        	if sock == mysocket:
			                data = sock.recv(4096)
			                if not data:
						self.chat_text.insert(END,'\nDisconnected from chat server')
						return 1
			                else:
						self.chat_text.insert(END,data+"\n")
		
	def send_it(self):
		
		self.stxt="["+self.name_text.get()+"]"+self.send_text.get()+"\n"
		#self.chat_text.insert(END,self.stxt)
   		mysocket.send(self.stxt)


app=chatapp()
