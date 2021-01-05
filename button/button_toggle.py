#!/usr/bin/env python3
##############################
# use of a button as a toggle
#  - press to turn led on
#  - press again to turn led off
##############################
# don't seem to need to use a resistor (default is to use a built-in pull-up resistor)
#
# ground ---- button leg / other leg ---- pin 20
#

from gpiozero import Button, LED
from signal import pause

button = Button(20)
led = LED(21)

# wow this library makes it easy
button.when_pressed = led.toggle 

pause()


