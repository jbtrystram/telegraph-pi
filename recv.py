#!/usr/bin/env python 

""" 
A simple send app to learn morse : send 2 values (._._ / ... / etc)
""" 

import socket
from sys import stdout

host = 'localhost' 
port = 50003
backlog = 5 
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog)
client, address = s.accept()
while 1: 
    data = client.recv(size)
    if data: 
        if (data == 'stop'):
            print''
            client.close()
            break
        elif (data == 'ti'):
            stdout.write(". ")
            stdout.flush()
        elif (data == 'ta'):
            stdout.write("_ ")
            stdout.flush()
        elif (data == 'slash'):
            stdout.write("/  ")
            stdout.flush()
