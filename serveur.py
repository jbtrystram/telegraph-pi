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
host = '127.0.0.1'


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    ping_flag = False
    dns_flag = False
    def ping(self, host):
        con = os.system('ping -c 1 ' + host)
        if (con == 0):
            return "OK"
        else:
            return "NOK"

    def dns(self, domain):
        return socket.gethostbyname(domain)

    def routes():
        process = subprocess.Popen(['route', '-n'], stdout=subprocess.PIPE)
        out, err = process.communicate()
        return(out)

    def isValidIP(self, addr):
        try:
            socket.inet_aton(addr)
            return addr
        except socket.error:
            help("noServerIp")

    def on_message(self, message):
        print message
        ping_flag = False
        dns_flag = False
        if message == 'Hello':
            print("La sonde est connectée. Attente d'une commande.")

        elif message == 'ping':
            self.ping_flag = True
            print ('flag set')
        elif self.ping_flag:
            print("je pingue mon brave")
            self.write_message(self.ping(message))
            self.ping_flag = False

        elif message == 'dns':
            self.dns_flag = True
        elif self.dns_flag	:
            self.write_message(dns(message))
            self.dns_flag = False

        elif message == 'routing_table':
            self.write_message(routes())
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
