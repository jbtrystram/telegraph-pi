#!/usr/bin/env python 

import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import signal
import sys
import os

port = 50003
host = '10.0.0.1'

################ DEFINITION DE LA PATROUILLE 
pat = "LION"

send_mode = ""

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
    	
    	#switch mode
    	def switch_transmission_mode(frame, signums):
    		global send_mode
        	self.write_message('switch')
        	send_mode = not send_mode
        	print ('APPUYER SUR ENTREE')

  	signal.signal(signal.SIGTSTP, switch_transmission_mode)

    def on_message(self, message):
    	global send_mode
        if (message not in {'.', '_', 'slash'} ): print (message)
        if (message == 'Hello'):
            print("Le client demande quoi faire! ")
            print("   e : lui envoyer du morse.")
            print("   r : les laisser envoyer du morse.")
            while True :
            	order = raw_input()
            	if (order == 'e') :
            		send_mode = True; 
                	self.write_message('recv')
                	break
            	elif (order == 'r') :
            		send_mode = False; 
                	self.write_message('send')
                	break
                else :
                	print("Attention mauvaise saisie! ")
                
        elif (message == 'ready to rcv'):
        	self.sendMorse()      	

       	elif (message == 'ready to send'):
       		print("LES SCOUTS TRANSMETTENT")
        	print('CTRL+Z reprendra la main sur la transmission')
        
        else :
        	if (message == 'slash') :
        		print ('/')
        	else :
        		print (message),
        	self.write_message('ack')



    #send
    def sendMorse(self):
    	global send_mode
    	print("OK c'est parti ! a = TI, e = TA, s = SLASH, q = quitter.")
        print('CTRL+Z proposera aux scouts de repondre')
        char = ""
        while (char != 'q' and send_mode == True):
            char = raw_input()
            if char == 'a' :
                self.write_message('ti')
                print ('.'),
            elif char == 'e' :
                self.write_message('ta')
                print ('_'),
            elif char == 's' :
                self.write_message('slash')
                print ('/'),
            elif char == 'q' :
                self.write_message('q')
            else :
                print ('invalid key')

    def on_close(self):
        exit(0)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/websocket', WebSocketHandler)
        ]
        tornado.web.Application.__init__(self, handlers)

  
  
if __name__ == '__main__':

    sys.stdout.write("\x1b]2;"+pat+"\x07")
    os.system("setterm -background red -foreground white")

    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(port, host)
    tornado.ioloop.IOLoop.instance().start()

    exit(0)
        
