# coding: utf8

import signal
import websocket
from time import sleep

#clean quit
def signal_handler(signal, frame):
	ws.close()
	exit(0)
signal.signal(signal.SIGINT, signal_handler)
SIGTSTP
 
if __name__ == "__main__":
	websocket.enableTrace(True)
	ws = websocket.create_connection("ws://127.0.0.1:8080/websocket")
    

	#socket is established ask for the operating mode
	ws.send("Hello")

	#wait for the answer
	sleep (15)
	instruction = ws.recv()
	if (instruction == 'recv'):
		message = ""
		while (message != 'q'):
			message = ws.recv()
			print (format(message)), # here we'll display leds
	elif (instruction == 'send'):
		while (1) : 
			pass #send data

	ws.close()