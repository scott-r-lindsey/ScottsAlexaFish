#!/usr/bin/python

import os
import signal
from time import sleep
import RPi.GPIO as GPIO

pid_file = os.path.dirname(os.path.realpath(__file__)) + '/../var/interaction.pid';

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

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


pid = os.getpgid(0);
f = open(pid_file, 'w')
f.write(str(pid))
f.close()

# -----------------------------------------------------------------------------
# stop the body motor
GPIO.output(17, GPIO.LOW)

# tap the tail a bit
GPIO.output(22, GPIO.HIGH)
sleep(.05)
GPIO.output(22, GPIO.LOW)
sleep(.5);
GPIO.output(22, GPIO.HIGH)
sleep(.05)
GPIO.output(22, GPIO.LOW)

GPIO.cleanup()

