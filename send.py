#!/usr/bin/env python 


import socket

host = 'localhost' 
port = 50003
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host,port))
data = ''

"""
def what's possible here
"""

import tty, sys, termios

class ReadChar():
    def __enter__(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    def __exit__(self, type, value, traceback):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

print ('Faites Du Morse ! 1 = Ti / 2 = Ta , 3 = /, 4 = quitter')

while (data != 'stop'):
    with ReadChar() as rc:
                data = rc

    if data == '1' :
        s.send('ti')
        print ('.'),
    elif data == '2' :
        s.send('ta')
        print ('_'),
    elif data == '3' :
        s.send('slash')
        print ('/'),
    elif data == '4' :
        s.send('stop')
        data = 'stop'
    else :
        print ('invalid key')

s.close() 
