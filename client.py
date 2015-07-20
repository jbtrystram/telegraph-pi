# coding: utf8

#!/usr/bin/env python 

import RPi.GPIO as GPIO
from time import sleep
#websocket
import websocket

port = '50003'
dest = '192.168.1.124'

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT) # LED OK
GPIO.setup(22,GPIO.OUT) # Gauche (TI)
GPIO.setup(18,GPIO.OUT) # Droite (TA)
GPIO.setup(16,GPIO.OUT) # Recv (centre vert)

GPIO.setup(15,GPIO.IN) #bouton droit
GPIO.setup(13,GPIO.IN) #bouton gauche

#eteindre tout
GPIO.output(7, False)
GPIO.output(22, False)
GPIO.output(18, False)
GPIO.output(16, False)


def switch_led_Ti() :
    GPIO.output(22, not GPIO.input(22))

def switch_led_Ta() :
    GPIO.output(18, not GPIO.input(18))

def led_output(word):
    if (word == 'ti') : switch_led_Ti()
    elif (word == 'ta') : switch_led_Ta()
    elif (word == 'slash'):
        switch_led_Ti()
        switch_led_Ta()
    sleep(0.30)
    if (word == 'ti') : switch_led_Ti()
    elif (word == 'ta') : switch_led_Ta()
    elif (word == 'slash'):
        switch_led_Ti()
        switch_led_Ta()

def sendMorse (ws):
    ws.send('ready to send')
    leave=""
    while (leave != "switch") :
        if GPIO.input(13):
            sleep(0.09)
            if (GPIO.input(15) and GPIO.input(13)):
                ws.send('slash')
                led_output('slash')
                leave = ws.recv() 
            else:
                ws.send('.')
                led_output('ti')
                leave = ws.recv() 
                       
        elif GPIO.input(15):
            sleep(0.09)
            if (GPIO.input(15) and GPIO.input(13)):
                ws.send('slash')
                led_output('slash')
                leave = ws.recv() 
            else:
                ws.send('_')
                led_output('ta')
                leave = ws.recv()
                print leave
        
    receiveMorse(ws)

def receiveMorse(ws) :
    message = ""
    ws.send('ready to rcv')
    while (message != 'q'):
        message = ws.recv()
        if (message == 'switch') :
            GPIO.output(16, False) #éteindre le Témoin de réception
            sendMorse(ws)
        else :
            print (format(message)),
            led_output(format(message))
    quit()

def quit() :
    GPIO.output(7, False)
    GPIO.output(22, False)
    GPIO.output(18, False)
    GPIO.output(16, False)
    exit(0)

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.create_connection("ws://"+dest+":"+port+"/websocket")
    
    #socket is established ask for the operating mode
    ws.send("Hello")
    #wait for the answer
    instruction = ws.recv()
    GPIO.output(7, True)

    if (instruction == 'recv'):
        GPIO.output(16, True) #Témoin de réception
        receiveMorse(ws)
    elif (instruction == 'send'):
        sendMorse(ws)
        