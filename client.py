# coding: utf8

#!/usr/bin/env python 

#import tty, sys, termios
from time import sleep
import os
import websocket
import socket

port = '50000'
dest = '10.0.0.1'

def ping(host):
    con = os.system('ping -c 1 ' + host)
    if (con == 0):
        return True
    else:
        return False

def isValidIP(addr):
    try:
        socket.inet_aton(addr)
        return addr
    except socket.error:
        help("noServerIp")

def isValidDomain(addr):
    try:
        socket.inet_aton(addr)
        return addr
    except socket.error:
        help("noServerIp")


if __name__ == "__main__":
	
    i = 0
    while (i<3):
        if ping(dest) : 
            i=i+1
        else : i=0

    print("connected and ready")
    sleep(0.5)

    websocket.enableTrace(True)
    ws = websocket.create_connection("ws://"+dest+":"+port+"/websocket")
    
    #socket is established ask for the operating mode
    ws.send("Hello")
    #then send the command we want
    while True :
        print("-------------------------------------------")
        print("1. Tester la connectivitée réseau.")
        print("2. Tester le DNS.")
        print("3. Table de routage de la sonde.")
        print("-------------------------------------------")

        choice = raw_input()

        if choice == "1" :
            print("Entrez une IP")
            print("-------------")
            ip = raw_input()
            print(ip)
            if isValidIP(ip):
                ws.send('ping')
                ws.send(ip)
                print (ws.recv())
            else:
                print("l\'IP entrée n'est pas valide")
        elif choice == "2":
                print("Entrez une IP ou un nom de domaine")
                print("----------------------------------")
                dns = raw_input()
                #print(dns);
                ws.send('dns')
                ws.send(dns)
                print (ws.recv())

        elif(choice == "3") :
                  print("Table de routageR")
                  ws.send('routing_table')
                  print (ws.recv())
        else :
                  printf("Entrez 1, 2 ou 3.")
