# coding: utf8
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop


class WebSocketHandler(tornado.websocket.WebSocketHandler):
	def open(self):
		pass
 
	def on_message(self, message):
    #    self.write_message(u"Your message was: " + message)
		if (message == 'Hello'):
			print("Le client demande quoi faire! ")
			print("   e : lui envoyer du morse.")
			print("   r : le laisser envoyer du morse.")
			order = raw_input()
			if (order == 'e') : order = 'recv'
			elif (order == 'r') : order = 'send'
			self.write_message(order)

			if (order == 'recv'):
				print("OK c'est parti ! i = TI et a = TA, q pour quitter")
				char = ""
				while (char != 'q'):
					char = raw_input()
					self.write_message(char)

 
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
	server.listen(8080)
	tornado.ioloop.IOLoop.instance().start()

