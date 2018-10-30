#!/bin/python

#simple script for shutting down the raspberry Pi at the press of a button

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Our function on what to do when the button is pressed
def Shutdown(channel):
    os.system("sudo shutdown -h now")

GPIO.add_event_detect(18, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)

#Now wait!
while 1:
    time.sleep(1)
