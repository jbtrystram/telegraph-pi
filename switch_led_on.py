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


def switch_led_Ti() :
	GPIO.output(22, not GPIO.input(22))

def switch_led_Ta() :
	GPIO.output(18, not GPIO.input(18))


while 1:
		if GPIO.input(13):
			switch_led_Ti()
			sleep(0.5)
			switch_led_Ti()
		elif GPIO.input(15):
			switch_led_Ta()
			sleep(0.5)
			switch_led_Ta()

