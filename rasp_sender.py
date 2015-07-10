#!/usr/bin/env python 

import tty, sys, termios
import socket
import RPi.GPIO as GPIO
from time import sleep

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

host = '192.168.1.124' #Pc de Jib
port = 50003
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host,port))
data = ''

GPIO.output(7, True)

def switch_led_Ti() :
    GPIO.output(22, not GPIO.input(22))

def switch_led_Ta() :
    GPIO.output(18, not GPIO.input(18))


while 1:

    if GPIO.input(13):
            switch_led_Ti()
            s.send('ti')
            sleep(0.25)
            switch_led_Ti()
    elif GPIO.input(15):
            switch_led_Ta()
            s.send('ta')
            sleep(0.25)
            switch_led_Ta()
    elif (GPIO.input(15) and GPIO.input(13)):
            switch_led_Ta()
            switch_led_Ti()
            s.send('slash')
            sleep(0.25)
            switch_led_Ta()
            switch_led_Ti()
    
s.close() 