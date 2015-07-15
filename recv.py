#!/usr/bin/env python 

""" 
A simple send app to learn morse : send 2 values (._._ / ... / etc)
""" 

import socket
import signal
from sys import stdout
from sys import exit

#gerer la sortie 
def signal_handler(signal, frame):
	client.close()
	exit(0)
signal.signal(signal.SIGINT, signal_handler)

#Fonction de decodage des caracteres 
def decode (m):
	if (m == "") :
		stdout.write(" ")
		stdout.flush()
	else :
		if (m == "._"):
			stdout.write("a")
			stdout.flush()
		elif (m == "_..."):
			stdout.write("b")
			stdout.flush()
		elif (m == "_._."):
			stdout.write("c")
			stdout.flush()
		elif (m == "_.."):
			stdout.write("d")
			stdout.flush()
		elif (m == "."):
			stdout.write("e")
			stdout.flush()
		elif (m == ".._."):
			stdout.write("f")
			stdout.flush()
		elif (m == "__."):
			stdout.write("g")
			stdout.flush()
		elif (m == "...."):
			stdout.write("h")
			stdout.flush()
		elif (m == ".."):
			stdout.write("i")
			stdout.flush()
		elif (m == ".___"):
			stdout.write("j")
			stdout.flush()
		elif (m == "_._"):
			stdout.write("k")
			stdout.flush()
		elif (m == "._.."):
			stdout.write("l")
			stdout.flush()
		elif (m == "__"):
			stdout.write("m")
			stdout.flush()
		elif (m == "_."):
			stdout.write("n")
			stdout.flush()
		elif (m == "___"):
			stdout.write("o")
			stdout.flush()
		elif (m == ".__."):
			stdout.write("p")
			stdout.flush()
		elif (m == "__._"):
			stdout.write("q")
			stdout.flush()
		elif (m == "._."):
			stdout.write("r")
			stdout.flush()
		elif (m == "..."):
			stdout.write("s")
			stdout.flush()
		elif (m == "_"):
			stdout.write("t")
			stdout.flush()
		elif (m == ".._"):
			stdout.write("u")
			stdout.flush()
		elif (m == "..._"):
			stdout.write("v")
			stdout.flush()
		elif (m == ".__"):
			stdout.write("w")
			stdout.flush()
		elif (m == "_.._"):
			stdout.write("x")
			stdout.flush()
		elif (m == "_.__"):
			stdout.write("y")
			stdout.flush()
		elif (m == "__.."):
			stdout.write("z")
			stdout.flush()
		else :
			m = '/'+m+'/'
			stdout.write(m)
			stdout.flush()

host = '192.168.1.124' 
port = 50009
backlog = 5 
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog)
client, address = s.accept()
lettre = ""
while 1: 
	data = client.recv(size)
	if data:
		if (data == 'stop'):
			client.close()
			break
		elif (data == 'ti'):
			lettre = lettre+"."
		elif (data == 'ta'):
			lettre = lettre+"_"
		elif (data == 'slash'):
			decode(lettre)
			lettre = ""