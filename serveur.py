#!/usr/bin/env python
# coding: utf8

import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import signal
import sys
import os
import socket
import subprocess

port = 50000
host = '10.0.0.1'



class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def ping(host):
        con = os.system('ping -c 1 ' + host)
        if (con == 0):
            return True
        else:
            return False

    def dns(domain):
        return socket.gethostbyname(domain)

    def routes():
		process = subprocess.Popen(['route', '-n'], stdout=subprocess.PIPE)
		out, err = process.communicate()
		return(out)

    def on_message(self, message):
        print message
        ping_flag = False
		dns_flag = False
		print (message)
        if message == 'Hello':
            print("La sonde est connectée. Attente d'une commande.")

        elif message == 'ping':
            ping_flag = True
        elif (ping_flag is True) and (isValidIP(message)):
            self.write(ping(message))
            ping_flag = False

        elif message == 'dns':
            dns_flag = True
        elif dns_flag is True and isValidDomaine(message):
            self.write(dns(message))
            dns_flag = False

        elif message == 'routing_table':
            self.write(routes())
        else:
            print ('unknown command')


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

    exit(0)
