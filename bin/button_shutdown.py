#!/usr/bin/env python
# Simple script for shutting down the raspberry Pi at the press of a button.  
# by Inderpreet Singh  
  
import RPi.GPIO as GPIO  
import time  
import os  
 
# Use the Broadcom SOC Pin numbers  
# Setup the Pin with Internal pullups enabled and PIN in reading mode.  
GPIO.setmode(GPIO.BCM)  
#GPIO.setup(23, GPIO.IN)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
# Our function on what to do when the button is pressed  
def Shutdown(channel):  
    os.system('mpg123 -q /opt/scott/ill-be-back.mp3; shutdown -h now &')

def goneHigh(channel):
    print "high " + str(channel) + "\n"


def goneLow(channel):
    print "low " + str(channel) + "\n"
 
# Add our function to execute when the button pressed event happens  
GPIO.add_event_detect(23, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)  

# Now wait!  
while 1:  
    time.sleep(1)  

