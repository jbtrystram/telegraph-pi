# coding: utf8

#!/usr/bin/env python 

#import tty, sys, termios
import RPi.GPIO as GPIO
from time import sleep
import os
import websocket

port = '50003'
dest = '10.0.0.1'

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


def ping (host):
	con = os.system('ping -c 1 '+host)
	if (con == 0): return True
	else : return False


def blink_receiv(rcv):
    GPIO.output(16, False)
    sleep(0.25)
    GPIO.output(16, True)
    sleep(0.15)
    GPIO.output(16, False)
    sleep(0.25)
    GPIO.output(16, True)
    sleep(0.15)
    GPIO.output(16, False)
    sleep(0.20)
    if (rcv) : GPIO.output(16, True)



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
        if (leave == 'q') : quit()
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
    print ("switch recevied L88")
    blink_receiv(True)
    receiveMorse(ws)

def receiveMorse(ws) :
    message = ""
    ws.send('ready to rcv')
    while (message != 'q'):
        print ('waiting msg')
        message = ws.recv()
        if (message == 'switch') :
            print ("switch recevied!")
            blink_receiv(False)
            sendMorse(ws)
        else :
            print (format(message)),
            led_output(format(message))
    ws.close()
    quit()

def quit() :
    GPIO.output(7, False)
    GPIO.output(22, False)
    GPIO.output(18, False)
    GPIO.output(16, False)
    os.system('halt')
    exit(0)

if __name__ == "__main__":
	
    i = 0
    while (i<3):
        if ping(dest) : 
            i=i+1
            GPIO.output(7, True)
            sleep(0.08*i)
            GPIO.output(7,False)
        else : i=0

    GPIO.output(7, True)
    sleep(0.5)
    GPIO.output(7,False)

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
        
