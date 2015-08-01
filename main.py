from driver import MoveDeg
from datetime import datetime
import PicoBorgRev
import logging

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
    MoveDeg(feedAmount)
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
