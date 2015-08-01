#!/usr/bin/env python
# coding: latin-1
from driver import MoveDeg
import sys
import PicoBorgRev
import logging
from datetime import datetime
from optparse import OptionParser

#Setup arguments
usage = "Usage: %prog -d <degrees>"
parser = OptionParser(usage=usage)
parser.add_option('-d', '--degrees', dest='feedAmount', type='int', \
    help='Degrees to turn the stepper.')
(opts, args) = parser.parse_args()
feedAmount = opts.feedAmount
if len(sys.argv) < 1:
    parser.print_help()
    sys.exit(1)

# Setup the PicoBorg Reverse
PBR = PicoBorgRev.PicoBorgRev()
# PBR.i2cAddress = 0x44                   # Uncomment and change the value if you have changed the board address
PBR.Init()

# Setup logging
logging.basicConfig(format='%(message)s', filename='feedings.log', level=logging.INFO)
now = datetime.now()
feedTime = str(now.strftime("%m/%d/%Y at %H:%M:%S"))

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