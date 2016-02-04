#!/usr/bin/python
#Multi-client chat application keeping chat records.
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
		sqlc=sqlconn.cursor()
		sqlc.execute('CREATE TABLE CHATTEXT(ID INT PRIMARY KEY, CHAT CHAR(1000))')
		sqlc.execute("INSERT INTO CHATTEXT VALUE (1,'')")
		print 'Table created'
	except:
		print 'Table already there, Maybe'
	finally:
		sqlconn.close()		
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
				print 'n'
				send_new_client(sockfd)
				print 'nb'
			else:
				try:
					data = sock.recv(recv_buffer)
					if data:
						strdata ='[' + str(sock.getpeername()) + '] ' + data
						broadcast(ssocket, sock, strdata)
						sqlconn = sqlite3.connect('a3.db')
						sqlc=sqlconn.cursor()
						print 'a'
						stmnt='''UPDATE CHATTEXT set CHAT = CHAT || "{}"  WHERE ID = 1'''.format(strdata)
						print stmnt 
						sqlconn.execute(stmnt)
						print 'b'
						sqlconn.commmit()
						print 'b1'
						sqlconn.close()
						print 'b2'
					else:
						if sock in SERVER_LIST:
							print 'c'
							serv_list.remove(sock)
							broadcast(ser_socket, sock, "\nClient (%s, %s) is offline\n" % addr)
				except:
					broadcast(ssocket, sock, "\nClient (%s, %s) is offline Exception\n" % addr)
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
def send_new_client(sock):
	sqlconn = sqlite3.connect('a3.db')
	sqlc=sqlconn.cursor()
	cursor=sqlc.execute('SELECT CHAT FROM CHATTEXT WHERE ID = 1')
	for row in cursor:
		sock.send(row[0])
		print row[0]
	sqlconn.close()
server()
