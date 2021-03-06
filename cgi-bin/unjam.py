#!/usr/bin/env python
# coding: latin-1
from driver import MoveDeg
import sys
import PicoBorgRev
import logging
from datetime import datetime
from optparse import OptionParser

# Setup the PicoBorg Reverse
PBR = PicoBorgRev.PicoBorgRev()
# PBR.i2cAddress = 0x44                   # Uncomment and change the value if you have changed the board address
PBR.Init()

# Setup logging
logging.basicConfig(format='%(message)s', filename='../feedings.log', level=logging.INFO)
now = datetime.now()
feedTime = str(now.strftime("%m/%d/%Y at %H:%M:%S"))

try:
    # Start by turning all drives off
    PBR.MotorsOff()
    # This is making my motor freak out for some reason. May be hardware.
    MoveDeg(-720)
    sleep(1)
    MoveDeg(360)
    sleep(1)
    MoveDeg(-180)
    sleep(1)
    MoveDeg(720)
    PBR.MotorsOff()
    # Log message to a file.
    logging.info("Attempted to unjam the feeder on " + feedTime)
except KeyboardInterrupt:
    # CTRL+C exit, turn off the drives and release the GPIO pins
    PBR.MotorsOff()
    logging.warning("[!]Keyboard interrupt at " + feedTime)
    print 'Terminated'
except:
    logging.warning("[!]Something went wrong at " + feedTime)
