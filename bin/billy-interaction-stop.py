#!/usr/bin/python

import os
import signal
import sys
from time import sleep
import RPi.GPIO as GPIO

pid_file = os.path.dirname(os.path.realpath(__file__)) + '/../var/interaction.pid';

# -----------------------------------------------------------------------------
# kill running 
if os.path.isfile(pid_file):
    with open(pid_file) as f:
        pid = f.read()

    try:
        print >> sys.stderr,  "Killing previous interaction with with pid " + str(pid)
        os.kill(int(pid), signal.SIGTERM) 
    except OSError:
        pass

    f.close()
    os.remove(pid_file)

# -----------------------------------------------------------------------------
# stop the body motor

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.output(17, GPIO.LOW)

# tap the tail a bit
GPIO.output(22, GPIO.HIGH)
sleep(.1)
GPIO.output(22, GPIO.LOW)
sleep(.5);
GPIO.output(22, GPIO.HIGH)
sleep(.1)
GPIO.output(22, GPIO.LOW)

