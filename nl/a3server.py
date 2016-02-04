#!/usr/bin/python
#Client server multi-client chat application using a python GUI.
#Server part


import sys
import socket
import select
import sqlite3

host = '127.0.0.1'
serv_list = []
port = 12345
recv_buffer = 4096

def server():
	try:
		sqlconn = sqlite3.connect('a3.db')
		
	ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ssocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
	ssocket.bind((host,port))
	ssocket.listen(10)
	serv_list.append(ssocket)
	print "Starting server, listening on port: "+host+":", str(port)
		while 1:
			ready_to_read, ready_to_write, in_error = select.select(serv_list, [],[],0)
			for sock in ready_to_read:
				print sock
				if sock == ssocket:
					sockfd, addr = ssocket.accept()
					serv_list.append(sockfd)
					print("Client Added: (%s, %s) " % addr)
					broadcast(ssocket,sockfd, "[%s:%s] entered our chatting room\n" % addr)
				else:
					try:
						data = sock.recv(recv_buffer)
						if data:
							broadcast(ssocket, sock, '[' + str(sock.getpeername()) + '] ' + data)
						else:
							if sock in SERVER_LIST:
								serv_list.remove(sock)
								broadcast(ser_socket, sock, "\nClient (%s, %s) is offline\n" % addr)
					except:
						broadcast(ssocket, sock, "\nClient (%s, %s) is offline\n" % addr)
						continue
		ssocket.close()
def broadcast(ssocket, sock, message):
	for socket in serv_list:
		if socket != ssocket and socket != sock:
			try:
				socket.send(message)
			except:
				socket.close()
				if socket in serv_list:
					serv_list.remove(socket)
server()
