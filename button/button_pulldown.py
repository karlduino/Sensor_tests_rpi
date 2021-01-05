#!/usr/bin/env python3
##############################
# use of a button with pull-down resistor
##############################
#
# pin 20 --------------------|
#                            |--- button leg / other leg ---- v3.3
# ground --- 10k resistor ---| 
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

# don't _need_ the bounce_time=None
# pull_up=False if using a pull-down resistor, as here
button = Button(20, pull_up=False, bounce_time=None) 

while not button.is_pressed:
    print("button is not pressed")
    sleep(1)

print("button was pressed")

