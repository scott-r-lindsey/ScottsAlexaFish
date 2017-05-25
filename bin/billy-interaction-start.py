#!/usr/bin/python

from __future__ import division
import os
import signal
import sys
from time import sleep
import RPi.GPIO as GPIO
import random

pid_file = os.path.dirname(os.path.realpath(__file__)) + '/../var/interaction.pid';

# -----------------------------------------------------------------------------
# graceful exit

def signal_term_handler(signal, frame):
    print 'got SIGTERM'
    GPIO.output(22, GPIO.LOW)
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_term_handler)

# -----------------------------------------------------------------------------
# kill running and replace pid file

if os.path.isfile(pid_file):
    with open(pid_file) as f:
        pid = f.read()

    try:
        os.kill(int(pid), signal.SIGTERM)
    except OSError:
        pass

    f.close()
    os.remove(pid_file)


pid = os.getpid();
print >> sys.stderr,  "Interaction start run with pid " + str(pid)
f = open(pid_file, 'w')
f.write(str(pid))
f.close()

# -----------------------------------------------------------------------------
# setup

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# activate body motor
GPIO.output(17, GPIO.HIGH)

# a tail tap should be between .08 and .16 seconds long
# a pause should be between .4 and .7 seconds long
# we tap the tail for four seconds only
# because the sound of the tail can confuse the microphone
i = 0.1
while (i < 4): 
    tap = random.uniform(.03, .10)
    pause = random.uniform(.4, .9)

    # tap the tail a bit
    GPIO.output(22, GPIO.HIGH)
    #print "tap, sleep " + str(tap) + "\n"
    sleep(tap)

    GPIO.output(22, GPIO.LOW)
    #print "pause, sleep " + str(pause) + "\n"
    sleep(pause)

    i = i + tap
    i = i + pause

    print "i is " + str(i) + "\n"

sleep(25)

# stand down
GPIO.output(17, GPIO.LOW)

