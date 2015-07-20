# telegraph-pi
A simple to project to create a Telegraph between two raspberrys with websockets

Hardware : rapsberry pi 
Slice of pi : http://shop.ciseco.co.uk/slice-of-pi-add-on-for-raspberry-pi/
Leds and Resistors
Calcul de la résistance : http://users.telenet.be/h-consult/elec/led.htm     (GPIO is 3.3V out)
On pourra trouver leds et résistances sur Conrad.
Jouer avec des boutons poussoirs : http://mchobby.be/wiki/index.php?title=Rasp-Hack-PiButton
autre tuto : http://nagashur.com/wiki/doku.php?id=raspberry_pi:

Boutons + résistances http://shop.mchobby.be/minikits/39-bouton-tactile-mini-kit-3232100000391.html?search_query=bouton&results=110

---------------------------------------------------------------------------------------------------------------
-----------------    Board Design (see in raw mode)   --------------- 

-----------------------------
|                       o 1  |            1 : Green Led = everything is OK 
|                            |
|     o 2         o 3        |            2 : Red Led : TA recevied, 3 : Red Led : Ti recevied
|                            |
|                            |
|     U 4     o 5     U 6    |         4 : push button : send a Ti 
|                            |         5 : Red Led : what you just send (ti or ta)
|                            |         6 : push button : send a Ta
-----------------------------


SIDES NOTES : 
For web socket to works, you need to add these to python : 
sudo pip install websocket-client tornado
