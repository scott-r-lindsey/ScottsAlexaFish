#!/usr/bin/python

import os
import signal
import sys
from time import sleep
import RPi.GPIO as GPIO

pid_file = os.path.dirname(os.path.realpath(__file__)) + '/../var/interaction.pid';

# -----------------------------------------------------------------------------
# graceful exit

def signal_term_handler(signal, frame):
    print 'got SIGTERM'
    sys.exit(0)
 
signal.signal(signal.SIGTERM, signal_term_handler)

# -----------------------------------------------------------------------------
# kill running and replace pid file

if os.path.isfile(pid_file):
    with open(pid_file) as f:
        pid = f.read()

#    try:
#        os.kill(int(pid), signal.SIGTERM)
#    except OSError:
#        pass
#
    f.close()
    os.remove(pid_file)


pid = os.getpid();
print >> sys.stderr,  "Interaction start run with pid " + str(pid)
f = open(pid_file, 'w')
f.write(str(pid))
f.close()

# -----------------------------------------------------------------------------
# wake up for a bit

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# activate body motor
GPIO.output(17, GPIO.HIGH)

# tap the tail a bit
GPIO.output(22, GPIO.HIGH)
sleep(.05)
GPIO.output(22, GPIO.LOW)
sleep(.5);
GPIO.output(22, GPIO.HIGH)
sleep(.05)
GPIO.output(22, GPIO.LOW)

# stay away for up to 30 seconds
sleep(20)

# stop the body motor
GPIO.output(17, GPIO.LOW)

#GPIO.cleanup()

