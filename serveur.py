#!/usr/bin/env python 

import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import signal

port = 50003
host = '192.168.1.124'


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
    	signal.signal(signal.SIGTSTP, self.switch_transmission_mode)
  
    def on_message(self, message):
    #    self.write_message(u"Your message was: " + message)
        if (message == 'Hello'):
            print("Le client demande quoi faire! ")
            print("   e : lui envoyer du morse.")
            print("   r : les laisser envoyer du morse.")
            while True :
            	order = raw_input()
            	if (order == 'e') : 
                	self.write_message('recv')
                	break
            	elif (order == 'r') : 
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
    	print("OK c'est parti ! i = TI et a = TA, s pour SLASH, q pour quitter.")
        print('CTRL+Z demandera aux scouts de repondre')
        char = ""
        while (char != 'q'):
            char = raw_input()
            if char == 'i' :
                self.write_message('ti')
                print ('.'),
            elif char == 'a' :
                self.write_message('ta')
                print ('_'),
            elif char == 's' :
                self.write_message('slash')
                print ('/'),
            elif char == 'q' :
                self.write_message('stop')
            else :
                print ('invalid key')

                       
    #switch mode
    def switch_transmission_mode(signal, frame, self):
        self.write_message('switch')

 
    def on_close(self):
        pass
 
 
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/websocket', WebSocketHandler)
        ]

        tornado.web.Application.__init__(self, handlers)

  
  
if __name__ == '__main__':
    
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(port, host)
    tornado.ioloop.IOLoop.instance().start()

    
        