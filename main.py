#!/usr/bin/env python
# coding: latin-1
from driver import MoveDeg
import PicoBorgRev
import logging
from datetime import datetime

# Setup the PicoBorg Reverse
PBR = PicoBorgRev.PicoBorgRev()
# PBR.i2cAddress = 0x44                   # Uncomment and change the value if you have changed the board address
PBR.Init()

# Set log file location
logging.basicConfig(format='%(message)s', filename='feedings.log', level=logging.INFO)
# Save the current datetime to a variable and format it
now = datetime.now()
feedTime = str(now.strftime("%m/%d/%Y at %H:%M:%S"))

feedAmount = raw_input("How many degrees would you like to turn the stepper? ")

try:
    # Start by turning all drives off
    PBR.MotorsOff()
    # Rotate 1 full revolution
    MoveDeg(int(feedAmount))
    PBR.MotorsOff()
    # Log message to a file.
    logging.info("Food dispensed on " + feedTime)
except KeyboardInterrupt:
    # CTRL+C exit, turn off the drives and release the GPIO pins
    PBR.MotorsOff()
    logging.warning("[!]Keyboard interrupt at " + feedTime)
    print 'Terminated'
except:
    logging.warning("[!]Something went wrong at " + feedTime)