#!/usr/bin/env python3
##############################
# use of a button
##############################
# don't seem to need to use a resistor
#
# ground ---- button leg / other leg ---- pin 20
#
# key features:
#       <https://gpiozero.readthedocs.io/en/stable/api_input.html?highlight=button#gpiozero.Button>
#   is_pressed
#   is_held
#   when_pressed()   # set to None to disable
#   when_released()  # set to None to disable
#   when_held()      # set to None to disable
#   wait_for_press()   # takes timeout value (or indefinite if None)
#   wait_for_release() # takes timeout value (or indefinite if None)
#   pull_up  # if True, it uses a pull-up resistor to set pin high by default
#   value    # 1 if pressed 0 if not

from gpiozero import Button
from time import sleep

button = Button(20)
while not button.is_pressed:
    print("button is not pressed")
    sleep(1)
print("button was pressed")

